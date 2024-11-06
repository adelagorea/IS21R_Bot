# Car Listings Scraper

This project contains a simple web scraping script (`scrapper.py`) that fetches car listings from the moldavian website [999.md](https://999.md). It extracts details like the car title, price, and image URL from multiple pages and saves them in a JSON file.

## Features

- Scrapes car listings from [999.md](https://999.md).
- Extracts data like the car title, price, and image URL.
- Saves the extracted data into a JSON file named based on the current date (e.g., `scrapped_2024_11_06.json`).
- Iterates through multiple pages of car listings until no more listings are found.

## Prerequisites

- Python 3.7+ must be installed on your machine.
- Internet connection to access the website being scraped.

## Setup and Installation

### 1. Clone or Download the Repository

Clone this repository to your local machine or download the files directly.

### 2. Install Dependencies
The required Python packages are listed in `requirements.txt`. Install them by running:
```bash
pip install -r requirements.txt
```

### 3. Run the Script
After installing the dependencies, you can run the script:
```bash
python scrapper.py
```