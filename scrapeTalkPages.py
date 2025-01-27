# scrapeTalkPages.py
# Eleanor Lin x ChatGPT
# Usage: python scrapeTalkPages.py [dump-file] [out-dir]
# out-dir should be a directory within which this script will make a subdirectory to store the results of scraping the XML from dump-file

import json
import mwxml
import os
import sys
import tqdm
import mwchatter as wc
import bz2

def main(fp, output_dir):
    # open the bz2 file
    with bz2.open(fp) as file:
        dump = mwxml.Dump.from_file(file)

        # make subdirectory if it does not already exist
        # dump file name format: zhwiki-20240401-pages-meta-history1.xml-p1p2289.bz2 
        subdirectory = os.path.join(output_dir, fp.split("/")[-1].replace(".bz2", "").replace(".xml", ""))

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
        pages = last - first + 1

        # see which pages are already parsed
        # files are named in format "{page.id}_{page.namespace}_{revision.id}.json"
        processed = os.listdir(subdirectory)
        processed = set()
        for filename in os.listdir(subdirectory):
            try:
                processed.add(int(filename.split("_")[0]))
            except ValueError:
                print(f"Skipping adding file '{filename}' to processed list, as it does not start with an integer.")

        print("Already processed {} files from this dump".format(len(processed)))
        print("Processing remaining {} pages from this dump".format(pages - len(processed)))

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
                    print("Encountered malformed Wikitext on page '{}' (id: {})".format(page.title, page.id))
                    print("Error:", e)
                except wc.signatureutils.NoUsernameError as e:
                    print("Encountered signature missing username on page '{}' (id: {})".format(page.title, page.id))
                    print("Error:", e)
                except Exception as e:
                    print("Encountered exception while parsing page '{}' (id: {})".format(page.title, page.id))
                    print("Error:", e)

if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Usage: python scrapeTalkPages.py [dump-file] [out-dir]")
        sys.exit(1)
    fp, output_dir = sys.argv[1], sys.argv[2]
    
    main(fp, output_dir)