# Ebay Data Scraper

This Python project scrapes laptop listings from eBay using BeautifulSoup (bs4) and saves the extracted data into an Excel file using pandas and openpyxl. The script is designed to gather information about laptops, including their name, price, shipping details, and links to the product pages.

## Features
- Scrapes laptop data such as name, price, shipping information, and product links.
- Handles multiple pages of eBay search results.
- Stores the collected data in an Excel file.
- Uses custom headers and cookies to simulate a real browser and avoid getting blocked.

## Requirements
- Python 3.7+
- Libraries:
  - requests
  - BeautifulSoup (bs4)
  - pandas
  - openpyxl

## Installation
1. Clone the repository or download the script.
2. Install the required Python libraries:
   ```bash
   pip install requests beautifulsoup4 pandas openpyxl
   ```
3. Ensure you have Python installed on your system.

## Usage
1. Modify the `url` variable in the script to match your specific search query on eBay.
2. Run the script:
   ```bash
   python scraper.py
   ```
3. The script will create an Excel file named `laptops.xlsx` in the same directory as the script.

## Project Structure
```
.
|-- scraper.py          # Main script for scraping eBay data
|-- laptops.xlsx        # Output file containing scraped data
|-- README.md           # Documentation (this file)
```

## How It Works
1. **HTTP Request:**
   - The script sends an HTTP GET request to the eBay search URL with custom headers and cookies to avoid being blocked by eBay's security systems.

2. **Data Extraction:**
   - Parses the HTML response using BeautifulSoup.
   - Extracts laptop details like name, price, shipping information, and product links.

3. **Pagination:**
   - Iterates through multiple pages of search results until there are no more pages.

4. **Data Storage:**
   - Appends the extracted data into a Python dictionary.
   - Converts the dictionary into a pandas DataFrame.
   - Saves the DataFrame to an Excel file using openpyxl.

## Example Output
The output file `laptops.xlsx` will have the following columns:
- **name:** The name/title of the laptop.
- **price:** The price of the laptop.
- **shipping:** The shipping cost or "Free Shipping" if applicable.
- **link:** The direct link to the product page.

### Sample Data:
| name                        | price    | shipping      | link                        |
|-----------------------------|----------|---------------|-----------------------------|
| Dell XPS 13 (32GB RAM)      | $1,299   | Free Shipping | https://www.ebay.com/...    |
| HP Spectre x360 (32GB RAM)  | $1,599   | $10 Shipping  | https://www.ebay.com/...    |

## Notes
- Make sure the eBay search query in the `url` variable is configured according to your requirements.
- If you encounter any CAPTCHA challenges, consider adjusting the headers or using a different User-Agent string.
- Avoid making requests too frequently to prevent being blocked by eBay's servers.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Feel free to submit issues or pull requests to enhance the project.

## Acknowledgments
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [eBay Developer Resources](https://developer.ebay.com/)

## Disclaimer
This project is for educational purposes only. Please ensure compliance with eBay's Terms of Service when using this script.

