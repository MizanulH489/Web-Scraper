import requests
from bs4 import BeautifulSoup
import json
import os

response = requests.get("https://en.wikipedia.org/wiki/Web_scraping")
bs = BeautifulSoup(response.text, "lxml")

# Find all the paragraphs on the page
paragraphs = bs.find_all([ "p","h1", "h2", "h3", "h4", "h5", "h6"])

# Create a list to store the paragraph texts
paragraph_texts = []

# Loop through the paragraphs and add their text to the list
for paragraph in paragraphs:
    paragraph_texts.append(paragraph.text)

# Create a dictionary to store the data
data = {
    "paragraphs": paragraph_texts   
}

# Specify the file path for output
output_file ="Sideprojects\TollTracker\TT_FE\output.json"

# Write the data to a new JSON file
with open("output.json", "w") as outfile:
    json.dump(data, outfile, indent=4)
