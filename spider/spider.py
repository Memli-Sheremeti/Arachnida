#!/usr/bin/env python3
from bs4 import BeautifulSoup
from parser import parse_user_input, Arguments
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
    count = 0
    for image in img:
        if re.search(r'.*\.jpg$', image.get("src")):
            download_image("https:" + image.get("src"), f"data/image{str(count)}.jpg")
            print(image.get("src"))
            count += 1
        else:
            print("rien de chez rien")


def spider(args: Arguments):
    ### having all img from the URL
    img = args.soup.find_all("img")
    scrapp_img_from_a_page(img)

    if args.option.r is True and args.option.l > 0:
        print("FINDING NEW PAGE")
        args.recursive_depth()
    ### FINDING OTHER URL IN THE PAGE
    # href = args.soup.find_all("a")
    # for i in href:
    #     print(args.url_parsed.scheme + "//" + args.url_parsed.netloc + args.url_parsed.path + i.get("href"))
    return 


def main():
    args = Arguments()
    try:
        parse_user_input(args)
        print(args)
        spider(args)
    except Exception as e:
        print(e)
    return


if __name__ == "__main__":
    main()
