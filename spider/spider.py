#!/usr/bin/env python3
from bs4 import BeautifulSoup
from creat_file_and_dir import create_the_img
from parser import parse_user_input, Arguments, validate_url
import urllib.parse as up
import requests
import re


def download_image(args: Arguments, link: str):
    url = args.url_parsed
    split_path = up.urlparse(link)
    if split_path.scheme == "" and split_path.netloc == "":
        image_url = url._replace(path="/").geturl() + link
    elif split_path.scheme == "":
        image_url = url.scheme + ":" + link
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
    args.url_visited.append(args.option.URL)
    return




def check_new_url(args: Arguments, new_link: any) -> bool:
    url = args.url_parsed
    if new_link.scheme != "":
        if validate_url(args, new_link.geturl()):
            return True
    elif new_link.netloc != "":
        if validate_url(args, url.scheme + ":" + new_link.geturl()): 
            return True
    elif new_link.path != "":
        test = url._replace(path="/").geturl() + new_link.path
        if validate_url(args, test):
            return True
    return False


def find_new_url(args: Arguments):
    href = args.soup.find_all("a")
    for link in href:
        new_link = up.urlparse(link.get("href"))
        if check_new_url(args, new_link):
            return
    return 


def spider(args: Arguments):
    scrapp_img_from_a_page(args)
    ## FINDING OTHER URL IN THE PAGE
    if args.option.r is True and args.option.l > 0:
        args.recursive_depth()
        find_new_url(args)
        spider(args)
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
