from graia.ariadne.app import Ariadne
from graia.ariadne.model import Group
from graia.ariadne.model import Friend
from graia.ariadne.event.mirai import NudgeEvent
from graia.ariadne.message.chain import MessageChain
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[NudgeEvent]))
async def getup(app: Ariadne, event: NudgeEvent):
    print("HEllO")
    # print(group.id)
    print(event.type)
    print(event)
    print(event.target)
    print(type(event.target))
    if event.target != 3161049483:
        return
    subject = event.subject
    if isinstance(subject, Group):
        await app.send_group_message(subject.id, MessageChain("你不要光天化日之下在这里戳我啊"))
    elif isinstance(subject, Friend):
        await app.send_friend_message(subject.id, MessageChain("别戳我，好痒!"))
    else:
        return
    # if event.type == "group":
        
        # await app.send_group_message(group.id, MessageChain("你不要光天化日之下在这里戳我啊"))
    # if event.context_type == "group" and event.group_id is not None:
    #     await app.send_group_message(event.group_id, MessageChain("你不要光天化日之下在这里戳我啊"))
    # elif event.context_type == "friend" and event.friend_id is not None:
    #     await app.send_friend_message(event.friend_id, MessageChain("别戳我，好痒！"))