#!/usr/bin/env python3
"""
Task 10 - Update school topics in a MongoDB collection
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document in a specified MongoDB collection.

    Parameters:
    - mongo_collection (pymongo.collection.Collection): The MongoDB collection.
    - name (str): The name of the school whose topics need to be updated.
    - topics (list): The new list of topics to replace the existing ones.

    Returns:
    - None
    """
    update_query = {"name": name}
    update_data = {"$set": {"topics": topics}}
    mongo_collection.update_many(update_query, update_data)
