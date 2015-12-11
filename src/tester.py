import unittest
import WikiComments as wc
import WikiIndentUtils as wiu
import TextBlocks as tb

class TestTextBlocks(unittest.TestCase):

    def test_basic_generate_blocks(self):
        sample = """Level1
                    : Level2
                    Level1
                    : Level2
                    : Level2
                    :: Level3
                    : Level2
                    Level1"""
        blocks = tb._generate_blocks(sample)
        self.assertEqual(len(blocks), 7)

    def test_generate_block_tree(self):
        sample = """Level1a
                    : Level2a
                    Level1b
                    : Level2b
                    : Level2b
                    :: Level3a
                    : Level2d
                    Level1c"""

        root_node = tb.generate_block_tree(sample)
        self.assertEqual(len(root_node.children), 3)
        self.assertEqual(len(root_node.children[1].children), 2)
        self.assertEqual(len(root_node.children[1].children[0].children), 1)
        self.assertEqual(len(root_node.children[1].children[1].children), 0)
        self.assertEqual(len(root_node.children[2].children), 0)
        root_node.pprint("")

class TestWikiIndentUtils(unittest.TestCase):

    def test_extract_indent_blocks(self):
        sample = """Level1
                    : Level2
                    Level1
                    : Level2
                    : Level2
                    :: Level3
                    : Level2
                    Level1"""
        text_blocks = wiu.extract_indent_blocks(sample)
        self.assertEqual(len(text_blocks), 7, text_blocks)

    def test_find_line_indent(self):
        samples = [
                    (" ::: level3", 3),
                    (": level1", 1),
                    ("   * level1", 1),
                    ("  Level0", 0),
                    ("### level3", 3)
                  ]
        for sample, answer in samples:
            indent = wiu.find_line_indent(sample)
            self.assertEqual(indent, answer, indent)

if __name__ == '__main__':
    unittest.main()
