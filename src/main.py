from copy_folder import copy_folder
from generate_page import generate_pages_recursive


def main():

    copy_folder("static", "public")
    generate_pages_recursive("./content", "./template.html", "./public")


if __name__ == "__main__":
    main()
