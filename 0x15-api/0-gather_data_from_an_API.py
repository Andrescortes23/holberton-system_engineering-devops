#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progres
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    employee_id = int(argv[1])
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    totaltasks = 0
    titles = []
    for a in todos:
        if a.get('userId') == employee_id:
            user = requests.get('https://jsonplaceholder.typicode.com/users')
            user = user.json()
            username = user[employee_id - 1]['name']
            if a.get('completed') is True:
                titles.append(a.get('title'))
            totaltasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(username, len(titles), totaltasks))
    for ti in titles:
        print("\t {}".format(ti))
