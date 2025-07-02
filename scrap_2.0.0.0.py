from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# Set up headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Sample ASIN
asin = "B08L9X5Y8Q"
url = f"https://www.amazon.com/dp/{asin}"

# Load page
driver.get(url)
time.sleep(3)  # Wait for JavaScript to load

# Parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract data (example placeholders)
price = soup.find('span', {'class': 'priceblock_ourprice'}).text if soup.find('span', {'class': 'priceblock_ourprice'}) else 'N/A'
seller = soup.find('a', {'id': 'sellerProfileTriggerId'}).text if soup.find('a', {'id': 'sellerProfileTriggerId'}) else 'N/A'
rating = soup.find('span', {'class': 'a-icon-alt'}).text if soup.find('span', {'class': 'a-icon-alt'}) else 'N/A'
reviews = soup.find('span', {'id': 'acrCustomerReviewText'}).text if soup.find('span', {'id': 'acrCustomerReviewText'}) else 'N/A'

# Store data
data = {
    'ASIN': asin,
    'Price': price,
    'Seller': seller,
    'Rating': rating,
    'Reviews': reviews
}
df = pd.DataFrame([data])

# Save to CSV
df.to_csv('amazon_data.csv', index=False)
print("Data saved to amazon_data.csv")

# Close driver
driver.quit()