"""
Test Generation Pipeline - Runs all models on all subjects.
Coordinates test generation across different models.
Supports both static subjects and dataset-loaded subjects.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import subprocess


# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


class TestGenerationPipeline:
    """
    Pipeline for running test generation across all models and subjects.
    """
    
    def __init__(
        self,
        subjects_dir: str = "subjects",
        output_dir: str = "generated_tests",
        models_config: Optional[Dict] = None
    ):
        """
        Initialize the pipeline.
        
        Args:
            subjects_dir: Directory containing subject code
            output_dir: Directory for generated tests
            models_config: Configuration for each model
        """
        self.base_dir = Path(__file__).parent.parent
        self.subjects_dir = self.base_dir / subjects_dir
        self.output_dir = self.base_dir / output_dir
        
        # Default model configurations
        self.models_config = models_config or {
            "your_model": {
                "enabled": True,
                "model_path": str(self.base_dir.parent / "lora_model"),
                "max_tokens": 1024,
            },
            "gpt": {
                "enabled": True,
                "model": "gpt-4",
                "use_mock": True,  # Set to False to use real API
            },
            "pynguin": {
                "enabled": True,
                "budget": 120,
            }
        }
    
    def get_subject_files(self) -> List[Path]:
        """Get all Python files in the subjects directory."""
        subject_files = []
        for file in self.subjects_dir.glob("*.py"):
            if file.name not in ["__init__.py", "dataset_loader.py"]:
                subject_files.append(file)
        return sorted(subject_files)
    
    def get_problem_description(self, subject_file: Path) -> str:
        """Extract problem description from subject file docstring."""
        try:
            with open(subject_file, 'r') as f:
                content = f.read()
            
            # Look for Problem Description in docstring
            if '"""' in content:
                docstring = content.split('"""')[1] if content.startswith('"""') else ""
                if "Problem Description:" in docstring:
                    desc_part = docstring.split("Problem Description:")[-1]
                    return desc_part.strip().split('"""')[0].strip()
            return ""
        except:
            return ""
    
    def run_your_model(self, subject_file: Path, output_file: Path) -> bool:
        """Run your fine-tuned model on a subject file."""
        config = self.models_config.get("your_model", {})
        if not config.get("enabled", True):
            print(f"Skipping your_model (disabled)")
            return False
        
        try:
            from models.my_model import YourModelTestGenerator
            
            generator = YourModelTestGenerator(
                model_path=config.get("model_path", "lora_model")
            )
            
            with open(subject_file, 'r') as f:
                source_code = f.read()
            
            # Get problem description if available (for dataset subjects)
            problem_description = self.get_problem_description(subject_file)
            
            test_code = generator.generate_tests(
                source_code,
                problem_description=problem_description,
                max_new_tokens=config.get("max_tokens", 1024)
            )
            
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w') as f:
                f.write(test_code)
            
            print(f"  ✓ your_model -> {output_file.name}")
            return True
            
        except Exception as e:
            print(f"  ✗ your_model failed: {e}")
            return False
    
    def run_gpt(self, subject_file: Path, output_file: Path) -> bool:
        """Run GPT baseline on a subject file."""
        config = self.models_config.get("gpt", {})
        if not config.get("enabled", True):
            print(f"Skipping gpt (disabled)")
            return False
        
        try:
            from models.gemini import GeminiTestGenerator, MockGeminiTestGenerator
            
            if config.get("use_mock", True):
                generator = MockGeminiTestGenerator(model=config.get("model", "gemini-1.5-pro"))
            else:
                generator = GeminiTestGenerator(model=config.get("model", "gemini-1.5-pro"))
            
            with open(subject_file, 'r') as f:
                source_code = f.read()
            
            # Get problem description if available
            problem_description = self.get_problem_description(subject_file)
            
            test_code = generator.generate_tests(source_code, problem_description)
            
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w') as f:
                f.write(test_code)
            
            print(f"  ✓ gpt -> {output_file.name}")
            return True
            
        except Exception as e:
            print(f"  ✗ gpt failed: {e}")
            return False
    
    def run_pynguin(self, subject_file: Path, output_dir: Path) -> bool:
        """Run Pynguin on a subject file."""
        config = self.models_config.get("pynguin", {})
        if not config.get("enabled", True):
            print(f"Skipping pynguin (disabled)")
            return False
        
        try:
            module_name = subject_file.stem
            
            # Run pynguin via subprocess
            cmd = [
                "pynguin",
                "--project-path", str(self.subjects_dir),
                "--output-path", str(output_dir),
                "--module-name", module_name,
                "--algorithm", "DYNAMOSA",
                "--budget", str(config.get("budget", 60)),
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=180
            )
            
            if result.returncode == 0:
                print(f"  ✓ pynguin -> {module_name}")
                return True
            else:
                print(f"  ✗ pynguin failed: {result.stderr[:100]}")
                return False
                
        except FileNotFoundError:
            print(f"  ✗ pynguin not installed")
            return False
        except subprocess.TimeoutExpired:
            print(f"  ✗ pynguin timed out")
            return False
        except Exception as e:
            print(f"  ✗ pynguin failed: {e}")
            return False
    
    def run_all(self) -> Dict:
        """
        Run all models on all subjects.
        
        Returns:
            Results dictionary with success/failure for each model-subject pair
        """
        results = {
            "timestamp": datetime.now().isoformat(),
            "subjects": {},
        }
        
        subject_files = self.get_subject_files()
        print(f"\n{'='*60}")
        print(f"Test Generation Pipeline")
        print(f"{'='*60}")
        print(f"Subjects: {len(subject_files)}")
        print(f"Models: your_model, gpt, pynguin")
        print(f"{'='*60}\n")
        
        for subject_file in subject_files:
            subject_name = subject_file.stem
            print(f"\n[{subject_name}]")
            
            results["subjects"][subject_name] = {}
            
            # Run your_model
            your_model_output = self.output_dir / "your_model" / f"test_{subject_name}.py"
            results["subjects"][subject_name]["your_model"] = self.run_your_model(
                subject_file, your_model_output
            )
            
            # Run GPT
            gpt_output = self.output_dir / "gpt" / f"test_{subject_name}.py"
            results["subjects"][subject_name]["gpt"] = self.run_gpt(
                subject_file, gpt_output
            )
            
            # Run Pynguin
            pynguin_output = self.output_dir / "pynguin"
            results["subjects"][subject_name]["pynguin"] = self.run_pynguin(
                subject_file, pynguin_output
            )
        
        # Save results
        results_file = self.output_dir / "generation_results.json"
        results_file.parent.mkdir(parents=True, exist_ok=True)
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n{'='*60}")
        print(f"Generation complete. Results saved to {results_file}")
        print(f"{'='*60}\n")
        
        return results


def main():
    parser = argparse.ArgumentParser(description="Run test generation pipeline")
    parser.add_argument("--subjects-dir", default="subjects", help="Subjects directory")
    parser.add_argument("--output-dir", default="generated_tests", help="Output directory")
    parser.add_argument("--model", choices=["your_model", "gpt", "pynguin", "all"], 
                        default="all", help="Which model to run")
    parser.add_argument("--use-real-gpt", action="store_true", 
                        help="Use real GPT API instead of mock")
    
    args = parser.parse_args()
    
    # Configure models based on args
    models_config = {
        "your_model": {"enabled": args.model in ["your_model", "all"]},
        "gpt": {"enabled": args.model in ["gpt", "all"], "use_mock": not args.use_real_gpt},
        "pynguin": {"enabled": args.model in ["pynguin", "all"]},
    }
    
    pipeline = TestGenerationPipeline(
        subjects_dir=args.subjects_dir,
        output_dir=args.output_dir,
        models_config=models_config
    )
    
    pipeline.run_all()


if __name__ == "__main__":
    main()
