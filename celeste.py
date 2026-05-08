from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class CelesteArchipelagoOptions:
    niko_celeste_include_core: CelesteIncludeCore
    niko_celeste_include_farewell: CelesteIncludeFarewell
    niko_celeste_include_b_face: CelesteIncludeBFace
    niko_celeste_include_c_face: CelesteIncludeCFace

class CelesteGame(Game):
    name = "Celeste"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = CelesteArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        if self.randophilia_niko_is_here:
            nikobjectives: List[GameObjectiveTemplate] = list()
            nikobjectives.extend(self.celeste_objectives(include_core=self.niko_celeste_include_core, include_farewell=self.niko_celeste_include_farewell))
            game_objective_templates.extend(nikobjectives)
        return game_objective_templates
 
    def celeste_objectives(self, include_core: bool, include_farewell: bool) -> List[GameObjectiveTemplate]:
        celeste_objectives: List[GameObjectiveTemplate] = list()
        celeste_objectives.append(
            GameObjectiveTemplate(
                label="Complete the CHAPTER on [FACE]",
                data={
                    "CHAPTER": (lambda: self.get_celeste_chapters(include_core=include_core, include_farewell=include_farewell), 1),
                    "FACE": (lambda: self.get_celeste_face(include_b=True, include_c=True), 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            )
        )
        
        return celeste_objectives   
    
    def get_celeste_chapters(self, include_core: bool, include_farewell: bool) -> List[str]:
        chapters = self.celeste_vanillachapters
        if include_core:
            chapters.extend(["Chapter 8: Core"])
        if include_farewell:
            chapters.extend(["Chapter 9: Farewell"])
        return chapters
    
    def get_celeste_face(self, include_b: bool, include_c: bool) -> List[str]:
        face: List[str] = ["Face A"]
        if include_b:
            face.extend(["Face B"])
        if include_c:
            face.extend(["Face C"])
        return face
    
    #Property
    @property
    def randophilia_niko_is_here(self) -> bool:
        return self.archipelago_options.randophilia_niko_is_here.value
    @property
    def niko_celeste_include_core(self) -> int:
        return self.archipelago_options.niko_celeste_include_core.value
    @property
    def niko_celeste_include_farewell(self) -> int:
        return self.archipelago_options.niko_celeste_include_farewell.value
             
    @functools.cached_property
    def celeste_vanillachapters(self) -> List[str]:
        """Chapters from the base game, excluding the Core and Farewell."""
        return [
            "Chapter 1: Forsaken City",
            "Chapter 2: Old Site",
            "Chapter 3: Celestial Resort",
            "Chapter 4: Golden Ridge",
            "Chapter 5: Mirror Temple",
            "Chapter 6: Reflection",
            "Chapter 7: The Summit"
        ]
    

class CelesteIncludeCore(Toggle):
    """
    Niko wants to include the eighth chapter, the Core, in the Keep.
    """
    display_name = "[Niko] Include The Core"
    default = False

class CelesteIncludeFarewell(Toggle):
    """
    Niko wants to include the farewell chapter in the Keep.
    """
    display_name = "[Niko] Include Farewell"
    default = False

class CelesteIncludeBFace(Toggle):
    """
    Niko wants to include the B-side remixes of the main chapters in the Keep.
    """
    display_name = "[Niko] Include B-Face"
    default = False

class CelesteIncludeCFace(Toggle):
    """
    Niko wants to include the C-side remixes of the main chapters in the Keep. Note that the C-sides are generally much more difficult than the B-sides, so enabling this option will add a lot of difficult objectives to the pool.
    """
    display_name = "[Niko] Include C-Face"
    default = False
    
 