# 今天是学习python的第7天，今天主要学习第六章，第七章，第八章
# 6.3.4 遍历字典中的所有值
favorite_language = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
print("The following languages have been mentioned:")
for language in favorite_language.values():
    print(language.title())
    # 使用values 或者 keys 可以返回一个只包含值或者键的列表
for key in favorite_language.keys():
    print(key.title())
for language in set(favorite_language.values()):  # 通过对重复元素调用set()，可以让python找出列表中独一无二的元素，并使用这些元素来创建一个集合
    print(language.title())
people_investigated = {'A', 'B', 'C', 'D'}
people_needed = {'A', 'B', 'C', 'D', 'E', 'H'}
for value in people_needed:
    if value not in people_investigated:
        print(value.title() + " 请参与调查！")
    else:
        print(value.title() + " 谢谢您参与调查！")
# 6.4 嵌套
# 6.4.1 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# 现实情况，创建多个外星人
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 显示前5个外星人
for alien in aliens:
    print(alien)
print("...")
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))
# 操作
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# 显示前五个外星人
# 显示前5个外星人
for alien in aliens[0:5]:
    print(alien)
print("...")
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n " + name.title() + "'s favorite languages are :")
    for language in languages:
        print("\t " + language.title())
# 7 用户输入和while循环
# message = input("Tell me something ,and I will repeat it back to you:　")
# print(message)
# 7.1.2 使用 int()来获得数值输入
age = input("How old are you? ")
print(int(age) >= 18)  # input 获得的数字 其实是字符
# 7.2.1 使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# 让用户选择何时退出
prompt = "\nTell me something , and I will repeat it back to you:"
prompt += "Enter 'quit ' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# 7.3.1 在列表之间移动元素
#首先，创建一个待验证的用户列表
#   和一个用于存储已验证用户的空列表
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]

#验证每个用户，直到没有用户可以验证为止
#   将每个验证的用户都移到已验证用户列表中
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("Verifying user :"+current_user.title())
    confirmed_users.append(current_user)

#显示已经验证过的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
