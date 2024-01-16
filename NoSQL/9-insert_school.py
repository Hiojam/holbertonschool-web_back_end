#!/usr/bin/env python3
"""
Task 9:
Insert a new document into a MongoDB collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a specified MongoDB collection.

    Parameters:
    - mongo_collection (pymongo.collection.Collection): The MongoDB collection.
    - **kwargs: Keyword arguments representing the fields and values
      of the new document.

    Returns:
    - ObjectId: The unique identifier (_id) of the newly inserted document.
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
