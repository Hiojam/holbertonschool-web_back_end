#!/usr/bin/env python3
"""
Task 11 - Retrieve schools by topic from a MongoDB collection
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve and return a list of schools that have a specific topic.

    Parameters:
    - mongo_collection (pymongo.collection.Collection): The MongoDB collection.
    - topic (str): The specific topic to filter schools by.

    Returns:
    - pymongo.cursor.Cursor: A cursor containing the schools matching
      the specified topic.
    """
    topics = mongo_collection.find({"topics": topic})
    return topics
