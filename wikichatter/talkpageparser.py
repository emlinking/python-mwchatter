from . import extractor
from . import page


def parse(text, title=None):
    p = page.Page(text, title)

    print("Calling extract_comments()")
    print("Before running comment extractor: p.sections =", p.sections)
    print("Before running comment extractor: p.sections[0].comments =", p.sections[0].comments)
    print("Before running comment extractor: p.sections[0]._subsections", p.sections[0]._subsections)
    print("Before running comment extractor: p.sections[0]._subsections[0].comments", p.sections[0]._subsections[0].comments)
    p.extract_comments(extractor.linear_extractor)
    
    print("After running comment extractor: p.sections =", p.sections)
    print("After running comment extractor: p.sections[0].comments =", p.sections[0].comments)
    print("After running comment extractor: p.sections[0]._subsections", p.sections[0]._subsections)
    print("After running comment extractor: p.sections[0]._subsections[0].comments", p.sections[0]._subsections[0].comments)
    return p.simplify()
