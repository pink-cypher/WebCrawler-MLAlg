#!/usr/bin/env python3
"""
Directory Fuzzer Wordlist Generator

This script generates a directory fuzzer wordlist from crawled website data.
It can be run directly from the command line.

Usage:
    python generate_directory_wordlist.py --input crawled_data.csv --output directory_wordlist.txt

Options:
    --input     Path to the crawled data CSV (default: backend/data/crawled_data.csv)
    --output    Path for the output wordlist file (default: backend/data/directory_wordlist.txt) 
"""

import argparse
from directory_fuzzer import create_directory_wordlist

def main():
    parser = argparse.ArgumentParser(description="Generate a directory fuzzer wordlist from crawled website data")
    parser.add_argument('--input', default='backend/data/crawled_data.csv', 
                        help='Path to the crawled data CSV file')
    parser.add_argument('--output', default='backend/data/directory_wordlist.txt',
                        help='Path for the output wordlist file')
    
    args = parser.parse_args()
    
    print(f"Generating directory fuzzer wordlist...")
    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    
    # Generate the wordlist
    wordlist = create_directory_wordlist(args.input, args.output)
    
    print(f"Successfully generated directory wordlist with {len(wordlist)} entries")
    print(f"Sample entries: {', '.join(wordlist[:10])}")

if __name__ == "__main__":
    main()