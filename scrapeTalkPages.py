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
    subdirectory = os.path.join(dir, fp.split("/")[-1].replace(".xml", ""))

    if not os.path.isdir(subdirectory):
        # Create the subdirectory if it does not exist
        os.makedirs(subdirectory)

        print(f"Subdirectory '{subdirectory}' created.")
    else:
        print(f"Subdirectory '{subdirectory}' already exists.")

    # loop over pages in dump file
    # we can extract total count of pages from filename: zhwiki-20240401-pages-meta-history1.xml-p1p2289.bz2 
    pages = fp.split("-")[-1].replace(".bz2", "")
    pages = pages.split("p")
    first, last = int(pages[-2]), int(pages[-1])
    pages = last - first

    # see which pages are already parsed
    processed = os.listdir(subdirectory)
    processed = set([int(filename.split("_")[0]) for filename in processed])

    for page in tqdm.tqdm(dump, total=pages):
        
        # grab only the Talk and User talk pages
        if (page.namespace in {1,3}) and (page.id not in processed):

            # grab most recent revision
            revision = None

            for revision in page:
                pass

            # create filename that saves key info about this page and revision
            save_path = "{}_{}_{}.json".format(page.id,
                                               page.namespace,
                                               revision.id)
            
            save_path = os.path.join(subdirectory, save_path)
            
            # parse the page
            try:
                parse = wc.parse(revision.text)

                # save the parse
                # https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/#convert-dictionary-in-python-to-json-file-using-jsondump
                with open(save_path, "w") as outfile:
                    json.dump(parse, outfile)
            except wc.error.MalformedWikitextError as e:
                print(e)

if __name__=="__main__":
    fp, dir = sys.argv[1], sys.argv[2]
    
    main(fp, dir)