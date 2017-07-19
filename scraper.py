from bs4 import BeautifulSoup
import requests
from lxml import html

url1="https://ca.indeed.com/jobs?q=electrical+engineer&l=Milton%2C+ON"

url = input("Type the url: " )
print(url)

def main(url):
	r = requests.get(url)
	
	soup = BeautifulSoup(r.content, 'html.parser')
	for i in soup.find_all("a"):
		print(i.get('href'))
	
main(url)
