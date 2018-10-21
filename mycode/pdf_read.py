# !/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
import os
import sys
import time
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter

# 文件夹的名字
filepath='/home/robot202/桌面/literatures'
# debug option
debug = 0
# input option
password = ''
pagenos = set()
maxpages = 0
# output option
outfile = None
outtype = None
imagewriter = None
rotation = 0
layoutmode = 'normal'
codec = 'utf-8'
pageno = 1
scale = 1
caching = True
showpageno = True
laparams = LAParams()
outfile = filepath+'/'+'temp.text'

rsrcmgr = PDFResourceManager(caching=caching)
outtype = 'text'
# outfp = sys.stdout   # 输出到终端

files = os.listdir(filepath)
for filename in files:
    outfp = file(outfile, 'w')
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams, imagewriter=imagewriter)
    fp = file(filepath+'/'+filename, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp, pagenos,
                              maxpages=maxpages, password=password,
                              caching=caching, check_extractable=True):
        page.rotate = (page.rotate + rotation) % 360
        interpreter.process_page(page)
    fp.close()
    # 读取text文件
    f = open(outfile, 'r')
    data0 = f.read()
    data = data0.split()
    for str in data:
        if str == 'some':
            print(filename)
            break
    os.remove(outfile)

