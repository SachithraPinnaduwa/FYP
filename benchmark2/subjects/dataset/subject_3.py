import csv
from collections import defaultdict
from typing import Dict, List, Set, AbstractSet

class SalesDataAnalyzer:
    """A realistic data analytics module that processes sales CSV data and performs grouping and aggregation."""
    
    def __init__(self):
        self.raw_data: List[Dict[str, str]] = []
        self.headers: List[str] = []

    def load_csv(self, filepath: str) -> int:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.headers = reader.fieldnames or []
                self.raw_data = [row for row in reader]
                return len(self.raw_data)
        except Exception as e:
            raise RuntimeError(f"Error reading CSV {filepath}") from e

    def total_revenue_by_region(self) -> Dict[str, float]:
        revenue_map = defaultdict(float)
        for row in self.raw_data:
            region = row.get('Region', 'Unknown')
            try:
                revenue = float(row.get('Revenue', 0.0))
                revenue_map[region] += revenue
            except ValueError:
                pass # Skip invalid numbers
                
        return dict(revenue_map)

    def top_performing_salesperson(self, region: str = None) -> str:
        sales = defaultdict(float)
        for row in self.raw_data:
            if region and row.get('Region') != region:
                continue
                
            person = row.get('Salesperson')
            if not person: continue
            
            try:
                val = float(row.get('Revenue', 0.0))
                sales[person] += val
            except ValueError:
                pass
                
        if not sales:
            return "No data"
            
        # Returns the salesperson with max revenue
        return max(sales.items(), key=lambda item: item[1])[0]

    def get_unique_product_categories(self) -> Set[str]:
        categories = {row.get('Category') for row in self.raw_data if row.get('Category')}
        return categories

