from pathlib import Path
import re 
import json

ITEM_TYPES = {"Armor": "LiShield",
              "Weapon": "LiSwords",
              "Rod": "LiWand2",
              "Scroll": "LiScrollText",
              "Wondrous Item": "LiComponent",
              "Ring": "LiComponent",
              "Wand": "LiWand",
              "Potion": "LiFlaskRound",
              "Staff": "RaCrystalWand"}
ITEM_RARITIES = ["Common", "Uncommon", "Very Rare", "Rare", "Legendary", "Artifact", "Varies"]
CLASSES = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

class Item:
    def __init__(self):
        self.tags = ["Item"]
        self.name = None
        self.attunement = False
        self.attunement_details = None
        self.classes = []
        self.icon = None
        self.rarity = None
        self.sources = ["[[Dungeon Master's Guide 2024]]"]
        self.type = None
        self.type_details = None
        self.description = []

def remove_links(line):
    with open(".\\z_Scripts\\header_dict.json", "r", encoding="utf-8") as f:
        header_dict = json.load(f)

    edited_line = line
    regex = r"[\s\S]*?(\[([^\]\[]*?)\]\([\s\S]*?\))[\s\S]*?"
    m = re.match(regex, edited_line)

    # Clean line of links
    while m is not None:
        to_replace = m.group(1)
        print(f"Found line to replace: {to_replace}")
        if m.group(2) != "":
            if m.group(2) in header_dict:
                print("\tFound non empty link. Replacing...")
                edited_line = edited_line.replace(to_replace, f"[[{header_dict[m.group(2)]}]]")
            else:
                print("Unknown header. Replacing...")
                edited_line = edited_line.replace(to_replace, f"[[{m.group(2)}]]")
        else:
            print("\tFound empty link. Removing...")
            edited_line = edited_line.replace(to_replace, "")
        m = re.match(regex, edited_line)
    
    return edited_line

def main():
    file = f"C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\raw-items.md"

    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        item = Item()
        items = []
        skip = False
        for line in lines:
            line = line.replace("’", "'")
            if skip:
                skip = False
                continue
            if line.startswith("###") and not line.startswith("####"):   # Line has a name
                if item.name is not None:
                    print("\tGot to end of a item...")
                    # Got to the end of a spell
                    items.append(item)
                    item = Item()
                # Get Name
                regex = r"[\s\S]*?\[([^\[\}]+?)\][\s\S]*?"
                m = re.match(regex, line)
                if m is not None:
                    item.name = m.groups()[0].strip()
                    print(f"Found Item: {item.name}")
                else:
                    regex = r"[\s\S]*?\[[\s\S]*\]\([\s\S]+\)([\s\S]+)"
                    m = re.match(regex, line)
                    if m is not None:
                        item.name = m.groups()[0].strip()
                        print(f"Found Item: {item.name}")
                    else:
                        print(f"Got weird line: {line}")
                        item.description.append(remove_links(line))
            elif line.startswith("_") and line.count("_") == 2 and line.endswith("_\n"):  # Item type and attunement
                print("\tFound item type and attunement details")
                if line.count(",") > 1:
                    split = line.split("),", 1)
                    if len(split) < 2:
                        split = line.split(",", 1)
                else:
                    split = line.split(",", 1)
                    
                type_details = split[0]
                rarity_details = split[1]

                # Get type
                for type in ITEM_TYPES.keys():
                    if type in type_details:
                        item.type = type
                        item.icon = ITEM_TYPES[type]

                    if "(" in type_details:
                        split = type_details.split("(")
                        item.type_details = split[1].replace(")", "").strip()

                # Get rarity
                rarity_count = 0
                for rarity in ITEM_RARITIES:
                    if rarity in rarity_details:
                        item.rarity = rarity
                        rarity_count = rarity_count + 1
                if rarity_count > 1:
                    item.rarity = "Varies"
                
                # Get attunement
                if "attunement" in rarity_details.lower():
                    item.attunement = True
                    if "attunement by" in rarity_details.lower():
                        split = rarity_details.split("by")
                        item.attunement_details = split[1][:-3].strip()

                        for clas in CLASSES:
                            if clas in item.attunement_details:
                                item.classes.append(f"[[{clas}]]")
            elif "Conceptopolis" in line:
                continue
            elif line.startswith("##") and "Magic Items (" in line:
                continue
            else:
                item.description.append(remove_links(line))
        items.append(item)

        for item in items:
            while item.description[0] == "\n":
                del item.description[0]

        with open(".\\z_Scripts\\item_dict.json", "w", encoding="utf-8") as f:
            json.dump([item.__dict__ for item in items], f, indent = 4)

if __name__ == "__main__":
    main()
