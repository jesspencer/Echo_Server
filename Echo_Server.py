#!/usr/bin/env python3 

from http.server import HTTPServer, BaseHTTPRequestHandler

#create a subclass of http.server.BaseHTTPRequestHandler
class HelloHandler(BaseHTTPRequestHandler):
	#define a method on the handler class for each http ver you want to handle
	#do get handles http requests 
	def do_GET(self):
		#sending status code 
		self.send_response(200) 
		#headers
		self.send_header('Content type', 'text/plain; charset=utf-8')
		#headers 
		self.end_headers()
		
		#response body 
		#instead of writing hello, used self.path and 1: to remove the '/'
		self.wfile.write(self.path[1:].encode())
		
if __name__=='__main__':
	#create an instance of htttp.server.httpServer give it handler class port number
	server_address = ('', 8000)
	httpd = HTTPServer(server_address, HelloHandler)
	#call the httpServer instance's server_forever method
	httpd.serve_forever()