import json


class Conf:

    config = {}

    with open("config/general.json", "r") as f:
        config = json.load(f)

