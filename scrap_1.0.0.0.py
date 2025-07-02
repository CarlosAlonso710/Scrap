import requests
from bs4 import BeautifulSoup
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Example: Scraping a hotel booking site
url = "https://example-hotel-site.com"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data
hotels = []
for hotel in soup.find_all('div', class_='hotel-card'):
    name = hotel.find('h2').text.strip()
    price = hotel.find('span', class_='price').text.strip()
    rating = hotel.find('span', class_='rating').text.strip()
    amenities = [a.text.strip() for a in hotel.find_all('li', class_='amenity')]
    hotels.append({
        'Name': name,
        'Price': price,
        'Rating': rating,
        'Amenities': ', '.join(amenities)
    })

# Save to DataFrame
df = pd.DataFrame(hotels)

# Upload to Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Hotel Data').sheet1
sheet.update([df.columns.values.tolist()] + df.values.tolist())
print("Data uploaded to Google Spreadsheet")