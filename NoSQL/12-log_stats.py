#!/usr/bin/env python3
"""
Task 12: Log Stats Analyzer
"""
from pymongo import MongoClient


def analyze_logs(logs):
    """
    Analyze logs and count HTTP methods and status checks.

    Parameters:
    - logs (list): List of log documents.

    Returns:
    - tuple: A tuple containing a dictionary with counts
      of HTTP methods and the number of status checks.
    """
    methods = {'GET': 0, 'POST': 0, 'PUT': 0, 'PATCH': 0, 'DELETE': 0}

    status_check = 0

    for doc in logs:
        method = doc.get('method', '')
        if method in methods:
            methods[method] += 1

        path = doc.get('path', '')
        if path == '/status':
            status_check += 1

    return methods, status_check


def print_results(log_count, methods, status_check):
    """
    Print log analysis results.

    Parameters:
    - log_count (int): Total number of logs.
    - methods (dict): Dictionary containing counts
      of each HTTP method.
    - status_check (int): Number of status checks.

    Returns:
    - None
    """
    print(f"{log_count} logs\nMethods:")
    for method, count in methods.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Retrieve logs from MongoDB
    logs = list(nginx_collection.find())
    log_count = len(logs)

    # Analyze logs
    methods, status_check = analyze_logs(logs)

    # Print results
    print_results(log_count, methods, status_check)
