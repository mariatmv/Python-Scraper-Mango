# Python-Scraper-Mango

## About the project
This is a simple web scraper. It's getting an url of a product in Mango's website, scraping the html and collecting the needed data (product name, price, color and available sizes) and outputing the collected data in a json file


## Requirements
Before executing the project you must have python, chromedriver, selenium and beautifulsoup4 installed.

For python - https://www.python.org/downloads/

For chromedriver - https://chromedriver.chromium.org/downloads
### Please keep in mind that you should install the version that is corresponding to the version of your browser. I'm using Chrome on version 96, so I included chromedriver version 96, but if you're using another version - make sure to replace the one in the project with the right one for you
For the last two, you can simply run the following commands in the terminal:

```
pip install selenium
```

```
pip install beautifulsoup4
```

## Aditional
You can change the URL that you want to be scraped by replacing the url in webscraper.py on line 6

## Behaviour
You'll see the newly created json file on the first run, where you can find the info for the product. The same file would be updated on re-run
