def makeconnection():
    """This function is used to make connection to the local database"""
    from mongoengine import connect
    connect("LocalDatabase")