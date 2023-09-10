install the Libraries

!pip install requests
!pip install requests
!pip install BeautifulSoup
import the Libraries

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time
Get URL and send Get request

url='https://books.toscrape.com/'
response=requests.get(url)
if response.status_code==200:
    print('request successful')
else:
    print('request failed')
request successful
Parse the HTML Content

# create  a soup object to parse the html content
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
Extract book Details for Page 1

#find all 20 books on page 1
books = soup.find_all('h3')
​
start_time= time.time()
books_extracted=0
# Iterate through the books and extract the information for each book
for book in books:
    book_url=book.find('a')['href']
    book_response=requests.get(url+book_url)
    book_soup=BeautifulSoup(book_response.content,"html.parser") 
   
    title = book_soup.find('h1').text
    category = book_soup.find('ul', class_="breadcrumb")
    if category:
        category_links = category.find_all('a')
        if len(category_links) >= 3:
            category = category_links[2].text.strip()
        else:
            category = "Category not found"
    else:
        category = "Breadcrumb element not found"
        
    rating = book_soup.find('p',class_='star-rating')['class'][1]
    price=book_soup.find('p',class_='price_color').text.strip()
    availability=book_soup.find('p',class_='availability').text.strip()
    
    books_extracted +=1
    end_time=time.time()
    total_time=(end_time-start_time)/60.0
    
    print(f'Title:{title}')
    print(f'Category:{category}')
    print(f'Rating:{rating}')
    print(f'Price:{price}')
    print(f'Availability:{availability}')
    print('*'*19)
print(books_extracted)
Extract details for all 50 pages

# create a list to hold all the book information 
books_data=[]
# loop through all 50 pages
for page_num in range(1,51):
    url=f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    response=request.get(url)
    soup=BeautifulSoup(response.content, 'html.parser')
#add extracted info to the list
   
    books = soup.find_all('h3')
​
    start_time= time.time()
    books_extracted=0
​
    for book in books:
        book_url=book.find('a')['href']
        book_response=requests.get(url+book_url)
        book_soup=BeautifulSoup(book_response.content,"html.parser") 
​
        title = book_soup.find('h1').text
        category = book_soup.find('ul', class_="breadcrumb")
        if category:
            category_links = category.find_all('a')
            if len(category_links) >= 3:
                category = category_links[2].text.strip()
            else:
                category = "Category not found"
        else:
            category = "Breadcrumb element not found"
​
        rating = book_soup.find('p',class_='star-rating')['class'][1]
        price=book_soup.find('p',class_='price_color').text.strip()
        availability=book_soup.find('p',class_='availability').text.strip()
​
        books_extracted +=1
        end_time=time.time()
        total_time=(end_time-start_time)/60.0
​
        print(f'Title:{title}')
        print(f'Category:{category}')
        print(f'Rating:{rating}')
        print(f'Price:{price}')
        print(f'Availability:{availability}')
        print('*'*19)
    print(books_extracted)
# create a list to hold all the book information 
books_data=[]
# loop through all 50 pages
for page_num in range(1,51):
    url=f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    response=requests.get(url)
    soup=BeautifulSoup(response.content, 'html.parser')
#add extracted info to the list
   
    books = soup.find_all('h3')
​
    start_time= time.time()
    books_extracted=0
​
    for book in books:
        book_url=book.find('a')['href']
        book_response=requests.get('https://books.toscrape.com/catalogue/'+book_url)
        book_soup=BeautifulSoup(book_response.content,"html.parser") 
​
        title = book_soup.find('h1').text
        category = book_soup.find('ul', class_="breadcrumb")
        if category:
            category_links = category.find_all('a')
            if len(category_links) >= 3:
                category = category_links[2].text.strip()
            else:
                category = "Category not found"
        else:
            category = "Breadcrumb element not found"
​
        rating = book_soup.find('p',class_='star-rating')['class'][1]
        price=book_soup.find('p',class_='price_color').text.strip()
        availability=book_soup.find('p',class_='availability').text.strip()
​
        
        end_time=time.time()
        total_time=(end_time-start_time)/60.0
​
        print(f'Title:{title}')
        print(f'Category:{category}')
        print(f'Rating:{rating}')
        print(f'Price:{price}')
        print(f'Availability:{availability}')
        print('*'*19)
    print(books_extracted)
# create a list to hold all the book information 
books_data=[]
# loop through all 50 pages
for page_num in range(1,51):
    url=f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    response=requests.get(url)
    soup=BeautifulSoup(response.content, 'html.parser')
#add extracted info to the list
   
    books = soup.find_all('h3')
​
    start_time= time.time()
    books_extracted=0
​
    for book in books:
        book_url=book.find('a')['href']
        book_response=requests.get('https://books.toscrape.com/catalogue/'+book_url)
        book_soup=BeautifulSoup(book_response.content,"html.parser") 
​
        title = book_soup.find('h1').text
        category = book_soup.find('ul', class_="breadcrumb")
        if category:
            category_links = category.find_all('a')
            if len(category_links) >= 3:
                category = category_links[2].text.strip()
            else:
                category = "Category not found"
        else:
            category = "Breadcrumb element not found"
​
        rating = book_soup.find('p',class_='star-rating')['class'][1]
        price=book_soup.find('p',class_='price_color').text.strip()
        availability=book_soup.find('p',class_='availability').text.strip()
​
        
        end_time=time.time()
        total_time=(end_time-start_time)/60.0
​
        books_data.append([title,category,rating,price,availability])
        print(books_data)
        print('*'*9)
        print(f'Total time taken:{total_time:.2f} minutes')
        print('*'*9)
        print(f'{page_num*len(books)} books extracted so far...')
**Export the data**
# convert list to dataframe
df=pd.DataFrame(books_data, columns=['Title','Category','Rating','Price','Availability'])
#display first 10 rows
print(df.head(10))
# save to csv
df.to_csv('books_scraped.csv',index=False)
print('data saved to books_scraped.csv')
