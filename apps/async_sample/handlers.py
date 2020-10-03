from typing import Optional, Awaitable

import tornado.web


class AsyncSampleHandlerFactory:
    @staticmethod
    def get_handlers():
        return [
            (r"/async/async_await", _AsyncAwaitHandler)
        ]


class _BaseAsyncSampleHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass


class _AsyncAwaitHandler(_BaseAsyncSampleHandler):
    async def get(self):
        import asyncio
        await asyncio.sleep(5)
        self.write('done!')
