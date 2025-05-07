# OLX Car Cover Scraper

A powerful Python web scraper designed to help you find and compare car covers on OLX.in. This tool automatically collects detailed information about car covers available in your area, making it easier to find the best deals and options for your vehicle.

## What This Tool Does

This scraper helps you:
- Find all car cover listings on OLX.in in one go
- Compare prices across different sellers
- Filter out irrelevant listings (like parking covers or garages)
- Save all information in an organized CSV file
- Access direct links to listings and product images
- Make informed decisions about car cover purchases

## Why Use This Tool?

- **Save Time**: Instead of manually browsing through OLX pages, get all listings in minutes
- **Better Comparison**: See all available options and prices in one place
- **Smart Filtering**: Automatically removes irrelevant listings
- **Data Organization**: All information is saved in a structured CSV format
- **Anti-Bot Protection**: Built-in measures to avoid getting blocked
- **Error Handling**: Automatically handles common issues and continues scraping

## Features

- Scrapes car cover listings from OLX.in
- Filters out irrelevant listings (parking covers, garages, etc.)
- Collects detailed information:
  - Title
  - Price
  - Location
  - Description
  - Image URL
  - Listing URL
- Saves data to CSV format
- Implements anti-bot detection measures
- Handles errors gracefully

## Requirements

- Python 3.7+
- Chrome browser installed
- ChromeDriver (automatically handled by the script)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd olx-car-cover-scraper
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix/MacOS
source .venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure you have Chrome browser installed
2. Run the scraper:
```bash
python olx_scraper.py
```

## What Happens When You Run the Code

1. **Initialization Phase:**
   - The script starts by setting up Chrome in headless mode
   - A random user agent is selected to avoid detection
   - ChromeDriver is initialized with anti-bot detection settings

2. **Scraping Process:**
   - The script visits OLX.in and searches for car covers
   - It processes up to 5 pages by default (configurable)
   - For each page:
     - Waits for the page to load completely
     - Finds all item listings
     - Filters out non-car-cover items
     - Extracts details from each valid listing

3. **Real-time Output:**
   You'll see messages like:
   ```
   Checking page 1...
   Found: Car Cover for Sedan - ₹1,500
   Found: Waterproof Car Cover - ₹2,000
   Checking page 2...
   ```

4. **Data Collection:**
   For each car cover listing, the script collects:
   - Title (e.g., "Waterproof Car Cover for Sedan")
   - Price (e.g., "₹1,500")
   - Location (e.g., "Mumbai, Maharashtra")
   - Description (e.g., "Brand new car cover, fits all sedans")
   - Image URL
   - Direct link to the OLX listing

5. **Saving Results:**
   - All collected data is saved to `car_covers.csv`
   - If the file already exists, a new file is created with a number suffix
   - You'll see a message like: "Saved 25 items to car_covers.csv"

## Output Format

The generated CSV file contains these columns:
- title: The listing title
- price: The listed price
- location: Where the item is located
- details: Additional description
- image_url: Link to the product image
- link: Direct link to the OLX listing

## Troubleshooting

Common issues and solutions:

1. **ChromeDriver Issues:**
   - Make sure Chrome is installed
   - Check Chrome version matches ChromeDriver
   - Run `setup_chromedriver.py` if needed

2. **No Results:**
   - Check internet connection
   - Verify OLX website accessibility
   - Try different user agent

3. **CSV File Issues:**
   - Ensure write permissions
   - Check disk space
   - Verify file isn't open in another program

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Selenium WebDriver
- OLX.in
- Python community 