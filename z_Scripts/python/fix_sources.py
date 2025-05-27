from pathlib import Path

def main():
    dir = Path("./DND SRD/Spells/")
    for file in Path.glob(dir, "*.md"):
        #print(file)
        lines = []
        needs_fixing = False
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if "sources:" in lines[i]:
                    if ":" in lines[i + 1]:
                        lines[i+1] = lines[i+1].replace(":", " -")
                        needs_fixing = True
                        break
                    elif "Acquisitions Incorperated" in lines[i + 1]:
                        lines[i+1] = lines[i+1].replace("Acquisitions Incorperated", "Acquisitions Incorporated")
                        needs_fixing = True
                        break
        
        if needs_fixing:
            print(f"Updated: {file.stem.title()}")
            with open(file, "w", encoding="utf-8") as f:
                f.writelines(lines)

if __name__ == "__main__":
    main()