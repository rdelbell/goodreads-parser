#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin
import argparse
import os
import datetime
import random

def scrape_group_bookshelf(url):
    """
    Scrape the Goodreads group bookshelf from the provided URL and return a DataFrame with book titles and authors.
    Handles pagination to scrape all available pages.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    all_data = []
    current_url = url

    while True:
        response = requests.get(current_url, headers=headers)
        print(f"Scraping {current_url} - Status: {response.status_code}")
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', id='groupBooks')
        if not table:
            print("Table with id='groupBooks' not found.")
            break
        book_rows = table.find_all('tr')[1:]  # Skip header row
        print(f"Found {len(book_rows)} books on this page.")
        for row in book_rows:
            cells = row.find_all('td')
            if len(cells) >= 3:
                title_link = cells[1].find('a')
                author_link = cells[2].find('a')
                title = title_link.text.strip() if title_link else "N/A"
                author = author_link.text.strip() if author_link else "N/A"
                all_data.append({'Title': title, 'Author': author})
                print(f"Added: {title} by {author}")
        next_page = soup.find('a', rel='next')
        if next_page and 'href' in next_page.attrs:
            current_url = urljoin(current_url, next_page['href'])
            print("Moving to next page:", current_url)
            time.sleep(random.uniform(2, 6))  # Polite delay with random sleep to avoid overloading the server
            time.sleep(1)  # Polite delay to avoid overloading the server
        else:
            print("No next page found, stopping.")
            break
    df = pd.DataFrame(all_data)
    return df

def main():
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description="Scrape Goodreads group bookshelf and save to CSV.")
    parser.add_argument("url", help="URL of the Goodreads group bookshelf to scrape.")
    parser.add_argument("output", help="Path to the output CSV file.")
    args = parser.parse_args()

    # Scrape the bookshelf
    df = scrape_group_bookshelf(args.url)
    
    if df.empty:
        print("No books were scraped. Check the URL or the scraping logic.")
    else:
        # Generate timestamp for the output file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        dir_name = os.path.dirname(args.output)
        final_file_name = f"goodreads_scaper_output_{timestamp}.csv"
        # file_name, file_ext = os.path.splitext(base_name)
        # final_file_name = f"{file_name}_{timestamp}{file_ext}"
        final_output_path = os.path.join(dir_name, final_file_name) if dir_name else final_file_name
        
        # Save the DataFrame to CSV
        df.to_csv(final_output_path, index=False)
        print(f"Saved {len(df)} books to '{final_output_path}'.")

if __name__ == "__main__":
    main()
