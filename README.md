# Scholarly Publications Fetcher  [![PyPI](https://img.shields.io/pypi/v/scholarly_publications?color=blue)](https://pypi.org/project/scholarly_publications)

The `scholarly_publications` package provides an easy-to-use interface for fetching publication data from Google Scholar. It allows users to retrieve detailed information about an author's publications, including titles, publication years, links, and citation counts. This package is designed for academics, researchers, and anyone interested in programmatically analyzing scholarly publication data.

## Installation

To install `scholarly_publications`, use the following pip command in your terminal:

```bash
pip install scholarly_publications
```

## Usage

### Using the CLI (Command Line Interface)

`scholarly_publications` can be easily used via its command-line interface. Here are some examples:

Fetch all publications for a given author ID:
```bash
scholarly_publications <author_id>
```

Fetch a specific number of publications for a given author ID:
```bash
scholarly_publications <author_id> --max=<number_of_publications>
```

### Using as a Python Package

You can also use `scholarly_publications` directly in your Python code. Here's how:

```python
from scholarly_publications import fetch_all_publications

# Fetch all publications for a given author ID
publications = fetch_all_publications('<author_id>')

# Fetch a specific number of publications for a given author ID
publications = fetch_all_publications('<author_id>', max_publications=<number_of_publications>)

print(publications)
```

## Contributing

We welcome contributions to `scholarly_publications`! If you have suggestions for improvements, please open an issue or a pull request.

## Status

[![Upload Python Package](https://github.com/ezefranca/scholarly_publications/actions/workflows/workflow.yml/badge.svg)](https://github.com/ezefranca/scholarly_publications/actions/workflows/workflow.yml)


## License

`scholarly_publications` is released under the MIT License. See the LICENSE file for more details.
