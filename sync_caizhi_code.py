#coding=utf-8
import os
import sys

if os.getuid() == 0:
	pass
else:
	print '当前用户不是root用户，请以root用户执行脚本'
	sys.exit(1)

cmd = 'cd /data/www'
res = os.system(cmd)
if res != 0:
	print '进入nginx服务器项目目录失败'
	sys.exit(1)

version = raw_input('请输入你想要同步的svn代码（master/branch）')		
if version == 'master':
	res = os.path.exists('/data/www/master')	
	if res = 0:
		cmd = 'rm -rf master'
		res = os.system(cmd)
		if res != 0:
		print '删除master项目文件夹失败'
		sys.exit(1)
	else:
		cmd = 'mkdir /data/www/master'
		res = os.system(cmd)
		if res != 0:
			print '新建master项目文件夹失败'
			sys.exit(1)
		print '没有检测到有master项目文件夹'
		sys.exit(1)	
	url = 'https://192.168.11.88/svn/MMAdmin/branches/v1.1.6'
elif version == 'branch':
	res = os.path.exists('/data/www/branch')
	if res = 0:
		cmd = 'rm -rf branch'
		res = os.system(cmd)
		if res != 0:
			print '删除branch项目文件夹失败'
			sys.exit(1)
	else:
		cmd = 'mkdir /data/www/branch'
		res = os.system(cmd)
		if res != 0:
			print '新建branch项目文件夹失败'
			sys.exit(1)
		print '没有检测到有branch项目文件夹'
		sys.exit(1)	
	url = 'https://192.168.11.88/svn/MMAdmin/branches/v1.1.6_0803'	
else:
	print '你输入的同步svn代码信息有误，请输入master或者branch'
	sys.exit(1)


if version == 'master':
	cmd = 'cd /data/www/master'
	res = os.system(cmd)
	if res != 0:
		print '进入master目录失败'
		sys.exit(1)
else:
	cmd = 'cd /data/www/branch'
	res = os.system(cmd)
	if res != 0:
		print '进入branch目录失败'
		sys.exit(1)

cmd = 'svn checkout '+url
res = os.system(cmd)
if res != 0:
	print '检出svn上的代码失败，请检查网络'
	sys.exit(1)
