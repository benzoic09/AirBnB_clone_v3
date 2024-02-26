#!/usr/bin/python3

from models import storage

def stats():
    """
    Retrieves the number of each objects by type
    """
    objs = storage.all().values()
    print(objs)
    obdict = {}
    for obj in objs:
        cls = obj.__class__
        clsname = obj.__class__.__name__
        obdict[clsname] = storage.count(cls)

    print(obdict)

stats()
