import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# Function to fetch a page
def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {url}", e)
        return None

# Function to scrape all pages
def scrape_all_pages():
    base_url = "https://999.md/ro/list/transport/cars?page="
    page = 1
    no_announcements = False
    today = datetime.now()
    formatted_date = f"{today.year}_{today.month:02}_{today.day:02}"
    results_file = f"scrapped_{formatted_date}.json"

    # Initialize the results file
    with open(results_file, 'w') as file:
        file.write("[")

    while not no_announcements:
        url = f"{base_url}{page}"
        soup = fetch_page(url)

        if soup is None:
            print(f"Failed to load page {page}")
            break

        announcements = soup.select(".ads-list-photo.large-photo .ads-list-photo-item")

        if len(announcements) == 0:
            no_announcements = True
            print(f"No announcements found on page {page}. Stopping.")
            break

        page_results = []

        for element in announcements:
            classes = element.get("class", [])
            if "js-booster-inline" in classes or "is-adsense" in classes:
                continue

            title_element = element.select_one(".ads-list-photo-item-title a")
            price_element = element.select_one(".ads-list-photo-item-price-wrapper")

            title = title_element.get_text(strip=True) if title_element else None
            price = price_element.get_text(strip=True).replace("\xa0", " ") if price_element else None
            href = title_element.get("href") if title_element else None
            id = href.split("/").pop() if href else None
            img_element = element.select_one(".ads-list-photo-item-thumb img")
            img_url = img_element.get("src") if img_element else None

            if not title or not id:
                continue

            page_results.append({
                "id": id,
                "title": title,
                "price": price,
                "image": img_url,
            })

        if page_results:
            with open(results_file, 'a') as file:
                data = json.dumps(page_results, indent=4)[1:-1]  # Remove surrounding brackets
                file.write((", " if page > 1 else "") + data)

        print(f"Page {page} processed.")
        page += 1

    # Finalize the results file
    with open(results_file, 'a') as file:
        file.write("]")

    print(f"Results have been saved to {results_file}")

# Start scraping
scrape_all_pages()
