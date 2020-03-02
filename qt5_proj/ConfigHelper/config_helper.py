import json
import os

class CfgHelper():
    def __init__(self):
        with open(os.path.split(os.path.realpath(__file__))[0] + r"\config.json", "rb") as f:
            self.cfg_dict = json.load(f)
        