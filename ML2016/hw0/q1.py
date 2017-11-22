# 輸入hw0_data.dat，請將指定column由小排到大並印出來。
# column的index從0開始
# 輸出一行，以逗點分隔。ex: 0,0,1,2,3,4,5
# . / Q1.sh  3  file.dat(第一個是column的index，第二個是檔案)
# 	輸出檔名: ans1.txt
import sys
import numpy as np


FILENAME = sys.argv[2]
INDEX = int(sys.argv[1])

RAWDATA = np.genfromtxt(FILENAME, autostrip=True)
# print(readData[index])  
SORTED_DATA = np.sort(RAWDATA[INDEX])    # sort -> small to big
# add comma and convert list to string
OUTPUT = ','.join(str(e) for e in SORTED_DATA)
# -7.667,-5.19,-3.557,-0.394,-0.137,0.997,1.0,1.635,2.932,5.43,7.672
print(OUTPUT)

# np.savetxt('ans1.txt', sortData, newline=',', fmt='%.3f')
# np.savetxt('ans1.txt', sortData[np.newaxis], newline='', fmt='%.3f', header='', footer='', comments='')
np.savetxt('ans1.txt', [OUTPUT], fmt='%s')


