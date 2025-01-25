import requests
import re
from bs4 import BeautifulSoup


def download_image(image_url: str, path: str):
    print(image_url)
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(path, "wb") as file:
            file.write(response.content)
        print("Done")
    else:
        print("FAILED")

def main():
    url = "https://fr.wikipedia.org/wiki/Python_(langage)"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    img = soup.find_all("img")
    count = 0
    for image in img:
        if re.search(r'.*\.jpg$', image.get("src")):
            download_image("https:" + image.get("src"), f"data/image{str(count)}.jpg")
            print(image.get("src"))
            count += 1
        # elif re.search(r'.*\.png$', image.get("src")):
        #     download_image("https:" + image.get("src"), f"data/image{str(count)}.jpg")
        #     print(image.get("src"))
        #     count += 1
        else:
            print("rien de chez rien")
    return

if __name__ == "__main__":
    main()
