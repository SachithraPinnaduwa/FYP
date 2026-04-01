import re

class MarkdownLinkExtractor:
    def __init__(self):
        self.link_pattern = re.compile(r'\[(.*?)\]\((.*?)\)')
        self.image_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')

    def extract_all(self, md_text: str) -> dict:
        results = {"links": [], "images": []}
        
        # We need to process line by line or findall
        # Need to be careful not to conflate links with images
        
        # A simple approach: find images first, register indices, then links
        for m in self.image_pattern.finditer(md_text):
            results["images"].append({
                "alt": m.group(1),
                "url": m.group(2),
                "pos": m.span()
            })
            
        for m in self.link_pattern.finditer(md_text):
            span = m.span()
            # if preceded by '!', it's an image, skip it
            if span[0] > 0 and md_text[span[0]-1] == '!':
                continue
            results["links"].append({
                "text": m.group(1),
                "url": m.group(2),
                "pos": span
            })
            
        return results