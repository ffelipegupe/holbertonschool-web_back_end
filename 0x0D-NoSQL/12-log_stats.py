#!/usr/bin/env python3
""" pymongo module """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log = len(list(nginx_collection.find()))
    print(log, "logs\nMethods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for meth in methods:
        print(
            "\tmethod {}: {}".format(
                meth, len(list(nginx_collection.find({"method": meth})))
                )
            )
    print(
        "{} status check".format(
            len(list(
                nginx_collection.find({"method": "GET", "path": "/status"})
                ))
            )
        )
