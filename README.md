# POC: Rate Limit 101

## by: Kevin Arista Solis

#### Description

Proof of Concept to demonstrate how rate limiting works. In this case, we will will take advantage of TCP's connection oriented communication between two different machines. We will mimic a client to server architecture. We will also be using a json file in order to mantain track of our client's IP address-- as that is what we will use to identify clients as unique.

Notice: in the real world, we should NOT use IP addresses as the client's unique identification.

1. This is too sensitive of a data! (it's could be classified as personal identifiable information) If database get's leaked, attackers could use this to attacks the user's computer, regardless of the application. Therefore it will not be a contained attack.
2. It is best to use some sort of username-- and you should not let user's have the same username. In addition, this username should be encypted with AES-CBC, etc.

### FUTURE IMPLEMENTATIONS:

We should never store data inside our database as plaintext! In fact, we should not send plaintext, through the network especially if it's sent via wireless networks. As they are literally broadcasted to anyone. Anyone could attempt to read any stream of bits flying through the air!

We should not use a hash function like SHA256 (a hashing algorithm) to scramble out bits, because a hash function is not pseudorandom.

Notice: A Hash function, although it does scramble data, does not do so uniquely. A hash-function is used to condense data down. Hashes are never good for encyption as they are:

1. Deterministic!

Eventually, we could handle multiple sockets using non-blocking I/O by using functions such as the select() as this could help us only handle the socket, if there is data to read for certain.

Note: this "data" could either mean a request or that the other end of our socket has closed the connection!

#### Pre-Reqs

You should have some prior knowledge on socket programming. You don't have to understand the underlying protocl behind TCP and how it works, but you should understand what it means to open and close a socket.

#### Libraries to install are:

- socket
- os
- json

#### Our data will resemble MongoDB's noSQL collection of documents:

```
[
    {
        "ip": ip,
        "count": count,
    },
    {
        ...
    }
]
```

## How to Run:

In our example: we just set up a simple client-server architecture. For this reason we have our client: `tcp_client.py` and out server: `rate_server.py`.

```
/* preferable split your terminal into two
 * panels in oder to see the print statements
 * of each program
*/
$ python rate_server.py
$ python tcp_client.py
```
