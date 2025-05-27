# Script Testing
```python
from dnd_content_loader import DndContentLoader
loader = DndContentLoader(loading_bar_disabled=True)
loader.load_spells_from_wiki()
loader.output_spells_md(@vault_path + "/DND SRD/Spells/")
```