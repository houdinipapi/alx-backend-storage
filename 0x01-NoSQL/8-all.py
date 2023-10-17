#!/usr/bin/env python3

"""
List all documents in a collection
"""


def list_all(mongo_collection):
    """
    Use find() to retrieve all documents in the collection
    """
    documents = list(mongo_collection.find())

    return documents
