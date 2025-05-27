---
tags:
  - Source
icon: LiBookMarked
---

# Lost Laboratory of Kwalish

## Items

```dataview
LIST
FROM #Item 
WHERE contains(sources, link(this.file.name))
SORT file.name ASCENDING
```

## Spells

```dataview
LIST
FROM #Spell
WHERE contains(sources, link(this.file.name))
SORT file.name ASCENDING
```

![[Lost-Laboratory-Of-Kwalish-Banner.jpg|banner]]
