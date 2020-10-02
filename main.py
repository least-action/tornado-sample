import tornado.ioloop
import tornado.web
import logging
import time
import json

from handlers.base_handlers import HomeHandler, PingHandler
from apps.tornado_docs.handlers import WebFrameworkHandlerFactory


def make_app():
    base_handlers = [
        (r"/", HomeHandler),
        (r"/ping", PingHandler)
    ]

    handlers = base_handlers
    # handlers.append(WebFrameworkHandlerFactory.get_handlers())

    return tornado.web.Application(handlers=handlers)


if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)

    logger = logging.getLogger()
    logging.addLevelName(1, 'TRACE')
    logging.trace = lambda msg: logging.log(1, msg)
    level = getattr(logging, config['logging']['level'].upper())
    logging.Formatter.converter = time.gmtime
    logging.basicConfig(format='[%(asctime)s] %(levelname)-5s: %(message)s',
                        datefmt='%Y-%m-%dT%H:%M:%SZ',
                        level=level)

    try:
        app = make_app()
        app.listen(config['port'])
        logging.info('server started with port {port}'.format(port=config['port']))
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logging.error(e)
    finally:
        logging.info('server stopped.')
