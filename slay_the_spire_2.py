from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class SlayTheSpire2ArchipelagoOptions:
    pass

class SlayTheSpire2Game(Game):
    name = "Slay the Spire 2"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = SlayTheSpire2ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []
        constraints.extend([
            GameObjectiveTemplate(
                label="Complete with Ascension ASCENSION unless indicated otherwise.",
                data={"ASCENSION": (self.ascension_levels, 1)},
            ),
        ])
        return constraints
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        if self.randophilia_nono_is_here:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="[NONO] Meet the Architect with the CHARACTER",
                    data={
                        "CHARACTER": (self.characters, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=4,
                ),
                GameObjectiveTemplate(
                    label="[NONO] Meet the Architect with the CHARACTER in Ascension ASCENSION",
                    data={
                        "CHARACTER": (self.characters, 1),
                        "ASCENSION": (self.ascension_levels, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="[NONO] Win a custom run with CHARACTER, with modifier BAD_MODIFIER, in Ascension ASCENSION",
                    data={
                        "CHARACTER": (self.characters, 1),
                        "BAD_MODIFIER": (self.bad_modifiers, 1),
                        "ASCENSION": (self.ascension_levels, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="[NONO] Win a custom run with CHARACTER, with modifiers GOOD_MODIFIER and BAD_MODIFIER, in Ascension ASCENSION",
                    data={
                        "CHARACTER": (self.characters, 1),
                        "GOOD_MODIFIER": (self.all_good_modifiers, 1),
                        "BAD_MODIFIER": (self.bad_modifiers, 1),
                        "ASCENSION": (self.ascension_levels, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="[NONO] Win a custom run with CHARACTER, with modifiers BICO_MODIFIER, GOOD_MODIFIER and BAD_MODIFIER, in Ascension ASCENSION",
                    data={
                        "CHARACTER": (self.characters, 1),
                        "BICO_MODIFIER": (self.bicolor_modifiers, 1),
                        "GOOD_MODIFIER": (self.except_bicolor_modifiers, 1),
                        "BAD_MODIFIER": (self.bad_modifiers, 1),
                        "ASCENSION": (self.ascension_levels, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=2,
                ),
            ])
        # Challenge for Niko
        if self.randophilia_niko_is_here:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="[NIKO] Meet the Architect with the CHARACTER",
                    data={
                        "CHARACTER": (self.characters, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=4,
                ),
                GameObjectiveTemplate(
                    label="[NIKO] Meet the Architect in ascension ASCENSION",
                    data={
                        "ASCENSION": (self.ascension_levels, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                )
            ])

        return game_objective_templates
    
    @property
    def randophilia_nono_is_here(self) -> bool:
        return self.archipelago_options.randophilia_nono_is_here.value
    
    @property
    def randophilia_niko_is_here(self) -> bool:
        return self.archipelago_options.randophilia_niko_is_here.value
    
    @staticmethod
    def ascension_levels() -> range:
        return range(0, 10+1, 1)

    @staticmethod
    def characters() -> List[str]:
        return ["Iron Clad","Silent","Regent","Necrobinder","Defect"]

    @staticmethod
    def all_good_modifiers() -> List[str]:
        return ["Draft","Sealed Deck","Hoarder","Specialized","Insanity","All Star","Flight","Vintage","Ironclad Cards","Silent Cards","Regent Cards","Necrobinder Cards","Defect Cards"]

    @staticmethod
    def except_bicolor_modifiers() -> List[str]:
        return ["Draft","Sealed Deck","Hoarder","Specialized","Insanity","All Star","Flight","Vintage"]
    
    @staticmethod
    def bicolor_modifiers() -> List[str]:
        return ["Ironclad Cards","Silent Cards","Regent Cards","Necrobinder Cards","Defect Cards"]

    @staticmethod
    def bad_modifiers() -> List[str]:
        return ["Deadly Events","Cursed Run","Bug Game Hunter","Midas","Murderous","Night Terrors","Terminal"]