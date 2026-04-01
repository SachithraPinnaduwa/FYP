from unsloth import FastModel
from unsloth.chat_templates import get_chat_template
import re
import torch
import gc

# Prevent PyTorch from allocating massive CPU thread pools that never get released
torch.set_num_threads(1)

class Gemma4BBaseModelGenerator:
    def __init__(self):
        print("Loading Gemma-3-4B-IT Model...")
        self.model, tokenizer = FastModel.from_pretrained(
            model_name="unsloth/gemma-3-4b-it",
            max_seq_length=2048,
            load_in_4bit=True,
        )
        self.tokenizer = get_chat_template(
            tokenizer,
            chat_template="gemma-3",
        )
        
        # Enable faster inference if available in the Unsloth FastModel
        try:
            from unsloth import FastLanguageModel
            FastLanguageModel.for_inference(self.model)
        except Exception:
            pass

    def generate_tests(self, code: str, problem_description: str = "") -> str:
        complex_input = f"Problem Description:\n{problem_description}\n\nCode to Test:\n{code}"
        prompt = f"Write a comprehensive Python unit test suite for the provided code. Do NOT include the original code in your response, only provide the test cases.\n\n{complex_input}"
        
        messages = [{
            "role": "user",
            "content": [{
                "type": "text",
                "text": prompt,
            }]
        }]
        
        # Wrap everything in torch.no_grad() to absolutely guarantee no tracking 
        with torch.no_grad():
            
            # Capture CPU inputs first to avoid hanging references on implicit copies
            cpu_inputs = self.tokenizer.apply_chat_template(
                messages,
                add_generation_prompt=True,
                tokenize=True,
                return_tensors="pt",
                return_dict=True,
                truncation=True, 
                max_length=1536 # Force cap: leave 512 for max_new_tokens to respect 2048 VRAM size
            )
            
            # Explicitly move to VRAM
            inputs = cpu_inputs.to("cuda")

            outputs = self.model.generate(
                **inputs, 
                max_new_tokens=512, 
                use_cache=True, 
                pad_token_id=self.tokenizer.eos_token_id,
                temperature=1.0, 
                top_p=0.95, 
                top_k=64
            )

            # Decode only the generated tokens
            input_length = inputs["input_ids"].shape[1]
            generated_tokens_tensor = outputs[0][input_length:]
            
            # Explicitly pull back to CPU and convert to standard Python list
            # This prevents the backend tokenizer from leaking implicit C++/Rust memory wrappers
            generated_tokens_list = generated_tokens_tensor.cpu().detach().tolist()
            
            # Proceed with standard generation decoding
            response_text = self.tokenizer.decode(generated_tokens_list, skip_special_tokens=True).strip()
            
            # Force empty internal state caching from HF core model
            if hasattr(self.model, "config") and hasattr(self.model.config, "use_cache"):
                self.model.config.use_cache = False
                self.model.config.use_cache = True

            # Destroy local references and clean RAM + VRAM immediately
            del cpu_inputs, inputs, outputs, generated_tokens_tensor, generated_tokens_list
            gc.collect()
            torch.cuda.empty_cache()
            
        # Try to extract Python code directly from markdown blocks
        try:
            code_blocks = re.findall(r'```(?:python)?\n(.*?)\n```', response_text, re.DOTALL)
            if code_blocks:
                response_text = "\n\n".join(code_blocks).strip()
        except IndexError:
            pass
            
        return response_text