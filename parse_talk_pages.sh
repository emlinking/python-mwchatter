# parse_talk_pages.sh
# Usage: parse_talk_pages.sh [zipped-filepath] [unzipped-dir] [out-dir]

ZIPFILE=$1

UNZIPFILE="${ZIPFILE##*/}"
UNZIPFILE="${UNZIPFILE%.*}"

UNZIPDIR=$2

OUTDIR=$3

# unzip file
if [ -f "$UNZIPDIR/$UNZIPFILE" ]; then
    echo "The file '$UNZIPDIR/$UNZIPFILE ' already exists. Skipping unzip."
else
    echo bzip2 -cdk $ZIPFILE > $UNZIPDIR/$UNZIPFILE 
    bzip2 -cdk $ZIPFILE > $UNZIPDIR/$UNZIPFILE 
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
echo "Successfully completed scraping. Deleting '$UNZIPDIR/$UNZIPFILE' to save space."
echo rm $UNZIPDIR/$UNZIPFILE
rm $UNZIPDIR/$UNZIPFILE
