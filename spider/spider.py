#!/usr/bin/env python3
from bs4 import BeautifulSoup
from parser import parse_user_input
import requests
import re


def download_image(image_url: str, path: str):
    print(image_url)
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(path, "wb") as file:
            file.write(response.content)
        print("Done")
    else:
        print("FAILED")


def scrapp_img_from_a_page(img):
    for image in img:
        if re.search(r'.*\.jpg$', image.get("src")):
            download_image("https:" + image.get("src"), f"data/image{str(count)}.jpg")
            print(image.get("src"))
            count += 1
        else:
            print("rien de chez rien")


def spider(args, link):
    resp = requests.get(args.URL)
    soup = BeautifulSoup(resp.text, "html.parser")
    print(args)
    print(soup)
    if args.r is True and args.l > 0:
            img = soup.find_all("img")
            scrapp_img_from_a_page(img)
    return 


def main():
    link = []
    args = parse_user_input()
    spider(args, link)
    return


if __name__ == "__main__":
    main()
