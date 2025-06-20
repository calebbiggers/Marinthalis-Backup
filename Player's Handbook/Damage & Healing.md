---
tags: []
sources:
  - "[[Player's Handbook 2024]]"
---

![[players-handbook-2024-banner.png|banner]]

# Damage & Healing

Injury and death are frequent threats in D&D, as detailed in the following rules.

## Hit Points

Hit Points represent durability and the will to live. Creatures with more Hit Points are more difficult to kill. Your Hit Point maximum is the number of Hit Points you have when uninjured. Your current Hit Points can be any number from that maximum down to 0, which is the lowest Hit Points can go.

Whenever you take damage, subtract it from your Hit Points. Hit Point loss has no effect on your capabilities until you reach 0 Hit Points.

### Bloodied

If you have half your Hit Points or fewer, you’re Bloodied, which has no game effect on its own but which might trigger other game effects.

## Resting

Adventurers can’t spend every hour adventuring. They need rest. Any creature can take hour-long [[#Short Rests]] in the midst of a day and an 8-hour [[#Long Rests|Long Rest]] to end it. Regaining Hit Points is one of the main benefits of a rest.

### Short Rests

A Short Rest is a 1-hour period of downtime, during which a creature does nothing more strenuous than reading, talking, eating, or standing watch. To start a Short Rest, you must have at least 1 Hit Point.

**_Benefits of the Rest._** When you finish the rest, you gain the following benefits:

**Spend Hit Point Dice.** You can spend one or more of your Hit Point Dice to regain [[#Hit Points]]. For each Hit Point Die you spend in this way, roll the die and add your Constitution modifier to it. You regain Hit Points equal to the total (minimum of 1 Hit Point). You can decide to spend an additional Hit Point Die after each roll.

**Special Feature.** Some features are recharged by a Short Rest. If you have such a feature, it recharges in the way specified in its description.

**_Interrupting the Rest._** A Short Rest is stopped by the following interruptions:
- Rolling [[Combat#Initiative|Initiative]]
- Casting a spell other than a cantrip
- Taking any damage

An interrupted Short Rest confers no benefits.

### Long Rests

A Long Rest is a period of extended downtime—at least 8 hours—available to any creature. During a Long Rest, you sleep for at least 6 hours and perform no more than 2 hours of light activity, such as reading, talking, eating, or standing watch.

During sleep, you have the [[Conditions#Unconscious|Unconscious]] condition. After you finish a Long Rest, you must wait at least 16 hours before starting another one.

**_Benefits of the Rest._** To start a Long Rest, you must have at least 1 Hit Point. When you finish the rest, you gain the following benefits:

**Regain All HP.** You regain all lost [[#Hit Points]] and all spent Hit Point Dice. If your Hit Point maximum was reduced, it returns to normal.

**Ability Scores Restored.** If any of your ability scores were reduced, they return to normal.

**Exhaustion Reduced.** If you have the [[Conditions#Exhaustion|Exhaustion]] condition, its level decreases by 1.

**Special Feature.** Some features are recharged by a Long Rest. If you have such a feature, it recharges in the way specified in its description.

**_Interrupting the Rest._** A Long Rest is stopped by the following interruptions:
- Rolling [[Combat#Initiative|Initiative]]
- Casting a spell other than a cantrip
- Taking any damage
- 1 hour of walking or other physical exertion

If you rested at least 1 hour before the interruption, you gain the benefits of a [[#Short Rests|Short Rest]].

You can resume a Long Rest immediately after an interruption. If you do so, the rest requires 1 additional hour per interruption to finish.

## Damage Rolls

Each weapon, spell, and damaging monster ability specifies the damage it deals. You roll the damage dice, add any modifiers, and deal the damage to your target. If there’s a penalty to the damage, it’s possible to deal 0 damage but not negative damage.

When attacking with a weapon, you add your ability modifier—the same modifier used for the attack roll—to the damage roll. A spell tells you which dice to roll for damage and whether to add any modifiers. Unless a rule says otherwise, you don’t add your ability modifier to a fixed damage amount that doesn’t use a roll, such as the damage of a [[#Blowgun]].

## Critical Hits

~~When you score a Critical Hit, you deal extra damage. Roll the attack’s damage dice twice, add them together, and add any relevant modifiers as normal. For example, if you score a Critical Hit with a [[#Dagger]], roll 2d4 for the damage rather than 1d4, and add your relevant ability modifier. If the attack involves other damage dice, such as from the Rogue’s Sneak Attack feature, you also roll those dice twice.~~

>[!dnd] House Rule
>We will be using a homebrew rule for more damaging critical hits. When you score a Critical Hit, you deal extra damage. Roll the attack’s damage dice once, add full dice damage, then add any relevant modifiers as normal. For example, if you score a Critical Hit with a [[#Dagger]], roll 1d4 for the damage, add one full dice damage (4), then add your relevant ability modifier. If the attack involves other damage dice, such as from the Rogue’s Sneak Attack feature, you also add full damage for these dice.
>
>Our other house rules are listed [[House Rules|here]]

## Saving Throws and Damage

Damage dealt via saving throws uses these rules.

### Damage against Multiple Targets

When you create a damaging effect that forces two or more targets to make saving throws against it at the same time, roll the damage once for all the targets. For example, when a wizard casts [[Fireball]], the spell’s damage is rolled once for all creatures caught in the blast.

### Half Damage

Many saving throw effects deal half damage (round down) to a target when the target succeeds on the saving throw. The halved damage is equal to half the damage that would be dealt on a failed save.

## Damage Types

Attacks and other harmful effects deal different types of damage. Damage types have no rules of their own, but other rules, such as [[#Resistance and Vulnerability|Resistance]], rely on the types. The Damage Types table offers examples to help a DM assign a type to a new effect.

|Type|Examples|
|---|---|
|Acid|Corrosive liquids, digestive enzymes|
|Bludgeoning|Blunt objects, constriction, falling|
|Cold|Freezing water, icy blasts|
|Fire|Flames, unbearable heat|
|Force|Pure magical energy|
|Lightning|Electricity|
|Necrotic|Life-draining energy|
|Piercing|Fangs, puncturing objects|
|Poison|Toxic gas, venom|
|Psychic|Mind-rending energy|
|Radiant|Holy energy, searing radiation|
|Slashing|Claws, cutting objects|
|Thunder|Concussive sound|

## Resistance and Vulnerability

Some creatures and objects have Resistance or Vulnerability to certain damage types. If you have Resistance to a damage type, damage of that type is halved against you (round down). If you have Vulnerability to a damage type, damage of that type is doubled against you. For example, if you have Resistance to Cold damage, such damage is halved against you, and if you have Vulnerability to Fire damage, such damage is doubled against you.

### No Stacking

Multiple instances of Resistance or Vulnerability that affect the same damage type count as only one instance. For example, if you have Resistance to Necrotic damage as well as Resistance to all damage, Necrotic damage is reduced by half against you.

### Order of Application

Modifiers to damage are applied in the following order: adjustments such as bonuses, penalties, or multipliers are applied first; Resistance is applied second; and Vulnerability is applied third.

For example, a creature has Resistance to all damage and Vulnerability to Fire damage, and it’s within a magical aura that reduces all damage by 5. If it takes 28 Fire damage, the damage is first reduced by 5 (to 23), then halved for the creature’s Resistance (and rounded down to 11), then doubled for its Vulnerability (to 22).

## Immunity

Some creatures and objects have Immunity to certain damage types and conditions. Immunity to a damage type means you don’t take damage of that type, and Immunity to a condition means you aren’t affected by it.

## Healing

Hit Points can be restored by magic, such as the [[Cure Wounds]] spell or a [[Potion of Healing]], or by a [[#Short Rests|Short]] or [[#Long Rests|Long Rest]].

When you receive healing, add the restored Hit Points to your current Hit Points. Your Hit Points can’t exceed your Hit Point maximum, so any Hit Points regained in excess of the maximum are lost. For example, if you receive 8 Hit Points of healing and have 14 Hit Points and a Hit Point maximum of 20, you regain 6 Hit Points, not 8.

## Dropping to 0 Hit Points

When a creature drops to 0 Hit Points, it either dies outright or falls [[Conditions#Unconscious|Unconscious]], as explained below.

### Instant Death

Here are the main ways a creature can die instantly.

**_Monster Death._** A monster dies the instant it drops to 0 Hit Points, although a Dungeon Master can ignore this rule for an individual monster and treat it like a character.

**_Hit Point Maximum of 0._** A creature dies if its Hit Point maximum reaches 0. Certain effects drain life energy, reducing a creature’s Hit Point maximum.

**_Massive Damage._** When damage reduces a character to 0 Hit Points and damage remains, the character dies if the remainder equals or exceeds their Hit Point maximum. For example, if your character has a Hit Point maximum of 12, currently has 6 Hit Points, and takes 18 damage, the character drops to 0 Hit Points, but 12 damage remains. The character then dies, since 12 equals their Hit Point maximum.

### Character Demise

If your character dies, others might find a magical way to revive your character, such as with the [[Raise Dead]] spell. Or talk with the DM about making a new character to join the group.

### Falling Unconscious

If you reach 0 Hit Points and don’t die instantly, you have the [[Conditions#Unconscious|Unconscious]] condition until you regain any Hit Points, and you now face making [[#Death Saving Throws]].

### Knocking Out a Creature

When you would reduce a creature to 0 Hit Points with a melee attack, you can instead reduce the creature to 1 Hit Point and give it the [[Conditions#Unconscious|Unconscious]] condition. It then starts a [[#Short Rests|Short Rest]], at the end of which that condition ends on it. The condition ends early if the creature regains any Hit Points or if someone takes an action to administer first aid to it, making a successful DC 10 Wisdom (Medicine) check.

### Death Saving Throws

Whenever you start your turn with 0 Hit Points, you must make a Death Saving Throw to determine whether you creep closer to death or hang on to life. Unlike other saving throws, this one isn’t tied to an ability score. You’re in the hands of fate now.

**_Three Successes/Failures._** Roll 1d20. If the roll is 10 or higher, you succeed. Otherwise, you fail. A success or failure has no effect by itself. On your third success, you become [[#Stabilizing a Character|Stable]]. On your third failure, you die.

The successes and failures don’t need to be consecutive; keep track of both until you collect three of a kind. The number of both is reset to zero when you regain any Hit Points or become Stable.

**_Rolling a 1 or 20._** When you roll a 1 on the d20 for a Death Saving Throw, you suffer two failures. If you roll a 20 on the d20, you regain 1 Hit Point.

**_Damage at 0 Hit Points._** If you take any damage while you have 0 Hit Points, you suffer a Death Saving Throw failure. If the damage is from a Critical Hit, you suffer two failures instead. If the damage equals or exceeds your Hit Point maximum, you die.

### Stabilizing a Character

You can take the [[Actions#Help|Help]] action to try to stabilize a creature with 0 Hit Points, which requires a successful DC 10 Wisdom (Medicine) check.

A Stable creature doesn’t make Death Saving Throws even though it has 0 Hit Points, but it still has the [[Conditions#Unconscious|Unconscious]] condition. If the creature takes damage, it stops being Stable and starts making Death Saving Throws again. A Stable creature that isn’t healed regains 1 Hit Point after 1d4 hours.

## Temporary Hit Points

Some spells and other effects confer Temporary Hit Points, which are a buffer against losing actual Hit Points, as explained below.

### Lose Temporary Hit Points First

If you have Temporary Hit Points and take damage, those points are lost first, and any leftover damage carries over to your Hit Points. For example, if you have 5 Temporary Hit Points and take 7 damage, you lose those points and then lose 2 Hit Points.

### Duration

Temporary Hit Points last until they’re depleted or you finish a [[#Long Rests|Long Rest]].

### Temporary Hit Points Don’t Stack

Temporary Hit Points can’t be added together. If you have Temporary Hit Points and receive more of them, you decide whether to keep the ones you have or to gain the new ones. For example, if a spell grants you 12 Temporary Hit Points when you already have 10, you can have 12 or 10, not 22.

### They’re Not Hit Points or Healing

Temporary Hit Points can’t be added to your Hit Points, healing can’t restore them, and receiving Temporary Hit Points doesn’t count as healing. Because Temporary Hit Points aren’t Hit Points, a creature can be at full Hit Points and receive Temporary Hit Points.

If you have 0 Hit Points, receiving Temporary Hit Points doesn’t restore you to consciousness. Only true healing can save you.
