from unsloth import FastLanguageModel

class Qwen35BaseModelGenerator:
    def __init__(self):
        print("Loading Qwen3.5-4B Base Model...")
        self.model, self.tokenizer = FastLanguageModel.from_pretrained(
            model_name="unsloth/Qwen3.5-4B",
            max_seq_length=4096,
            dtype=None,
            load_in_4bit=True,
        )
        FastLanguageModel.for_inference(self.model)

    def generate_tests(self, code: str, problem_description: str = "") -> str:
        # Base models perform better with file continuation rather than instruction formatting
        prompt = f"{code}\n\n# ==========================================\n# Comprehensive Python unit test suite below\n# ==========================================\nimport unittest\n\n"
        
        # Note: Unsloth defaults Qwen3.5 to the Qwen3-VL processor which expects text natively 
        # via the text= kwarg rather than as a positional arg, which defaults to interpreting as images.
        inputs = self.tokenizer(text=[prompt], return_tensors="pt").to("cuda")
        
        outputs = self.model.generate(
            **inputs, 
            max_new_tokens=1536, 
            use_cache=True, 
            pad_token_id=self.tokenizer.eos_token_id,
            temperature=0.2, # Lower temperature to prevent the base model from hallucinating
            top_p=0.9
        )

        decoded_output = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Strip the prompt length to isolate the generated tests
        if decoded_output.startswith(prompt):
            response_text = decoded_output[len(prompt):].strip()
        else:
            # Fallback if there's any decoded mismatch at the very beginning
            response_text = decoded_output
            
        # Post-processing: Base models may drift into generating markdown, explanations, 
        # or other random text after completing the code. Let's truncate at common drift points.
        
        # If it accidentally wraps the answer in markdown blocks after the fact
        if "```" in response_text:
            response_text = response_text.split("```")[0].strip()
            
        # If it starts generating headers or explanatory text
        if "###" in response_text:
            response_text = response_text.split("###")[0].strip()
            
        # Often the file is done after unittest.main()
        if "unittest.main()" in response_text:
            parts = response_text.split("unittest.main()")
            # Keep up to the first unittest.main() call, discard the rest
            response_text = parts[0] + "unittest.main()\n"
            
        return "import unittest\n\n" + response_text
