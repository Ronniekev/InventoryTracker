import json


def inventory_tracker(recipe, inventory):
    """ - Recieves two dictionaries one representing the necessarry ingredients
    for a recipe and the other representing the inventory of ingredients.
    - Returns a list that represent ingredients in stock and
    a dictionary representing ingredient amounts required.
    - Transmits error message when recipe ingredient value isn't properly identified."""

    in_stock = []
    out_of_stock = {}
    if not recipe:
        raise ValueError("Recipe list cannot be empty.")

    for ingredient, need in recipe.items():
        if not need or need <= 0:
            raise ValueError(f"Recipe missing required quantity for {ingredient}")
        have = inventory.get(ingredient, 0)
        if have >= need:
            in_stock.append(ingredient)
        else:
            out_of_stock[ingredient] = need - have
        
    return in_stock, out_of_stock






