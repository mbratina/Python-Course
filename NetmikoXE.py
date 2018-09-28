from  netmiko import ConnectHandler
if __name__ == "__main__":
    # Uses SSH TCP Port 22
    #CSR1KV = {'device_type':'cisco_ios','ip':'192.168.10.80','username':'admin','password':'cisco'}
    # Uses  Telnet TCP Port 23
    CSR1KV = {'device_type':'cisco_ios_telnet','ip':'192.168.10.80','username':'admin','password':'cisco'}
    net_connect=ConnectHandler(**CSR1KV)
    net_connect.find_prompt()
    output = net_connect.send_command("show ip inter brief")
    print output