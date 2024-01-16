#!/usr/bin/env python3
"""
Task 8:
List all documents in a MongoDB collection
"""


def list_all(mongo_collection):
    """
    Retrieve and return all documents from a given MongoDB collection.

    Parameters:
    - mongo_collection (pymongo.collection.Collection): The MongoDB collection.

    Returns:
    - list: A list containing all documents in the collection.
    """
    all_documents = list(mongo_collection.find())
    return all_documents
