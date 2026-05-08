from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class DarkSoulsRemasteredArchipelagoOptions:
    niko_dsr_include_aota:DSRNikoIncluteAotA

class DarkSoulsRemasteredGame(Game):
    name = "Dark Souls Remastered"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = DarkSoulsRemasteredArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        # Niko's objectives
        if self.randophilia_niko_is_here:
            nikobjectives: List[GameObjectiveTemplate] = list()

    # Property
    @property
    def randophilia_niko_is_here(self) -> bool:
        return self.archipelago_options.randophilia_niko_is_here.value

    @functools.cached_property
    def dsr_vanillabosses(self) -> List[str]:
        """Boss in vanilla game"""
        return [
            "Asylum Demon",
            "Bell Gargoyles",
            "Ceaseless Discharge",
            "Centipede Demon",
            "Chaos Witch Quelaag",
            "Crossbreed Priscilla",
            "Dark Sun Gwyndolin",
            "Demon Firesage",
            "Four Kings",
            "Gaping Dragon",
            "Great Grey Wolf Sif",
            "Gwyn, Lord of Cinder",
            "Iron Golem",
            "Moonlight Butterfly",
            "Nito, Lord of the Dead",
            "Ornstein and Smough",
            "Pinwheel",
            "Seath the Scaleless",
            "Stray Demon",
            "Taurus Demon",
            "The Bed of Chaos"
        ]
    
    @functools.cached_property
    def dsr_aotabosses(self) -> List[str]:
        """Boss in Artorias of the Abyss DLC game"""
        return [
            "Artorias the Abysswalker",
            "Black Dragon Kalameet",
            "Manus, Father of the Abyss",
            "Sanctuary Guardian"
        ]


        
class DSRNikoIncluteAotA(Toggle):
    """
    Niko wants to include Artorias of the Abyss in the Keep.
    """
    display_name = "[NONNikoO] Include AotA"
    default = True