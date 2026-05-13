from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import OptionSet, Toggle, Range
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class VampireSurvivorsArchipelagoOptions:
    niko_vs_include_dlc: VampireSurvivorsNikoIncludeDLC

class VampireSurvivorsGame(Game):
    name = "Vampire Survivors"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = VampireSurvivorsArchipelagoOptions
    

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()
        
        if self.randophilia_niko_is_here:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Complete a un in this MAP",
                    data={
                        "MAP": (lambda: self.areas(self.niko_LegacyOfTheMoonspell), 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),  
            ])
        return game_objective_templates
    
#Property
    @property
    def randophilia_niko_is_here(self) -> bool:
        return self.archipelago_options.randophilia_niko_is_here.value
    @property
    def niko_LegacyOfTheMoonspell(self) -> bool:
        return "Legacy of the Moonspell" in self.archipelago_options.niko_vs_include_dlc
    
    def areas(self, dlc: bool) -> List[str]:
        areas = self.vs_vanilla_area
        if dlc:
            areas.extend(self.vs_moonspell_area)        
        return areas

    @functools.cached_property
    def vs_vanilla_area (self) -> List[str]:
        """Areas in vanilla game"""
        return [
            "AAA",
            "BBB",
        ]
    @functools.cached_property
    def vs_moonspell_area (self) -> List[str]:
        """Areas in Legacy Of the moonspell game"""
        return [
            "111",
            "222",
        ]
class VampireSurvivorsNikoIncludeDLC(OptionSet):
    """
    The DLC Niko wants to include in the pool.
    The DLCs are:
    - Legacy of the Moonspell
    - Tides of the Foscari
    - Emergency Meeting
    - Operation Guns
    - Ode to Castlevania
    - Emerald Diorama
    - Ante Chamber
    """
    display_name = "[NIKO] Vampire Survivors Included DLCs"
    valid_keys = {
        "Legacy of the Moonspell",
        "Tides of the Foscari",
        "Emergency Meeting",
        "Operation Guns",
        "Ode to Castlevania",
        "Emerald Diorama",
        "Ante Chamber"
    }
    default = valid_keys