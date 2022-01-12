import random

from hoshino import Service, priv
from nonebot import MessageSegment

sv = Service('mute', manage_priv=priv.SUPERUSER, enable_on_default=True, visible=False)

@sv.on_fullmatch('烟我')
async def mute(bot, event):
    gid = event.group_id
    uid = event['user_id']
    try:
        ban = random.randint(1,3600)
        notice = '你的' + str(ban) + '秒套餐来啦'
        await bot.set_group_ban(group_id=gid, user_id=uid, duration=ban)
        await bot.send(event, notice)
    except Exception as ex:
        sv.logger.error(ex)
        await bot.send(event, '禁言...禁言它失败了')