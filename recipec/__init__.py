from __future__ import unicode_literals

from os.path import abspath, dirname, join

import textx.scoping.providers as scoping_providers
from recipec.mm_classes import (
    Ingredient, IngredientAlias, IngredientTypeDef, PlanEntry)
from textx import language, metamodel_from_file


def get_grammar_path(name):
    this_folder = dirname(abspath(__file__))
    return join(this_folder, "grammar", name)


@language('recipe-config', '*.config')
def config_lang():
    return metamodel_from_file(get_grammar_path("Config.tx"))


@language('recipe-ingredient', '*.ingredient')
def ingredient_lang():
    return metamodel_from_file(get_grammar_path("Ingredient.tx"),
                               classes=[IngredientTypeDef, IngredientAlias])


@language('recipe-recipe', '*.recipe')
def recipe_lang():
    mm = metamodel_from_file(get_grammar_path("Recipe.tx"),
                             classes=[Ingredient])
    config_provider = scoping_providers.PlainNameGlobalRepo(
        "**/*.config", glob_args={"recursive": True})
    ingredient_type_provider = scoping_providers.PlainNameGlobalRepo(
        "**/*.ingredient", glob_args={"recursive": True})
    mm.register_scope_providers({
        "Recipe.persons": config_provider,
        "Ingredient.type": ingredient_type_provider,
        "Ingredient.unit": scoping_providers.ExtRelativeName(
            "type", "units", "extends"),
    })
    return mm


@language('recipe-plan', '*.plan')
def plan_lang():
    mm = metamodel_from_file(get_grammar_path("Plan.tx"),
                             classes=[PlanEntry])
    mm.register_scope_providers({
        "*.*": scoping_providers.PlainNameImportURI()  # noqa: each import is a recipe model
    })
    return mm
