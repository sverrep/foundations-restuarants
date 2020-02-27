import http.server
import socketserver

# A simple script to use the python CGI server in python3
# Using CGIHTTPRequestHandler in place of SimpleHTTPRequestHandler
# allows python scripts to be called as an action (POST)

# define the handler to be the CGI server
handler = http.server.CGIHTTPRequestHandler

# point the handler to a directory with scripts
handler.cgi_directories = ["/cgi-scripts"]

# define the server using the handler
PORT = 80
httpd = socketserver.TCPServer(("35.242.248.4", PORT), handler)

# Set variables which the CGIHTTPRequestHandler expects
httpd.server_name = "myServer"
httpd.server_port = PORT

print("staring CGI server...")

# run the server. To kill it, issue Ctrl + C
httpd.serve_forever()