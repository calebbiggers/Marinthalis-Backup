---
tags:
  - Source
icon: LiBookMarked
---

# Explorer's Guide to Wildemount

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

![[explorers-guide-to-wildemount-banner.jpg|banner]]
