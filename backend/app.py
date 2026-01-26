import os
import threading
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Config via environment variables
MODEL_NAME = os.environ.get("MODEL_NAME", "lora_model")
MAX_SEQ_LENGTH = int(os.environ.get("MAX_SEQ_LENGTH", "2048"))
LOAD_IN_4BIT = os.environ.get("LOAD_IN_4BIT", "True").lower() in ("1", "true", "yes")
DEVICE = os.environ.get("DEVICE", "cuda")

# Lazy-loaded model/tokenizer
_model_lock = threading.Lock()
model = None
tokenizer = None


def load_model():
    global model, tokenizer
    with _model_lock:
        if model is None or tokenizer is None:
            try:
                from unsloth import FastLanguageModel
            except Exception as e:
                raise RuntimeError("Failed to import unsloth. Ensure it's installed.") from e

            model, tokenizer = FastLanguageModel.from_pretrained(
                model_name=MODEL_NAME,
                max_seq_length=MAX_SEQ_LENGTH,
                dtype=None,
                load_in_4bit=LOAD_IN_4BIT,
            )
            # Move to inference mode helper if available
            try:
                FastLanguageModel.for_inference(model)
            except Exception:
                pass


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/generate-tests", methods=["POST"])
def generate_tests():
    data = request.get_json(force=True)
    code = data.get("code")
    description = data.get("description", "")
    max_new_tokens = int(data.get("max_new_tokens", 512))

    if not code:
        return jsonify({"error": "Missing 'code' field in JSON body."}), 400

    # Ensure model is loaded
    try:
        load_model()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    complex_input = f"Problem Description:\n{description}\n\nCode to Test:\n{code}"

    messages = [
        {
            "role": "user",
            "content": (
                "Write a comprehensive Python unit test suite for the provided code.\n\n"
                f"{complex_input}"
            ),
        }
    ]

    try:
        input_ids = tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt",
        )

        # Move tensors to device if possible
        import torch
        device = torch.device("cuda" if DEVICE == "cuda" and torch.cuda.is_available() else "cpu")
        input_ids = input_ids.to(device)

        attention_mask = input_ids.ne(tokenizer.pad_token_id).long()

        with torch.no_grad():
            outputs = model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,
                max_new_tokens=max_new_tokens,
                eos_token_id=tokenizer.eos_token_id,
                pad_token_id=tokenizer.eos_token_id,
            )

        generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return jsonify({"tests": generated})

    except Exception as e:
        return jsonify({"error": f"Generation failed: {e}"}), 500


if __name__ == "__main__":
    # For local debugging only. Use a WSGI server in production.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
