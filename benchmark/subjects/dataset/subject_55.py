class AutocompleteSystem:
    def __init__(self, sentences: list, times: list):
        self.root = {}
        self.search_term = ""
        self.curr = self.root
        for s, t in zip(sentences, times):
            self.add_record(s, t)

    def add_record(self, sentence: str, time: int):
        node = self.root
        for char in sentence:
            if char not in node:
                node[char] = {"#": 0}
            node = node[char]
            node["#"] += time

    def input(self, c: str) -> list:
        if c == "#":
            self.add_record(self.search_term, 1)
            self.search_term = ""
            self.curr = self.root
            return []
            
        self.search_term += c
        if self.curr and c in self.curr:
            self.curr = self.curr[c]
            return self._get_top_3(self.curr, self.search_term)
        
        self.curr = None
        return []

    def _get_top_3(self, node: dict, prefix: str) -> list:
        results = []
        self._dfs(node, prefix, results)
        results.sort(key=lambda x: (-x[1], x[0]))
        return [res[0] for res in results[:3]]

    def _dfs(self, node: dict, path: str, results: list):
        if "#" in node and node.get("#", 0) > 0:
            results.append((path, node["#"]))
        for char, child in node.items():
            if char != "#":
                self._dfs(child, path + char, results)