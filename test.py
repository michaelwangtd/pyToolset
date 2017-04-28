# !/usr/bin/env python
# -*- coding:utf-8 -*-

from core import systm
from core import inout


# print systm.getCurrentTimeStamp()
# print systm.getCurrentFormatDate('-')

# systm.initDataCacheDirByDate()
# print systm.getCurrentFromatTime(':')
testPath = inout.getCacheResultFilePath('test.txt')
print testPath
testList = ['1','2','3']
inout.writeList2Txt(testPath,testList)