#!/usr/bin/env python3
"""
return list of school by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    return list of schools
    """
    return mongo_collection.find({"topics": topic})
