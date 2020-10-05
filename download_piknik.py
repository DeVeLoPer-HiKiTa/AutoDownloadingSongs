from selenium import webdriver
import requests 
from bs4 import BeautifulSoup as BS


URL = 'https://sefon.fm/artist/103-splin/'
asked = False

browser = webdriver.Firefox()

my_URL = URL
i = 1
while i < 7:
	print("number of page: " + str(i) + " pages url of songs: " + my_URL)
	r = requests.get(my_URL)
	html = BS(r.content, 'html.parser')

	songs = html.select('div.b_list_mp3s > div.mp3 > div.duration > div.download > a')

	for s in songs:
		s_url = 'https://sefon.fm' + s['href']

		browser.get(s_url)
		print("downloading songs url: " + s_url)
		elements2 = browser.find_elements_by_css_selector('a.b_btn.download.no-ajix')

		elements2[0].click()

		if not asked:
			input("next?")
			asked = True
	
	i += 1
	my_URL = URL + str(i) + '/'

print('END: songs is downloaded')