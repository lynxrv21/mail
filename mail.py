#!usr/bin/env/python
# --*--codding:utf-8--*--

import re
import sys
from email.parser import Parser
from email.utils import parseaddr
from email.utils import getaddresses
from email import message_from_file

if __name__ == '__main__':
    try:
        path = sys.argv[1]
        try:
            msg = message_from_file(open(path, "r"))
            # print msg
            if msg.is_multipart():
                print "Your file seems to be multipart message... I'd better skip it"
            else:
                Body = msg.get_payload()
                headers = Parser().parse(open(path, "r"))

                if not headers["Subject"] and headers["From"] and headers["To"] and Body:
                    print "! Error: check your file, noting to do here"
                else:
                    if not Body:
                        print "! Warning: no 'Body' field in your file"
                    elif not headers["From"]:
                        print "! Warning: no 'From' field in your file"
                    elif not headers["To"]:
                        print "! Warning: no 'To' field in your file"

                    raw_from = parseaddr(headers["From"])
                    raw_to = parseaddr(headers["To"])
                    raw_subject = parseaddr(headers["Subject"])
                    raw_cc = parseaddr(headers["Cc"])
                    raw_bcc = parseaddr(headers["Bcc"])
                    # print raw_from
                    # print raw_to
                    # print raw_subject
                    # print raw_cc

                    mail_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}")
                    url_pattern = re.compile(r"^(ht|f)tp(s?)\:\/\/[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*(:(0-9)*)*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?")

                    for item in headers["From"].split():
                        if re.match(mail_pattern, item):
                            print item

                    for item in headers["To"].split():
                        if re.match(mail_pattern, item):
                            print item

                    for item in headers["Subject"].split():
                        if re.match(mail_pattern, item):
                            print item

                    # for item in headers["Cc"].split():
                    #     if re.match(mail_pattern, item):
                    #         print item
                    #
                    # for item in headers["Bcc"].split():
                    #     if re.match(mail_pattern, item):
                    #         print item

                    Body_l = Body.split()
                    print "here goes body"
                    for item in Body_l:
                        if re.match(url_pattern, item):
                            print item

                        address = parseaddr(item)
                        if re.match(mail_pattern, address[1]):
                            print address[1]
                    # print "nei"
                    #
                    # print headers["Cc"].split()

        except IOError:
            print "! Error: file or path not found"
    except IndexError:
        print "! Error: please, enter message file path"

    # emails
    # r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$'
    # ^(?("")("".+?""@)|(([0-9a-zA-Z]((\.(?!\.))|[-!#\$%&'\*\+/=\?\^`\{\}\|~\w])*)(?<=[0-9a-zA-Z])@))(?(\[)(\[(\d{1,3}\.){3}\d{1,3}\])|(([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,6}))$
    # \s?[A-Z0-9_-+%]+@[A-Z0-9_-+%]+\.[A-Z0-9]\s?

    # urls
    # ^(ht|f)tp(s?)\:\/\/[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*(:(0-9)*)*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$

