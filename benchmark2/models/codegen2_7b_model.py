import sys
from types import ModuleType

# Mock transformers.onnx for Salesforce/codegen2 backward compatibility
if "transformers.onnx" not in sys.modules:
    dummy_onnx = ModuleType("transformers.onnx")
    class DummyOnnxConfigWithPast:
        pass
    class DummyPatchingSpec:
        pass
    dummy_onnx.OnnxConfigWithPast = DummyOnnxConfigWithPast
    dummy_onnx.PatchingSpec = DummyPatchingSpec
    sys.modules["transformers.onnx"] = dummy_onnx

from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch
import re

alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

class Codegen2_7bModelGenerator:
    def __init__(self):
        print("Loading CodeGen2-7B Model...")
        self.checkpoint = "Salesforce/codegen2-7B"
        
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(self.checkpoint)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.checkpoint,
            trust_remote_code=True,
            revision="main",
            quantization_config=quantization_config,
            device_map="auto",
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True
        )
        print(f"Memory footprint: {self.model.get_memory_footprint() / 1e6:.2f} MB")

    def generate_tests(self, code: str, problem_description: str = "") -> str:
        complex_input = f"Problem Description:\n{problem_description}\n\nCode to Test:\n{code}"
        instruction = "Write a comprehensive Python unit test suite for the provided code."
        prompt = alpaca_prompt.format(instruction, complex_input, "")

        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to("cuda")
        outputs = self.model.generate(
            input_ids, 
            max_new_tokens=512, 
            use_cache=True, 
            pad_token_id=self.tokenizer.eos_token_id
        )

        decoded_output = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        try:
            if "### Response:" in decoded_output:
                response_text = decoded_output.split("### Response:")[1].strip()
            else:
                response_text = decoded_output
                
            code_blocks = re.findall(r'```(?:python)?\n(.*?)\n```', response_text, re.DOTALL)
            if code_blocks:
                response_text = "\n\n".join(code_blocks).strip()
        except IndexError:
            response_text = ""
            
        return response_text
