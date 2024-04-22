#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using a REST API.
"""

import json
import sys
from urllib import request, error


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    employee_url = f'{base_url}users/{employee_id}'
    todo_url = f'{base_url}todos?userId={employee_id}'

    try:
        with request.urlopen(employee_url) as response:
            employee_data = json.loads(response.read().decode())
        with request.urlopen(todo_url) as response:
            todo_data = json.loads(response.read().decode())
    except error.HTTPError as e:
        print(f"Error: {e}")
        return

    employee_name = employee_data.get('name', 'Unknown Employee')
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get('completed'))

    print(
            f"Employee {employee_name}
            is done with tasks({completed_tasks}/{total_tasks}): ")
    for task in todo_data:
        if task.get('completed'):
            print(f"\t{task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
