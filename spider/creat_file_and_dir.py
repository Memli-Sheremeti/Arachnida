import os


def create_the_directory(path: str) -> None:
    try:
        os.mkdir(path)
    except OSError as e:
        if e.errno != 17:
            raise Exception(e)
    return


def create_the_img(args, path: str, response) -> None:
    path = path.split("/")
    path = path[len(path) - 1]
    path = args.option.p + path
    print(path)
    with open(path, "wb") as file:
        file.write(response.content)

def main():
    return


if __name__ == "__main__":
    main()
