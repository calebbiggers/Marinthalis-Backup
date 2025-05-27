from pathlib import Path
import re 
import json

def main():
    directories = [ Path(r"C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\z_Website"),
                    Path(r"C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\D&D Rules\\Equipment"),
                    Path(r"C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\D&D Rules\\Gameplay"),
                    Path(r"C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\D&D Rules\\Wondrous Items"),
                    Path(r"C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\D&D Rules\\Classes"),
                    Path(r"C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\D&D Rules\\Subclasses"),
    ]

    dictionary = {}
    for directory in directories:
        for file in Path.rglob(directory, "*.md"):
            file_name = file.stem
            with open(file, "r", encoding="utf-8") as f:
                headings = []

                # Get all the headings
                lines = f.readlines()
                for line in lines:
                    if "# " in line and "[" not in line:
                        # This is a title
                        headings.append(line.replace("#", "").strip())
                
                # Got all the titles
                for heading in headings:
                    if heading.count(",") == 1: # Crossbow, Hand
                        barfoo = heading.split(",")
                        bar = barfoo[0].strip()
                        foo = barfoo[1].strip()
                        dictionary[heading] = [f"{file_name}#{heading}\\|{heading}"]
                        dictionary[f"{foo} {bar}"] = [f"{file_name}#{heading}\\|{foo} {bar}"]
                    elif heading.count(":") == 1:   # Level 3: Ability
                        split = heading.split(":")
                        ability = split[1].strip()
                        if ability in dictionary:
                            print(f"Found duplicate heading: {ability}")
                            dictionary[ability].append(f"{file_name}#{heading.strip()}\\|{ability}")
                        else:
                            dictionary[ability] = [f"{file_name}#{heading.strip()}\\|{ability}"]
                    else:   # Other heading
                        if heading in dictionary:
                            print(f"Found duplicate heading: {heading}")
                            dictionary[heading].append(f"{file_name}#{heading}\\|{heading}")
                        else:
                            dictionary[heading] = [f"{file_name}#{heading}\\|{heading}"]
    


    for heading, links in dictionary.items():
        dictionary[heading] = list(set(links))

    # Special Cases
    dictionary["Advantage"] = "D20 Tests#Advantage/Disadvantage\\|Advantage"
    dictionary["Disadvantage"] = "D20 Tests#Advantage/Disadvantage\\|Disadvantage"

    dictionary["Long Rest"] = "Damage & Healing#Long Rests\\|Long Rest"
    dictionary["Long"] = "Damage & Healing#Long Rests\\|Long"
    dictionary["Short Rest"] = "Damage & Healing#Short Rests\\|Short Rest"
    dictionary["Short"] = "Damage & Healing#Short Rests\\|Short"

    dictionary["Acrobatics"] = "Proficiency#Skill List\\|Acrobatics"
    dictionary["Animal Handling"] = "Proficiency#Skill List\\|Animal Handling"
    dictionary["Arcana"] = "Proficiency#Skill List\\|Arcana"
    dictionary["Athletics"] = "Proficiency#Skill List\\|Athletics "
    dictionary["Deception"] = "Proficiency#Skill List\\|Deception"
    dictionary["History"] = "Proficiency#Skill List\\|History"
    dictionary["Insight"] = "Proficiency#Skill List\\|Insight"
    dictionary["Intimidation"] = "Proficiency#Skill List\\|Intimidation"
    dictionary["Investigation"] = "Proficiency#Skill List\\|Investigation"
    dictionary["Medicine"] = "Proficiency#Skill List\\|Medicine"
    dictionary["Nature"] = "Proficiency#Skill List\\|Nature"
    dictionary["Perception"] = "Proficiency#Skill List\\|Perception"
    dictionary["Performance"] = "Proficiency#Skill List\\|Performance"
    dictionary["Persuasion"] = "Proficiency#Skill List\\|Persuasion"
    dictionary["Religion"] = "Proficiency#Skill List\\|Religion"
    dictionary["Sleight of Hand"] = "Proficiency#Skill List\\|Sleight of Hand"
    dictionary["Stealth"] = "Proficiency#Skill List\\|Stealth"
    dictionary["Survival"] = "Proficiency#Skill List\\|Survival"

    dictionary["Area of Effect"] = "Spells#Areas of Effect\\|Area of Effect"

    dictionary["Reaction"] = "Actions#Reactions\\|Reaction"

    dictionary["Ritual"] = "Spells#Rituals\\|Ritual"

    # Remove unneeded options
    del dictionary["Other"]
    del dictionary["Spellcasting"]
    del dictionary["As a Level 1 Character"]
    del dictionary["As a Multiclass Character"]
    del dictionary["Weapon Mastery"]
    del dictionary["Ability Score Improvement"]
    del dictionary["Extra Attack"]
    del dictionary["Channel Divinity"]
    del dictionary["Fighting Style"]
    del dictionary["Evasion"]

    del dictionary["Epic Boon"] # May need to remove later
    del dictionary["Expertise"] # May need to remove later

    for heading, links in dictionary.items():
        if len(links) > 1:
            print(f"Found multiple links:")
            print(f"\t{links}")
            for link in links:
                if "The World of Marinthalis" in link:
                    dictionary[heading] = link
                    continue
                elif "The Party" in link:
                    dictionary[heading] = link
                    continue
                elif "D20" in link:
                    dictionary[heading] = link
                    continue
                elif "Weapons" in link:
                    dictionary[heading] = link
                    continue
            if type(dictionary[heading]) is list:
                index = input("\tPlease enter the index of the correct link: ")
                while int(index) >= len(links):
                    index = input("\tPlease enter the index of the correct link: ")
                dictionary[heading] = links[int(index)]
        else:
            dictionary[heading] = links[0]

    dictionary = dict(sorted(dictionary.items()))
    with open("header_dict.json", "w", encoding="utf-8") as f:
        json.dump(dictionary, f, indent = 4)

if __name__ == "__main__":
    main()