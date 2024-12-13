from . import extractor
from . import page


def parse(text, title=None):
    p = page.Page(text, title)

    print("Calling p.extract_comments(extractor.linear_extractor)")
    p.extract_comments(extractor.linear_extractor)
    
    print("After running comment extractor: p.sections =", p.sections)
    print("After running comment extractor: p.sections[0]._subsections", p.sections[0]._subsections)
    return p.simplify()
