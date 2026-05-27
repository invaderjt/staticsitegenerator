import unittest
from block_functions import *


class TestTextNode(unittest.TestCase):
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

    def text_block_to_block_type(self):
        texty = """
### skipadooda

# boopaloo

```
some code goes here
and some more here
```

> first he told me
> then he said
> finally he added

- eggs
- milk
- cheese
- bread

1. help
2. this
3. is 
4. a very 
5. long
6. test string

> this quote
shouldn't work

that will be all
thank you for testing
with me

"""
        output = []
        for line in markdown_to_blocks(texty):
            output.append(block_to_block_type(line))
        match = [BlockType.HEADING, BlockType.HEADING, BlockType.CODE, BlockType.QUOTE, BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST, BlockType.PARAGRAPH, BlockType.PARAGRAPH]
        self.assertListEqual(match, output)


if __name__ == "__main__":
    unittest.main()