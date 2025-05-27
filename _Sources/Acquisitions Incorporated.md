---
tags:
  - Source
icon: LiBookMarked
---

# Acquisitions Incorporated

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

![[Acquisitions-Incorporated-Banner.jpg|banner]]
