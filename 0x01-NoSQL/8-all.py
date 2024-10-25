#!/usr/bin/env python3
"""
list all documents
"""


def list_all(mongo_collection):
    """
    list all docs
    """
    return list(mongo_collection.find())
