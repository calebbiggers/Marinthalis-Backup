---
tags:
  - Source
icon: LiBookMarked
---

# Fizban's Treasury of Dragons

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

![[Fizbans-Treasury-Of-Dragons-Banner.jpg|banner]]
