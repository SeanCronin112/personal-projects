import webbrowser
import requests
from bs4 import BeautifulSoup

word = str(input("Enter your word: ")).lower()
url = 'https://www.dictionary.com/browse/{}'.format(word)


response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

pretty_file = soup.prettify().split()

definition = ""
i = 21

while(pretty_file[i] != 'more."'):
	definition += pretty_file[i] + " "
	i = i + 1

definition = word.capitalize() + ": " + definition[0].upper() + definition[1:-4]

print(definition)
