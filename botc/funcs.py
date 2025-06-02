from typing import Dict, List, Union
from botc.consts import Character

def load_character(name: str, character_dict: Dict[str, Union[str, List[str]]]) -> Character:
    return Character(
        name=name,
        ability=str(character_dict["ability"]),
        icon_url=str(character_dict["icon_url"]),
        reminders=list(character_dict["reminders"]),
        character_type=str(character_dict["character_type"]),
        effects=list(character_dict["effects"])
    )
