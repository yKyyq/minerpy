import requests
from bs4 import BeautifulSoup

class Site:
    def __init__(self, website):
        self.website = website
        self.response = None

    def show(self):
        return self.website
    
    def connection(self):
        try:
            self.response = requests.get(self.website)
            if self.response.status_code == 200:
                print("Connection Successful!")
                return True
        except requests.exceptions.RequestException as e:
            print(f"Connection Failed: {e}")
            return False

    def getRobots(self):
        if self.connection():
            try:
                response = requests.get(f"{self.website}/robots.txt")
                if response.status_code == 200:
                    return response.text
                else:
                    print(f"Failed To Retrieve robots.txt (Status code: {response.status_code})")
            except requests.exceptions.RequestException as e:
                print(f"Failed To Retrieve The 'robots.txt' File: {e}")

    def sourceCode(self):
        if self.connection():
            try:
                soup = BeautifulSoup(self.response.text, 'lxml')
                return soup.prettify()
            except Exception as e:
                print(f"Failed To Retrieve Source Code: {e}")

    def getLinks(self):
        if self.connection():
            try:
                soup = BeautifulSoup(self.response.text, 'lxml')
                links = soup.find_all('a')
                linkList = []
                for link in links:
                    href = link.get('href')
                    if href:
                        linkList.append(href)
                return linkList
            except Exception as e:
                print(f"Failed To Retrieve The Links: {e}")
    
    def getText(self):
         if self.connection():
            try:
                soup = BeautifulSoup(self.response.text, 'lxml')
                return soup.get_text()
            except Exception as e:
                print(f"Failed To Retrieve Text: {e}")