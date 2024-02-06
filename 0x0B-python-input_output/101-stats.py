#!/usr/bin/python3
"""
This is '101-stats' module.
Functions and Classes:
    def print_results(size, status_code)
    def main()
"""


from sys import stdin


def print_results(size, status_code):
    """print stats since start"""
    print("File size: {}".format(size))
    for k in status_code.keys():
        if status_code[k] != 0:
            print("{}: {}".format(k, status_code[k]))


def main():
    """read input then compute stats"""
    status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
                   '403': 0, '404': 0, '405': 0, '500': 0}

    size = 0
    n_lines = 0
    try:
        for line in stdin:
            # get last portion of line containing status code and file size
            # then split the two arguments
            s = line.rstrip().split("HTTP/1.1\" ")
            numbers = s[-1].split(" ")

            status_code[numbers[0]] += 1
            size += int(numbers[-1])

            # increase number of lines read and check to print out
            n_lines += 1
            if n_lines >= 10:
                print_results(size, status_code)
                n_lines = 0
    except KeyboardInterrupt:
        print_results(size, status_code)


# start the script
main()
