import argparse
from .fetcher import fetch_all_publications
import json

def main():
    parser = argparse.ArgumentParser(description="Fetch publications from Google Scholar.")
    parser.add_argument("author_id", help="Google Scholar author ID")
    parser.add_argument("--max", type=int, default=None, help="Maximum number of publications to fetch")
    parser.add_argument("--sortby", type=str, default=None, help="How to sort publications (cited/pubdate)")
    args = parser.parse_args()

    publications = fetch_all_publications(args.author_id, args.max, args.sortby)
    print(json.dumps(publications, indent=4))
    print()

if __name__ == "__main__":
    main()
