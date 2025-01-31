# MWChatter
This is a library currently in development to parse conversations on Wikipedia
talk pages.

I (emlinking) have made some modifications to accomodate parsing Chinese Wiki Talk Pages, in addition to English ones.

## Files added by emlinking
- test/multilingual_test.py: run to test parsing of English and non-English pages
- test/print_test_result.py: show section of a parsed test page

## Basic use ##
    import wikichatter as wc

    text = open(some_talk_page).read()
    parsed_text = wc.parse(text)
    print(parse_text)

## Current output ##
`tpp.parse()` generates output composed of dictionaries and lists
observing the following json schema

    {
        "$schema": "http://json-schema.org/draft-04/schema#",

        "definitions": {
            "page": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "sections": {
                        "type": "array",
                        "items": {"$ref": "#/definitions/section"}
                    }
                }
            },
            "section": {
                "type": "object",
                "properties": {
                    "heading": {"type": "string"},
                    "comments": {
                        "type": "array",
                        "items": {"$ref": "#/definitions/comment"}
                    },
                    "subsections": {
                        "type": "array",
                        "items": {"$ref": "#/definitions/section"}
                    }
                }
            },
            "comment": {
                "type": "object",
                "properties": {
                    "author": {"type": "string"},
                    "time_stamp": {"$ref": "#/definitions/time_stamp"},
                    "comments": {
                        "type": "array",
                        "items": {"$ref": "#/definitions/comment"}
                    },
                    "text_blocks": {
                        "type": "array",
                        "items": {"$ref": "#/definitions/text_block"}
                    },
                    "cosigners": {
                        "type": "array",
                        "items": {"$ref": "#/definitions/signature"}}
                }
            },
            "signature": {
                "type": "object",
                "properties": {
                    "author": {"type": "string"},
                    "time_stamp": {"$ref": "#/definitions/time_stamp"}
                }
            },
            "text_block": {
                "type": "string"
            },
            "time_stamp": {
                "type": "string",
                "pattern": "[0-9]{2}:[0-9]{2}, [0-9]{1,2} [a-zA-Z]+ [0-9]{4} \\(UTC\\)"
            }
        },

        "$ref": "#/definitions/page"
    }

`cosigners` of a comment are found when multiple signatures all occur on the same line.
In this case the first is designated the signer and the rest are listed as cosigners.

## Known Problems ##
* We currently assemble comments linearly, this occasionally leads to a mis-attribution
of text. In some cases a person will reply within another person's comment. In this
case the person replying will have the text they are replying to attributed to them.
* Responses are based on indentation. On occasion a person replying will break
indentation, moving up a level. This leads their entire comment to be moved up
a level. This has specifically been observed to happen when a user inserts an
image, since attempting to indent the image may not make sense. In this cases
users commenting below them will be interpreted to be replying to the person
that broke indentation rather than the original poster.

Additional issues (added by emlinking):
* Even in the original package, sometimes an extra empty comment is parsed at the end of a section.
* The package may miss user signatures in some cases--_find_signatures_in_nodes() searches for signatures by first looking for timestamps. When users don't use the default signature formatting (see below for an example from https://zh.wikipedia.org/wiki/User_talk:Mayfly~zhwiki), the parse will not capture their signatures from the text.

Keegan Peterzell
維基媒體基金會社群聯絡員

2015年3月20日 (五) 10:40 (UTC) 

* The lead of a talk page and subsequent comments may get parsed as a single comment if the users did not properly start a section to put their comment into.

## Running tests ##
From base directory
`python -m unittest test.<text_file>`

# Authors

* Kevin Schiroo
* Eleanor Lin

