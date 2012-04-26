#!/usr/bin/env python
#coding:utf-8

import web
from config import settings

urls = ('/','501fun_t_api.twitterapi.ttcbk.index',
    '/auth','501fun_t_api.twitterapi.ttauth.auth',
    '/api/(.*)','501fun_t_api.twitterapi.ttapi.api',
)

app = web.application(urls, globals())
application = app.wsgifunc()
if __name__=="__main__":
#    app.run()
    pass

