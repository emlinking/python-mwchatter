from . import extractor
from . import page


def parse(text, title=None):
    p = page.Page(text, title)

    print("Calling p.extract_comments(extractor.linear_extractor)")
    p.extract_comments(extractor.linear_extractor)
    return p.simplify()
