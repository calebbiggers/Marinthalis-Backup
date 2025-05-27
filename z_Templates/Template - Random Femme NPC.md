<%*
	let name;
	if(tp.file.title.startsWith("Untitled")){
		name = await tp.user.random_femme() + " " + await tp.user.random_last();
		await tp.file.rename(name);
	}
_%>
---
tags:
- Random-NPC
aliases:
type: Randomized NPC
alignment:
race: <%await tp.user.random_race()%>
age:
age_group: <%await tp.user.random_age_group()%>
pronouns:
- She
- Her
- Hers
pronounced:
gender: Female
sexuality:  <%await tp.user.random_sexuality()%>
occupations:
location:
groups:
religions:
owns:
status: Alive
relationship_status:
classes:
subclasses:
level:
birthday:
style: NPC
family:
friends:
subordinates:
enemies:
image: "[[placeholder-NPC.webp]]"
icon: RaPerspectiveDiceRandom
---

![[NPC-Banner.jpg|banner]]