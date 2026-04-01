class Paginator:
    def __init__(self, data: list, page_size: int = 10):
        self.data = data
        self.page_size = max(1, page_size)
        self.total_items = len(data)
        
    @property
    def total_pages(self) -> int:
        return (self.total_items + self.page_size - 1) // self.page_size

    def get_page(self, page_number: int) -> list:
        if page_number < 1 or page_number > self.total_pages:
            return []
            
        start_idx = (page_number - 1) * self.page_size
        end_idx = start_idx + self.page_size
        return self.data[start_idx:end_idx]
        
    def get_page_info(self, page_number: int) -> dict:
        return {
            "current_page": page_number,
            "total_pages": self.total_pages,
            "has_next": page_number < self.total_pages,
            "has_prev": page_number > 1,
            "data": self.get_page(page_number)
        }