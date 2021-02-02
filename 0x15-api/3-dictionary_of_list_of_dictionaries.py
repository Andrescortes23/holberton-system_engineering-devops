#!/usr/bin/python3
"""Export all to json"""

import requests
import json


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    the_dict = {}
    for a in users:
        the_list = []
        for b in todos:
            if a['id'] == b['userId']:
                task = {}
                task["task"] = b["title"]
                task["completed"] = b["completed"]
                task["username"] = a['username']
                the_list.append(task)
        the_dict[a['id']] = the_list

    with open("todo_all_employees.json", 'w') as file:
        json.dump(the_dict, file)
