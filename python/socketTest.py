import socket
hosts = ['www.uc.edu', 'www.google.com', 'www.bing.com']

print ('Working from hosts: ' + socket.getfqdn())

for h in hosts:
    print (h + ': ' + socket.gethostbyname(h))