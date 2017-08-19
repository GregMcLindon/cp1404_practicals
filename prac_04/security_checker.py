"""Validates user names against a list"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

logon_username = str(input("Enter username: "))
if logon_username in usernames:
    print("Access granted")
else:
    print("Access denied")