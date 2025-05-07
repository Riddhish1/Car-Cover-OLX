# 🚗 OLX Car Cover Scraper

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.15.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

*A powerful web scraper to find the best car covers on OLX.in* 🛡️

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Output](#output) • [Troubleshooting](#troubleshooting)

</div>

## ✨ What This Tool Does

This scraper helps you find and compare car covers on OLX.in efficiently:

- 🔍 Find all car cover listings in one go
- 💰 Compare prices across different sellers
- 🎯 Filter out irrelevant listings (parking covers, garages)
- 💾 Save all information in an organized CSV file
- 🔗 Access direct links to listings and product images
- 📊 Make informed decisions about car cover purchases

## 🚀 Features

- **Smart Scraping**: Automatically collects data from OLX.in
- **Intelligent Filtering**: Removes irrelevant listings
- **Rich Data Collection**:
  - 📝 Title
  - 💵 Price
  - 📍 Location
  - 📄 Description
  - 🖼️ Image URL
  - 🔗 Listing URL
- **Anti-Bot Protection**: Built-in measures to avoid detection
- **Error Handling**: Graceful recovery from common issues

## 🛠️ Requirements

- Python 3.7 or higher
- Google Chrome browser
- Internet connection

## 📥 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Riddhish1/Car-Cover-OLX.git
   cd Car-Cover-OLX
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Unix/MacOS
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

1. Ensure Chrome browser is installed
2. Run the scraper:
   ```bash
   python olx_scraper.py
   ```

## 📊 What Happens When You Run the Code

### 1. Initialization Phase
- 🖥️ Chrome starts in headless mode
- 🎭 Random user agent selection
- 🛡️ Anti-bot protection setup

### 2. Scraping Process
- 🌐 Visits OLX.in
- 📑 Processes up to 5 pages
- 🔄 For each page:
  - ⏳ Waits for content to load
  - 🔍 Finds item listings
  - 🎯 Filters relevant items
  - 📝 Extracts details

### 3. Real-time Output
```
Checking page 1...
Found: Car Cover for Sedan - ₹1,500
Found: Waterproof Car Cover - ₹2,000
Checking page 2...
```

### 4. Data Collection
For each listing:
- 📝 Title (e.g., "Waterproof Car Cover for Sedan")
- 💵 Price (e.g., "₹1,500")
- 📍 Location (e.g., "Mumbai, Maharashtra")
- 📄 Description
- 🖼️ Image URL
- 🔗 Direct link

### 5. Saving Results
- 💾 Saves to `car_covers.csv`
- 🔄 Creates new file if exists
- ✅ Shows summary message

## 📋 Output Format

The CSV file contains:
| Column | Description |
|--------|-------------|
| title | Listing title |
| price | Listed price |
| location | Item location |
| details | Description |
| image_url | Product image link |
| link | OLX listing URL |

## 🔧 Troubleshooting

### ChromeDriver Issues
- ✅ Verify Chrome installation
- 🔄 Check Chrome version
- 🛠️ Run setup if needed

### No Results
- 🌐 Check internet connection
- 🔍 Verify OLX accessibility
- 🎭 Try different user agent

### CSV File Issues
- 📝 Check write permissions
- 💾 Verify disk space
- 🔒 Ensure file isn't locked

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🔧 Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Selenium WebDriver](https://www.selenium.dev/)
- [OLX.in](https://www.olx.in)
- Python community

---

<div align="center">
Made with ❤️ by [Your Name]
</div> 