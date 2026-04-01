import re

class HTMLSanitizer:
    def __init__(self):
        self.allowed_tags = {"b", "i", "em", "strong", "a"}
        self.tag_pattern = re.compile(r'<(/?)(\w+)([^>]*)>')

    def sanitize(self, html_input: str) -> str:
        def replace_tag(match):
            is_closing = match.group(1) == '/'
            tag_name = match.group(2).lower()
            if tag_name in self.allowed_tags:
                if is_closing:
                    return f"</{tag_name}>"
                # Strip all attributes for safety
                return f"<{tag_name}>"
            return ""

        # Remove script tags and content entirely
        no_scripts = re.sub(r'<script.*?>.*?</script>', '', html_input, flags=re.IGNORECASE | re.DOTALL)
        
        # Sanitize remaining HTML
        return self.tag_pattern.sub(replace_tag, no_scripts)