import asyncio

class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport: asyncio.Transport) -> None:
        peername = transport.get_extra_info("peername")
        print(f"Connection from {peername}")
        self.transport = transport

    def data_received(self, data: bytes) -> None:
        message = data.decode()
        print("Data recieved: {!r}".format(message))
        self.transport.write((f"Echoed back: {message}").encode())
        print(f"Closing connection from {self.transport.get_extra_info('peername')}")
        # BaseTransport.close(): This method is used to close the calling
        # 'transport' object, after which the connections between different
        # systems will be stopped. The corresponding protocol of the transport
        # will automatically call its 'connection_lost()' method
        self.transport.close()

loop = asyncio.get_event_loop()
coro = loop.create_server(EchoServerClientProtocol, "127.0.0.1", 8181)
server = loop.run_until_complete(coro)

print(f"Serving on {server.sockets[0].getsockname()}")
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
