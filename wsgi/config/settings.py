#!/usr/bin/env python
# coding: utf-8
import web

render = web.template.render('templates/', cache=False)

web.config.debug = False

consumer_key = "A3Di73EDiyHM8u2IyxHLw"
consumer_secret = "pSSGT09FSR3ONawurMbEp5CLPeiptNs8XFwBxprEMI"

#for j.mp link
no_jmp = False 
bitly_name = ''
bitly_key = ''

