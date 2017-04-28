# !/usr/bin/env python
# -*- coding:utf-8 -*-

import prop
import os
import codecs
import xlwt

"""
    获取路径相关
"""

def getPoolTxtFilePath(fileName):
    '''
        获取ifengDataPlayground目录下textpool目录下文件路径
    '''
    if fileName:
        if isinstance(fileName,str):
            return os.path.join(prop.IFENGTXTPOOL,fileName)


def getCacheResultFilePath(fileName):
    '''
        获取ifengDataPlayground目录下cache目录文件路径
    '''
    if fileName:
        if isinstance(fileName,str):
            return os.path.join(prop.IFENGCACHEDATA,fileName)


"""
    文件输入相关
"""

def readListFromTxt(filePath):
    '''
        读取文本信息形成列表
        只是将整行内容存储到列表中
    '''
    infoList = []
    if os.path.exists(filePath):
        f = codecs.open(filePath,'r',encoding='utf-8')
        while True:
            line = f.readline()
            if line:
                temp = line.strip()
                infoList.append(temp)
            else:
                break
        f.close()
    return infoList


"""
    文件输出相关
"""

def writeList2Txt(filePath,infoList):
    '''
        以列表形式将数据输出到txt文本
    '''
    if infoList:
        f = codecs.open(filePath,'w','utf-8')
        for i in range(len(infoList)):
            outputLine = infoList[i].strip()
            finalOutput = outputLine + '\n'
            f.write(finalOutput.encode('utf-8'))
        f.close()
        print '写入完成...'


def writeContent2Excel(infoList, outputFilePath):
    """
        “覆盖”的方式写入数据
    """
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('Sheet1')
    for i in range(len(infoList)):
        for j in range(len(infoList[i])):
            sheet.write(i, j, infoList[i][j])
        print('写入第【', str(i), '】条数据...')
    xls.save(outputFilePath)
    print('数据写入完成...')