"""
Script to load dataset subjects and generate tests using various models.
This script orchestrates the entire workflow:
1. Load subjects from the KAKA22/CodeRM-UnitTest dataset
2. Save them as Python files
3. Generate tests for each subject using your chosen model (Gemini or your fine-tuned model)
4. Save the generated tests

Supported models:
- gemini / baseline_gpt: Google's Gemini models (requires GEMINI_API_KEY in .env)
- your_model: Your fine-tuned model with LoRA adapters
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List
from tqdm import tqdm

from subjects.dataset_loader import DatasetSubjectLoader, DatasetSubject


class TestGenerationPipeline:
    """
    Pipeline for generating tests from dataset subjects.
    """
    
    def __init__(
        self,
        max_subjects: int = 50,
        split: str = "train",
        model_type: str = "gemini",
        model_name: str = "gemini-1.5-pro",
        model_path: str = "lora_model",
        ollama_base_url: str = "http://localhost:11434",
        output_base_dir: str = None
    ):
        """
        Initialize the test generation pipeline.
        
        Args:
            max_subjects: Maximum number of subjects to process
            split: Dataset split to use
            model_type: Type of model to use ('gemini', 'your_model', 'ollama')
            model_name: Model name (for Gemini/Ollama)
            model_path: Path to LoRA model (for your_model)
            ollama_base_url: Base URL for Ollama API (for ollama)
            output_base_dir: Base directory for generated tests (auto-generated if None)
        """
        self.max_subjects = max_subjects
        self.split = split
        self.model_type = model_type
        self.model_name = model_name
        self.model_path = model_path
        self.ollama_base_url = ollama_base_url
        self.base_dir = Path(__file__).parent
        
        # Set output directory based on model type if not specified
        if output_base_dir is None:
            output_base_dir = f"generated_tests/{model_type}"
        
        self.output_base_dir = self.base_dir / output_base_dir
        self.output_base_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize components
        self.loader = None
        self.generator = None
        self.subjects = []
        
        # Results tracking
        model_info = model_name if model_type in ["gemini", "baseline_gpt", "ollama"] else model_path
        self.results = {
            "model_type": model_type,
            "model_name": model_info,
            "total_subjects": 0,
            "successful_generations": 0,
            "failed_generations": 0,
            "subjects": []
        }
    
    def setup_loader(self):
        """Initialize the dataset loader."""
        print("Setting up dataset loader...")
        self.loader = DatasetSubjectLoader(
            output_dir="subjects_dataset",
            max_subjects=self.max_subjects,
            split=self.split
        )
    
    def setup_generator(self):
        """Initialize the test generator based on model type."""
        print(f"Setting up test generator (type: {self.model_type})...")
        
        if self.model_type == "gemini" or self.model_type == "baseline_gpt":
            print(f"  Model: {self.model_name}")
            
            # Import only when needed
            from models.gemini import GeminiTestGenerator
            self.generator = GeminiTestGenerator(model=self.model_name)
            
            if not self.generator.api_key:
                raise ValueError(
                    "No Gemini API key found. Please set GEMINI_API_KEY in .env file.\n"
   
                )
        
        elif self.model_type == "ollama":
            print(f"  Model: {self.model_name}")
            print(f"  Base URL: {self.ollama_base_url}")
            
            # Import only when needed
            from models.ollama_model import OllamaTestGenerator
            self.generator = OllamaTestGenerator(
                model=self.model_name,
                base_url=self.ollama_base_url
            )
            
            # Check connection
            if not self.generator._check_connection():
                raise ConnectionError(
                    f"Cannot connect to Ollama at {self.ollama_base_url}.\n"
                    "Make sure Ollama is running: ollama serve\n"
                    "Install Ollama from: https://ollama.ai/"
                )
            print("  ✓ Connected to Ollama")
        
        elif self.model_type == "your_model":
            print(f"  Model path: {self.model_path}")
            
            # Import only when needed
            try:
                from models.my_model import YourModelTestGenerator
                self.generator = YourModelTestGenerator(model_path=self.model_path)
                print("  Note: Model will be loaded on first generation (this may take a moment)")
            except ImportError as e:
                raise ImportError(
                    f"Failed to import your_model. Make sure dependencies are installed:\n"
                    f"  pip install unsloth torch transformers\n"
                    f"Error: {e}"
                )
        
        else:
            raise ValueError(
                f"Unknown model type: {self.model_type}. "
                f"Supported types: 'gemini', 'baseline_gpt', 'ollama', 'your_model'"
            )
    
    def load_and_save_subjects(self):
        """Load subjects from dataset and save as Python files."""
        print("\n" + "="*60)
        print("STEP 1: Loading and saving subjects from dataset")
        print("="*60)
        
        # Load the dataset
        self.loader.load_dataset()
        
        # Extract subjects
        self.subjects = self.loader.extract_subjects()
        print(f"Extracted {len(self.subjects)} subjects")
        
        # Save subjects as Python files
        subject_files = self.loader.save_subjects_as_files()
        print(f"Saved {len(subject_files)} subject files")
        
        # Save ground truth tests for comparison
        gt_files = self.loader.save_ground_truth_tests()
        print(f"Saved {len(gt_files)} ground truth test files")
        
        self.results["total_subjects"] = len(self.subjects)
        
        return subject_files
    
    def generate_tests_for_subjects(self):
        """Generate tests for all loaded subjects."""
        print("\n" + "="*60)
        print("STEP 2: Generating tests for subjects")
        print("="*60)
        
        if not self.subjects:
            raise ValueError("No subjects loaded. Run load_and_save_subjects() first.")
        
        for subject in tqdm(self.subjects, desc="Generating tests"):
            subject_result = {
                "id": subject.id,
                "success": False,
                "output_file": None,
                "error": None
            }
            
            try:
                # Generate tests
                print(f"\nGenerating tests for {subject.id}...")
                test_code = self.generator.generate_tests(
                    code=subject.code,
                    problem_description=subject.question
                )
                
                # Save generated tests
                output_file = self.output_base_dir / f"test_{subject.id}.py"
                
                # Add header with metadata
                model_info = self.model_name if self.model_type in ["gemini", "baseline_gpt", "ollama"] else self.model_path
                test_content = f'''"""
Generated Tests for: {subject.id}
Model Type: {self.model_type}
Model: {model_info}
Source: {subject.source}

Problem Description:
{subject.question}
"""

{test_code}
'''
                
                with open(output_file, 'w') as f:
                    f.write(test_content)
                
                subject_result["success"] = True
                subject_result["output_file"] = str(output_file)
                self.results["successful_generations"] += 1
                
                print(f"✓ Successfully generated tests for {subject.id}")
                
            except Exception as e:
                subject_result["error"] = str(e)
                self.results["failed_generations"] += 1
                print(f"✗ Failed to generate tests for {subject.id}: {e}")
            
            self.results["subjects"].append(subject_result)
    
    def save_results_summary(self):
        """Save a summary of the generation results."""
        summary_file = self.output_base_dir / "generation_summary.json"
        
        with open(summary_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\nResults summary saved to {summary_file}")
    
    def print_summary(self):
        """Print a summary of the generation results."""
        print("\n" + "="*60)
        print("GENERATION SUMMARY")
        print("="*60)
        print(f"Total subjects processed: {self.results['total_subjects']}")
        print(f"Successful generations: {self.results['successful_generations']}")
        print(f"Failed generations: {self.results['failed_generations']}")
        print(f"Success rate: {self.results['successful_generations'] / max(self.results['total_subjects'], 1) * 100:.1f}%")
        print("="*60)
    
    def run(self):
        """Run the complete pipeline."""
        print("\n" + "="*60)
        print("TEST GENERATION PIPELINE")
        print("="*60)
        print(f"Max subjects: {self.max_subjects}")
        print(f"Dataset split: {self.split}")
        print(f"Model type: {self.model_type}")
        if self.model_type in ["gemini", "baseline_gpt", "ollama"]:
            print(f"Model name: {self.model_name}")
            if self.model_type == "ollama":
                print(f"Ollama URL: {self.ollama_base_url}")
        else:
            print(f"Model path: {self.model_path}")
        print(f"Output directory: {self.output_base_dir}")
        print("="*60)
        
        # Setup
        self.setup_loader()
        self.setup_generator()
        
        # Load and save subjects
        self.load_and_save_subjects()
        
        # Generate tests
        self.generate_tests_for_subjects()
        
        # Save results
        self.save_results_summary()
        
        # Print summary
        self.print_summary()
        
        print(f"\n✓ Pipeline complete! Generated tests saved to {self.output_base_dir}")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Generate tests from dataset subjects using various models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate tests using Gemini (default)
  python generate_tests_from_dataset.py --model-type gemini --model-name gemini-1.5-pro
  
  # Generate tests using Ollama
  python generate_tests_from_dataset.py --model-type ollama --model-name codellama
  
  # Generate tests using your fine-tuned model
  python generate_tests_from_dataset.py --model-type your_model --model-path lora_model
  
  # Use baseline_gpt (alias for gemini)
  python generate_tests_from_dataset.py --model-type baseline_gpt
  
  # Process 100 subjects with Ollama
  python generate_tests_from_dataset.py --max-subjects 100 --model-type ollama --model-name deepseek-coder
        """
    )
    parser.add_argument(
        "--max-subjects",
        type=int,
        default=50,
        help="Maximum number of subjects to process (default: 50)"
    )
    parser.add_argument(
        "--split",
        default="test",
        help="Dataset split to use (default: test)"
    )
    parser.add_argument(
        "--model-type",
        choices=["gemini", "baseline_gpt", "ollama", "your_model"],
        default="gemini",
        help="Type of model to use (default: gemini)"
    )
    parser.add_argument(
        "--model-name",
        default="gemini-2.5-flash",
        help="Model name for Gemini/Ollama. "
             "Gemini: gemini-1.5-pro, gemini-1.5-flash, gemini-2.0-flash, gemini-2.5-flash. "
             "Ollama: codellama, deepseek-coder, llama2, mistral, etc."
    )
    parser.add_argument(
        "--model-path",
        default="lora_model",
        help="Path to LoRA model for your_model (default: lora_model)"
    )
    parser.add_argument(
        "--ollama-base-url",
        default="http://localhost:11434",
        help="Base URL for Ollama API (default: http://localhost:11434)"
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory for generated tests (default: generated_tests/<model_type>)"
    )
    
    args = parser.parse_args()
    
    # Run the pipeline
    pipeline = TestGenerationPipeline(
        max_subjects=args.max_subjects,
        split=args.split,
        model_type=args.model_type,
        model_name=args.model_name,
        model_path=args.model_path,
        ollama_base_url=args.ollama_base_url,
        output_base_dir=args.output_dir
    )
    
    try:
        pipeline.run()
    except KeyboardInterrupt:
        print("\n\n⚠ Pipeline interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n✗ Pipeline failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
