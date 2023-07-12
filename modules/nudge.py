from graia.ariadne.app import Ariadne
from graia.ariadne.model import Group
from graia.ariadne.model import Friend
from graia.ariadne.event.mirai import NudgeEvent
from graia.ariadne.message.chain import MessageChain
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema


from loguru import logger
from .util.logstr import nudge_str

channel = Channel.current()

@channel.use(ListenerSchema(listening_events=[NudgeEvent]))
async def getup(app: Ariadne, event: NudgeEvent):
    logger.info(nudge_str(event))
    if event.target != app.account:
        return
    subject = event.subject
    if isinstance(subject, Group):
        await app.send_group_message(subject.id, MessageChain("你不要光天化日之下在这里戳我啊"))
    elif isinstance(subject, Friend):
        await app.send_friend_message(subject.id, MessageChain("别戳我，好痒!"))
    else:
        return
