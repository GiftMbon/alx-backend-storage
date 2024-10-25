#!/usr/bin/env python3
"""
update schoool topics
"""


def update_topics(mongo_collection, name, topics):
    """
    update school topics
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
