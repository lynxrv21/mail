#!usr/bin/env/python
# --*--codding:utf-8--*--

import re
import sys
from email.parser import Parser
from email.utils import parseaddr
from email import message_from_file


def headers_fields(source_list, re_pattern):
    app_list = []
    for taken in source_list:
        taken = taken.strip('<,>')
        if re.match(re_pattern, taken):
            app_list.append(taken)
    return app_list


def mails_urls(source_list, m_pattern, u_pattern):
    app_mail_list = []
    app_url_list = []
    for taken in source_list:
        taken = taken.strip('<,>')
        if re.match(m_pattern, parseaddr(taken)[1]):
            app_mail_list.append(parseaddr(taken)[1])
        elif re.match(u_pattern, taken):
            app_url_list.append(taken)
    return (app_mail_list, app_url_list)


if __name__ == '__main__':
    try:
        path = sys.argv[1]
        try:
            msg = message_from_file(open(path, "r"))
            if msg.is_multipart():
                print "Your file seems to be multipart message... I'd better skip it"
            elif msg.get_content_type() == 'text/plain':
                Body_raw = msg.get_payload()
                headers = Parser().parse(open(path, "r"))

                if not headers["Subject"] and not headers["From"] and not headers["To"] and not Body_raw:
                    print "! Error: check your file, noting to do here"
                else:
                    mail_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}")
                    url_pattern = re.compile(r"(((ht|f)tp(s?))\:\/\/)?((www.|[a-zA-Z].)[a-zA-Z0-9\-\.]+\.([a-zA-Z0-9\-\.]{2,}))+(\:[0-9]+)*(\/($|[a-zA-Z0-9\.+\,\;\?\'\\\+&amp;%\$#\=~_\-]+))*")

                    From_email = []
                    To_email = []
                    Cc_email = []
                    Bcc_email = []
                    Subject_email = []
                    Subject_url = []

                    Body = Body_raw.split()
                    Body_url = []
                    Body_email = []

                    if not headers["From"]:
                        print "! Warning: no 'From' field in your file"
                    else:
                        From_email = headers_fields(headers["From"].split(), mail_pattern)
                        if not From_email:
                            print "! Warning: no valid e-mail address in From"
                        else:
                            print "== %s emails in From: ==" % len(From_email)
                            for mail in From_email:
                                print mail

                    if not headers["To"]:
                        print "! Warning: no 'To' field in your file"
                    else:
                        To_email = headers_fields(headers["To"].split(), mail_pattern)
                        if not To_email:
                            print "! Warning: no valid e-mail address in To"
                        else:
                            print "== %s emails in To: ==" % len(To_email)
                            for mail in To_email:
                                print mail

                    if headers["Cc"]:
                        Cc_email = headers_fields(headers["Cc"].split(), mail_pattern)
                        print "== %s emails in Cc: ==" % len(Cc_email)
                        for mail in Cc_email:
                            print mail

                    if headers["Bcc"]:
                        Bcc_email = headers_fields(headers["Bcc"].split(), mail_pattern)
                        print "== %s emails in Bcc: ==" % len(Bcc_email)
                        for mail in Bcc_email:
                            print mail

                    if not headers["Subject"]:
                        print "! Warning: no 'Subject' field in your file"
                    else:
                        Subject_email, Subject_url = mails_urls(headers["Subject"].split(), mail_pattern, url_pattern)
                        if Subject_email:
                            print "== %s emails in subject: ==" % len(Subject_email)
                            for mail in Subject_email:
                                print mail

                        if Subject_url:
                            print "== %s urls in subject: ==" % len(Subject_url)
                            for url in Subject_url:
                                print url

                    if not Body_raw:
                        print "! Warning: no 'Body' field in your file"
                    else:
                        Body_email, Body_url = mails_urls(Body, mail_pattern, url_pattern)
                        if not Body_email:
                            print "! Warning: no e-mail address in body"
                        else:
                            print "== %s emails in body: ==" % len(Body_email)
                            for mail in Body_email:
                                print mail

                        if not Body_url:
                            print "! Warning: no URL address in body"
                        else:
                            print "== %s urls in body: ==" % len(Body_url)
                            for url in Body_url:
                                print url
                    headers_mail = len(From_email) + len(To_email) + len(Subject_email) + len(Cc_email) + len(Bcc_email)
                    urls = len(Body_url)+len(Subject_url)
                    print "== %s Total urls ==" % urls
                    mails = len(Body_email) + headers_mail
                    print "== %s Total email addresses ==" % mails

        except IOError:
            print "! Error: file or path not found"
    except IndexError:
        print "! Error: please, enter message file path"