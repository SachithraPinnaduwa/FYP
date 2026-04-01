import unittest

class TestSalesDataAnalyzer(unittest.TestCase):
    """Test suite for SalesDataAnalyzer class."""
    
    def setUp(self):
        self.analyzer = SalesDataAnalyzer()
        self.test_data = [
            {'Region': 'North', 'Salesperson': 'Alice', 'Revenue': 1000, 'Category': 'Electronics'},
            {'Region': 'North', 'Salesperson': 'Bob', 'Revenue': 1500, 'Category': 'Electronics'},
            {'Region': 'South', 'Salesperson': 'Alice', 'Revenue': 2000, 'Category': 'Clothing'},
            {'Region': 'South', 'Salesperson': 'Charlie', 'Revenue': 800, 'Category': 'Electronics'},
            {'Region': 'East', 'Salesperson': 'Bob', 'Revenue': 1200, 'Category': 'Clothing'},
        ]
        
        # Mock CSV file content
        self.mock_csv_content = """Region,Salesperson,Revenue,Category
North,Alice,1000,Electronics
North,Bob,1500,Electronics
South,Alice,2000,Clothing
South,Charlie,800,Electronics
East,Bob,1200,Clothing
"""
    
    def test_load_csv(self):
        """Test loading CSV data."""
        # Create a temporary file
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(self.mock_csv_content)
            temp_file = f.name
        
        try:
            count = self.analyzer.load_csv(temp_file)
            self.assertEqual(count, 5)
            self.assertEqual(self.analyzer.headers, ['Region', 'Salesperson', 'Revenue', 'Category'])
        finally:
            import os
            os.unlink(temp_file)
    
    def test_total_revenue_by_region(self):
        """Test revenue aggregation by region."""
        # Load test data
        self.analyzer.load_csv(self.mock_csv_content)
        
        result = self.analyzer.total_revenue_by_region()
        
        # Check expected results
        self.assertIn('North', result)
        self.assertIn('South', result)
        self.assertIn('East', result)
        self.assertEqual(result['North'], 2500)
        self.assertEqual(result['South'], 2800)
        self.assertEqual(result['East'], 1200)
    
    def test_top_performing_salesperson(self):
        """Test finding top salesperson."""
        self.analyzer.load_csv(self.mock_csv_content)
        
        # Test without region filter
        top_salesperson = self.analyzer.top_performing_salesperson()
        self.assertIn(top_salesperson, ['Alice', 'Bob', 'Charlie'])
        
        # Test with region filter
        top_salesperson_north = self.analyzer.top_performing_salesperson('North')
        self.assertEqual(top_salesperson_north, 'Bob')
        
        top_salesperson_south = self.analyzer.top_performing_salesperson('South')
        self.assertEqual(top_salesperson_south, 'Alice')
    
    def test_get_unique_product_categories(self):
        """Test getting unique product categories."""
        self.analyzer.load_csv(self.mock_csv_content)
        
        categories = self.analyzer.get_unique_product_categories()
        
        self.assertIn('Electronics', categories)
        self.assertIn('Clothing', categories)
        self.assertEqual(len(categories), 2)
    
    def test_invalid_revenue_handling(self):
        """Test handling of invalid revenue values."""
        invalid_data = [
            {'Region': 'North', 'Salesperson': 'Alice', 'Revenue': 'invalid', 'Category': 'Electronics'},
            {'Region': 'North', 'Salesperson': 'Bob', 'Revenue': 1500, 'Category': 'Electronics'},
        ]
        
        self.analyzer.raw_data = invalid_data
        
        # Should not raise exception, just skip invalid entries
        result = self.analyzer.total_revenue_by_region()
        self.assertEqual(len(result), 1)
        self.assertEqual(list(result.values())[0], 1500)

if __name__ == '__main__':
    unittest.main()
