# !/usr/bin/env python
# -*- coding:utf-8 -*-

from core import inout
from core import systm

if __name__ == '__main__':
    inputFileName = inout.getPoolTxtFilePath('30_rg_longtime.txt')
    outputFilepath = inout.getCacheResultFilePath('30_rg_longtime.xls')

    infoList = inout.readListFromTxt(inputFileName)

    resultList = []
    for item in infoList:
        tempList = item.strip().split('\t')
        if len(tempList)==10:
            resultList.append(tempList)
        # print len(tempList),tempList
    inout.writeContent2Excel(resultList,outputFilepath)