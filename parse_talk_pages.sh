# parse_talk_pages.sh
# Usage: parse_talk_pages.sh [zipped-filepath] [out-dir]

ZIPFILE=$1

UNZIPFILE="${ZIPFILE%.*}"

OUTDIR=$2

# unzip file
if [ -f "$UNZIPFILE" ]; then
    echo "The file '$UNZIPFILE' already exists. Skipping unzip."
else
    echo bzip2 -dk $ZIPFILE
    bzip2 -dk $ZIPFILE
fi

# scrape file
echo python ~/projects/code-switching/wiki/python-mwchatter/scrapeTalkPages.py $UNZIPFILE $OUTDIR
python ~/projects/code-switching/wiki/python-mwchatter/scrapeTalkPages.py $UNZIPFILE $OUTDIR

# Check if the scraping succeeded
if [ $? -ne 0 ]; then
    echo "Python script to scrape talk pages failed."
    exit 1
fi

# delete unzipped file to save server space
echo "Successfully completed scraping. Deleting '$UNZIPFILE' to save space."
echo rm $UNZIPFILE
rm $UNZIPFILE
