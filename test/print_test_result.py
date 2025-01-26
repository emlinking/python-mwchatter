import json
import pprint
import argparse

def read_and_pretty_print_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        pprint.pprint(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read and pretty print a JSON file.')
    parser.add_argument('file_path', type=str, help='The path to the JSON file')
    args = parser.parse_args()
    
    read_and_pretty_print_json(args.file_path)