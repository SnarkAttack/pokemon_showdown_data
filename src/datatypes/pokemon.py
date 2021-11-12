from .base import BaseDataType

class Pokemon(BaseDataType):

    def __init__(self, 
                 num,
                 name,
                 types,
                 baseStats,
                 abilities,
                 heightm,
                 weightkg,
                 color,
                 eggGroups,
                 prevo=None,
                 evos=None,
                 evoLevel=None,
                 gender=None,
                 baseSpecies=None,
                 forme=None,
                 formeOrder=None,
                 otherFormes=None,
                 evoType=None,
                 changesFrom=None,
                 gen=None,
                 tags=None,
                 requiredItem=None,
                 evoItem=None,
                 baseForm=None,
                 canGigantamax=None,
                 evoCondition=None,
                 canHatch=None,
                 cosmeticFormes=None,
                 battleOnly=None,
                 requiredAbility=None,
                 requiredItems=None,
                 evoMove=None,
                 cannotDynamax=None,
                 requiredMove=None,
                 maxHP=None):
        self.num = num
        self.name = name
        self.types = types
        self.base_stats = baseStats
        self.abilities = abilities
        self.height = heightm
        self.weight = weightkg
        self.color = color
        self.egg_groups = eggGroups
        self.prevo = prevo
        self.evos = evos
        self.evo_level = evoLevel
        self.gender = gender
        self.base_species = baseSpecies
        self.forme = forme
        self.forme_order = formeOrder
        self.other_formes = otherFormes
        self.evo_type = evoType
        self.changes_from = changesFrom
        self.gen = gen
        self.tags = tags
        self.required_item = requiredItem
        self.evo_item = evoItem
        self.base_form = baseForm
        self.can_gigantamax = canGigantamax
        self.evo_condition = evoCondition
        self.can_hatch = canHatch
        self.cosmetic_formes = cosmeticFormes
        self.battle_only = battleOnly
        self.required_ability = requiredAbility
        self.required_items = requiredItems
        self.evo_move = evoMove
        self.cannot_dynamax = cannotDynamax
        self.required_move = requiredMove
        self.max_hp = maxHP

    
