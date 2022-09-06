#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress. """


import requests
import json
import sys

if __name__ == "__main__":
    
    user_id = sys.argv[1]
    users = requests.get('https://jsonplaceholder.typicode.com/users/' + user_id)
    data_users = users.json()
    value_name = data_users.get('name')

    list_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    for index in list_todos.items():
        list_dicts = list_todos.json()
    value_n_task = list_dicts.get('completed')
    trues = 0
    falses = 0
    titles = []
    print "Employee {value_name} is done with tasks({Ntasks}/{Ttasks}):".fortmat(value_name, Ntasks, Ttasks)
            
