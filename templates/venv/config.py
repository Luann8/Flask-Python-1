import os, random, string

class Config(object):
    CSRF_ENABLE = True
    SECRET = 'dd8595450878f87b401cb93ccd6dedd2e73e6c62f95acfc256da5fa6e496f912'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    
class DevelopmentConfig(config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http:/;%s/%s' % (IP_HOST, PORT_HOST)
    
app_config = {
    'development': DevelopmentConfig(),
    'testing:' : None,
    'production': None

}

app_active = os.getenv('FLASK_ENV')

if app_config is None:
    app_config = 'development'