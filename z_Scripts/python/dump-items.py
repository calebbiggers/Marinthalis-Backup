from pathlib import Path
import json 

def write_item(file, item):
    file.write("---\ntags:\n  - Item\n")
    file.write(f"type: {item["type"]}\n")
    file.write(f"attunement: {item["attunement"]}\n")
    file.write(f"attunement_details: {item["attunement_details"]}\n")
    file.write("classes:\n")
    for c in item["classes"]:
        file.write(f"  - \"{c}\"\n")
    file.write(f"icon: {item["icon"]}\n")
    file.write(f"rarity: {item["rarity"]}\n")
    file.write(f"type: {item["type"]}\n")
    file.write(f"type_details: {item["type_details"]}\n")
    file.write("sources: \n")
    file.write("  - \"[[Dungeon Master's Guide 2024]]\"\n")
    file.write("---\n")

    file.write(f">[!{item["rarity"].lower()}-{item["type"].replace(" ", "-").lower()}-callout] {item["name"]}\n")
    
    file.write(f">_{item["type"]}")
    if item["type_details"] != None:
        file.write(f" ({item["type_details"]}) ")
    file.write(f", ")
    file.write(f"{item["rarity"]}")
    if item["attunement"]:
        file.write(f" (Requires Attunement")
        if item["attunement_details"] != None:
            file.write(f" {item["attunement_details"]}")
        file.write(")")
    file.write("_\n>\n")

    for line in item["description"]:
        file.write(f">{line.replace("’", "'")}")
    file.write("\n\n![[dungeon-masters-guide-2024.avif|banner]]")

def main():
    path = Path("C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\z_Scripts\\item_dict.json")
    with open(path, "r") as file:
       items = json.load(file)

    out = Path("C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\z_Scripts\\Item Output")
    for item in items:
        item_path = Path.joinpath(out, f"{item["name"].replace("/", "-")}.md")
        with open(item_path, "w+", encoding="utf-8") as item_file:
            write_item(item_file, item)
            

if __name__ == "__main__":
    main()