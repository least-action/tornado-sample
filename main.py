import tornado.ioloop
import tornado.web
import logging
import json

from handlers.base_handlers import HomeHandler, PingHandler


def make_app():
    handlers = [
        (r"/", HomeHandler),
        (r"/ping", PingHandler)
    ]

    return tornado.web.Application(handlers=handlers)


if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)

    try:
        app = make_app()
        app.listen(config['port'])
        tornado.ioloop.IOLoop.current().start()
        logging.info('server started - listening {port} port'.format(port=config['port']))
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logging.error(e)
    finally:
        logging.info('server stopped.')
