from test_function import max_for_dict
messages = [
    {'name': 'ola', 'time': 10, 'text':'123'},
    {'name': 'ola', 'time': 20, 'text':'1234'},
    {'name': 'ola', 'time': 30, 'text':'12356'}
]
max_for_dict(messages, 'time')

