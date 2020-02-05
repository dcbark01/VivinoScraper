import os
import json


def load_results_json(file):
    with open(file, 'r') as infile:
        data = json.load(infile)
    return data