from bs4 import BeautifulSoup
from typing import Any
import requests

class browser:
    def search(self, search: str) -> dict[str, str]:
        self.INPUT: str = str(search)
        self.URL: str = f"https://www.google.com/search?q={self.INPUT}"

        self.RESPONSE: requests.Response = requests.request('get', self.URL)
        self.SOUP: BeautifulSoup = BeautifulSoup(self.RESPONSE.content, 'html.parser')
        
        self.result_links = self.SOUP.find_all("a", href= True)

        self.SEARCH_RESULTS = {}

        self.ITERATION_INDEX = 0
        
        for i in self.result_links:
            LINK: str = f"{i['href']}"
            H3_ELEMENT: Any = i.find("h3")

            if H3_ELEMENT != None:

                H3_TITLE: str = str(H3_ELEMENT.text)
                
                self.SEARCH_RESULTS.update({
                    f"{self.ITERATION_INDEX}":{
                        "Title" : H3_TITLE,
                        "Link" : LINK
                    }
                })
                
                self.ITERATION_INDEX += 1
                
        return self.SEARCH_RESULTS
