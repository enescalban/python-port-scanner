import pyfiglet
import sys
import socket
from datetime import datetime
import simple_colors

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
print(simple_colors.blue("www.enescalban.com"))
print(simple_colors.blue("https://github.com/enescalban"))
print("_" * 50)

# End Header :)

target = input(str(simple_colors.red("TARGET IP: ")))

# Banner
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning Target at: " + str(datetime.now()))
print("_" * 50)

try:
	
	# will scan ports between 1 to 65,535
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		
		# returns an error indicator
		result = s.connect_ex((target,port))
		if result ==0:
			print( simple_colors.green("Port {} is open".format(port))) 
		s.close()
		
except KeyboardInterrupt:
		print("\n Exiting Program!")
		sys.exit()
except socket.gaierror:
		print("\n Hostname Could Not Be Resolved!")
		sys.exit()
except socket.error:
		print("\ Server not responding!")
		sys.exit()
