import time


def print_text(file, speed):
    f = open(file, "r")
    for line in f:
        if line == "\n":
            continue
        text = line.split(" ")
        print(line)
        time.sleep(len(text) / speed)
    f.close()


def reformat_file(file):
    f = open(file, "r")
    paragraphs = f.readlines()
    f.close()

    tmp = ""
    for paragraph in paragraphs:
        lines = paragraph.split(". ")
        for line in lines:
            tmp += line + "\n"

    f = open(file, "w")
    f.write(tmp)
    f.close()


reformat_file("sample.txt")
print_text("sample.txt", 4)
