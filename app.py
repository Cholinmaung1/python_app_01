import sys
from ip_file_valid import ip_file_valid
from ip_address_valid import ip_addr_valid
from ip_address_reach import ip_addr_reach
from ssh_conn import ssh_conn
from create_thread import create_threads

#Saving the list of IP addresses in ip.txt to a variable
ip_list = ip_file_valid()

#Verifying the validity of each IP address in the list
try: 
    ip_addr_valid(ip_list)
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

#Verifying the reachability of each IP address in the list
try:
    ip_addr_reach(ip_list)
    
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

#Calling threads creation function for one or multiple SSH connections
create_threads(ip_list, ssh_conn)

#End of program
