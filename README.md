# Keymaster's Keep's Games for Randophilia
Games implementations for Keymaster's Keep in Randophilia.

# How do you edit the Keep Games?
You have to either fork this repository, or request dev access.

In both cases, you will have to create a branch, add your modifications, then do a Merge Request to the main branch.

# How do you test my changes?
If you can run the Archipelago Launcher locally from sources, add KMK sources in "worlds" subfolder, then replace KMK/games/ content with the content of this repository.

Otherwise, you can open the apworld archive, replace the "games" folder content by the content of this repository ; then place the edited apworld in the "custom_worlds" folder of you Archipelago Launcher install.

# How to add YOU as a Randophilia Keep Player?
Add an option for your presence in the Keep in [randophilia.py](https://github.com/NonoRobo/RandophiliaKeepGames/blob/main/_randophilia_.py).

The idea is to have only player-related options in the yaml file: treat game options as YOU-centered, so if you want flexibility on your game difficulty, it doesn't impact other players potentially playing the same game.

# How to add game challenges?
## Notes on Keep Generation
When generating the Keep's content, it will first pick a game, then a challenge in the selected game.

All games (including meta-games) are equally weighted => the more games you have enabled for you, the more likely you are to have checks to do in a Coop Keep.

Challenges define their own weight within the game => be mindful of the weights of other players' challenges to keep things even.

## Game file structure

We will use [Slay the Spire](https://github.com/NonoRobo/RandophiliaKeepGames/blob/main/slay_the_spire_2.py) 2 as example.

`SlayTheSpire2ArchipelagoOptions` is for game options displayed in the yaml file.

`SlayTheSpire2Game` is for the game definition itself. There are some info for display and generation, then the two main functions we need to implement:
- `optional_game_constraint_templates` is for extra constraints when the Room is a single game trial.
- `game_objective_templates` is for the actual challenges.
- Properties, usually related to yaml options.
- Static methods, usually related to challenges variables.

## Game Objective Template

Both trial room constaints and challenges have the same structure (constraints don't use weight and difficulty flags).
- `label` is the name of the objective: you can use some words as variable. Best practice is to write variables in all caps.
- `data` is the dictionary matching each of your variables with the variable options.
- `is_time_consuming` and `is_difficult` are only used for generation, with the global yaml option.
- the highest the `weight` of a challenge, the more likely it is to be selected during generation.

## Best practices

Depending on the game, it might be pertinent to "claim" nominatively a challenge, or not... I don't know, let's be clever all together? ^^
