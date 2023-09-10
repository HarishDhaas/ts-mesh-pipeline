#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests
from bs4 import BeautifulSoup
import csv  

class web_scraper:
    def __init__(self, url):
        self.url = url
        self.data = [] 

    def fetch_page(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def parse_page(self, html):
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            spans = soup.find_all('span', class_='nontrimmed')
            for span in spans:
                data = span.get_text(strip=True) 
                self.data.append(data) 

    def save_to_csv(self, filename):
        if self.data:
            with open(filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                for item in self.data:
                    csv_writer.writerow([item])

    def scrape(self):
        html = self.fetch_page()
        self.parse_page(html)

if __name__ == "__main__":
    url = '''https://ieg.worldbankgroup.org/ieg-search?search_api_fulltext=tenders&field_topic
    =All&field_sub_category=All&content_type_1=&field_organization_tags=All&type_2_op=not&type_
    2%5B%5D=homepage_spotlight_feature&sort_by=search_api_relevance&sort_order=DESC'''
    
    scraper = web_scraper(url)
    scraper.scrape()
    
    csv_filename = 'tender_data.csv'
    scraper.save_to_csv(csv_filename)


# In[ ]:




