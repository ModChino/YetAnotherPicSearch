from typing import Optional

from nonebot import get_driver
from nonebot.config import BaseConfig


class Config(BaseConfig):

    # 私聊发送图片立即搜图，否则需要先发送搜图命令
    search_immediately = True
    # 隐藏所有搜索结果的缩略图
    hide_img: bool = False
    # saucenao 得到低相似度结果时隐藏结果缩略图（包括 ascii2d 和 whatanime）
    hide_img_when_low_acc: bool = False
    # whatanime 得到 R18 结果时隐藏结果缩略图
    hide_img_when_whatanime_r18: bool = False
    # saucenao 相似度低于这个百分比将被认定为相似度过低
    saucenao_low_acc: int = 60
    # 是否在 saucenao 相似度过低时自动使用 ascii2d
    use_ascii2d_when_low_acc: bool = True
    # 若结果消息有多条，采用合并转发方式发送搜图结果
    forward_search_result: bool = True
    # 大部分请求所使用的代理: http(s)://
    proxy: Optional[str] = None
    # 搜图结果缓存过期时间（天）
    cache_expire: int = 7
    # saucenao APIKEY，必填，否则无法使用 saucenao 搜图
    saucenao_api_key: str = ""
    # exhentai cookies，选填，没有的情况下自动改用 e-hentai 搜图
    exhentai_cookies: str = ""

    class Config:
        extra = "ignore"


config = Config(**get_driver().config.dict())
