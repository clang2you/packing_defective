import json

class CfgHelper():
    def __init__(self):
        with open(r"example.json", "rb") as f:
            self.cfg_dict = json.load(f)
        