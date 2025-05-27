<%*
let title;
let rarity;
let type;
if (tp.file.title.startsWith("Untitled")){
	await tp.file.move("/Homebrew/Wondrous Items/" + tp.file.title);
	title = await tp.system.prompt("Enter Item Name");
	await tp.file.rename(title);
	rarity = await tp.system.suggester(["Common", "Uncommon", "Rare", "Very Rare", "Legendary", "Artifact"], ["Common", "Uncommon", "Rare", "Very Rare", "Legendary", "Artifact"]);
	type = await tp.system.suggester(["Weapon", "Armor", "Wondrous Item", "Potion", "Scroll", "Staff", "Wand", "Rod", "Ring", "Shield"], ["Weapon", "Armor", "Wondrous Item", "Potion", "Scroll", "Staff", "Wand", "Rod", "Ring", "Shield"]);
}
_%>
---
tags: [Item]
type: <%type%>
rarity: <%rarity%>
icon: <%await tp.user.get_item_icon(type)%>
sources:
  - "[[Homebrew]]"
---

>[!<%rarity.replace(" ", "-")%>-<%type.replace(" ","-")%>-callout] <%title%>
> <% tp.file.cursor(0) %>
>