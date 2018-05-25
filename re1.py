import requests  
import re 
import numpy as np 
  
html = requests.get('http://47.94.195.238/wap/index.htm')  
html.encoding = 'utf-8' #这一行是将编码转为utf-8否则中文会显示乱码。  

# goods = {"名称":"goods","现价":0,"销量":0}
name = re.findall('<p style="font-size:12px">(.*?)</p>',html.text,re.S)
price = re.findall('现价:</span><font color="#FF0000" style="font-weight:bold">¥(.*?)</font>',html.text,re.S)
sales = re.findall('销量:<font color="#FF0000">(.*?)</font>件',html.text,re.S)  #通过正则表达抓取网页的内容

name = np.array(name).reshape(int(len(name)),1)
price = np.array(price).reshape(int(len(price)),1)
sales = np.array(sales).reshape(int(len(price)),1)#对获得的数据整型
sum = np.c_[name,price,sales] #合并这三个数组 方便之后往字典中添加数据
list = []

for i in range(213):
	# goods["名称"] = sum[i][0]
	# goods["现价"] = sum[i][1]
	# goods["销量"] = sum[i][2]
	goods = dict(名称=sum[i][0],现价=sum[i][1],销量 = sum[i][2]) #将其加入字典中
	list.append(goods) #追加到list列表中
for each in list: 
	print(each)
