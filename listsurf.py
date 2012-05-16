#!/usr/bin/env python


import logging

from brubeck.connections import Mongrel2Connection
from brubeck.request_handling import Brubeck
from brubeck.templating import load_jinja2_env

from handlers import (AccountLoginHandler,
                      AccountLogoutHandler,
                      AccountCreateHandler,
                      ListDisplayHandler,
                      ListAddHandler,
                      APIListDisplayHandler)

from queries import init_db_conn


###
### Configuration
###

# Instantiate database connection
db_conn = init_db_conn()

# Routing config
handler_tuples = [
    (r'^/login', AccountLoginHandler),
    (r'^/logout', AccountLogoutHandler),
    (r'^/create', AccountCreateHandler),
    (r'^/add_item', ListAddHandler),
    (r'^/api', APIListDisplayHandler),
    (r'^/$', ListDisplayHandler),
]

# Application config
config = {
    'msg_conn': Mongrel2Connection('tcp://127.0.0.1:9999','tcp://127.0.0.1:9998'),
    'handler_tuples': handler_tuples,
    'template_loader': load_jinja2_env('./templates'),
    'db_conn': db_conn,
    'login_url': '/login',
    'cookie_secret': 'OMGSOOOOOSECRET',
    'log_level': logging.DEBUG,
}


# Instantiate app instance
app = Brubeck(**config)
app.run()
