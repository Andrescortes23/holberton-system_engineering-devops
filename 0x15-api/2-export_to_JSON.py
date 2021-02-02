#!/usr/bin/python3
"""Export to Json"""

import requests
from sys import argv
import json

if __name__ == '__main__':
    target = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(target)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(target)).json()
    the_list = []
    the_dict = {}
    for a in todos:
        task = {}
        task["task"] = a["title"]
        task["completed"] = a["completed"]
        task["username"] = user["username"]
        the_list.append(task)
    the_dict[target] = the_list

    with open("{}.json".format(target), 'w') as file:
        json.dump(the_dict, file)
