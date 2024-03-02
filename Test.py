import requests
from bs4 import BeautifulSoup

url = "https://faradars.org/courses/basic-introduction-to-shell-script-programming-in-linux-fvlnx9710"

response = requests.get(url)
print(response)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print("Failed to retrieve the webpage.")