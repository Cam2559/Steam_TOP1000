import os
import pandas as pd
from apify_client import ApifyClient
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path

#loading the .env file 
load_dotenv()

#Loads the Apify API token from the `apify_token` environment variable using `os.getenv()`.
apify_token = os.getenv("apify_token")

# Create an Apify client object
# This allows Python to communicate with the Apify platform
client = ApifyClient(apify_token)

# Get today's date and format it as YYYY-MM-DD
# This is used later for timestamped filenames
today = datetime.today().strftime("%Y-%m-%d")

# Define the folder where CSV files will be saved
output_dir = Path(r"D:\Steam_top1000\Data")

# Define the Actor input settings
run_input = {

    # Empty query means no keyword filtering
    "query": "",

    # Steam search URL for the Top Sellers page
    "steamSearchUrls": [
        "https://store.steampowered.com/search/?filter=topsellers"
    ],

    # Maximum number of games to retrieve
    "maxItems": 1000,

    # Use United States Steam store data
    "country": "US",

    # Return results in English
    "language": "english"
}

# Run the Apify Steam scraper Actor
run = client.actor(
    "lokki/steam-top-sellers-scraper"
).call(run_input=run_input)

# Retrieve all scraped dataset items from the completed Actor run
items = list(

    client.dataset(
        run["defaultDatasetId"]
    ).iterate_items()
)

# Convert the returned JSON data into a pandas DataFrame
df = pd.DataFrame(items)

# Print all dataframe column names
print(df.columns)

# Display the first few rows of the dataset
print(df.head())

# Create a timestamped filename
filename = output_dir / f"steam_top_sellers_{today}.csv"

# Export the dataframe to a CSV file

df.to_csv(filename, index=False)

# Print confirmation message showing where the file was saved
print(f"Saved {len(df)} rows to {filename}")