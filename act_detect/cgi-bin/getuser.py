#! /usr/bin/python2.7
# -*- coding:utf-8 -*-
__author__ = 'wen'

import cgi
import time
from svmutil import *

acts_name = {
    'wanshouji': '玩手机',
    'tiaoyue': '跳跃',
    'shangdianti': '上电梯',
    'xiadianti': '下电梯',
    'shanglouti': '上楼梯',
    'xialouti': '下楼梯',
    'zoulu': '走路',
    'zuoxia': '坐下',
    'zhanqi': '站起',
    'test': '测试',
    'qita': '其他'
}
acts_code = {
    8: '玩手机',
    7: '跳跃',
    5: '上电梯',
    6: '下电梯',
    3: '上楼梯',
    4: '下楼梯',
    2: '走路',
    1: '坐下',
    0: '站起',
    -1: '其他'
}
acts_dict_inverts = {0: 'zhanqi', 1: 'zuoxia', 2: 'zoulu', 3: 'shanglouti', 4: 'xialouti', 5: 'shangdianti',
                     6: 'xiadianti', 7: 'tiaoyue', 8: 'wanshouji', -1: 'qita'}

form = cgi.FieldStorage()

max1 = float(form.getvalue('max1'))
max2 = float(form.getvalue('max2'))
max3 = float(form.getvalue('max3'))
min1 = float(form.getvalue('min1'))
min2 = float(form.getvalue('min2'))
min3 = float(form.getvalue('min3'))
mean1 = float(form.getvalue('mean1'))
mean2 = float(form.getvalue('mean2'))
mean3 = float(form.getvalue('mean3'))
std1 = float(form.getvalue('std1'))
std2 = float(form.getvalue('std2'))
std3 = float(form.getvalue('std3'))
IQR1 = float(form.getvalue('IQR1'))
IQR2 = float(form.getvalue('IQR2'))
IQR3 = float(form.getvalue('IQR3'))
fival1 = float(form.getvalue('fival1'))
fival2 = float(form.getvalue('fival2'))
fival3 = float(form.getvalue('fival3'))
iqr_s = float(form.getvalue('iqr_s'))
guid = form.getvalue('guid')

# 2s窗口
y, x = svm_read_problem('..//2s.txt')
matrix1 = [{1: max1, 2: min1, 3: mean1, 4: std1, 5: fival1, 6: IQR1}]
model1 = svm_train(y, x)
p_label2, p_acc2, p_val2 = svm_predict([-1], matrix1, model1)

# 4s窗口
y, x = svm_read_problem('..//4s.txt')
matrix2 = [{1: max2, 2: min2, 3: mean2, 4: std2, 5: fival2, 6: IQR2}]
model2 = svm_train(y, x)
p_label4, p_acc4, p_val4 = svm_predict([-1], matrix2, model2)

# 6s窗口
y, x = svm_read_problem('..//6s.txt')
matrix3 = [{1: max3, 2: min3, 3: mean3, 4: std3, 5: fival3, 6: IQR3, 7: iqr_s}]
model3 = svm_train(y, x)
p_label6, p_acc6, p_val6 = svm_predict([-1], matrix3, model3)

act = -1
if p_label6[0] != -1:
    act = int(p_label6[0])
if p_label4[0] != -1:
    act = int(p_label4[0])
if p_label2[0] != -1:
    act = int(p_label2[0])
print "Content-type:text/html"
print
print(act)

t1 = time.strftime('%Y-%m-%d %H:%M:%S')

with open('..//act_data//' + guid + '.txt', 'a+') as f:
    f.write(
        t1 + ' ' + acts_code[act] + ' ' + str(max1) + ' ' + str(min1) + ' ' + str(mean1) + ' ' + str(std1) + ' ' + str(
            fival1) + ' ' + str(
            IQR1) + ' ' + str(max2) + ' ' + str(min2) + ' ' + str(mean2) + ' ' + str(std2) + ' ' + str(
            fival2) + ' ' + str(IQR2) + ' ' + str(max3) + ' ' + str(min3) + ' ' + str(mean3) + ' ' + str(
            std3) + ' ' + str(fival3) + ' ' + str(IQR3) + ' ' + str(iqr_s) + '\n')

