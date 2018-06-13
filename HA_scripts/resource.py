import paramiko 
import sys 
import time 
import os
import constants
import json
import threading
sys.path.append(os.getcwd())
cur_Dir = os.getcwd()

node_name_file = cur_Dir + '/node.json' 
with open(node_name_file) as f2:
     node = json.load(f2)

def ssh_connection(ip_address, username, password):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(hostname=ip_address, username=username, password=password)
    return ssh

def standby_node(node_names):
    ssh = ssh_connection(constants.primary_node_ip, constants.username, constants.password)
    stdin, stdout, stderr = ssh.exec_command('pcs cluster standby ' + node_names)
    print "Node %s is into standby mode" %node_names

def unstandby_node(node_names):
    ssh = ssh_connection(constants.primary_node_ip, constants.username, constants.password)
    stdin, stdout, stderr = ssh.exec_command('pcs cluster unstandby ' + node_names)
    print "Node %s is into active state" %node_names

def main():
    while True:
        for i in range(0,len(node['nodes'])):
	        node_n = node['nodes'][i]['node_name']
		standbytime = node['nodes'][i]['standby_time']
		unstandbytime = node['nodes'][i]['unstandby_time']
		t1 = threading.Timer(standbytime, standby_node , args=(node_n, ))
		t1.start()
	        time.sleep(10)
		t2 = threading.Timer(unstandbytime, unstandby_node, args=(node_n, ))
		t2.start()
		time.sleep(10)
	  
main()
   
