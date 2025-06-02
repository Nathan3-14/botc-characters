from typing import List
from botc import (
    console,
    counts, Character,
    load_character,
    character_colours, colour_townsfolk, colour_outsider, colour_minion, colour_demon
)


player_count = 9
chosen_characters: List[Character] = [load_character("baron", {
        "ability": "There are extra Outsiders in play. [+2 Outsiders]",
        "icon_url": "https://wiki.bloodontheclocktower.com/images/6/6d/Icon_baron.png",
        "reminders": [],
        "character_type": "minion",
        "effects": ["+2outsider"]
    })
]
character_path = "./characters_tb.json"

while True:
    console.print(f"Current Characters: {", ".join([f"[{character_colours[character.character_type]}]{" ".join([part.capitalize() for part in character.name.split(" ")])}[/{character_colours[character.character_type]}]" for character in chosen_characters])}")
    console.print(f"Required Counts:")
    console.print(f"\t[{colour_townsfolk}]Townsfolk: {counts[player_count]["townsfolk"]}[/{colour_townsfolk}]")
    console.print(f"\t[{colour_outsider}]Outsider: {counts[player_count]["outsider"]}[/{colour_outsider}]")
    console.print(f"\t[{colour_minion}]Minion: {counts[player_count]["minion"]}[/{colour_minion}]")
    console.print(f"\t[{colour_demon}]Demon: 1[/{colour_demon}]")
    action = input("")
    match action:
        case "q" | "quit" | "exit":
            break
