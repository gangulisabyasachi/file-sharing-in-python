# Import necessary modules
import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import png
import os

# Assigning the appropriate port value
PORT = 8010

# This finds the name of the computer user
# Use HOME for macOS
user_home = os.environ['HOME']

# Changing the directory to access the files on the desktop
desktop = os.path.join(user_home, 'Desktop')
os.chdir(desktop)

# Creating a HTTP request
Handler = http.server.SimpleHTTPRequestHandler

# Finding the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

# Converting the IP address into the form of a QR code
url = pyqrcode.create(link)

# Saves the QR code in the specified directory
url.svg("/Users/sabyasachiganguli/Desktop/code/projects/myqr.svg", scale=8)

# Opens the QR code image in the web browser
webbrowser.open('/Users/sabyasachiganguli/Desktop/code/projects/myqr.svg')

# Creating the HTTP request and serving the folder in the specified PORT
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    print("Type this in your browser:", IP)
    print("or use the QR Code")
    httpd.serve_forever()
