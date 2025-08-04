
import zmq
import json


def RecipeTracker(recipe, inventory):
    """ - Recieves two dictionaries one representing the necessarry ingredients
    for a recipe and the other representing the inventory of ingredients.
    - Returns two dictionaries that represent ingredients in stock and
    ingredients in need.
    - Transmits error message when recipe ingredient value isn't properly identified."""

    inStock = {}
    outOfStock = {}

    for ingredient, need in recipe.items():
        if not need or need <= 0:
            return f"Error: Recipe missing Ingredient {ingredient} required value", False
        have = inventory.get(ingredient, 0)
        inStock[ingredient] = min(need, have)
        if need - have > 0:
            outOfStock[ingredient] = need - have
        
    return inStock, outOfStock

environment = zmq.Context()

replySocket = environment.socket(zmq.REP)

replySocket.bind("tcp://*:5555")

#wait for message from program

while True:
    message = replySocket.recv()

    jsonMessage = message.decode("utf-8")

    data = json.loads(jsonMessage)

    recipe, inventory = data

    inStock, outOfStock = RecipeTracker(recipe, inventory)

    if not outOfStock:
        respond = {'Error': inStock}
    else:
        respond = {'In Stock': inStock, 'Missing' : outOfStock}
    
    respondJson = json.dumps(respond)
    replySocket.send(respondJson)





