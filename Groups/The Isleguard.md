---
tags:
  - Group
aliases: []
alignment: Lawful Neutral
hq: "[[Baldur's Gate]]"
icon: LiShield
leaders: 
location: 
pronounced: 
type:
---

![[Group-Banner.webp|banner]]

# The Isleguard

The Isleguard is the naval force and military arm of [[The Council of Isles]], tasked with maintaining order across the seas of [[Marinthalis]]. Serving as both law enforcement and military, they protect member islands, patrol dangerous waters, and defend against pirates and other threats. The Isleguard is a respected and disciplined force, ensuring peace and stability in a world dominated by vast oceans and scattered islands.

## Ranks

Fleet Admiral, Admiral, Commodore, Captain, Lieutenant, Warrant Officer, Petty Officer, Seaman

### Fleet Admiral

_Fleet Admiral_ is the highest rank of the Isleguard and is the commander of the entire organization.

```dataview
LIST
FROM #NPC OR #PC OR #Character
WHERE contains(groups,link(this.file.name)) AND rank = "Fleet Admiral"
SORT file.name ASCENDING
```

### Admiral

_Admiral_ is the second highest rank of the Isleguard. Only three members hold this title at any time. Each Admiral is stationed in and responsible for one of the three capital cities of [[Marinthalis]]: [[Baldur's Gate]], [[Neverwinter]], and [[Waterdeep]].

```dataview
LIST
FROM #NPC OR #PC OR #Character
WHERE contains(groups,link(this.file.name)) AND rank = "Admiral"
SORT file.name ASCENDING
```

### Commodore

_Commodore_ is the third highest rank of the Isleguard. These officers can have varying duties and amounts of authority.

```dataview
LIST
FROM #NPC OR #PC OR #Character
WHERE contains(groups,link(this.file.name)) AND rank = "Commmodore"
SORT file.name ASCENDING
```

### Captain

_Captain_ is the fourth highest rank of the Isleguard. One of the duties that a Isleguard Captain could have is to be the commander of one of the several Isleguard branches established on the islands around the world. In addition, Captains are often seen navigating the seas in order to keep order. In these cases, the captain is the leader of the ship, as long as there are no higher-ranking Isleguard members on board.

```dataview
LIST
FROM #NPC OR #PC OR #Character
WHERE contains(groups,link(this.file.name)) AND rank = "Captain"
SORT file.name ASCENDING
```

### Lieutenant

_Lieutenant_ is the fifth highest rank of the Isleguard. Lieutenants often lead smaller naval missions, oversee specific tasks or duties within larger commands, or manage day-to-day operations in ports, cities, and outposts.

```dataview
LIST
FROM #NPC OR #PC OR #Character
WHERE contains(groups,link(this.file.name)) AND rank = "Lieutenant"
SORT file.name ASCENDING
```

### Warrant Officer

_Warrant Officer_ is a specialized officer rank. These experienced personnel have unique expertise in a technical, tactical, or logistical area and serve as advisors and senior specialists rather than as traditional command leaders.

```dataview
LIST
FROM #NPC OR #PC OR #Character
WHERE contains(groups,link(this.file.name)) AND rank = "Warrant Officer"
SORT file.name ASCENDING
```

### Petty Officer

_Petty Officer_ is a non-commissioned rank responsible for directly supervising enlisted sailors. They manage daily tasks, maintain discipline among lower-ranking sailors, and assist higher-ranking officers.

```dataview
LIST
FROM #NPC OR #PC OR #Character
WHERE contains(groups,link(this.file.name)) AND rank = "Petty Officer"
SORT file.name ASCENDING
```

### Seaman

_Seaman_ is the standard enlisted rank of the Isleguard, representing fully trained sailors. They perform regular duties on ships, at docks, and within Isleguard outposts under the supervision of Petty Officers.
```dataview
LIST
FROM #NPC OR #PC OR #Character
WHERE contains(groups,link(this.file.name)) AND rank = "Seaman"
SORT file.name ASCENDING
```

### Seaman Recruit

_Seaman Recruit_ is the entry-level enlisted rank. These are new sailors undergoing initial training, often assigned basic tasks and chores while learning their roles
```dataview
LIST
FROM #NPC OR #PC OR #Character
WHERE contains(groups,link(this.file.name)) AND rank = "Seaman Recruit"
SORT file.name ASCENDING
```

## Special Groups

### The Azure Pact

The Azure Pact is the elite magical division of the Isleguard, composed of highly skilled mages. These Azure Mages each hold a rank equivalent to captain. Their mastery over magic and tactical prowess make them a formidable presence, ensuring that the arcane remains a tool of order rather than chaos. They carry the title of "Magus".

```dataview
LIST
FROM #NPC OR #PC OR #Character
WHERE contains(groups,link(this.file.name)) AND rank = "Azure Magus"
SORT file.name ASCENDING
```

## Known Members

```dataview
TABLE WITHOUT ID
link(file.name) as "Name", rank as "Rank"
FROM #NPC or #PC or #Character
WHERE contains(groups,link(this.file.name))
SORT file.rank ASCENDING
```
![[Group-Banner.webp|banner]]
