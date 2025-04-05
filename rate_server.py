import socket
import os
import json

LIMIT = 5

listen_on = ("127.0.0.1", 60000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(listen_on)
server.listen(1)

# making sure the db file exists
if os.path.isfile("database.json"):
    print("file exists")
else:
    with open("database.json", "w") as db:
        json.dump([], db, indent=4)

while True:
    client, client_addr = server.accept()
    print("new client")

    print("validating...")
    collection = []
    with open("database.json", "r") as db:
        collection = json.load(db)

    requested = False
    limit_exceeded = False
    if collection != []:
        for i, doc in enumerate(collection):
            # if the registered doc is the user we are looking for:
            if doc["ip"] == client_addr[0]:
                registered = True
                # check current number of requests user has on file
                count = doc["count"]
                while count < LIMIT:
                    req = client.recv(1024).decode()
                    if len(req) == 0:
                        client.close()
                        print("client disconnected")
                        break
                    else:
                        print(f"({req}) from {client_addr}")
                        count += 1
                        doc["count"] = count
                        if count == 5:
                            limit_exceeded = True
                        requested = True
                # only push local db iff the db has been modified
                if requested:
                    with open("database.json", "w") as db:
                        json.dump(collection, db, indent=4)

                # once we've reached out target user, we don't have to keep looking
                break
    else:
        new_doc = {"ip": client_addr[0], "count": 1}
        count = 0

        while count < LIMIT:
            req = client.recv(1024).decode()
            if len(req) == 0:
                client.close()
                print("client disconnected")
                break
            else:
                print(f"({req}) from {client_addr}")
                count += 1
                new_doc["count"] = count
                if count == 5:
                    limit_exceeded = True
                requested = True

        # we append bc there was no prior entree associated with user
        collection.append(new_doc)
        # only push local db iff the db has been modified
        if requested:
            with open("database.json", "w") as db:
                json.dump(collection, db, indent=4)

    if limit_exceeded:
        print("Client has reached their limit.")
    client.close()
