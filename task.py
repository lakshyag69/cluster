#!/usr/bin/python3
import os
def cluster():
	m_ip=input("enter the ip where you want to configure master")
	os.system('scp /root/task/task.sh root@{}:/root/task.sh'.format(m_ip))
	os.system('ssh root@{} bash /root/task.sh'.format(m_ip))
	os.system('scp /root/task/core-site.tmp root@{}:/etc/hadoop/core-site.xml'.format(m_ip))
	os.system("ssh root@{} sed -i 's/master/{}/g' /etc/hadoop/core-site.xml".format(m_ip,m_ip))
cluster()
