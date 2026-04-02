from typing import List, Dict
import re

def extract_div_attributes(html_snippet: str) -> List[Dict[str, str]]:
    div_attributes = []
    div_pattern = re.compile(r'<div\s+([^>]+)>')
    attribute_pattern = re.compile(r'(\w+)\s*=\s*["\']([^"\']+)["\']')

    div_matches = div_pattern.findall(html_snippet)
    for match in div_matches:
        attributes = {}
        attribute_matches = attribute_pattern.findall(match)
        for attr, value in attribute_matches:
            attributes[attr] = value
        div_attributes.append(attributes)

    return div_attributes