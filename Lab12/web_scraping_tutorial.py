import random
import time
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

url = "https://example.com/products"

for attempt in range(4):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        break

    except requests.HTTPError as error:
        status = error.response.status_code

        if status == 429:
            retry_after = error.response.headers.get("Retry-After")
            delay = int(retry_after) if retry_after else 2 ** attempt
            time.sleep(delay)
            continue

        print(f"HTTP error {status}")
        break

    except RequestException as error:
        print("Request failed:", error)

        if attempt < 3:
            time.sleep(2 ** attempt)

else:
    print("Unable to retrieve the page")
    response = None

if response is not None:
    soup = BeautifulSoup(response.text, "html.parser")

    for product in soup.select(".product"):
        name = product.select_one(".name")

        if name:
            print(name.get_text(" ", strip=True))
        else:
            print("Product name missing")