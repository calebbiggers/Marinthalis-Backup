---
tags:
  - Source
---

# Player's Handbook 2024

## Classes

```dataview
LIST
FROM #Class
WHERE contains(sources, link(this.file.name))
SORT file.name ASCENDING
```

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

## Feats

```dataview
LIST
FROM #Feat
WHERE contains(sources, link(this.file.name))
SORT file.name ASCENDING
```

![[players-handbook-2024-banner.png|banner]]
