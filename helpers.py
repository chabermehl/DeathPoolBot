from datetime import datetime
from tabulate import tabulate


def command_logger(user, command):
    print(f'{user} input {command} @ {datetime.now()}.')


def pretty_print(entries):
    formatted_entries = []
    for entry in entries:
        formatted_entries.append(
            [entry, entries[entry]["picked_by"], entries[entry]["status"], entries[entry]["age"]])
    formatted_entries.sort(key=lambda x: x[3])
    formatted_entries.reverse()
    return tabulate(formatted_entries, headers=['Person', 'Picked By', 'Status', 'Age'])
