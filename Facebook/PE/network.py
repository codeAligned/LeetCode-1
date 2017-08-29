#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# network port
# 2. 是一道 Network 的题。大概意思是讲 有一项 Network Service 要升级，大家决定 启用新的 Port 来减少 confusion。
# 这项迁移工程需要很久，所以需要 System 每天 report。
# 请你写一个 Script，输入 <hostName port1 port2> as command line argument, 
# output the 迁移 progress，和那些 host running both version 和 host which does not running any version.

# subprocess
# netstat -tulpn | grep process-name

import sys
from subprocess import *

# _, host, port1, port2 = sys.argv

ls = Popen(["ls", "-l"], stdout=PIPE)
grep = Popen(["grep", "network"], stdin=ls.stdout)

# print(grep.communicate())
# subprocess.Popen(["netstat", "-tulpn", "|", "grep", "network"])
