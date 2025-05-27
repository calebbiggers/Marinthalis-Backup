---
tags: [Source]
icon: LiBookMarked
type: Source
---
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