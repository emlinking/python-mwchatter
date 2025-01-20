# multlingual_test.py
import os
import wikichatter as wc

TEST_DIR = "test/"
TEST_FILES = "test/multilingual_test_list.txt"

def main():
    with open(TEST_FILES, "r") as f:
        test_files = f.readlines()

        for tf in test_files:
            tf = os.path.join(TEST_DIR, tf.strip().split(",")[0])

            test_text = open(tf, "r").read()

            parse = wc.parse(test_text)
            print(parse)
            
if __name__=="__main__":
    main()