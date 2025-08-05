import zmq
import json


def main(send_data):

    context = zmq.Context()

    requestSocket = context.socket(zmq.REQ)

    # connect requestSocket to a remote requestSocket
    requestSocket.connect("tcp://localhost:5555")

    requestSocket.send_string(json.dumps(send_data))

    message = requestSocket.recv_string()

    print(message)


if __name__ == "__main__":

    print('test case 1: Missing value inventory value proceeds forward')
    data = {'Green Pepper': 5,
        'Onion' : 2,
         'Tomato': 4
         }, {'Green Pepper': 7, 
         'Onion': 1,
          'Tomato': 0 }
    main(data)

    print('test case 2 : Error missing recipe ingredients')
    data = {
         }, {'Green Pepper': 7, 
         'Onion': 1,
          'Tomato': 0 }
    main(data)

    print('test case 3: Inventory values empty, but still process')
    data = {'Green Pepper': 5,
        'Onion' : 2,
         'Tomato': 4
         }, { }
    main(data)

    print('test case 4: The perfect call')

    data = {'Spinach': 20,
        'Oranges' : 6,
         'Green Apples': 4
         }, {'Spinach': 19, 
         'Oranges': 6,
          'Green Apples': 4}
    main(data)




