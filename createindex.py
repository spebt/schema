import pathlib
from bs4 import BeautifulSoup as bs


# Get all json files in v1 folder
path_posix_list = list(pathlib.Path('v1').glob('*.json'))
# Make raw html
raw_html = ""
raw_html += '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Schema API Usage</title></head><body>'
raw_html += '<h1>Available API:</h1>'
for path in path_posix_list:
        raw_html += '<li>/' + str(path)+'</li>'
soup = bs(raw_html, 'html.parser')

# Write to index.html   
with open('index.html', 'w') as f:
    f.write(soup.prettify())