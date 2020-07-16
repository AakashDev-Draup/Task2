def assignactions(role):
    """
        :parameter
        role_read : roles which have read only access level
        role_read : roles which have access level to write
        role_read : roles which have access level to delete
        :returns
        This function returns the access level based on the roles
    """

    role_read = ['HR', 'Researcher']
    role_write = ['SDE', 'Analyst']
    role_delete = ['Admin']

    if role in role_read:
        return 'r'
    elif role in role_write:
        return 'w'
    elif role in role_delete:
        return 'd'
    else:
        pass


def addrole(user):
    """
        :parameter
        role : to keep track of the roles
        action : to keep track of access levels from the role
        :returns
        This function is used to add roles and based on that access levels to the user
    """

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

    """
    :parameter
    role : to keep track of the roles
    action : to keep track of access levels from the role
    :returns
    This function removes the roles and associated access levels
    """

    print(user.roles)
    no = int(input("Enter the no of roles to remove:"))
    role = []
    action = []
    for _ in range(no):
        role.append(input("Enter the role:"))
        action.append(assignactions(role))
    user.update_one(pull_all_roles=role)
    user.update_one(pull_all_actions=action)
    action = []
    for role in user.roles:
        action.append(assignactions(role))
    user.update_one(add_to_set_actions=action)
    user.reload()
    print(user.roles)


