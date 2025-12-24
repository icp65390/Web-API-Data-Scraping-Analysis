import requests
import pandas as pd

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Fetch data from API
response = requests.get(url)

# Convert JSON to Python object
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)

# Save data as CSV
df.to_csv("../data/posts_data.csv", index=False)

print("API data fetched and saved successfully!")

