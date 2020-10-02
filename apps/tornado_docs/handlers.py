from typing import Optional, Awaitable

import tornado.web


class WebFrameworkHandlerFactory:
    @staticmethod
    def get_handlers():
        handlers = [
            (r"/tutorials/webframework($|\/.*)", _WebFrameworkHandler)
        ]

        return handlers


class _BaseWebFrameworkHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass


class _WebFrameworkHandler(_BaseWebFrameworkHandler):
    def get(self):
        self.write('web framework')
