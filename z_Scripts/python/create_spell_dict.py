from pathlib import Path
import re 
import json

class Spell:
    def __init__(self):
        self.name = None
        self.school = None
        self.level = None
        self.classes = []
        self.casting_time = None
        self.ritual = False
        self.range = None
        self.components = []
        self.concentration = False
        self.duration = None
        self.description = []
        self.scales = False

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
    file = f"C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\raw_spells.md"

    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        spell = Spell()
        spells = []
        skip = False
        for line in lines:
            line = line.replace("’", "'")
            if skip:
                skip = False
                continue
            if line.startswith("###") and not line.startswith("####"):   # Line has a name
                if spell.name is not None:
                    print("\tGot to end of a spell...")
                    # Got to the end of a spell
                    spells.append(spell)
                    spell = Spell()
                # Get Name
                regex = r"[\s\S]*?\[([^\[\}]+?)\][\s\S]*?"
                m = re.match(regex, line)
                if m is not None:
                    spell.name = m.groups()[0].strip()
                    print(f"Found Spell: {spell.name}")
                else:
                    print(f"Got weird line: {line}")
                    spell.description.append(remove_links(line))
            elif line.startswith("_") and "_Level" in line: # Spell level and school
                print("\tFound spell level and school")
                split = line.split(" ")
                spell.level = int(split[1])
                spell.school = split[2].strip()
                spell.classes = [c.replace("(", "").replace(",", "").replace(")", "").replace("_", "").replace("\n", "") for c in split[3:]]
                spell.description.append(remove_links(line))
            elif line.startswith("_") and "Cantrip" in line: # Cantrip and school
                print("\tFound cantrip and school")
                split = line.split(" ")
                spell.level = 0
                spell.school = split[0].replace("_", "")
                spell.classes = [c.replace("(", "").replace(",", "").replace(")", "").replace("_", "").replace("\n", "") for c in split[2:]]
                spell.description.append(remove_links(line))
            elif line.startswith("---"):    # Get rid of breaks
                continue
            elif line.startswith("## []") and "Spells (" in line:
                continue
            elif "**Casting Time:**" in line:   # Casting time
                spell.casting_time = line.split(":", 1)[1].replace("*", "").replace("\n", "").strip()
                spell.ritual = ("ritual" in spell.casting_time.lower())
                spell.description.append(remove_links(line))
                skip = True
            elif "**Range:**" in line:  # Range
                spell.range = line.split(":", 1)[1].replace("*", "").replace("\n", "").strip()
                spell.description.append(remove_links(line))
                skip = True
            elif "**Components:**" in line:  # Components
                spell.components = [c.strip() for c in line.split(":", 1)[1].replace("*", "").replace("\n", "").strip().split(",", 2)]
                for i in range(len(spell.components)):
                    if spell.components[i].startswith("M"):
                        m_component = spell.components[i]
                        del spell.components[i]
                        spell.components.extend([x.replace(")", "").strip() for x in m_component.split("(", 1)])
                spell.description.append(remove_links(line))
                skip = True
            elif "**Duration:**" in line:  # Duration
                if "[Concentration]" in line:
                    spell.concentration = True
                spell.duration = remove_links(line.split(":", 1)[1].replace("*", "").replace("\n", "").strip())
                spell.description.append(remove_links(line))
            elif "**_Cantrip Upgrade._**" in line or "**_Using a Higher-Level Spell Slot._**" in line:
                spell.scales = True
                spell.description.append(remove_links(line))
            else:
                spell.description.append(remove_links(line))
        spells.append(spell)


        for spell in spells:
            spell.duration = spell.duration.replace("[[Spells#Concentration\\|Concentration]]", "Concentration")
            while spell.description[0] == "\n":
                del spell.description[0]
            while spell.description[-1] == "\n":
                del spell.description[-1]

        with open(".\\z_Scripts\\spell_dict.json", "w", encoding="utf-8") as f:
            json.dump([spell.__dict__ for spell in spells], f, indent = 4)

if __name__ == "__main__":
    main()
