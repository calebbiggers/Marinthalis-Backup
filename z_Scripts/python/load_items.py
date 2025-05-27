from dnd_content_loader import DndContentLoader

def main():
    # Create content loader
    loader = DndContentLoader(loading_bar_disabled=False)

    # Load items from wiki
    loader.load_wondrous_items_from_wiki()

    # Write items to files
    loader.output_wondrous_items_md("./DND SRD/Wondrous Items/")

if __name__ == "__main__":
    main()