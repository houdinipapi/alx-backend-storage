#!/usr/bin/env python3

"""
List of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return: list of school having a specific topic.
    """

    schools = mongo_collection.find({"topics": topic})
    return list(schools)
