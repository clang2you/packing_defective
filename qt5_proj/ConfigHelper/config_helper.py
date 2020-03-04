import json
import os


class CfgHelper():
    def __init__(self):
        try:
             with open(os.path.split(os.path.realpath(__file__))[0] + r"\config.json", "rb") as f:
                 self.cfg_dict = json.load(f)
        except:
            self.cfg_dict = {}

    def SaveConfigToJson(self, cfg_dict):
        with open(os.path.split(os.path.realpath(__file__))[0] + r"\config.json", "w") as f:
                 json.dump(cfg_dict, f)