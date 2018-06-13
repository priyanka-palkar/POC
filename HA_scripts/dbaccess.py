import MySQLdb
import sys
import os
import constants
import time

sys.path.append(os.getcwd())
cur_Dir = os.getcwd()

host_file = cur_Dir + '/hosts'
f1 = open(host_file,"r")
host_machines = f1.readlines()

try:
    for host_machine_ip in host_machines:
       	host_machine_ip = host_machine_ip.rstrip()
	db = MySQLdb.connect(host_machine_ip,constants.username,constants.password,constants.database_name)
	print "Connected to host %s database '%s'" %(host_machine_ip,constants.database_name)
	cursor = db.cursor()
	cursor.execute("select * from " + constants.table_name)
	data = cursor.fetchall()
	print data
	db.close()
	time.sleep(10)
except:
    print "Host: %s is down" %host_machine_ip
