# 07 Web Scraping

# Not every website as an API to work wtih.
# In situations like that the only way to get the data we want is to parse the html behind a webpage, get rid of all the html tags, and extract the avtual data.
# This technic is called Web Scraping
# In this example we are going to write a program that extract the list of the newst questions form https://stackoverflow.com/questions/
# This is called a Web Crawler or a Web Spider.

# For this we are going to use the "beautifulsoup4" package

import requests
from bs4 import BeautifulSoup


response = requests.get("https://stackoverflow.com/questions") # Using the ".get()" method form the "resquest" module to download the web page.
content_html = response.text # This returns the html content with the ".text" atribute
soup = BeautifulSoup(content_html, "html.parser") # 

questions = soup.select(".question-summary") # We pass the CSS selector we type "." and then the name of the class. In this case ".question-summary". This will return a list.

for question in questions:
    print(question.select_one(".question-hyperlink").getText()) # The ".select_one()" method can be used in this particular case because which question only as one title, so we don't need to return  a list.
    print(question.select_one(".vote-count-post").getText())