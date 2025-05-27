from pathlib import Path

def main():
    path = Path("C:\\Users\\cbiggers\\Documents\\Obsidian\\DND")

    files = path.rglob("* Of *.md")
    for file in files:
        if "Of" in file.name:
            print(f"{file.name}")
            file.rename(f"{file.name.replace("Of", "of")}")


if __name__ == "__main__":
    main()