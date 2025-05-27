---
tags:
  - Source
icon: LiBookMarked
---

# Xanathar's Guide to Everything

## Subclasses

```dataview
LIST
FROM #Subclass 
WHERE contains(sources, link(this.file.name))
SORT file.name ASCENDING
```

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

![[xanathars-guide-to-everything-banner.jpg|banner]]
