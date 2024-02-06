#!/usr/bin/python3
"""
This is '100-append_after' module.
Functions and Classes:
    append_after(filename="", search_string="", new_string="")
"""


def append_after(filename="", search_string="", new_string=""):
    """
    insert txt line to file
    """
    with open(filename, "r", encoding="UTF-8") as f:
        # store file content in 'content'
        content = f.read()
        f.seek(0, 0)

        # new_string properties
        s_size = len(new_string)
        insertions = 0

        # store sum of lines' sizes
        sizes = 0

        for line in f:
            sizes += len(line)
            if search_string in line:
                index = sizes + (s_size*insertions)
                content = content[:index] + new_string + content[index:]
                insertions += 1

    with open(filename, "w", encoding="UTF-8") as f:
        f.write(content)
