# -*- coding: utf-8 -*-

import os
import sys

# 主函数
def main():
	# 设置读取文件的路径
    path = sys.argv[1]
    # 处理类型 web, android, ios
    handleType = sys.argv[2]
    # 遍历该文件夹所有文件
    for file in os.listdir(path):
    	if handleType == 'android':
    		# 安卓，移除
    		androidFolder = path + '/android'
    		if not os.path.exists(androidFolder):
    			os.makedirs(androidFolder)
    			
        	if file.find('@2x') > -1:
        		newName = file.replace(' ', '-').replace('(', '-').replace(')', '').replace('℃','').replace('（','-').replace('）','').replace('--','-').replace('-','_').replace('@2x','')
       			os.rename(os.path.join(path,file),os.path.join(androidFolder, newName))
     	else:
     		if file.find('png') > -1 or file.find('svg') > -1:
       		# 网页 / 苹果  
		        newName = file.replace(' ', '-').replace('(', '-').replace(')', '').replace('℃','').replace('（','-').replace('）','').replace('--','-')
		        os.rename(os.path.join(path,file),os.path.join(path, newName))


if __name__ == "__main__":
    main()


