

# Introspider - Tesco.com Scraper

Introspider is a Python Scrapy spider designed to scrape product data from Tesco.com, one of the largest e-commerce platforms. This spider allows you to gather product information such as name, price, and other relevant details.

## Installation

Before running the scraper, make sure you have Python and Scrapy installed on your system.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/basudab/Scrapy_projects.git
   cd intro/intro
   ```

2. **Install Python and Scrapy:**

   If you haven't already, install Python from [Python's official website](https://www.python.org/downloads/). Then, install Scrapy using pip:

   ```bash
   pip install scrapy
   ```

## Usage

Navigate to the `intro/intro` folder in your command prompt or Python shell.

To run the scraper and save the output in JSON format, use the following command:

```bash
scrapy crawl introspider -o output.json
```

To save the output in CSV format, use the following command:

```bash
scrapy crawl introspider -o output.csv
```

## Customization

In the `introspider.py` file, you can modify the product name to scrape different products. Look for the following line and replace `'product_name'` with the desired product:

```python
start_urls = ['https://www.tesco.com/groceries/en-GB/search?query=product_name']
```

Replace `'product_name'` with the product you want to scrape.

---

Feel free to customize this README according to your project's specific requirements and add any additional information or sections as needed. Save this content in a file named `README.md` with the .md extension in your GitHub repository.
