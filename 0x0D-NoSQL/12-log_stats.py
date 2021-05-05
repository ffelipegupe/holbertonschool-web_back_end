#!/usr/bin/env python3
""" pymongo module """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print(f'{nginx_collection.find().count_docments()} logs')
    print('Methods:')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for _method in methods:
        method_count = nginx_collection.find(
            {'method': _method}
        ).count_documents()

        print(f'\tmethod {_method}: {method_count}')

    status_check_count = nginx_collection.find(
        {'method': 'GET', 'path': '/status'}
    ).count_documents()
    print(f'{status_check_count} status check')
