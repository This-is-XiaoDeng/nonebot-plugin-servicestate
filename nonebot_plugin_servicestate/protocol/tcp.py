from __future__ import annotations

from typing import Union, Dict

from .protocol import BaseProtocol, BaseProtocolData

from nonebot.log import logger
import asyncio


class TCPPRotocolData(BaseProtocolData):
    port: int = 80


class TCP_Protocol(BaseProtocol):
    _PROTOCOL_NAME = "TCP"
    _DATA_MODEL = TCPPRotocolData

    async def detect(self) -> bool:
        connect_func = asyncio.open_connection(self.host, self.port)
        try:
            await asyncio.wait_for(connect_func, self.timeout)
            logger.debug(f"TCP -> {self.host}:{self.port} OK")
            return True
        except:
            logger.debug(f"TCP -> {self.host}:{self.port} FAIL")
            return False
