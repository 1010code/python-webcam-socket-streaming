# python-webcam-socket-streaming
Python OpenCV webcam send sending frames through TCP socket. 

## What is a network Socket?
- A software structure within a network node
- Serves as an endpoint to send & receive
- A combination of protocpl type, IP adress and Port number for data communication

## Implementation of Sockets
In standard interent protocols like TCP and UDP, socket address is the combination of:

```
socket address = (IP address, port number)
```

Depending on the operating system, you can easily find the IP address of your machine. Go to the terminal window and run this command:
#### macOS

```
ipconfig getifaddr en0
```
#### Windows/Linux/Ubuntu

```
ifconfig
```

> For Windows users. The required IP address will show against IPv4 Address.

> For Linux and Ubuntu users. The required IP address will be for Wifi LAN (inet).

## client-server model
- Server creates socket on startup
- May serve several  clients concurrently
- A client should know the server IP and port

![](./screenshot/img01.png)

## Python Server module

![](./screenshot/img02.png)

## Reference
- [kittinan/socket](https://gist.github.com/kittinan/e7ecefddda5616eab2765fdb2affed1b)