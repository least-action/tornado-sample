import tornado.ioloop
import tornado.web
import logging
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


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
