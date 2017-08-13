import time
import os
def main1():
    while True:
     wait=int(input('请输入你背每条歇后语的思考时间（秒数）'))
     print('快去背诵歇后语吧:')
     for key in word:
      print(key)
      time.sleep(wait)
     os.system('cls')
     lis=','.join(word)
     inp=input('请输入你刚才背的全部歇后语(两句之间用英文逗号分隔，按顺序来哦！)')
     if lis==inp:
      print('Bingo!')
     else:
      print('Ahoh!')
word = ['泥菩萨过河自身难保', '小葱拌豆腐一清二白', '隔着门缝看人把人看扁了']
while True:
 try:
  a=input('管理小斩斩，请输入密码（输exit退出）')
  if a=='admin':
   while True:
    try:
      s=input('请输入命令')
      if s=='exit':
           main1()
    except:
     print('输入错误，等待1秒')
  elif a=='exit':
    main1()
 except:
   print('输入错误，等待1秒')  
