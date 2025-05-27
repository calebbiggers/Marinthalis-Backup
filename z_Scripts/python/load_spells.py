from dnd_content_loader import DndContentLoader

def main():
    # Create content loader
    loader = DndContentLoader(loading_bar_disabled=False)

    # Load spells from dnd wiki
    loader.load_spells_from_wiki()

    # Output Spell files
    loader.output_spells_md("./DND SRD/Spells/")


if __name__ == '__main__':
    main()
