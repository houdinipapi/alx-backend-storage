#!/usr/bin/env python3

"""
Top students
"""


def top_students(mongo_collection):
    """
    Return: All students sorted by average score.
    """
    top_student = mongo_collection.aggregate(
        [
            {
                "$project": {
                    "name": "$name", "averageScore": {"$avg": "$topics.score"}}
            },
            {"$sort": {"aveargeScore": -1}},
        ]
    )

    return top_student
