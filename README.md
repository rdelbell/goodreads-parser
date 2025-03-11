# goodreads-parser

# Goodreads Group Bookshelf Scraper

## Overview
This tool scrapes a Goodreads group bookshelf and saves the list of books (title and author) to a CSV file. It handles pagination to collect all books across multiple pages, making it ideal for archiving or analyzing group reading lists.

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`

## Running the tool

```
python scraper.py "https://www.goodreads.com/group/bookshelf/1126547-the-emerald?utf8=%E2%9C%93&per_page=100" .

Scraping https://www.goodreads.com/group/bookshelf/1126547-the-emerald?utf8=%E2%9C%93&per_page=100 - Status: 200
Found 100 books on this page.
Added: Crime and Punishment by Dostoevsky, Fyodor
Added: Man’s Search for Meaning by Frankl, Viktor E.
Added: The Wasteland, Prufrock and Other Poems by Eliot, T.S.
Added: The Complete Poems of Emily Dickinson by Dickinson, Emily
Added: The Book of Hours by Rilke, Rainer Maria
Added: The Turquoise Bee: The Tantric Lovesongs of the Sixth Dalai Lama by Gyatso, Tsangyang
[...]
Added: The Cult of the Black Virgin by Begg, Ean
No next page found, stopping.
Saved 610 books to 'goodreads_scaper_output_20250311_110125.csv'.
```
