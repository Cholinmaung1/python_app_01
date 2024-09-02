import sys
import subprocess

#check ping
def ip_addr_reach(list):
    for ip in list:
        ip = ip.rstrip("\n")
        ping_reply = subprocess.call("ping %s -n 2" %(ip,), stdout=subprocess.DEVNULL, stderr = subprocess.DEVNULL)

        if ping_reply == 0:
            print("ping is ok")
            continue
        else:
            print("ping is not ok")
            sys.exit()
        
