#!/usr/bin/env python3
from bs4 import BeautifulSoup
from creat_file_and_dir import create_the_img
from parser import parse_user_input, Arguments
import urllib.parse as up
import requests
import re


def download_image(args: Arguments, link: str):
    split_path = up.urlparse(link)
    print(split_path)
    if split_path.scheme == "" and split_path.netloc == "":
        image_url = args.option.URL + link
    elif split_path.scheme == "":
        image_url = args.url_parsed.scheme + ":" + link
    response = requests.get(image_url)
    if response.status_code == 200:
        create_the_img(args, link, response)
    else:
        print("FAILED")
    return


def scrapp_img_from_a_page(args: Arguments):
    img = args.soup.find_all("img")
    for image in img:
        if re.search(r'.*\.jpg$', image.get("src")):
            download_image(args, image.get("src"))
        elif re.search(r'.*\.jpeg$', image.get("src")):
            download_image(args, image.get("src"))
        elif re.search(r'.*\.png$', image.get("src")):
            download_image(args, image.get("src"))
        elif re.search(r'.*\.gif$', image.get("src")):
            download_image(args, image.get("src"))
        elif re.search(r'.*\.bmp$', image.get("src")):
            download_image(args, image.get("src"))
        else:
            continue
    args.add_url_visited(args.option.URL)
    print(args.url_visited)



def find_other_url(args: Arguments):
    href = args.soup.find_all("a")
    count = 0
    for link in href:
        new_link = up.urlparse(link.get("href"))
        print(new_link)
        count += 1
        if count == 2:
            # print(args.url_parsed.geturl(__path__) + new_link.path)
            break
    return


def spider(args: Arguments):
    if args.option.l < 0:
        return
    # scrapp_img_from_a_page(args)
    ### FINDING OTHER URL IN THE PAGE
    if args.option.r is True and args.option.l > 0:
        args.recursive_depth()
        new_url = find_other_url(args)
    return 


def main():
    args = Arguments()
    try:
        parse_user_input(args)
        spider(args)
    except Exception as e:
        print(e)
    return


if __name__ == "__main__":
    main()
