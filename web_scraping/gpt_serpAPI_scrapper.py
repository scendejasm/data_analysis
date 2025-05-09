from serpapi import GoogleSearch
import requests
import csv

# Your SerpAPI key
api_key = "a8f0389bc0cf328d4d867763f48192d106e7868c541a00c50f3c304a9a7d8008"

params = {
        "engine": "google",
        "q": "gyms in Riverside",
        "location": "Riverside, California, United States",
        "google_domain": "google.com",
        "hl": "en",
        "gl": "us",
        "tbm": "lcl", # Set tbm to 'lcl' for local business search
        "api_key": api_key,
        }

search = GoogleSearch(params)
data = search.get_dict()

# Print the results for testing 

#Process the results

if "local_results" in data:
    # Extract the list of gyms

    gyms = data["local_results"]

    # Specify the export file name
    csv_file = "gyms_scrape_export.csv"

    # Define the CSV headers
    csv_headers = ["title", 
                   "rating", 
                   "reviews",
                   "description", 
                   "type",
                   "phone", 
                   "address"]

    # Write the extractd data to CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)
        writer.writeheader() # Write the header row

        # Write each gym's information
        for gym in gyms:
            writer.writerow({
                "title": gym.get("title", ""),
                "rating": gym.get("rating", ""),
                "reviews": gym.get("reviews", ""),
                "description": gym.get("description", ""),
                "type": gym.get("type", ""),
                "phone": gym.get("phone", ""),
                "address": gym.get("address", "")
                })

    print(f"Data has been succesfully exported to {csv_file}")





