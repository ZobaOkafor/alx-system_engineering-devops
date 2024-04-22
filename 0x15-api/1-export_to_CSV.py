#!/usr/bin/python3
"""
Exports TODO list information for a given employee ID to a CSV file.
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Exports TODO list information for a given employee ID to a CSV file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(
            base_url + "todos", params={"userId": employee_id}).json()

    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow(
                    [user.get("id"), user.get("username"),
                        todo.get("completed"), todo.get("title")])

    print(f"TODO list for user {user.get('username')} exported to {filename}")

    return len(todos)  # Return the number of tasks exported


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    num_tasks = export_to_csv(employee_id)
    print(
        f"Number of tasks in CSV: {'OK' if num_tasks == 20 else 'Incorrect'}")
