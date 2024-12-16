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
<<<<<<< HEAD
echo python ~/projects/code-switching/wiki/python-mwchatter/scrapeTalkPages.py $UNZIPFILE $OUTDIR
python ~/projects/code-switching/wiki/python-mwchatter/scrapeTalkPages.py $UNZIPFILE $OUTDIR
=======
echo python ~/projects/code-switching/scrapeTalkPages.py $UNZIPDIR/$UNZIPFILE $OUTDIR
python ~/projects/code-switching/scrapeTalkPages.py $UNZIPDIR/$UNZIPFILE $OUTDIR
>>>>>>> a44404e3eb1ee11a892f229096ec3c650d509910

# Check if the scraping succeeded
if [ $? -ne 0 ]; then
    echo "Python script to scrape talk pages failed."
    exit 1
fi

# delete unzipped file to save server space
<<<<<<< HEAD
echo "Successfully completed scraping. Deleting '$UNZIPFILE' to save space."
echo rm $UNZIPFILE
rm $UNZIPFILE
=======
echo "Successfully completed scraping. Deleting '$UNZIPDIR/$UNZIPFILE' to save space."
echo rm $UNZIPDIR/$UNZIPFILE
rm $UNZIPDIR/$UNZIPFILE
>>>>>>> a44404e3eb1ee11a892f229096ec3c650d509910
