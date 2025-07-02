import requests
from bs4 import BeautifulSoup
import pandas as pd

# Example: Scraping a hypothetical dealer site
url = "https://example-dealer-site.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data
dealers = []
for dealer in soup.find_all('div', class_='dealer-info'):
    name = dealer.find('h2').text.strip()
    address = dealer.find('p', class_='address').text.strip()
    contact = dealer.find('p', class_='contact').text.strip()
    dealers.append({'Name': name, 'Address': address, 'Contact': contact})

# Save to CSV
df = pd.DataFrame(dealers)
df.to_csv('dealers.csv', index=False)
print("Data saved to dealers.csv")