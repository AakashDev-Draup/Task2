def assignactions(role):

    """This function returns the access level based on the roles"""

    #roles which have read only access
    role_read = [""]
    # roles which have write access
    role_write = [""]
    # roles which have delete access
    role_delete = [""]

    if role in role_read:
        return 'r'
    elif role in role_write:
        return 'w'
    elif role in role_delete:
        return 'd'
    else:
        pass


def addrole(user):

    """This function is used to add roles and based on that access levels to the user"""

    print(user.roles)
    no = int(input("Enter the no of roles to add:"))
    role = []
    action = []
    for _ in range(no):
        role.append(input("Enter the role:"))
        action.append(assignactions(role))
    user.update_one(add_to_set_roles=role)
    user.update_one(add_to_set_actions=action)
    user.reload()
    print(user.roles)


def removerole(user):

    """This function removes the roles and associated access levels"""

    print(user.roles)
    no = int(input("Enter the no of roles to remove:"))
    role = []
    action = []
    for _ in range(no):
        role.append(input("Enter the role:"))
        action.append(assignactions(role))
    user.update_one(pull_all_roles=role)
    user.update_one(pull_all_actions=action)
    user.reload()
    print(user.roles)


