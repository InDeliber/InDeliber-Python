import wxpy


bot = wxpy.Bot(cache_path=True, console_qr=True)
# 消息处理
"""
消息处理——每当机器人接收到消息时，会自动执行以下两个步骤
    将消息保存到 Bot.messages 中
    查找消息预先注册的函数，并执行(若有匹配的函数)
"""

# 消息对象
"""
消息对象——消息对象代表每一条从微信获取到的消息
"""

while True:
    print(bot.messages)