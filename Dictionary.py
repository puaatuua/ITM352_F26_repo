# Simple dictionary example

country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "France": "Paris"
}

print("Country Capitals", country_capitals)
print(country_capitals["Canada"])

country_capitals["England"] = "London"
print(country_capitals["England"])

print("Germany" in country_capitals)
print("spain" not in country_capitals)
