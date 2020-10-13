import requests
from bs4 import BeautifulSoup 

x=requests.get("https://realpython.com/working-with-files-in-python/") 
soup = BeautifulSoup(x.content, 'html.parser')  
print(soup.title.string)        