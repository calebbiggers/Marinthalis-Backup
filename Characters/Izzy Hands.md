---
tags:
  - PC
aliases:
  - Izzy
age: 50
alignment: Neutral Good
birthday: 
classes:
  - "[[Sorcerer]]"
enemies: 
family: 
friends:
  - "[[Gnar Rosewater|Gnar]]"
  - "[[Grommet Payne]]"
  - "[[Keiran Thalassa|Keiran]]"
gender: Male
groups:
  - "[[The Barrel Pirates]]"
icon: LiUserCircle2
image: "[[izzy-wanted-poster.png]]"
level: 5
location: "[[Baldur's Gate]]"
occupations:
  - Pirate
origin: 
owns: 
played_by: "[[Emily]]"
pronounced: 
pronouns:
  - He/Him
lineages:
  - "[[Elf]]"
relationship_status: 
religions: 
sexuality: 
status: Alive
style: NPC
subclasses:
  - "[[Wild Magic Sorcery]]"
subordinates: 
type: NPC
---

# Izzy Hands

>[!NPC-Wiki] `=this.file.name` `$= !dv.current().pronouns ? "" : "(" + dv.current().pronouns + ")"`
>
> |             |                                                                        |
> |:----------- |:---------------------------------------------------------------------- |
> | **Played By** | `$= !dv.current().played_by ? "N/A" : dv.current().played_by` |
>
>`$= dv.paragraph(dv.func.embed(dv.current().image))`
>
> |                   |                                                                                                                                                          |
> |:----------------- |:-------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Race**          | `$= !dv.current().race ? "N/A" : dv.current().race`                                                                                                      |
> | **Age**           | `$= !dv.current().age ? "N/A" : dv.current().age`                                                                                                        |
> | **Sexuality**     | `$= !dv.current().sexuality ? "N/A" : dv.current().sexuality`                                                                                            |
> | **Status**        | `$= !dv.current().status ? "N/A" : dv.current().status`                                                                                                  |
> | **Relationships** | `$= !dv.current().relationship_status ? "N/A" : dv.current().relationship_status`                                                                        |
> | **Religions**     | `$= !dv.current().religions ? "None" : dv.current().religions.join(", ")`                                                                                |
> |                   |                                                                                                                                                          |
> | **Location**      | `$= !dv.current().location ? "N/A" : dv.current().location`                                                                                              |
> | **Origin**        | `$= !dv.current().origin ? "N/A" : dv.current().origin`                                                                                                  |
> | **Occupation**    | `$= !dv.current().occupations ? "None" : dv.current().occupations.join(", ")`                                                                            |
> | **Owns**          | `$= !dv.current().owns ? "N/A" : dv.current().owns.join(", ")`                                                                                           |
> | **Groups**        | `$= !dv.current().groups ? "None" : dv.current().groups.join(", ")`                                                                                      |
> |                   |                                                                                                                                                          |
> | **Class**         | `$= !dv.current().classes ? "N/A" : dv.current().classes.join(", ")` `$= !dv.current().subclasses ? "" : "(" + dv.current().subclasses.join(", ") + ")"` |
> | **Level**         | `$= dv.current().level`                                                                                                                                            |

## Description

>[!quote] Read To Players
>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vulputate iaculis dui, ut aliquet velit. Vivamus eu ornare sem. Quisque tincidunt, leo ac malesuada lobortis, dui nisl varius nunc, fermentum tincidunt velit nulla et ipsum. In mi nulla, hendrerit ac augue vel, porta porta urna. Nunc congue pretium eros, eu euismod arcu efficitur eget. Aliquam molestie neque in felis mollis, at accumsan enim tempus. Fusce rhoncus sollicitudin mauris, eget posuere risus tristique sagittis. Maecenas gravida dui dui, sit amet accumsan ipsum maximus vel. In tincidunt, elit nec tempor hendrerit, dui metus pulvinar ipsum, fringilla malesuada erat ex vitae mi. Sed non ullamcorper tellus, ac consectetur nunc. Sed lacus urna, accumsan quis nunc quis, scelerisque rutrum ipsum.

## Background

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vulputate iaculis dui, ut aliquet velit. Vivamus eu ornare sem. Quisque tincidunt, leo ac malesuada lobortis, dui nisl varius nunc, fermentum tincidunt velit nulla et ipsum. In mi nulla, hendrerit ac augue vel, porta porta urna. Nunc congue pretium eros, eu euismod arcu efficitur eget. Aliquam molestie neque in felis mollis, at accumsan enim tempus. Fusce rhoncus sollicitudin mauris, eget posuere risus tristique sagittis. Maecenas gravida dui dui, sit amet accumsan ipsum maximus vel. In tincidunt, elit nec tempor hendrerit, dui metus pulvinar ipsum, fringilla malesuada erat ex vitae mi. Sed non ullamcorper tellus, ac consectetur nunc. Sed lacus urna, accumsan quis nunc quis, scelerisque rutrum ipsum.

## Related NPCs

### Family

```dataview
LIST FROM #NPC or #PC
WHERE contains(family, link(this.file.name))
SORT file.name ASCENDING
```

### Friends

```dataview
LIST FROM #NPC or #PC
WHERE contains(friends, link(this.file.name))
SORT file.name ASCENDING
```

### Enemies

```dataview
LIST FROM #NPC or #PC
WHERE contains(enemies, link(this.file.name))
SORT file.name ASCENDING
```

## Notes

- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vulputate iaculis dui, ut aliquet velit. Vivamus eu ornare sem. Quisque tincidunt, leo ac malesuada lobortis, dui nisl varius nunc,
- Sed non ullamcorper tellus, ac consectetur nunc. Sed lacus urna, accumsan quis nunc quis, scelerisque rutrum ipsum.


![[PC-Banner.jpg|banner]]
