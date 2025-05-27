from dnd_content_loader import DndContentLoader

def main():
    # Create content loader
    loader = DndContentLoader(loading_bar_disabled=False)

    # Load items from wiki
    loader.load_beastiary_from_csv("./z_Scripts/Bestiary.csv")

    # Write items to files
    
if __name__ == "__main__":
    main()