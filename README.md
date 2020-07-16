# Task2

Hello,

To access the Role based control app run the main.py using python interpreter.
It gives the following options:

Welcome to xyz:

Enter 1 to Add user: To add a new user you select this option. You have to enter a username that is unique to the database.

Enter 2 to Delete user: To delete a user from the database you use this option.
  
Enter 3 to Update user details: To update a user record from the database you use this option.

Enter 4 to access data: To access the resources in database you have to use this option. 
You need to enter your username and the required operation you wantto perform i.e. read , write or delete. 
You should have the appropriate access level to perform the operation.

Enter 5 to assign role: You can assign the roles for a user using this option. You need to enter the username for the user here.
A single user can have multiple roles and based on these roles the access levels are assigned to the user.

Enter 6 to remove role: You can remove the roles from a given user using this option.You need to enter the username for the user here.
You can remove multiple roles of a user from the database. This also modifies the access levels based on role removal.

Enter 7 to exit


Following points are to be Noted:

The role based access control was developed on a local server.

Add user, delete user , update user and access resource from the database were imported from pre created functions.


Following is the problem statement:

Role Based Access Control:

Implement a role-based authentication system. System should be able to assign a role to user and remove a user from the role.
Entities are USER, ACTION TYPE, RESOURCE, ROLE

ACTION TYPE defines the access level (Ex: READ, WRITE, DELETE)
Resource Storage: Database (PostgreSQL or Mongo)
Access to resources for users are controlled strictly by the role. One user can have multiple roles. 
Given a user, action type and resource system should be able to tell whether user has access or not.
Note:
• Create class-based structure using OOPS concept.
• Follow file structure to make code maintainable and production ready.
• Go through git commands and push the code in git with README.md.
• This is a command line application.
• You do not need to create functionality to add/delete/update users or any other entities. You can get it pre-created.


