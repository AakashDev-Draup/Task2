def makeconnection():
    """This function is used to make connection to our database"""
    from mongoengine import  connect
    connect("LocalDatabase")