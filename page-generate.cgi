#!/usr/bin/python

#classes
import os
import sys
import cgi
import gzip
import StringIO
print "Content-type: text/html\r\n"
tpl_header=open("header.html", "r")
tpl_plugin=open("plugin-list.html", "r")
tpl_footer=open("footer.html", "r")
tpl_complete=open("complete.html", "w")
tpl_header_lite=open("header_lite.html", "r")
tpl_footer_lite=open("footer_lite.html", "r")
tpl_index =open("index.html", "w")

tpl_index.write(tpl_header_lite.read())
tpl_index.write(tpl_footer_lite.read())

tpl_complete.write(tpl_header.read())
tpl_complete.write(tpl_plugin.read())
tpl_complete.write(tpl_footer.read())


tpl_header.close
tpl_header_lite.close
tpl_plugin.close
tpl_footer.close
tpl_footer_lite.close
tpl_index.close
tpl_complete.close