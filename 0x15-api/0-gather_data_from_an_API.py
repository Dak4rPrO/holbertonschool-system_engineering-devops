#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress. """


import requests
import json
import sys

if __name__ == "__main__":
    
    def ident(user_id=int):
        
        user_id = sys.argv[1]
        users = requests.get('https://jsonplaceholder.typicode.com/users/' + user_id)
        data_users = users.json()
        value_name = data_users.get('name')

        list_todos = requests.get('https://jsonplaceholder.typicode.com/todos/' + user_id)
        for index in list_todos.items():
            list_dicts = list_todos.json()
        value_n_task = list_dicts.get('completed')
        
        
        return "Employee {value_name} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):".fortmat(value_name, Ntasks, Ttasks)