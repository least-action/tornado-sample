from typing import Optional, Awaitable

import tornado.web
import logging


class AsyncSampleHandlerFactory:
    @staticmethod
    def get_handlers():
        return [
            (r"/async/async_await", _AsyncAwaitHandler),
            (r"/async/non_async", _NonAsyncHandler)
        ]


class _BaseAsyncSampleHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass


class _AsyncAwaitHandler(_BaseAsyncSampleHandler):
    async def get(self):
        logging.info('received req')
        import asyncio
        await asyncio.sleep(5)
        self.write('done!')


class _NonAsyncHandler(_BaseAsyncSampleHandler):
    def get(self):
        self.write('done!')
