from pathlib import Path
import re 
import json 

def remove_links(line, header_dict):
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

def fix_links(line, header_dict):
    edited_line = line
    regex = r"\[\[([a-zA-Z\,\'\-\_\s]+?)\]\]"
    found = re.findall(regex, edited_line)
    if found:
        print(found)
        for i in found:
            if i in header_dict:
                print(f"\tReplacing <{i}> with <{header_dict[i]}>")
                edited_line = edited_line.replace(i, header_dict[i])

    return edited_line

def fix_file(file, header_dict):
    input_lines = []
    output_lines = []
    with open(file, "r", encoding="utf-8") as f:
        print(f"Checking file: {file.stem.title()}")
        input_lines = f.readlines()
        has_type = False
        for input_line in input_lines:
            # Fix for duplicate type property
            if "type: " in input_line and not has_type:
                has_type = True
            elif "type: " in input_line and has_type:
                print("\tFound duplicate type field. Removing...")
                continue
            
            output_line = fix_links(remove_links(input_line, header_dict), header_dict)
            output_lines.append(output_line)    

    if(input_lines == output_lines):
        print(f"No Update")
        return False
    else:
        if len(input_lines) - len(output_lines) > 5:
            print("Updated file has more than a 5 line difference. Skipping...")
            return False

        if input("Should this file be replaced?: ") != "y":
            return False

        with open(file, "w", encoding="utf-8") as f:
            f.writelines(output_lines)
            print(f"Updated")
            return True


def main():

    with open(".\\z_Scripts\\header_dict.json", "r", encoding="utf-8") as f:
        header_dict = json.load(f)

    to_fix = Path(r"C:\\Users\\cbiggers\\Documents\\Obsidian\\DND\\D&D Sources\\Player's Handbook 2024\\Gameplay")

    count = 0
    if to_fix.is_dir():
        print("Found Directory...")
        for file in to_fix.rglob("*.md"):
            if fix_file(file, header_dict):
                count = count + 1
    else:
        if fix_file(file, header_dict):
            count = count + 1

    print(f"FIXED {count} FILES...")

if __name__ == "__main__":
    main()