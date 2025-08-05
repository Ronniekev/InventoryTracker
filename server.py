import zmq
import json
from InventoryTracker import inventory_tracker

environment = zmq.Context()

replySocket = environment.socket(zmq.REP)

replySocket.bind("tcp://*:5555")

#wait for message from program

while True:
    message = replySocket.recv_string()


    data = json.loads(message)
    if len(data) != 2:
        response_message = {'Error': 'Expecting 2 dictionaries (ingredients, inventory).'}

    else:
        try:
            recipe, inventory = data
            in_stock, out_of_stock = inventory_tracker(recipe, inventory)

            response_message = {'In Stock': in_stock, 'Missing' : out_of_stock}
        except ValueError as error:
            response_message = {'Error': str(error)}
        
    
    replySocket.send_string(json.dumps(response_message))
