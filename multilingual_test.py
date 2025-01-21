# multlingual_test.py
import json
import os
import pprint
import wikichatter as wc

TEST_DIR = "test/"
TEST_FILES = "test/multilingual_test_list.txt"

def main():
    with open(TEST_FILES, "r") as f:
        test_files = f.readlines()

        for tf in test_files:
            url = tf.strip().split(",")[1]
            tf = os.path.join(TEST_DIR, tf.strip().split(",")[0])

            test_text = open(tf, "r").read()

            parse = wc.parse(test_text)

            outpath = os.path.join("test/", tf, ".json")

            with open(outpath, "w") as f:
                json.dump(parse, f)
                
            print(tf, url, outpath)

if __name__=="__main__":
    main()