#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    start = end = 0
    size = len(text)
    while end < size:
        while text[start] == ' ':
            start += 1
            end += 1
        while end < size and text[end] not in '.?:':
            end += 1
        # print("going to print {}, {}".format(start, end))
        print(text[start:end+1], end="")
        if end != size:
            print("\n")
        end += 1
        start = end
