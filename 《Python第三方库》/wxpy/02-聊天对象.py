# ============================================================================================ 聊天对象
# burgundy = bot.friends().search('Burgundy')[0]
# print(burgundy)

# ============ 发送消息、图片（注意图片大小）、文件
# burgundy.send('================测试开始=================')
# burgundy.send('@img@yu.jpg')
# burgundy.send('图片传输成功')
# burgundy.send('@img@yu.gif')
# burgundy.send('图片传输成功')
# burgundy.send_image('D://yu.jpg')
# burgundy.send('图片传输成功')
# burgundy.send_image("D://yu.gif")
# burgundy.send('图片传输成功')
# burgundy.send_file("D://wxpy.rar")
# burgundy.send('文件传输成功')

#  ============================================================================================ 各种不同类型聊天对象的继承关系
"""
基础类
    基本聊天对象 Chat
        所有的聊天对象均继承于此类型
        拥有 微信ID、昵称 等属性
        拥有 发送消息 Chat.send(), 获取头像 Chat.get_avatar() 等方法
        单个用户 (User) 和群聊 (Group) 的基础类
    单个聊天对象 User
        继承于 Chat，表示个体聊天对象 (而非群聊)。
        拥有 性别、省份、城市、是否为好友 等属性
        拥有 加为好友 User.add(), 接受为好友 User.accept() 等方法
        好友(Friend)、群聊成员(Member)，和公众号(MP) 的基础类
        被以下聊天对象所继承
            好友对象 Friend
            群成员对象 Member
            公众号对象 MP
实际类
    好友 Friend
    群聊 Group
    群成员 Member
    公众号 MP
"""
# ====================================== User 单个聊天对象：好友、群成员、公众号
# burgundy = bot.friends(update=True).search('Burgundy')[0]
# 获得备注名称
# print(burgundy.remark_name)
# 设置备注名称
# burgundy.set_remark_name('傻屌')
# print(burgundy.remark_name)

# 性别：男 = 1；女 = 2
# def getSex(user):
#     if user.sex == 1:
#         print('男性')
#     else:
#         print('女性')
# getSex(burgundy)

# 省份 + 城市 + 个性签名
# print('省份：' + burgundy.province)
# print('城市：' + burgundy.city)
# print('个性签名：' + burgundy.signature)

# 是否为好友
# 若为好友关系，返回对应的好友，否则返回 False
# print(burgundy.is_friend)
# liuChen = bot.groups().search('CrossFit')[0]
# print(liuChen)
# groupMember = liuChen.search('私房')[0]
# print(groupMember)
# print(groupMember.is_friend)

# 把当前用户加为好友
# 参数:	verify_content – 验证信息(文本)
# add(verify_content='')

# accept(verify_content='')[源代码]
# 接受当前用户为好友
# 参数:	verify_content – 验证信息(文本)
# 返回:	新的好友对象
# 返回类型:	wxpy.Friend

# ====================================== 继承与 User的 Friend对象

# ====================================== 继承与 User的 Group对象
# 获得群成员列表
# liuchen = bot.groups().search('Cross')[0]
# for member in liuchen:
#     print(member)
# print('总计会员个数为：' + str(len(liuchen)))

# 返回群主对象
# owner = liuchen.owner
# print(owner)
# print(owner.name)
# print(owner.remark_name)
# print(owner.is_friend)
# print(owner.signature)

# 判断自己在本群中是否为管理员
# print(liuchen.is_owner)

# 找到自己
# print(liuchen.self)

# 更新群信息
# liuchen.update_group()

# add_members(users, use_invitation=False)[源代码]
# 向群聊中加入用户

# 参数:	
# users – 待加入的用户列表或单个用户
# use_invitation – 使用发送邀请的方式
# remove_members(members)[源代码]
# 从群聊中移除用户

# 参数:	members – 待移除的用户列表或单个用户
# rename_group(name)[源代码]
# 修改群聊名称

# 参数:	name – 新的名称，超长部分会被截断 (最长32字节)

# ====================================== 继承与 User的 Member 群成员对象
# display_name
# 在群聊中的显示昵称
# 大囍子 = bot.groups().search('Cross')[0].search('大囍子')[0]
# print(大囍子)
# print(大囍子.display_name)
# print(大囍子.name)
# print(大囍子.is_friend)
# print(大囍子.remark_name)
# print(大囍子.province)
# print(大囍子.city)
# print(大囍子.signature)
# 大囍子 = 大囍子.is_friend
# print(大囍子.remark_name)
# print(大囍子.province)
# print(大囍子.city)
# print(大囍子.signature)

# remove()[源代码]
# 从群聊中移除该成员

# name
# 该群成员的友好名称
# 具体为: 从 群聊显示名称、昵称(或群名称)，或微信号中，按序选取第一个可用的

# ====================================== 继承与 User的 MP 公众号对象

# ====================================== 聊天对象合集
# 好友、公众号、群聊成员的合集

# stats() 与 stats_text()，可用来统计好友或群成员的性别和地区分布:
# print(bot.friends().stats())
# print(bot.friends().stats_text())

liuchen = bot.groups().search('CrossFit')[0]
liuchen.update_group()
members = liuchen.members
print(members.stats_text())