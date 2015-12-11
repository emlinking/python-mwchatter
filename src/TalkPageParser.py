import mwparserfromhell as mwp
import IndentTree
import WikiComments as wc

class Page:
    def __init__(self):
        self.indent = -2

    def __str__(self):
        return "Talk_Page"

class Section:
    def __init__(self, heading):
        self.heading = heading
        self.indent = -1

    def __str__(self):
        return self.heading

def parse(text):
    root = IndentTree.IndentTreeNode(None, Page())
    parse_list = []
    wikicode = mwp.parse(text)
    sections = wikicode.get_sections()
    for section in sections:
        section_text = str(section)
        comments = wc.get_linear_merge_comments(section_text)
        if len(comments) > 0:
            headings = mwp.parse(section_text).filter_headings()
            if len(headings) > 0:
                heading = "\n" + "\n".join([str(h) for h in headings])
            else:
                heading = "NO HEADING FOUND"
            parse_list.append(Section(heading))
        parse_list.extend(comments)
    root.generate_tree_from_list(parse_list)
    return root
