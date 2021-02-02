#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progres
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    target = argv[1]
    name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(target)).json()
    name = name.get('name')

    tasks = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(target)).json()
    completed = []
    for a in tasks:
        if a['completed'] is True:
            completed.append(a['title'])
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(completed), len(tasks)))
    for a in completed:
        print("\t {}".format(a))
