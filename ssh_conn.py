import paramiko
import time
import os.path



#switch_ip = '192.168.245.129'  # Replace with your switch IP address
############################################################################
def ssh_conn(ip):
    cred_file_path = input("Enter your cred_file_path")
    if os.path.isfile(cred_file_path) == True:
        print("Cred File path is ok")
    else:
        print("Cred file path is not ok")
    with open(cred_file_path, "r") as cred_file:
        cred_file.seek(0)
        username = cred_file.readlines()[0].split(",")[0].rstrip("\n")
        cred_file.seek(0)
        password = cred_file.readlines()[0].split(",")[1].rstrip("\n")
    #################################################################################
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=ip.rstrip("\n"), username=username, password=password, look_for_keys=False, allow_agent=False)
        print(f"Connected to {ip}")

        ssh_session = client.invoke_shell()
        time.sleep(1)
        ssh_session.recv(1000)  # Clear buffer

        commands = ['enable', 'terminal length 0', 'show ip interface brief', 'show version']

        for cmd in commands:
            ssh_session.send(cmd + '\n')
            time.sleep(2)  # Adjust time based on your network's latency

        output = ""
        while ssh_session.recv_ready():
            output += ssh_session.recv(65535).decode('utf-8')

        print(output)

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as sshException:
        print(f"Unable to establish SSH connection: {sshException}")
    except Exception as e:
        print(f"Exception in connecting to the switch: {e}")
    finally:
        client.close()
        print("Connection closed.")

