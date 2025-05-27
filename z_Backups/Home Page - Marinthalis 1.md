---
tags:
  - HomePage
icon: LiHome
type: Home Page
---

# Home Page - Marinthalis 1

<span><h1 align="center">Home Page - Marinthalis</h1></span>
 ----
 >[!multi-column|3 no-title]
 >>[!default] Quick Adds
 >>`button-NewMascNPCID`
 >>`button-NewFemmeNPCID`
 >>`button-NewNPCID`
 >>`button-NewItemID`
 >
 >>[!info]
 >
 >>[!info]
  ---

## Tasks

```tasks
not done 
path does not include z_Session Notes
```
 ---

## To Do Files

```dataview
TABLE WITHOUT ID
link(file.name) as "Name", type as "Type", file.mtime as "Last Opened"
FROM #TODO
SORT file.mtime ASC
```
 ---

## Last Updates

 ```dataview
TABLE WITHOUT ID
link(file.name) as "Name", type as "Type", file.mtime as "Last Opened"
SORT file.mtime DESC
LIMIT 20
```
