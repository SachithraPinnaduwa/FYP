import sqlite3
from typing import List, Tuple, Optional

class ProductInventoryDB:
    """A realistic SQLite3 database manager for product inventory."""
    
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self._initialize_schema()

    def _initialize_schema(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                sku TEXT NOT NULL UNIQUE,
                price REAL NOT NULL,
                stock INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add_product(self, name: str, sku: str, price: float, initial_stock: int = 0) -> int:
        if price < 0:
            raise ValueError("Price cannot be negative")
            
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO products (name, sku, price, stock) VALUES (?, ?, ?, ?)',
                (name, sku, price, initial_stock)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            self.conn.rollback()
            raise ValueError(f"Product {name} or SKU {sku} already exists")

    def update_stock(self, sku: str, quantity: int) -> bool:
        cursor = self.conn.cursor()
        
        # We need to read current stock first to prevent going below zero
        cursor.execute('SELECT stock FROM products WHERE sku = ?', (sku,))
        result = cursor.fetchone()
        
        if not result:
            return False
            
        current_stock = result[0]
        new_stock = current_stock + quantity
        
        if new_stock < 0:
            return False # Insufficient stock
            
        cursor.execute('UPDATE products SET stock = ? WHERE sku = ?', (new_stock, sku))
        self.conn.commit()
        return cursor.rowcount > 0

    def get_low_stock_items(self, threshold: int = 10) -> List[Tuple[str, str, int]]:
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT name, sku, stock FROM products WHERE stock < ? ORDER BY stock ASC', 
            (threshold,)
        )
        return cursor.fetchall()
        
    def close(self):
        self.conn.close()
