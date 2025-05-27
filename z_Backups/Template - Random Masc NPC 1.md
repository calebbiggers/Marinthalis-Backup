---
tags:
  - Randomized-NPC
aliases: []
age: 
alignment: 
birthday: 
classes: 
gender: Male
icon: RaPerspectiveDiceRandom
level: 
location: 
occupations: 
pronounced: 
pronouns: He/Him
race: "[[Human]]"
relationship_status: 
religions: 
sexuality: Straight
status: Alive
style: NPC
subclasses: 
type: Randomized NPC
---

# Template - Random Masc NPC 1

> [!npc-wiki]+ `=this.file.name` (`=this.pronouns`)
> **Pronounced:** "`=this.pronounced`"
> ![[PlaceholderImage.png]]
> ## Bio
>  |
> ---|---|
> **Race** | `=this.race` |
> **Age** | `=this.age_group` |
> **Gender** | `=this.gender` |
> **Sexuality** | `=this.sexuality` |
> **Alignment** | `=this.alignment` |
> **Relationships Status** | `=this.relationship_status` |
> **Status** | `=this.status` |
> ## Info
>  |
> ---|---|
> **Classes** | `=this.classes` |
> **Subclasses** | `=this.subclasses` |
> **Occupations** | `=this.occupations` |
> **Groups** | `=link(this.associated_groups)` |
> **Religions** | `=link(this.religions)` |
> **Location** | `=link(this.location)` |
> **Home** | `$= (dv.current().home == null) ? "" : dv.current().home` |

## **`=this.file.name`** <span style="font-size: medium">(`=this.occupations`)</span>

> [!info|overview]+ Overview
> <% tp.file.cursor(0) %>

### Generation

`button-InsertIslandID`

### Description

### DM Notes
