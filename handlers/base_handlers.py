from typing import Optional, Awaitable
import datetime

import tornado.web


class _BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass


class HomeHandler(_BaseHandler):
    def get(self):
        self.redirect('/ping')


class PingHandler(_BaseHandler):
    def get(self):
        self.write({'isAlive': True, 'now': str(datetime.datetime.utcnow())})
