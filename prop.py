# !/usr/bin/env python
# -*- coding:utf-8 -*-

import os

"""
    python toolset main file
    property：protected
"""

'''
    directory name
'''
CACHE = 'cache'
BACKUP = 'backup'
JSONPOOL = 'jsonpool'


'''
    project
'''
# root path
ROOTPATH = 'D:\\workstation\\repositories\\pyToolset'


'''
    data
'''
# ifengDataPlayground
IFENGDATAPLAYGROUND = 'D:\\workstation\\ifengDataPlayground'
# ifengjsonpool
IFENGJSONPOOL = os.path.join(IFENGDATAPLAYGROUND,JSONPOOL)
# ifengcachedata
IFENGCACHEDATA = os.path.join(IFENGDATAPLAYGROUND,CACHE)
# ifengbackupdata
IFENGBACKUPDATA = os.path.join(IFENGDATAPLAYGROUND,BACKUP)


