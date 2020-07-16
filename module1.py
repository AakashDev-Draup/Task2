from mongoengine import Document, StringField, ListField
from localconnect import makeconnection

makeconnection()


class User(Document):
    """This class has all the attributes for a new user"""
    username = StringField(unique=True, required=True, max_length=10)
    meta = {'allow_inheritance': True}


class accesslevel(User):
    """This class has the roles and actions for the user from the User class"""
    roles = ListField(StringField())
    actions = ListField(StringField())


if __name__ == "__main__":

    while True:
        print("Welcome to xyz")
        print("Enter 1 to Add user:")
        print("Enter 2 to Delete user:")
        print("Enter 3 to Update user details:")
        print("Enter 4 to access data:")
        print("Enter 5 to assign role")
        print("Enter 6 to remove role")
        print("Enter 7 to exit")
        val = int(input("Please enter your choice:"))
        if val == 1:
            from useroperation import deleteuser
            user = adduser()
            user.save()
        elif val == 2:
            from useroperation import adduser
            deleteuser()
        elif val == 3:
            from useroperation import updateuser
            updateuser()
        elif val == 4:
            name = input("Please enter the username:")
            obj = User.objects(username=name).get()
            if obj:
                enter = input("Enter r to Read, w to write and d to delete:")
                if enter in obj.actions:
                    from useroperation import accessdata
                    accessdata(enter)
                else:
                    print("You don't have the required access level")
            else:
                print("user not found")

        elif val == 5:
            name = input("Please enter the username:")
            obj = User.objects(username=name).get()
            if obj:
                from userroles import addrole
                addrole(obj)
            else:
                print("user not found")
        elif val == 6:
            name = input("Please enter the username:")
            obj = User.objects(username=name).get()
            if obj:
                from userroles import removerole
                removerole(obj)
            else:
                print("user not found")
        elif val == 7:
            exit()
        else:
            print("Please enter a valid choice")

        val = int(input('Choose 1 to quit and 2 to continue:'))
        if val == 1:
            exit()
        else:
            continue



