import os
# This script pings a list of IP addresses and prints the result. 


ip_list = []

for i in range(1, 25):
    ip_list.append("192.168.1." + str(i))

for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"{ip} is successfully pinged.")
    else:
        print(f"{ip} is not reachable.")
    print(response)

