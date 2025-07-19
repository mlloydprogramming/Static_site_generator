import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, code_block_to_html_node, paragraph_block_to_html_node, blockquote_to_html_node
from block_type import BlockType
class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE_BLOCK)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # def test_code_block_to_html_node(self):
    #     block = "```\ncode\nand more code\n```"
    #     print(code_block_to_html_node(block))

    # def test_paragraph_block_to_html_node(self):
    #     block = """
    #     This is a **paragraph** with _some_ text.
    #     some more text here.

    #     this is a new paragraph
    #     """
    #     print(paragraph_block_to_html_node(block))

    def test_blockquote_to_html_node(self):
        block = "> This is a quote\n> with multiple lines"
        print(blockquote_to_html_node(block))



if __name__ == "__main__":
    unittest.main()
