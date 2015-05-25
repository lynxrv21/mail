#!usr/bin/env/python
# --*--codding:utf-8--*--

import re
import sys
from email.parser import Parser
from email.utils import parseaddr
from email import message_from_file

if __name__ == '__main__':

    # print sys.argv[1:]
    try:
        path = sys.argv[1]
        # print path
        try:
            msg = message_from_file(open(path, "r"))
            # print msg
            if msg.is_multipart():
                for payload in msg.get_payload():
                    print payload.get_payload()
            else:
                print msg.get_payload()

            headers = Parser().parse(open(path, "r"))

            if not headers["Subject"] & headers["From"] & headers["To"] :
                print "not"
            else:
                print "is"

            From = parseaddr(headers["From"])
            print "From: %s" % From[1]
            print "To: %s" % headers["To"]
            print "Subject: %s" % headers["Subject"]



        except IOError:
            print "Error: file or path not found"
    except IndexError:
        print "Error: please, enter message file path"

        # r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$'
        # \s?[A-Z0-9_-+%]+@[A-Z0-9_-+%]+\.[A-Z0-9]\s?