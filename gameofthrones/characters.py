"""This module retrieves all the game of thrones characters"""

import os
import json
import string
from colorama import Fore, Back, Style

from logger import Logger

class Characters():
    def __init__(self, season=None, log_level="ERROR"):
        """Constructor """
        self.season = season
        self.data = os.path.join(os.path.dirname(__file__), "data")
        self.log_level = log_level
        log_obj = Logger("/tmp/gameofthrones.log")
        self.log = log_obj.configure_logger(logger_level=log_level)

    def _gen_all_characters(self, color=False):
        """Generate characters by season"""
        file = os.path.join(self.data, "characters-gender-all.json")
        ret = []
        all_characters = json.load(open(file, "r"))
        for alphabet in string.ascii_uppercase:
            if color:
                ret.append(Fore.YELLOW + str(alphabet) + Style.RESET_ALL)
            else:
                ret.append(str(alphabet))
            for gender in all_characters:
                if color:
                    ret.append(Fore.GREEN + str(gender).upper() + Style.RESET_ALL)
                char_list = []
                for characters in all_characters[gender]:
                    if alphabet == characters[0]:
                        char_list.append(str(characters))
                if color:
                    ret .append(Fore.RED + ",".join(char_list) + Style.RESET_ALL)
                else:
                    ret.append(", ".join(char_list))
        return ("\n".join(ret))






