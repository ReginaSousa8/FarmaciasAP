from socketserver import ThreadingTCPServer
from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from services.FarmaciaServices import *

class MyXMLRPCServer (ThreadingTCPServer,SimpleXMLRPCServer):
    pass

# Create server
server = MyXMLRPCServer(("localhost", 12345),SimpleXMLRPCRequestHandler, logRequests=True, allow_none=True, encoding=None)
server.register_introspection_functions()
server.register_multicall_functions()

# Register an instance; all the methods of the instance are
server.register_instance(FarmaciaServices())
server.serve_forever()







'''
try:
    print('Use Control-C to exit')
    print("Server up")
    

except KeyboardInterrupt:
    print('Exiting')
'''


