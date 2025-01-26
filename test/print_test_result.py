import json
import pprint
import argparse

def read_and_pretty_print_json(file_path, head):
    with open(file_path, 'r') as file:
        data = json.load(file)

        for section in data["sections"]:
            if section["heading"] == head:
                pprint.pprint(section)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read and pretty print a JSON file.')
    parser.add_argument('file_path', type=str, help='The path to the JSON file')
    parser.add_argument('section', type=str, help="Name of section to display")
    args = parser.parse_args()
    
    read_and_pretty_print_json(args.file_path, args.section)