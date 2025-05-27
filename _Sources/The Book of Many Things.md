---
tags:
  - Source
icon: LiBookMarked
---

# The Book of Many Things

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

![[The-book-of-many-things-banner.jpg|banner]]
