#!/usr/bin/python3
"""
This script lists all states from the db hbtn_0e_0_usa
"""


def main():
    """
    List states table of 'hbtn_0e_0_usa' database in ascending
    order by ids
    """
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
