#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using a REST API.
"""

import sys
import requests


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
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    employee_data = employee_response.json()
    todo_data = todo_response.json()

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
