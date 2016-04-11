#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import cgi

print 'Content-type: text/html\r\n\r'
print '''
<html>
<head><title> Status Updated! </title></head>
<body bgcolor="#333333" text="white">
	<form action="../dashboard.html" method="POST">
		<input type="submit" value="Back to Dashboard">
	</form>
'''

form = cgi.FieldStorage()
status = form.getfirst("status", "").upper()

if "status" in form:
	inputStatus = form["status"].value

	sysIn = "echo "+inputStatus+" >> status.txt "
	os.system(sysIn)

print '''
</body>
</html>
'''
