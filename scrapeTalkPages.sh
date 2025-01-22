#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <out-dir> <screen-name-prefix> <dump-file-list>"
    exit 1
fi

# Assign the arguments to variables
OUT_DIR=$1
SCREEN_NAME_PREFIX=$2
DUMP_FILE_LIST=$3

# Check if the file exists
if [ ! -f "$DUMP_FILE_LIST" ]; then
    echo "File not found: $DUMP_FILE_LIST"
    exit 1
fi

# Read each line from the file and store it in an array
DUMP_FILES=()
while IFS= read -r line; do
    DUMP_FILES+=("$line")
done < "$DUMP_FILE_LIST"

# Iterate over each dump file in the array
for DUMP_FILE in "${DUMP_FILES[@]}"; do
    # Extract the base name of the dump file to use in the screen name
    BASE_NAME=$(basename "$DUMP_FILE")
    
    # Create a unique screen name using the prefix and base name
    SCREEN_NAME="${SCREEN_NAME_PREFIX}_${BASE_NAME}"
    
    # Start a new detached screen session with the created screen name
    screen -dmS "$SCREEN_NAME" bash -c "python3 scrapeTalkPages.py \"$DUMP_FILE\" \"$OUT_DIR\""
    if [ $? -ne 0 ]; then
        echo "Failed to start screen session: $SCREEN_NAME"
        exit 1
    fi
done