# InventoryTracker Microservice

### About

This service receives 2 lists of ingredients from a Client

- List 1 is a key-value pair  (ingredient, amount required)
- List 2 represents the inventory for each ingredient

Returns 2 lists
- List 1 represents ingredients that are fully available
- List 2 represents the amount of each ingredient required to restock


### Communication Contract

This service runs using the zeroMQ req/rep model. After downloading files from github run server.py file to listen for requests on port 5555. 

```bash

# Server setup
environment = zmq.Context()
replySocket = environment.socket(zmq.REP)
replySocket.bind("tcp://*:5555")

```

## Request Data
Set up a zeroMQ client and define data to send

```bash
import zmq
import json

context = zmq.Context()
requestSocket = context.socket(zmq.REQ)
# connect requestSocket to a remote requestSocket
requestSocket.connect("tcp://localhost:5555")

request_data = [
    {'Green Pepper': 5, 
        'Onion' : 2,
         'Tomato': 4
         }, 
         {'Green Pepper': 7, 
         'Onion': 1,
          'Tomato': 0
         }
         ]

```

### Send Request

```bash

data = json.dumps(request_data)
socket.send_string(data)

```

### Receive Data 

Responses will be received in JSON format and decoded by thr recv_string() function before presenting to users..

```bash

message = requestSocket.recv_string()
print(message)

```

### Succesful Output

```bash

{"In Stock": ["Green Pepper"], "Missing": {"Onion": 1, "Tomato": 4}}

```

## UML Sequence Diagram

![alt text](<uml diagram.jpg>)

### Author

Ronniekev





