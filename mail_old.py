#!usr/bin/env/python
# --*--codding:utf-8--*--

import re
import sys
from email.parser import Parser
import email

if __name__ == '__main__':

    # print sys.argv[1:]
    path = sys.argv[1]
    # print path
    headers = Parser().parse(open(path, "r"))
    print "From: %s" % headers["From"]
    print "To: %s" % headers["To"]
    print "Subject: %s" % headers["Subject"]

    msg = email.message_from_file(open(path, "r"))
    # print msg
    if msg.is_multipart():
        for payload in msg.get_payload():
            print payload.get_payload()
    else:
        print msg.get_payload()

