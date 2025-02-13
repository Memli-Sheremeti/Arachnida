from bs4 import BeautifulSoup
from creat_file_and_dir import create_the_directory
import urllib.parse as up
import argparse
import requests


class Arguments:
    def __init__(self):
        self.url_visited: list = []
        self.option: argparse.Namespace = None
        self.url_parsed: up.ParseResult = None
        self.rq: requests.Response = None
        self.soup: BeautifulSoup = None
        return
    
    def __str__(self):
       return f'LST URL: {self.url_visited}\nOPTION: {self.option}\nURL-PARSED: {self.url_parsed}\nRq: {self.rq}\n'
    
    def recursive_depth(self):
        if self.option.l > 0:
            self.option.l -= 1
        return
    
    def check_if_not_url_visited(self, url: str):
        if url not in self.url_visited:
                return True
        return False


def arg_user() -> argparse.Namespace:
    arg = argparse.ArgumentParser()
    arg.add_argument("URL")
    arg.add_argument("-r", action="store_true", help="recursively downloads the images in a URL received as a parameter.")
    arg.add_argument("-l", type=int, default=5, metavar="N", help="indicates the maximum depth level of the recursive download. If not indicated, it will be 5.")
    arg.add_argument("-p", type=str, default="./data", metavar= "PATH", help="indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used")
    return arg.parse_args()


def error_option(args: Arguments) -> None:
    if args.option.l != 5 and args.option.r is False:
        raise Exception(f"usage: [-h] [-r] [-l N] [-p PATH] URL\nerror: argument -l: invalid without -r")
    return


def request_url(args: Arguments, url: str) -> None:
    try:
       tmp = requests.get(url)
       if tmp.status_code != 200:
           raise Exception(f'Invalid URL: {url}')
       args.rq = tmp
       args.soup = BeautifulSoup(args.rq.text, "html.parser")
    except Exception as e:
        raise Exception(f'Invalid URL: {url}')


def split_url(args: Arguments) -> None:
    try:
        args.url_parsed = up.urlparse(args.option.URL)
    except Exception as e:
        raise Exception(e)
    return


def parse_user_input(args: Arguments) -> Arguments:
    try: 
        args.option = arg_user()
        create_the_directory(args, args.option.p)
        error_option(args)
        request_url(args, args.option.URL)
        split_url(args)
    except Exception as e:
        raise Exception(e)
    return args


def validate_url(args: Arguments, url: str) -> bool:
    if args.check_if_not_url_visited(url):
        try:
            request_url(args, url)
            args.option.URL = url
            split_url(args)
            return True
        except Exception as e:
            return False
    return False


def main():
    return


if __name__ == "__main__":
    main()
