class InMemoryTable:
    def __init__(self, name: str, columns: list):
        self.name = name
        self.columns = columns
        self.rows = []
        self._auto_id = 1

    def insert(self, record: dict) -> int:
        row = {"_id": self._auto_id}
        for col in self.columns:
            if col in record:
                row[col] = record[col]
            else:
                row[col] = None
                
        self.rows.append(row)
        self._auto_id += 1
        return row["_id"]

    def select(self, conditions: dict = None) -> list:
        if not conditions:
            return [dict(r) for r in self.rows]
            
        results = []
        for row in self.rows:
            match = True
            for k, v in conditions.items():
                if row.get(k) != v:
                    match = False
                    break
            if match:
                results.append(dict(row))
        return results

    def delete(self, conditions: dict) -> int:
        initial_count = len(self.rows)
        self.rows = [r for r in self.rows if not all(r.get(k) == v for k, v in conditions.items())]
        return initial_count - len(self.rows)