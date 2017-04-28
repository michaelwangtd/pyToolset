# !/usr/bin/env python
# -*- coding:utf-8 -*-

from core import inout
from core import systm

def getDifSet(finalFullSetList,partSetList):
    resultList = []
    for item in partSetList:
        if item not in finalFullSetList:
            resultList.append(item)
    return resultList


def cleanFullSetList(fullSetList):
    resultList = []
    for item in fullSetList:
        temp = item.strip().split('\s+')[0]
        resultList.append(temp)
    return resultList


if __name__ == '__main__':

    # 路径
    inFullSetPath = inout.getPoolTxtFilePath('All-false-329043826423715.txt')
    # inFullSetPath = inout.getPoolTxtFilePath('t1.txt')
    inPartSetPath = inout.getPoolTxtFilePath('All-15554627590856.txt')
    # inPartSetPath = inout.getPoolTxtFilePath('t2.txt')

    currentDate = systm.getCurrentFormatDate()
    outFileName = 'result_'+currentDate+'.txt'
    outResultPath = inout.getCacheResultFilePath(outFileName)
    # 加载数据
    fullSetList = inout.readListFromTxt(inFullSetPath)
    print 'fullSet' + str(len(fullSetList))
    finalFullSetList = cleanFullSetList(fullSetList)
    print 'finalFullSetList' +str(len(finalFullSetList))
    partSetList = inout.readListFromTxt(inPartSetPath)
    print 'partSet' + str(len(partSetList))

    exit(0)

    #
    time1 = systm.getCurrentFromatTime(':')
    print 'time1:' + str(time1)
    difSetList = getDifSet(finalFullSetList,partSetList)
    time2 = systm.getCurrentFromatTime(':')
    print 'time2:' + str(time2)

    print difSetList
    print outResultPath
    # 输出
    inout.writeList2Txt(outResultPath,difSetList)
    print '结束...'

