# 
from typing import Optional

from graia.ariadne.message.parser.base import ChainDecorator
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain

from graia.broadcast.exceptions import ExecutionStop

from loguru import logger

import psycopg2 as pg

from modules.constant.database import DATABASE, USER, PASSWORD, HOST

class ContainCityKW(ChainDecorator):
    """检测是否有中国城市关键词"""

    def __init__(self) -> None:
        self.list = []
        with pg.connect(database=DATABASE,
                  user=USER,
                  password=PASSWORD,
                  host=HOST) as conn:
            cursor = conn.cursor()
            cursor.execute("select name from city")
            result = cursor.fetchall()
            for item in result:
                self.list.append(item[0])
        self.kwds = ""
            # self.keyword = ''
        
    async def __call__(self, chain: MessageChain, _) -> Optional[MessageChain]:
        # logger.info("Check City Keywords")
        self.kwds = ""
        flag = 0
        for keyword in self.list:
            if keyword in chain:
                if flag:
                    self.kwds += f",{keyword}"
                else:
                    flag = 1
                    self.kwds += keyword
        if self.kwds == "":
            raise ExecutionStop
        chain.append(self.kwds)
        return chain
    

def resolve(chain: MessageChain) -> list[str]:
    """用于解析城市"""
    print("HERE")
    s = chain.get(Plain)
    return s[-1].display.split(",")