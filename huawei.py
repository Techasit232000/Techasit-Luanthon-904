Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("# -*- coding:utf-8 -*-
from openstack import connection

# create connection
username = "replace-with-your-username" # username
password = "replace-with-your-password" # user password
projectId = "replace-with-your-projectId"    # project ID
userDomainId = "replace-with-your-domainId"  # account ID
auth_url = "https://iam.example.com/v3"    # endpoint url
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)

# set parameters
limit = 5

# define function for listing servers
def list_servers():
    # get server list with params
    servers = conn.compute.servers(limit=limit)
    # iterate servers list
    for server in servers:
        print(server)

# visit API
list_servers()")
       
SyntaxError: EOL while scanning string literal
>>> 