from dataclasses import dataclass
from typing import List
from rich.console import Console

console = Console()

counts = {
    5: {"townsfolk": 3, "outsider": 0, "minion": 1, "demon": 1},
    6: {"townsfolk": 3, "outsider": 1, "minion": 1, "demon": 1},
    7: {"townsfolk": 5, "outsider": 0, "minion": 1, "demon": 1},
    8: {"townsfolk": 5, "outsider": 1, "minion": 1, "demon": 1},
    9: {"townsfolk": 5, "outsider": 2, "minion": 1, "demon": 1},
    10: {"townsfolk": 7, "outsider": 0, "minion": 2, "demon": 1},
    11: {"townsfolk": 7, "outsider": 1, "minion": 2, "demon": 1},
    12: {"townsfolk": 7, "outsider": 2, "minion": 2, "demon": 1},
    13: {"townsfolk": 9, "outsider": 0, "minion": 3, "demon": 1},
    14: {"townsfolk": 9, "outsider": 1, "minion": 3, "demon": 1},
    15: {"townsfolk": 9, "outsider": 2, "minion": 3, "demon": 1},
}

character_colours = {
    "townsfolk": "#6bd0ef",
    "outsider": "#529cb3",
    "minion": "#ee181c",
    "demon": "#8a1113"
}
colour_townsfolk = character_colours["townsfolk"]
colour_outsider = character_colours["outsider"]
colour_minion = character_colours["minion"]
colour_demon = character_colours["demon"]

@dataclass
class Character:
    name: str
    ability: str
    icon_url: str
    reminders: List[str]
    character_type: str
    effects: List[str]
    
@dataclass
class CharacterReduced:
    name: str
    character_type: str
    effects: List[str]