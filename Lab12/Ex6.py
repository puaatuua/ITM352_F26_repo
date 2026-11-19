# Use the requests package to retrieve a page of mortgate rate info from the Hawaii Board of Realtors site

# Name: Ava Puaatuua
# Date: Nov. 18, 2026

import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find("table")
rows = table.find_all("tr")

current_bank = ""
for row in rows[1:]:
    cells = [cell.get_text(" ", strip=True) for cell in row.find_all("td")]
    if not cells:
        continue

    # Rows with 5 columns include the Lender in the first cell
    if len(cells) == 5:
        current_bank = cells[0]
        rate_info = cells[1:]
    else:
        rate_info = cells

    print(f"{current_bank}: {', '.join(rate_info)}")
