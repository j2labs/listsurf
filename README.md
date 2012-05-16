# List Surf

This is a simple project designed to demonstrate building websites with [Brubeck](http://brubeck.io).

Assuming you've already installed Brubeck you can turn on listsurf by checking out the repo, turning on MongoDB and typing `./listsurf.py`.

That looks like this.

    $ mongod
    $ git clone https://github.com/j2labs/listsurf.git
    $ cd listsurf
    $ ./listsurf.py


# The Code

I have attempted to document the code clearly and hope you find it readable.

In `listsurf.py` you will find two main groups of logic: the URL map and Brubeck's config.

The URL map (aka `handler_tuples`) looks like this.

    handler_tuples = [
        (r'^/login', AccountLoginHandler),
        (r'^/logout', AccountLogoutHandler),
        (r'^/create', AccountCreateHandler),
        (r'^/add_item', ListAddHandler),
        (r'^/api', APIListDisplayHandler),
        (r'^/$', ListDisplayHandler),
    ]

So we see login/logout urls, a url for creating an account, a url for adding an item, an api url (provides a JSON feed) and finally the main url ('/') is an item list.

The next are of concern is the Brubeck config. The name of the values should speak for themselves so I will just copy the config here.

    config = {
        'msg_conn': Mongrel2Connection('tcp://127.0.0.1:9999','tcp://127.0.0.1:9998'),
        'handler_tuples': handler_tuples,
        'template_loader': load_jinja2_env('./templates'),
        'db_conn': db_conn,
        'login_url': '/login',
        'cookie_secret': 'OMGSOOOOOSECRET',
        'log_level': logging.DEBUG,
    }


# Screens

Not a particularly exciting design, but gets the job done. And hey, the design elements are big!

## Login screen

![Login screen](/j2labs/listsurf/raw/master/media/screens/login_window.png)

## Create account

![Create account](/j2labs/listsurf/raw/master/media/screens/create_account.png)

## List of links

![List of links](/j2labs/listsurf/raw/master/media/screens/list_of_links.png)

## Adding a link

![Adding a link](/j2labs/listsurf/raw/master/media/screens/adding_link.png)

## Bookmarklet

![Bookmarklet](/j2labs/listsurf/raw/master/media/screens/bookmarklet.png)

## JSON API

![JSON API](/j2labs/listsurf/raw/master/media/screens/api_output.png)

