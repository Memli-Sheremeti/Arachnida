import os


def create_the_directory(path: str) -> None:
    try:
        os.mkdir(path)
    except OSError as e:
        if e.errno != 17:
            raise Exception(e)
    return


def main():
    return


if __name__ == "__main__":
    main()
