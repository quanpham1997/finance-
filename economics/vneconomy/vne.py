import time
import csv
import os.path
import numpy as np 
import pandas as pd 
import requests 
from bs4 import BeautifulSoup 
import tldextract

def request_with_check(url):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36 , For: tutorial'}
    page_response = requests.get(url, headers=headers, timeout=60)
    if page_response.status_code>299:
        raise AssertionError("page content not found, status: %s"%page_response.status_code)
    
    return page_response 



def get_details(single_article):
    
    # A title is in <a></a> with the 'class' attribute set to: title
    title = single_article.find('a')['title']

    # A safeguard against some empty articles in the deeper pages of the site
    if title == None:
        #print('Empty Article')
        return None
    
    # the link to an article is the Href attribute
    link = single_article.find('a')['href']  
    
    # The first Paragraph is in <p></p>
    first_p = single_article.find('p',{'data-type':'sapo'}).text
    
    
    #date is also in <span></span> withe the Class == date
    date = single_article.find('span',{'class':'infonews-time'})['title']
    
    return title, link, first_p, date  


def single_page(Url_page,page_id = 1):

    news_list = []

    #Making the Http request
    page = request_with_check(Url_page)
    
    #Calling the Html.parser to start extracting our data
    html_soup = BeautifulSoup(page.text, 'html.parser')
    
    # The Articles Class
    articles = html_soup
    
    # The single Articles List
    articleItems = articles.find_all('div' ,{'class':'infonews'})

    # Looping, for each single Article
    for article in articleItems:
        if get_details(article) == None:
            continue
        
        title, link, first_p, date = get_details(article)
        news_list.append({'id_page':page_id,
                          'title':title,   
                          'date':date,
                          'link': link,
                          'first_p':first_p})

    return news_list


links  = []
for i in range (1 , 3700):
    link = f'http://vneconomy.vn/timeline/6/trang-{i}.htm'
    links.append(link)



    
def dict_to_csv (filename,news_dict):
    
    #Setting the Dataframe headers
    fields = news_dict[0]
    fields = list(fields.keys())
    
    #Checking if the file already exists, if Exists we woulb pe appending, if Not we creat it
    has_header = False
    if os.path.isfile(filename):
        with open(filename, 'r') as csvfile:
            sniffer = csv.Sniffer()
            has_header = sniffer.has_header(csvfile.read(2048))
    
    with open(filename, 'a',errors = 'ignore', encoding= 'utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        if(has_header == False):
            writer.writeheader()  
        for row in range(len(news_dict)):
            item = news_dict[row]
            writer.writerow(item)

def parsing_category_pages(number_pages_start, number_pages_end):
    start_time = time.time()
    #Looping over the specified nupber of Pages:
    for p in range(number_pages_start,number_pages_end):
       
        
        url =  links[p]
        #getting the start page
        page = request_with_check(url)
        #get domain name
        ext = tldextract.extract(links[0])
        domain = ext.domain
        print(f'Parsing: {url}')
        #Calling the Html Parser
        html_soup = BeautifulSoup(page.text, 'html.parser')
        
        page_news = single_page(url,p)
        
        #Saving to a CSV
        filename = 'news_file'+str(domain)+'_page_'+ str(number_pages_start)+'_to_page_'+str(number_pages_end)
        dict_to_csv(f'{filename}.csv',page_news)
        
        
        print("--- %s seconds ---" % (time.time() - start_time))
    
    print("--- %s seconds ---" % (time.time() - start_time))
    return True


parsing_category_pages (number_pages_start = 300, number_pages_end=780)




