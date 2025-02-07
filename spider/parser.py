import urllib.parse as up
import argparse
import requests

class Arguments:
    def __init__(self):
        self.url_visited: list = []
        self.option: argparse.Namespace = None
        self.url_parsed: up.ParseResult = None
        self.resp: requests.Response = None
        return
    
    def __str__(self):
       return f'LST URL: {self.url_visited}\n OPTION: {self.option}\n URL-PARSED: {self.url_parsed}\n Resp: {self.resp}'

    def replace_url(self, url: str):
        self.option.URL = url
        return
    
    def recursive_depth(self):
        if self.option.l > 0:
            self.option.l -= 1
        return
    
    def add_url_visited(self):
        if self.option.URL not in self.url_visited:
            self.url_visited.append(self.option.URL)


def arg_user():
    arg = argparse.ArgumentParser()
    arg.add_argument("URL")
    arg.add_argument("-r", action="store_true", help="recursively downloads the images in a URL received as a parameter.")
    arg.add_argument("-l", type=int, default=5, metavar="N", help="indicates the maximum depth level of the recursive download. If not indicated, it will be 5.")
    arg.add_argument("-p", type=str, default="/data/", metavar= "PATH", help="indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used")
    return arg.parse_args()


def error_option(args: Arguments) -> None:
    if args.option.l != 5 and args.option.r is False:
        raise Exception(f"usage: [-h] [-r] [-l N] [-p PATH] URL\nerror: argument -l: invalid without -r")
    return

def check_url(args: Arguments) -> None:
    # NEED TO CHECK IF I CAN USE a url parser !
    try:
       args.resp = requests.get(args.option.URL)
    except Exception:
        raise Exception(f'Invalid URL: {args.option.URL}')


def parse_user_input(args: Arguments):
    args.option = arg_user()
    try: 
        error_option(args)
        check_url(args)
    except Exception as e:
        raise Exception(e)
    return args


def main():
    return


if __name__ == "__main__":
    main()
