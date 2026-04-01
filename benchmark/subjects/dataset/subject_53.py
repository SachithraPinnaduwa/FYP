class PaginationLinks:
    def __init__(self, base_url: str, total_pages: int, current_page: int):
        self.base_url = base_url
        self.total_pages = total_pages
        self.current_page = max(1, min(current_page, total_pages))

    def _make_url(self, page: int) -> str:
        sep = '&' if '?' in self.base_url else '?'
        return f"{self.base_url}{sep}page={page}"

    def get_links(self) -> dict:
        links = {
            "first": self._make_url(1),
            "last": self._make_url(self.total_pages)
        }
        if self.current_page > 1:
            links["prev"] = self._make_url(self.current_page - 1)
        if self.current_page < self.total_pages:
            links["next"] = self._make_url(self.current_page + 1)
        return links