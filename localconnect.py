from mongoengine import connect


def makeconnection():
    """This function is used to make connection to the local database"""
    connect("LocalDatabase")