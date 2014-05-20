#!/bin/env python
###
###
###
Author = 'Adam Grigolato'
Version = '0'
###
###
# IMPORTS #
from dulwich.repo import Repo
from dulwich.server import DictBackend, TGitServer
import threading




repo = Repo.init("remote", mkdir=True)
cid = repo.do_commit("message", commiter="test <test@test>")
backend = DictBackend({'/': repo})
dul_server = TCPGitServer(backend, 'localhost', 0)
threading.Thread(target=dul_Server.serve).start()
server_address, server_port = dul_server.socket.getsockname()

