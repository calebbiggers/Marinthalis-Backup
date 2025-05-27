from pathlib import Path
import json 

def write_spell(file, spell):
    file.write("---\ntags:\n  - Spell\n")
    file.write(f"casting_time: {spell["casting_time"]}\n")
    file.write("classes:\n")
    for c in spell["classes"]:
        file.write(f"  - \"[[{c}]]\"\n")
    file.write("components:\n")
    for c in spell["components"]:
        file.write(f"  - {c}\n")
    file.write(f"concentration: {str(spell["concentration"]).lower()}\n")
    file.write(f"duration: {spell["duration"]}\n")
    file.write("icon: LiWand2\n")
    file.write(f"level: {spell["level"]}\n")
    file.write(f"range: {spell["range"]}\n")
    file.write(f"ritual: {str(spell["ritual"]).lower()}\n")
    file.write("schools:\n")
    file.write(f"  - {spell["school"]}\n")
    file.write("sources: \n")
    file.write("  - \"[[Player's Handbook 2024]]\"\n")
    file.write("---\n")

    file.write(f">[!spell-callout] {spell["name"]}\n")
    for line in spell["description"]:
        file.write(f">{line.replace("’", "'")}")
    file.write("\n\n![[players-handbook-banner.png|banner]]")

def main():
    path = Path("C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\z_Scripts\\spell_dict.json")
    with open(path, "r") as file:
       spells = json.load(file)

    out = Path("C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\z_Scripts\\Spell Output")
    for spell in spells:
        spell_path = Path.joinpath(out, f"{spell["name"].replace("/", "-")}.md")
        with open(spell_path, "w+", encoding="utf-8") as spell_file:
            write_spell(spell_file, spell)
            

if __name__ == "__main__":
    main()
