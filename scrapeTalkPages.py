# scrapeTalkPages.py
# Eleanor Lin x ChatGPT
# Usage: python scrapeTalkPages.py [dump-file] [out-dir]
# out-dir should be a directory within which this script will make a subdirectory to store the results of scraping the XML from dump-file

import json
import mwxml
import os
import sys
import tqdm
import wikichatter as wc

def main(fp, dir):
    # read in dump file
    dump = mwxml.Dump.from_file(open(fp))

    # make subdirectory if it does not already exist
    subdirectory = os.path.join(dir, fp.replace(".xml", ""))

    if not os.path.isdir(subdirectory):
        # Create the subdirectory if it does not exist
        os.makedirs(subdirectory)

        print(f"Subdirectory '{subdirectory}' created.")
    else:
        print(f"Subdirectory '{subdirectory}' already exists.")

    # loop over pages in dump file
    for page in tqdm.tqdm(dump):
        
        # grab only the Talk and User talk pages
        if page.namespace in {1,3}:

            # grab most recent revision
            revision = None

            for revision in page:
                pass

            # create filename that saves key info about this page and revision
            save_path = "{}_{}_{}_{}.json".format(page.id,
                                                  page.namespace,
                                                  revision.id, 
                                                  revision.timestamp).replace(":", "-")
            
            save_path = os.path.join(subdirectory, save_path)
            
            # parse the page
            parse = wc.parse(revision.text)

            # save the parse
            # https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/#convert-dictionary-in-python-to-json-file-using-jsondump
            with open(save_path, "w") as outfile:
                json.dump(parse, outfile)

if __name__=="__main__":
    fp, dir = sys.argv[1], sys.argv[2]

    main(fp, dir)