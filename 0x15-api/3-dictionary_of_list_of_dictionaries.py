#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using a REST API and exports the data in JSON format.
"""

import json
import requests
import sys


def export_to_json(data):
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    all_employees_tasks = {}
    users = requests.get(base_url + "users").json()
    for user in users:
        user_id = user['id']
        user_name = user['username']
        todos = requests.get(
                base_url + "todos", params={"userId": user_id}).json()
        user_tasks = []
        for todo in todos:
            user_tasks.append({
                "username": user_name,
                "task": todo["title"],
                "completed": todo["completed"]
            })
        all_employees_tasks[str(user_id)] = user_tasks

    export_to_json(all_employees_tasks)
