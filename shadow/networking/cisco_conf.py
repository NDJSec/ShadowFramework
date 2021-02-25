from netmiko import ConnectHandler 


def connect(ip_addr, username, passwd):
    print('Connecting to host ' + ip_addr)
    cisco_switch = {
        'device_type':'cisco_ios',
        'host':ip_addr,
        'username':username,
        'password':passwd,
        'conn_timeout':10
    }
    net_connect = ConnectHandler(**cisco_switch)

    


def config(opt):
    if(opt == '1'):
        #Set hostname
        print("Setting hostname")
        pass
    if(opt == '2'):
        #Set motd
        pass
    if(opt == '3'):
        #Configure Passwords
        pass
    if(opt ==  '4'):
        #Configure VLANs 
        pass
    if(opt == '5'):
        #Copy run start
        pass
    if(opt == '6'):
        output = connect.net_connect.send_command('show run')
        print(output)
    if(opt == '99'):
        print('Exiting ...')

