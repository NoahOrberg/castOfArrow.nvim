# -*- coding: utf-8 -*-

import neovim
import time
from requests.exceptions import ConnectionError

@neovim.plugin
class castOfArrow(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command("CastSatanha")
    def castSatanha(self):
        self.nvim.command("echo 'AAAA'")
