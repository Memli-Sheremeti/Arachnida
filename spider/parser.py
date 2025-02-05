import argparse
import requests


def arg_user():
    arg = argparse.ArgumentParser()
    arg.add_argument("URL")
    arg.add_argument("-r", action="store_true", help="recursively downloads the images in a URL received as a parameter.")
    arg.add_argument("-l", type=int, default=5, metavar="N", help="indicates the maximum depth level of the recursive download. If not indicated, it will be 5.")
    arg.add_argument("-p", type=str, default="/data/", metavar= "PATH", help="indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used")
    return arg.parse_args()

def check_url(URL):
    # NEED TO CHECK IF I CAN USE a url parser !
    try:
        requests.get(URL)
    except Exception as e:
        print(f'Invalid URL: {URL} nodename nor servname provided, or not known')
        return False
    return True

def parse_user_input():
    args = arg_user()
    if check_url(args.URL) is False:
        exit(1)
    return args


def main():
    return


if __name__ == "__main__":
    main()
