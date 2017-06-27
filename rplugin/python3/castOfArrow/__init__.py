# -*- coding: utf-8 -*-

import neovim
import time
import random
from requests.exceptions import ConnectionError

@neovim.plugin
class castOfArrow(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command("CastSatanha")
    def castSatanha(self):
        satanha = ["hjklキー使えってこと!?師匠なのに!","こんな方向キー使う奴野放しにしてるなんて天界どうかしてるっ!!","矢印キーで移動するようとするなんて・・・悪っ!!", "どう!?矢印キーなんて最高に悪魔的な行為でしょっ!!", "矢印キーの形態はすべて掌握しているわ それもすべて・・・","上矢印とかkってなに!?"]
        self.nvim.command("echo " + random.choice(satanha))
