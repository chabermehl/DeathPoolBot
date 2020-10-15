import math
from datetime import datetime
from tabulate import tabulate
import pandas as pd


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


def process_csv():
    picks_dictionary = {}

    # Read in some data from csv do minor cleaning
    data = pd.read_csv('DeathPool.csv')
    just_picks = data[7:].fillna(0)

    pickers = clean_data(just_picks['picker'])
    u90 = clean_data(just_picks['u90'])
    u40 = clean_data(just_picks['u40'])
    pick3 = clean_data(just_picks['pick3'])

    # shove it all in a dict cuz im lazy
    picks_dictionary["pickers"] = pickers
    picks_dictionary["u90"] = u90
    picks_dictionary["u40"] = u40
    picks_dictionary["pick3"] = pick3

    return picks_dictionary


def clean_data(datas):
    cleaned = []
    for data in datas:
        # check for bad/misisng values
        if data != 0:
            cleaned.append(data)
    return cleaned


def build_picks(dict):
    picks = {}

    pickers = dict["pickers"]
    u90 = dict["u90"]
    u40 = dict["u40"]
    pick3 = dict["pick3"]
