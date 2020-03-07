import json
import os
import codecs


class CfgHelper():
    def __init__(self):
        try:
            with open(os.path.split(os.path.realpath(__file__))[0] + r"\config.json", "rb") as f:
                self.cfg_dict = json.load(f)
        except:
            self.cfg_dict = {"MySQL": None, "Line": None, "Section": None,
                             "QcInfo": None, "Admin": None, "DefReasons": None}
            self.SaveConfigToJson(self.cfg_dict)

    def SaveConfigToJson(self, cfg_dict):
        with codecs.open(os.path.split(os.path.realpath(__file__))[0] + r"\config.json", "w", encoding="utf-8") as f:
            json.dump(cfg_dict, f, ensure_ascii=False)
