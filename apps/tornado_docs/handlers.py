from typing import Optional, Awaitable

import tornado.web


class WebFrameworkHandlerFactory:
    @staticmethod
    def get_handlers():
        return [
            (r"/tutorials/webframework", _WebFrameworkHandler),
            (r"/tutorials/webframework/initialize", _InitializeHandler, dict(init='initialized_value'))
        ]


class _BaseWebFrameworkHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass


class _WebFrameworkHandler(_BaseWebFrameworkHandler):
    def get(self):
        self.write('tutorial - web framework')


class _InitializeHandler(_BaseWebFrameworkHandler):
    def initialize(self, init):
        self.init = init

    def get(self):
        self.write(self.init)


