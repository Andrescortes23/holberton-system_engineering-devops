#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progres
"""
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = int(argv[1])
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    complet = 0
    totaltasks = 0
    titles = []
    for a in todos:
        if a.get('userId') == employee_id:
            user = requests.get('https://jsonplaceholder.typicode.com/users')
            user = user.json()
            username = user[employee_id - 1]['name']
            if a.get('completed') is True:
                titles.append(a.get('title'))
                complet += 1
            totaltasks += 1
    print("Employee {} is done with tasks({}/{}):".format(username,
                                                          complet, totaltasks))
    for ti in titles:
        print("\t {}".format(ti))
