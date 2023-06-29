import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

headers = Headers().generate()
print(headers)
page = requests.get('https://www.imdb.com/chart/tvmeter/', headers=headers)

if page.status_code == 200:

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("div", class_="ipc-metadata-list-summary-item__tc")

    for result in results:
            name = result.find("h3", class_="ipc-title__text")
            rating = result.find("span", class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")
            try:
                print(name.text + " " + rating.text)
            except:
                 print(name)

else:
    print("Error: " + str(page.status_code))