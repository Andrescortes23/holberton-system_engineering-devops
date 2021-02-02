#!/usr/bin/python3
"""Export to csv"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    target = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(target)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(target)).json()

    with open("{}.csv".format(target), 'w') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for a in todos:
            writer.writerow([a['userId'], user['username'],
                             a['completed'], a['title']])
