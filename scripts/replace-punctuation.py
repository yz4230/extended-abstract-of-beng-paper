import argparse


def replace_punctuations(text: str) -> str:
    table = str.maketrans({"。": "．", "、": "，"})
    return text.translate(table)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The filename to replace punctuations.")
    args = parser.parse_args()

    filename = args.filename
    with open(filename, "r") as file:
        text = file.read()

    new_text = replace_punctuations(text)
    with open(filename, "w") as file:
        file.write(new_text)


if __name__ == "__main__":
    main()
