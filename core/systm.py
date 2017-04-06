# !/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from core import inout
import prop
import os

"""
    时间相关
"""
def getCurrentTimeStamp():
    '''

    '''
    return time.time()

def getCurrentFormatDate(link=''):
    '''

    '''
    dateFormat = '%Y' + link + '%m' + link + '%d'
    return time.strftime(dateFormat,time.localtime(time.time()))


"""
    文件相关
"""
