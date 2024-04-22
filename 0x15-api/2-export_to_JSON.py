#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using a REST API and exports it to a JSON file.
"""

import json
import requests
import sys


def export_to_json(employee_id):
    """
    Retrieves and exports information about an employee's TODO
    list progress to a JSON file.

    Args:
        employee_id (str): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(
            base_url + "todos", params={"userId": employee_id}).json()

    tasks = [
            {"task": todo.get("title"), "completed": todo.get("completed"),
                "username": user.get("username")} for todo in todos]
    data = {employee_id: tasks}

    filename = f"{employee_id}.json"
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

    print(f"TODO list for user {user.get('username')} exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_to_json(employee_id)
