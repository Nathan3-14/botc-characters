import re
from typing import List
from botc import (
    console,
    counts, CharacterReduced,
    load_character,
    character_colours, colour_townsfolk, colour_outsider, colour_minion, colour_demon
)
from botc.funcs import load_character_reduced


player_count = 9
chosen_characters: List[CharacterReduced] = [load_character_reduced("baron", {
        "character_type": "minion",
        "effects": ["+2outsider"]
    })
]
character_path = "./characters_tb.json"

while True:
    count_townsfolk = counts[player_count]["townsfolk"]
    count_outsider = counts[player_count]["outsider"]
    count_minion = counts[player_count]["minion"]
    count_demon = counts[player_count]["demon"]
    
    #* Add Effects *#
    for character in chosen_characters:
        if len(character.effects) == 0:
            continue
        for effect in character.effects:
            args = effect.split(".")
            effect_temp = args[0]
            
            #* Choice required *#
            if "!" in args[0]:
                effect_choice = input(f"A: {args[1]}, B: {args[2]}\n\t>> ")
                effect_choice_index = -1
                if effect_choice.upper() == "A":
                    effect_choice_index = 1
                elif effect_choice.upper() == "B":
                    effect_choice_index = 2
                else:
                    console.print("[red bold]Invalid option, skipping effect[/red bold]")
                    continue
                
                effect_temp = args[effect_choice_index]
                if "?" in args[effect_choice_index]:
                    effect_value = input("Enter a value\n\t>> ")
                    effect_temp = effect_temp.replace("?", effect_value)
                
            
            #* Execute Current Effect *#
            if "+" or "-" in effect_temp:
                add_bool = "+" in effect_temp
                match effect_temp[2:]:
                    case "townsfolk":
                        count_townsfolk += (add_bool * 2 - 1) * int(effect_temp[1])
                        count_outsider -= (add_bool * 2 - 1) * int(effect_temp[1])
                    case "outsider":
                        count_outsider += (add_bool * 2 - 1) * int(effect_temp[1])
                        count_townsfolk -= (add_bool * 2 - 1) * int(effect_temp[1])
                    case "minion":
                        count_minion += (add_bool * 2 - 1) * int(effect_temp[1])
                        count_townsfolk -= (add_bool * 2 - 1) * int(effect_temp[1])
                    case "demon":
                        count_demon += (add_bool * 2 - 1) * int(effect_temp[1])
                        count_outsider -= (add_bool * 2 - 1) * int(effect_temp[1])
            else:
                match effect_temp:
                    case "not_in_bag":
                        console.print(f"[bold]REMINDER - Don't add {character.name} to bag[/bold]")
    
    console.print(f"Current Characters: {", ".join([f"[{character_colours[character.character_type]}]{" ".join([part.capitalize() for part in character.name.split(" ")])}[/{character_colours[character.character_type]}]" for character in chosen_characters])}")
    console.print(f"Required Counts:")
    console.print(f"\t[{colour_townsfolk}]Townsfolk: {count_townsfolk}[/{colour_townsfolk}]")
    console.print(f"\t[{colour_outsider}]Outsider: {count_outsider}[/{colour_outsider}]")
    console.print(f"\t[{colour_minion}]Minion: {count_minion}[/{colour_minion}]")
    console.print(f"\t[{colour_demon}]Demon: {count_demon}[/{colour_demon}]")
    action = input("")
    match action:
        case "q" | "quit" | "exit":
            break
        case "help" | "h":
            console.print("\n*****\nHelp here!\n*****\n")


#TODO Load from file TODO#