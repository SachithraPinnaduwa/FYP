from unsloth import FastLanguageModel
from unsloth.chat_templates import get_chat_template
import torch
import re

class BaseModelGenerator:
    def __init__(self):
        print("Loading Base Model...")
        self.model, self.tokenizer = FastLanguageModel.from_pretrained(
            model_name="unsloth/Qwen2.5-Coder-7B-Instruct-bnb-4bit",
            max_seq_length=2048,
            dtype=None,
            load_in_4bit=True,
        )
        self.tokenizer = get_chat_template(
            self.tokenizer,
            chat_template="qwen-2.5", 
        )
        FastLanguageModel.for_inference(self.model)

    def generate_tests(self, code: str, problem_description: str = "") -> str:
        user_content = (
            "Write a comprehensive Python unit test suite for this code.\n"
            "Do NOT include the original code in your response, only provide the test cases.\n\n"
            f"Problem Description:\n{problem_description}\n\n"
            f"Code to Test:\n{code}"
        )
        
        messages = [
            {"role": "system", "content": "You are a helpful coding assistant that writes Python unit tests."},
            {"role": "user", "content": user_content},
        ]
        
        prompt = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )

        device = "cuda" if torch.cuda.is_available() else "cpu"
        inputs = self.tokenizer([prompt], return_tensors="pt").to(device)
        
        with torch.inference_mode():
            outputs = self.model.generate(
                **inputs, 
                max_new_tokens=2048, 
                use_cache=True, 
                pad_token_id=self.tokenizer.eos_token_id
            )

        input_len = inputs["input_ids"].shape[1]
        new_tokens = outputs[0][input_len:]
        response_text = self.tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
        
        # Try to extract python code
        code_blocks = re.findall(r"""```(?:python)?\n(.*?)\n```""", response_text, re.DOTALL)
        if code_blocks:
            response_text = "\n\n".join(code_blocks).strip()
            
        return response_text
