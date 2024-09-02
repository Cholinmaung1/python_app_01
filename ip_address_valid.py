import sys

def ip_addr_valid(list):
    for ip_addr in list:
        ip_addr = ip_addr.rstrip("\n")
        ip_addr_split = ip_addr.split(".")
        
        octet1 = int(ip_addr_split[0])
        octet2 = int(ip_addr_split[1])
        octet3 = int(ip_addr_split[2])
        octet4 = int(ip_addr_split[3])

        if (len(ip_addr_split) == 4) and (1 <= octet1 <=254) and (octet1 != 127) and (octet1 !=169 or octet2 !=254) and (0 <= octet2 <=255) and (0 <= octet3 <= 255) and (0 <= octet4 <= 255):
            continue
        else:
            print("ip is invalid")
            sys.exit()



