# Usage: ./scrapeTalkPages.sh [file-with-input-filepaths] [out-dir] [screen-prefix]
# Read the list of zipped filenames
input_file="$1"

# Loop through each filename in the input file
while IFS= read -r filename; do
    # Extract the part of the filename for the screen name
    screen_name=$(echo "$filename" | grep -oP 'p\d+p\d+')

    # concat screen_name and screen-prefix
    screen_name="${3}_$screen_name"

    # Open a new screen and run the Python script
    screen -dmS "process_$screen_name" bash -c "python3 scrapeTalkPages.py $filename $2"
done < "$input_file"

echo "All screens have been launched."