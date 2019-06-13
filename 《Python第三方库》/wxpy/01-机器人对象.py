import wxpy

bot = wxpy.Bot(cache_path=True ,console_qr=1)

# Bot.self, 把自己作为一个聊天对象
# bot.self.add()
# bot.self.send('你好')
# bot.self.accept()
# bot.self.send('傻屌')

# ===== 2
# Bot.file_helper, 文件传输助手

# my_firend = bot.friends().search('Burgundy')[0]
# bot.file_helper.send_image('d://english-house.png')

# ===== 3 Bot.friends() 获取所有好友
# print('=' * 30 + '所有好友' + '=' * 30)
# friends = bot.friends(update=True)
# for friend in friends:
#     print(friend)

# ===== 4 Bot.groups() 获取所有群聊
# print('=' * 30 + '所有群聊' + '=' * 30)
# groups = bot.groups(update=True)
# for group in groups:
#     print(group)

# ===== 5 Bot.mps() 获取所有公众号
# print('=' * 30 + '所有公众号' + '=' * 30)
# mps = bot.mps(update=True)
# for mp in mps:
#     print(mp)

# ===== 6 Bot.chats() 获取所有聊天对象（包括，好友、群聊、公众号）
# print('=' * 30 + '聊天窗口' + '=' * 30)
# chats = bot.chats()
# for chat in chats:
#     print(chat)

# ========== 搜索聊天对象
# ===== 7 聊天对象.search() 获得搜索结果，均为列表  (Bot.search()，搜索任何聊天对象)

# ===== 8 聊天对象.ensure_one() 希望获得唯一结果    
#         确保搜索结果是唯一的，并取出唯一结果


# ===== 9 创建一个新的群聊
# print('=' * 100)
# friend1 = bot.friends().search('Burgundy')[0]
# print(friend1)
# print(bot.user_details(friend1))
# friend2 = bot.friends().search('凤英')[0]
# print(friend2)
# print(bot.user_details(friend2))
# test_group = bot.create_group([friend1, friend2], topic='测试群')
# print(test_group)
# test_group.send('Hello, Wechat')

# firends = bot.groups().search('测试群', friend1)
# print(firends)

# ===== 10 获得详细信息
# firends = bot.friends()
# for firend in firends:
#     print(bot.user_details(firend))
# @bot.register()
# def print_others(msg):
#     print(msg)

# @bot.register(my_firend)
# def reply_my_friend(msg):
#     return 'received:{}({})'.format(msg.text, msg.type)

# @bot.accept_friend()
# wxpy.embed()


