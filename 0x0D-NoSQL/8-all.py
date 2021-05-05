#!/usr/bin/env python3
""" pymongo module """


def list_all(mongo_collection):
    """ Function that lists all documents in a collection """
    doc = mongo_collection.find()
    if doc:
        return doc
    else:
        return []
