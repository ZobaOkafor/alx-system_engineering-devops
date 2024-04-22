#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(
            base_url + "todos",
            params={"userId": employee_id}).json()

    completed_tasks = [
            task.get("title") for task in todos if task.get("completed")]
    total_tasks = len(todos)

    print(
        "Employee {} is done with tasks({}/{}): "
        .format(user.get("name"), len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
