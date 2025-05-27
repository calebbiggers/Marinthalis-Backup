---
tags:
  - Source
icon: LiBookMarked
---

# Homebrew

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
FROM #Item and !#Template
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

![[Homebrew-Banner.jpg|banner]]
