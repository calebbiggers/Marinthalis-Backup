# Templater Code Snippits
## `=this.file.name`
### User Inputted name
```js
let title;
if (tp.file.title.startsWith("New NPC")){
	title = await tp.system.prompt("Enter NPC Name");
	await tp.file.rename(title);
}
```
### Random Masc name
```js
let name;
if(tp.file.title.startsWith("New Masc NPC")){
	name = await tp.user.random_masc() + " " + await tp.user.random_last();
	await tp.file.rename(name);
}
```

### Random Femme name
```js
let name;
if(tp.file.title.startsWith("New Femme NPC")){
	name = await tp.user.random_femme() + " " + await tp.user.random_last();
	await tp.file.rename(name);
}
```

### Random Age Group
```js
await tp.user.random_age_group();
```

### Random Sexuality
```js
await tp.user.random_sexuality();
```

### Random Race
```js
await tp.user.random_race();
```

### Random Island
```js
await tp.user.random_island();
```