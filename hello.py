#!/usr/bin/env python3
import os
import cgi
import cgitb
import json
import templates

cgitb.enable()
print("Content-type: text/html")
print()

form = cgi.FieldStorage()
