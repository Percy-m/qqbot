from graia.ariadne.app import Ariadne
from graia.ariadne.model import Group
from graia.ariadne.model import Friend
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.saya import Channel
from graia.ariadne.message.element import At, Plain

from graia.ariadne.message.parser.base import ContainKeyword, DetectPrefix
from .util.citykw import ContainCityKW, resolve

from typing import Annotated

# from graia.broadcas
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()

# @channel.use(ListenerSchema(listening_events=[GroupMessage],
#                             decorators=[ContainKeyword(keyword="上海"),
#                                         ContainKeyword(keyword="香港")]))
# async def keywords_contain(app: Ariadne, event: GroupMessage, message: MessageChain):
#     print("HERE")
#     print(event)
#     print(message)
#     # print(decorator)
#     await app.send_group_message(event.sender.group.id, MessageChain("上海不行"))
    # source = event.source
    # await app.send_group_message(event.sender.group.id, MessageChain(At(target=event.sender.id), Plain(" HELLO")), quote=source)


@channel.use(
    ListenerSchema(listening_events=[GroupMessage])
)
async def catch_keywords(app: Ariadne, group: Group, message: Annotated[MessageChain, ContainCityKW()]):
    
    namelist = resolve(message)
    url = ''
    await app.send_group_message(group.id, MessageChain(namelist))