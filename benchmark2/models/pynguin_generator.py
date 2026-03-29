import os
import subprocess
import tempfile
import resource

def set_memory_limit():
    # Limit to ~3GB of memory to prevent OOM
    # resource.RLIMIT_AS is maximum area (in bytes) of address space which may be taken by the process
    # 3GB = 3 * 1024 * 1024 * 1024 = 3221225472 bytes
    max_mem = 3 * 1024 * 1024 * 1024
    resource.setrlimit(resource.RLIMIT_AS, (max_mem, max_mem))

class PynguinGenerator:
    def __init__(self):
        print("Initializing Pynguin Generator...")
        # Pynguin requires python 3.10 specifically for best compatibility.
        # Ensure that it is installed in your current environment: `pip install pynguin`
        try:
            # Setting environment variable mandatory for Pynguin to run
            os.environ["PYNGUIN_DANGER_AWARE"] = "1"
        except Exception as e:
            print(f"Failed to set PYNGUIN_DANGER_AWARE: {e}")

    def generate_tests(self, code: str, problem_description: str = "") -> str:
        with tempfile.TemporaryDirectory() as tmpdir:
            module_name = "subject_module"
            target_file = os.path.join(tmpdir, f"{module_name}.py")
            
            with open(target_file, "w", encoding="utf-8") as f:
                f.write(code)
                
            cmd = [
                "pynguin",
                "--project-path", tmpdir,
                "--output-path", tmpdir,
                "--module-name", module_name,
                "--maximum-search-time", "15",  # 15 seconds max per file
                "--seed", "42"  # Ensure deterministic runs if possible
            ]
            
            env = os.environ.copy()
            env["PYNGUIN_DANGER_AWARE"] = "1"
            
            # Execute Pynguin with a hard timeout to prevent processes running infinitely or ballooning memory
            try:
                result = subprocess.run(
                    cmd, 
                    env=env, 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE, 
                    text=True,
                    timeout=25, # Force kill after 25 seconds
                    preexec_fn=set_memory_limit # Enforce max memory
                )
            except subprocess.TimeoutExpired:
                return "# Pynguin generation timed out after 25 seconds."
            except Exception as e:
                return f"# Exception occurred while running Pynguin: {e}"
            
            generated_test_path = os.path.join(tmpdir, f"test_{module_name}.py")
            if os.path.exists(generated_test_path):
                with open(generated_test_path, "r", encoding="utf-8") as f:
                    generated_test_code = f.read()
                
                # We need to strip out Pynguin's absolute imports and change it to default benchmark subject import
                # For `run_benchmark.py`, we usually don't need the exact file import name if it is executed dynamically
                # or evaluate script handles it, but just in case, Pynguin uses `import subject_module`
                # Let's clean the module name substitution simply.
                return generated_test_code.replace("import subject_module", "")
            else:
                error_msg = result.stderr if result.stderr else result.stdout
                return f"# Pynguin failed to generate tests.\n# Error or output:\n# {error_msg.replace(chr(10), chr(10) + '# ')}"
