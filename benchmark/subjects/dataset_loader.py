"""
Dataset-based subjects loader for benchmark.
Loads subjects from the KAKA22/CodeRM-UnitTest dataset used for training.
"""

import os
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from datasets import load_dataset


@dataclass
class DatasetSubject:
    """A subject loaded from the dataset."""
    id: str
    question: str
    code: str
    ground_truth_tests: List[str]
    difficulty: str = ""
    source: str = "KAKA22/CodeRM-UnitTest"


class DatasetSubjectLoader:
    """
    Loads subjects from the KAKA22/CodeRM-UnitTest dataset.
    """
    
    def __init__(
        self,
        output_dir: str = "subjects_dataset",
        cache_dir: Optional[str] = None,
        max_subjects: Optional[int] = 50,
        split: str = "test"
    ):
        """
        Initialize the dataset loader.
        
        Args:
            output_dir: Directory to save extracted subjects
            cache_dir: HuggingFace cache directory
            max_subjects: Maximum number of subjects to load (default: 50, None for all)
            split: Dataset split to use ('train', 'test', or 'validation')
        """
        self.base_dir = Path(__file__).parent.parent
        self.output_dir = self.base_dir / output_dir
        self.cache_dir = cache_dir
        self.max_subjects = max_subjects
        self.split = split
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.dataset = None
        self.subjects: List[DatasetSubject] = []
    
    def load_dataset(self) -> None:
        """Load the dataset from HuggingFace."""
        print(f"Loading KAKA22/CodeRM-UnitTest dataset (split: {self.split})...")
        
        try:
            # Try loading the specified split
            self.dataset = load_dataset(
                "KAKA22/CodeRM-UnitTest",
                split=self.split,
                cache_dir=self.cache_dir
            )
        except ValueError:
            # If test split doesn't exist, use train split with a subset
            print(f"Split '{self.split}' not found, using 'train' split...")
            full_dataset = load_dataset(
                "KAKA22/CodeRM-UnitTest",
                split="train",
                cache_dir=self.cache_dir
            )
            # Use last 20% as test set
            if self.split == "test":
                split_idx = int(len(full_dataset) * 0.8)
                self.dataset = full_dataset.select(range(split_idx, len(full_dataset)))
            else:
                self.dataset = full_dataset
        
        print(f"Loaded {len(self.dataset)} examples")
    
    def extract_subjects(self) -> List[DatasetSubject]:
        """
        Extract subjects from the dataset.
        
        Returns:
            List of DatasetSubject objects
        """
        if self.dataset is None:
            self.load_dataset()
        
        self.subjects = []
        num_to_process = min(len(self.dataset), self.max_subjects or len(self.dataset))
        
        print(f"Extracting {num_to_process} subjects...")
        
        for idx in range(num_to_process):
            example = self.dataset[idx]
            
            # Extract fields from the dataset
            question = example.get("question", "")
            code = example.get("code_ground_truth", "")
            unit_tests = example.get("unit_tests", [])
            
            # Skip if no code
            if not code or not code.strip():
                continue
            
            # Generate a unique ID based on the code
            code_hash = hashlib.md5(code.encode()).hexdigest()[:8]
            subject_id = f"subject_{idx:04d}_{code_hash}"
            
            # Extract test code from unit_tests list
            ground_truth_tests = []
            if unit_tests:
                for test_item in unit_tests:
                    if isinstance(test_item, dict) and test_item.get("code"):
                        ground_truth_tests.append(test_item["code"])
                    elif isinstance(test_item, str):
                        ground_truth_tests.append(test_item)
            
            subject = DatasetSubject(
                id=subject_id,
                question=question,
                code=code,
                ground_truth_tests=ground_truth_tests,
            )
            
            self.subjects.append(subject)
        
        print(f"Extracted {len(self.subjects)} valid subjects")
        return self.subjects
    
    def save_subjects_as_files(self) -> Dict[str, Path]:
        """
        Save each subject's code as a Python file.
        
        Returns:
            Dictionary mapping subject ID to file path
        """
        if not self.subjects:
            self.extract_subjects()
        
        file_paths = {}
        
        for subject in self.subjects:
            # Create the Python file with the code
            file_path = self.output_dir / f"{subject.id}.py"
            
            # Add module docstring with the question
            module_content = f'''"""
Dataset Subject: {subject.id}
Source: {subject.source}

Problem Description:
{subject.question}
"""

{subject.code}
'''
            
            with open(file_path, 'w') as f:
                f.write(module_content)
            
            file_paths[subject.id] = file_path
        
        # Save metadata
        metadata_file = self.output_dir / "subjects_metadata.json"
        metadata = [asdict(s) for s in self.subjects]
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"Saved {len(file_paths)} subject files to {self.output_dir}")
        print(f"Metadata saved to {metadata_file}")
        
        return file_paths
    
    def save_ground_truth_tests(self, output_dir: str = "ground_truth_tests") -> Dict[str, Path]:
        """
        Save ground truth tests for comparison.
        
        Args:
            output_dir: Directory to save ground truth tests
            
        Returns:
            Dictionary mapping subject ID to test file path
        """
        if not self.subjects:
            self.extract_subjects()
        
        gt_dir = self.base_dir / output_dir
        gt_dir.mkdir(parents=True, exist_ok=True)
        
        file_paths = {}
        
        for subject in self.subjects:
            if not subject.ground_truth_tests:
                continue
            
            file_path = gt_dir / f"test_{subject.id}.py"
            
            # Combine all ground truth tests
            test_content = f'''"""
Ground Truth Tests for: {subject.id}
Source: {subject.source}
"""

import unittest
import sys
sys.path.insert(0, '..')

# Import the subject module
try:
    from subjects_dataset.{subject.id} import *
except ImportError:
    pass

# Ground truth tests from the dataset
{chr(10).join(subject.ground_truth_tests)}


if __name__ == '__main__':
    unittest.main()
'''
            
            with open(file_path, 'w') as f:
                f.write(test_content)
            
            file_paths[subject.id] = file_path
        
        print(f"Saved {len(file_paths)} ground truth test files to {gt_dir}")
        
        return file_paths
    
    def get_subject_by_id(self, subject_id: str) -> Optional[DatasetSubject]:
        """Get a subject by its ID."""
        for subject in self.subjects:
            if subject.id == subject_id:
                return subject
        return None
    
    def get_subjects_with_tests(self) -> List[DatasetSubject]:
        """Get only subjects that have ground truth tests."""
        return [s for s in self.subjects if s.ground_truth_tests]


def setup_dataset_benchmark(
    max_subjects: int = 50,
    split: str = "train",
    start_idx: int = 0
) -> Tuple[Path, Path, List[DatasetSubject]]:
    """
    Set up the benchmark using the dataset.
    
    Args:
        max_subjects: Maximum number of subjects to use
        split: Dataset split to use
        start_idx: Starting index in the dataset (to get different examples)
        
    Returns:
        Tuple of (subjects_dir, ground_truth_dir, subjects_list)
    """
    loader = DatasetSubjectLoader(
        output_dir="subjects_dataset",
        max_subjects=max_subjects,
        split=split
    )
    
    # Load and skip to start_idx
    loader.load_dataset()
    
    # Manually adjust dataset to start from start_idx
    if start_idx > 0 and start_idx < len(loader.dataset):
        end_idx = min(start_idx + max_subjects, len(loader.dataset))
        loader.dataset = loader.dataset.select(range(start_idx, end_idx))
    
    loader.extract_subjects()
    loader.save_subjects_as_files()
    loader.save_ground_truth_tests()
    
    return (
        loader.output_dir,
        loader.base_dir / "ground_truth_tests",
        loader.subjects
    )


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Load subjects from dataset")
    parser.add_argument("--max-subjects", type=int, default=50, help="Max subjects to load")
    parser.add_argument("--split", default="train", help="Dataset split")
    parser.add_argument("--start-idx", type=int, default=0, help="Starting index")
    
    args = parser.parse_args()
    
    subjects_dir, gt_dir, subjects = setup_dataset_benchmark(
        max_subjects=args.max_subjects,
        split=args.split,
        start_idx=args.start_idx
    )
    
    print(f"\nSetup complete!")
    print(f"Subjects directory: {subjects_dir}")
    print(f"Ground truth tests: {gt_dir}")
    print(f"Total subjects with tests: {len([s for s in subjects if s.ground_truth_tests])}")
