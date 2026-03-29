from unsloth import FastLanguageModel
import re

alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

class Qwen35BaseModelGenerator:
    def __init__(self):
        print("Loading Qwen3.5-4B Base Model...")
        self.model, self.tokenizer = FastLanguageModel.from_pretrained(
            model_name="unsloth/Qwen3.5-4B",
            max_seq_length=2048,
            dtype=None,
            load_in_4bit=True,
        )
        FastLanguageModel.for_inference(self.model)

    def generate_tests(self, code: str, problem_description: str = "") -> str:
        complex_input = f"Problem Description:\n{problem_description}\n\nCode to Test:\n{code}"
        instruction = "Write a comprehensive Python unit test suite for the provided code."
        prompt = alpaca_prompt.format(instruction, complex_input, "")

        # Note: Unsloth defaults Qwen3.5 to the Qwen3-VL processor which expects text natively 
        # via the text= kwarg rather than as a positional arg, which defaults to interpreting as images.
        inputs = self.tokenizer(text=[prompt], return_tensors="pt").to("cuda")
        outputs = self.model.generate(
            **inputs, 
            max_new_tokens=512, 
            use_cache=True, 
            pad_token_id=self.tokenizer.eos_token_id
        )

        decoded_output = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
        
        try:
            response_text = decoded_output.split("### Response:")[1].strip()
            # Try to extract python code
            code_blocks = re.findall(r'```(?:python)?\n(.*?)\n```', response_text, re.DOTALL)
            if code_blocks:
                response_text = "\n\n".join(code_blocks).strip()
        except IndexError:
            response_text = ""
            
        return response_text
