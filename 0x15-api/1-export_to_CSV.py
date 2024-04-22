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
    username = user.get("username")
    todos = requests.get(
            base_url + "todos", params={"userId": employee_id}).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                    [employee_id, username, todo.get("completed"),
                        todo.get("title")])

    return len(todos)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    num_tasks = export_to_csv(employee_id)
    print(
        f"Number of tasks in CSV: {'OK' if num_tasks == 20 else 'Incorrect'}")
