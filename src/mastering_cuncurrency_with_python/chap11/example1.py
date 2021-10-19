import asyncio

class EchoServerClientProtocol(asyncio.Protocol):
    # Protocol.connection_made(Transport): this method is automatically called
    # whenever a connection from another system is made. The 'transport'
    # argument holds the 'transport' object that is associated with the
    # connection. Again, each 'transport' needs to be paired with a protocol;
    # we generally store this transport object as an attribute of this specific
    # protocol object in the 'connection_made()' method
    def connection_made(self, transport: asyncio.Transport) -> None:
        # BaseTransport.get_extra_info(): This method returns, as the name
        # suggests, additional channel-specific information for the calling
        # 'transport' object. The result can include information regarding the
        # socket, the pipe, and the subprocess associated with the transport.
        # 'BaseTransport.get_extra_info("peername")' is used in order to obtain
        # the remote address from which the transport travelled
        peername = transport.get_extra_info("peername")
        print("Connection from {}".format(peername))
        self.transport = transport

    # Protocol.data_received(data): This method is automatically called
    # whenever the one system that we are connected to sends its data. Note
    # that the 'data' argument, which holds the sent information, is usually
    # represented in bytes, so th 'decode()' function of Python should be used
    # before 'data' is processed further
    def data_received(self, data: bytes) -> None:
        message = data.decode()
        print("Data recieved: {!r}".format(message))

loop = asyncio.get_event_loop()
coro = loop.create_server(EchoServerClientProtocol,
        '127.0.0.1', 8181)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print("Serving on {}".format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
