import unittest

class TestMarkdownLinkExtractor(unittest.TestCase):
    def test_basic_link(self):
        md = "Check out [Google](https://google.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["links"]), 1)
        self.assertEqual(result["links"][0]["url"], "https://google.com")
        self.assertEqual(result["links"][0]["text"], "Google")
        
    def test_basic_image(self):
        md = "![alt text](https://example.com/image.png)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(result["images"][0]["url"], "https://example.com/image.png")
        self.assertEqual(result["images"][0]["alt"], "alt text")
        
    def test_link_with_image(self):
        md = "![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_2(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_3(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_4(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_5(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_6(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_7(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_8(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_9(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_10(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_11(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_12(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_13(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_14(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_15(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_16(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_17(self):
        md = "Check out ![alt](img.png) [Link](url.com)"
        extractor = MarkdownLinkExtractor()
        result = extractor.extract_all(md)
        self.assertEqual(len(result["images"]), 1)
        self.assertEqual(len(result["links"]), 1)
        
    def test_link_with_image_in_text_18(self):
        md = "Check