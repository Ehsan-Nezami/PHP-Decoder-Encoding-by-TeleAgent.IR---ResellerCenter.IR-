'''
    File name: PHP Decoder "Encoding by TeleAgent.IR - ResellerCenter.IR".py
    Author: Ehsan Nezami
    Date created: 19/11/2018
    Web: http://nezami.me/
    Python Version: 2.7
'''

import os
import re
import base64
import zlib

def listFiles(path, extension):
    return [f for f in os.listdir(path) if f.endswith(extension)]

path_name = raw_input("What is your path of php files? \n Example : C:\\files\\ \n ")
for files in listFiles(path_name, '.php'):
	print files
		
	start = '$_QXXCZD("'
	end = '"));'
	
	f=open(files,'r')
	for input in f.readlines():
		data= re.findall(re.escape(start)+"(.*)"+re.escape(end),input)
		for x in data:
			x=base64.b64decode(x)
	
			start1 = '.$_ZUI("'
			end1 = '"));'
			data1= re.findall(re.escape(start1)+"(.*)"+re.escape(end1),x)
			for x1 in data1:
				x1=base64.b64decode(x1)
				start2 = '$_IRRGRHMF("'
				end2 = '"));'
				data2= re.findall(re.escape(start2)+"(.*)"+re.escape(end2),x1)
	
				for x2 in data2:
					x2=base64.b64decode(x2)
					start3 = '$_EFTYPYA("'
					end3 = '"));'
					data3= re.findall(re.escape(start3)+"(.*)"+re.escape(end3),x2)
	
					for x3 in data3:
						x3=base64.b64decode(x3)
						start4 = '$_AOKDOJCRH("'
						end4 = '"));'
						data4= re.findall(re.escape(start4)+"(.*)"+re.escape(end4),x3)
	
						for x4 in data4:
							x4=base64.b64decode(x4)
	
							start5 = '$_NZHLDCOUMASYWHUKYETFVEDDJELK("'
							end5 = '")));'
							data5= re.findall(re.escape(start5)+"(.*)"+re.escape(end5),x4)
							for x5 in data5:
								compressed = base64.b64decode(x5)
								decoded=zlib.decompress(compressed, -15)
								print decoded
								output=file('dec-'+files,'a')
								output.write(decoded)