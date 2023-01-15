print("今天是学习python 的第七天")
#昨天学习了
print("我昨天学习了 if 语句 包括 布尔类型 什么东西是否在列表中等")
print("今天要学习，字典 while语句")
#第六章 字典
alien_0={'color':'green'}#一堆键值之间用冒号分隔
print(alien_0['color'])
#对字典添加值
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)
#修改字典中的值
alien_0={'color':'green'}
print("The alien is "+alien_0['color']+".")

alien_0['color']='yellow'
print("The alien is "+alien_0['color']+".")
alien_0={'x_position': 0,'y_position':25,'speed':'fast'}
print("Original x-position: "+str(alien_0['x_position']))
#向右移动外星人
#根据外星人的速度决定将其运动多远
if alien_0['speed']=='slow':
    x_increment =1
elif alien_0['speed'] =='medium':
    x_increment =2
else:
    #这个外星人的速度一定很快
    x_increment=3
#新位置 = 老位置 + 增量
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x-position: "+str(alien_0['x_position']))
# 删除 键-值 对 
alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)
#P 6-1
old_people={'first_name':'Nokyhan','last_name':'Nokyhan','age':20,'city':'LYG'}
print(old_people)
for key,value in old_people.items():# key 和value 一对值，用来存储键-值
    print("\nKey :"+ key)
    print("Value :"+ str(value) )
