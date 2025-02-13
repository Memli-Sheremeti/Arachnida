import os
import sys


def check_the_path(path: str) -> str:
    if ".." in path or "~" in path:
        raise OSError("Error on the path of the directory")
    if path[-1] != '/':
        path = path + '/'
    if path[0] != '.':
        path = './' + path
    return path


def create_the_directory(args: any, path: str) -> None:
    try:
        args.option.p = check_the_path(path)
        os.mkdir(path)
    except OSError as e:
        if e.errno != 17:
            raise Exception(e)


def create_the_img(args: any, path: str, response) -> None:
    try:
        path = path.split("/")
        path = path[len(path) - 1]
        path = args.option.p + path
        with open(path, "wb") as file:
            file.write(response.content)
    except OSError as e:
        if e.errno != 17:
            raise Exception(e)


def main():
    return


if __name__ == "__main__":
    main()
