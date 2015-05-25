#!usr/bin/env/python
# --*--codding:utf-8--*--

import re
import sys
from email.parser import Parser
import email

if __name__ == '__main__':

    a = """Delivered-To: lynxrv@mail.ru
Return-path: <tanushkanu@gmail.com>
Authentication-Results: mxs.mail.ru; spf=pass (mx48.mail.ru: domain of gmail.com designates 209.85.217.181 as permitted sender) smtp.mailfrom=tanushkanu@gmail.com smtp.helo=mail-lb0-f181.google.com;
	 dkim=pass header.i=gmail.com
Received-SPF: pass (mx48.mail.ru: domain of gmail.com designates 209.85.217.181 as permitted sender) client-ip=209.85.217.181; envelope-from=tanushkanu@gmail.com; helo=mail-lb0-f181.google.com;
Received: from mail-lb0-f181.google.com ([209.85.217.181]:34568)
	by mx48.mail.ru with esmtp (envelope-from <tanushkanu@gmail.com>)
	id 1YqJ2j-0002xv-Bm
	for lynxrv@mail.ru; Thu, 07 May 2015 13:28:38 +0300
X-Mru-BL: 0:99
X-Mru-TLS: TLSv1.2:AES128-GCM-SHA256
X-Mru-BadRcptsCount: 0
X-Mru-PTR: off
X-Mru-NR: 1
X-Mru-OF: Linux (Google)
X-Mru-RC: US
Received: by mail-lb0-f181.google.com with SMTP id ga7so27486907lbc.1
        for <lynxrv@mail.ru>; Thu, 07 May 2015 03:28:37 -0700 (PDT)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20120113;
        h=mime-version:in-reply-to:references:date:message-id:subject:from:to
         :content-type;
        bh=rVhzmRH3G9U8X+pnFLwM3chsmkpNdJZnyy+3rHvwbMs=;
        b=04cH43H0wTz25v9toawc2R3dCTjQNio0DXQj5lzg/2A14oiWOxVTWQm8r3GvSpU13l
         ZZy5S6Wtf4hqL7iMFjnaNKYD1cSs/qVU3tQLKZs3eR2aY+py3l6lQwMVoQBxu+li+hJ6
         KhE1vp9tysfcVaR51+0zgwuaCyYjS4b9XK2EhsAeoSTSHkfXb8uVGVQ8uZuj4VsnybYu
         OwolQyZY1soEI31Z6/UmiO+GF9ssYySf3jo1nzdXQounlPQoM0uaAaWcaAgWcr8AAB4z
         gaEjhoSh2B+Qk5eyWgZe6AXKM2QlV/KqlLwtb1KFoyo4OA2v7XyFmJmIJUyj57NEixGL
         I68g==
MIME-Version: 1.0
X-Received: by 10.152.163.36 with SMTP id yf4mr2520355lab.55.1430994517163;
 Thu, 07 May 2015 03:28:37 -0700 (PDT)
Received: by 10.112.97.66 with HTTP; Thu, 7 May 2015 03:28:37 -0700 (PDT)
In-Reply-To: <1429121164.897873643@f436.i.mail.ru>
References: <1429121164.897873643@f436.i.mail.ru>
Date: Thu, 7 May 2015 13:28:37 +0300
Message-ID: <CACPRW=ooid4+Qxwx0wZNQyDsR8o=2zTrYfOmxV2XEjTeEwam-Q@mail.gmail.com>
Subject: Re: polska
From: Tetiana Pud <tanushkanu@gmail.com>
To: Lynx <lynxrv@mail.ru>
Content-Type: multipart/alternative; boundary=001a11336a9cdf034205157b5f9e
X-DMARC-Policy: no
X-Mras: Ok
X-Mru-Authenticated-Sender: tanushkanu@gmail.com
X-Spam: undefined

--001a11336a9cdf034205157b5f9e
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: base64

0J/RgNC40LLRltGCDQoNCtCU0YPQttC1INC00Y/QutGD0Y4NCg0K0KLRltC70YzQutC4INC/0L7Q
sdCw0YfQuNC70LAg0YLQstGW0Lkg0LvQuNGB0YIgOikNCg0K0KLQsNC90Y8NCg0KMTUg0LrQstGW
0YLQvdGPIDIwMTUg0YAuIDIxOjA2IEx5bnggPGx5bnhydkBtYWlsLnJ1PiDQvdCw0L/QuNGB0LDQ
sjoNCg0KPg0KPg0KPiDQn9GA0LjQstGW0YIsINCi0LDQvdGPIQ0KPiDQodC60LjQtNCw0Y4g0LfQ
vtGI0LjRgiDQtyDQv9C+0LvRjNGB0YzQutC+0ZcNCj4NCj4g0KHRgtC10L/QsNC9DQo+DQo+INCa
INGN0YLQvtC80YMg0L/QuNGB0YzQvNGDINC/0YDQuNC70L7QttC10L3RiyDRgdGB0YvQu9C60Lgg
0L3QsCDRgdC70LXQtNGD0Y7RidC40LUg0YTQsNC50LvRizoNCj4NCj4gKjEuIFplc3p5dCBDd2lj
emVuLnBkZiogKDk4LjIg0JzQsSkNCj4NCj4g0KHRgdGL0LvQutCwINC00LvRjyDRgdC60LDRh9C4
0LLQsNC90LjRjyDRhNCw0LnQu9C+0LI6DQo+IGh0dHA6Ly9maWxlcy5tYWlsLnJ1LzMzQUEzMkY1
OTNFQzRCNkE4OTBEREI0M0ZFRUJGNkUyDQo+INCk0LDQudC70Ysg0LHRg9C00YPRgiDRhdGA0LDQ
vdC40YLRjNGB0Y8g0LTQviAxNS4wNS4yMDE1DQo+DQo+DQo=
--001a11336a9cdf034205157b5f9e
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: base64

PGRpdiBkaXI9Imx0ciI+0J/RgNC40LLRltGCPGRpdj48YnI+PC9kaXY+PGRpdj7QlNGD0LbQtSDQ
tNGP0LrRg9GOPC9kaXY+PGRpdj48YnI+PC9kaXY+PGRpdj7QotGW0LvRjNC60Lgg0L/QvtCx0LDR
h9C40LvQsCDRgtCy0ZbQuSDQu9C40YHRgiA6KTwvZGl2PjxkaXY+PGJyPjwvZGl2PjxkaXY+0KLQ
sNC90Y88L2Rpdj48L2Rpdj48ZGl2IGNsYXNzPSJnbWFpbF9leHRyYSI+PGJyPjxkaXYgY2xhc3M9
ImdtYWlsX3F1b3RlIj4xNSDQutCy0ZbRgtC90Y8gMjAxNSDRgC4gMjE6MDYgTHlueCA8c3BhbiBk
aXI9Imx0ciI+Jmx0OzxhIGhyZWY9Im1haWx0bzpseW54cnZAbWFpbC5ydSIgdGFyZ2V0PSJfYmxh
bmsiPmx5bnhydkBtYWlsLnJ1PC9hPiZndDs8L3NwYW4+INC90LDQv9C40YHQsNCyOjxicj48Ymxv
Y2txdW90ZSBjbGFzcz0iZ21haWxfcXVvdGUiIHN0eWxlPSJtYXJnaW46MCAwIDAgLjhleDtib3Jk
ZXItbGVmdDoxcHggI2NjYyBzb2xpZDtwYWRkaW5nLWxlZnQ6MWV4Ij4NCjxkaXY+PGJyPjxicj7Q
n9GA0LjQstGW0YIsINCi0LDQvdGPITxicj7QodC60LjQtNCw0Y4g0LfQvtGI0LjRgiDQtyDQv9C+
0LvRjNGB0YzQutC+0Zc8YnI+PGJyPtCh0YLQtdC/0LDQvTwvZGl2Pg0KPGJyPjxkaXY+DQoNCg0K
0Jog0Y3RgtC+0LzRgyDQv9C40YHRjNC80YMg0L/RgNC40LvQvtC20LXQvdGLINGB0YHRi9C70LrQ
uCDQvdCwINGB0LvQtdC00YPRjtGJ0LjQtSDRhNCw0LnQu9GLOjxicj48YnI+DQoNCjxiPjEuIFpl
c3p5dCBDd2ljemVuLnBkZjwvYj4gKDk4LjIg0JzQsSk8YnI+DQoNCjxicj4NCtCh0YHRi9C70LrQ
sCDQtNC70Y8g0YHQutCw0YfQuNCy0LDQvdC40Y8g0YTQsNC50LvQvtCyOiA8YSBocmVmPSJodHRw
Oi8vZmlsZXMubWFpbC5ydS8zM0FBMzJGNTkzRUM0QjZBODkwRERCNDNGRUVCRjZFMiIgdGFyZ2V0
PSJfYmxhbmsiPmh0dHA6Ly9maWxlcy5tYWlsLnJ1LzMzQUEzMkY1OTNFQzRCNkE4OTBEREI0M0ZF
RUJGNkUyPC9hPg0KDQo8YnI+DQo8Zm9udCBzaXplPSItMSIgY29sb3I9IiM2NzZBNzMiPtCk0LDQ
udC70Ysg0LHRg9C00YPRgiDRhdGA0LDQvdC40YLRjNGB0Y8g0LTQviAxNS4wNS4yMDE1PC9mb250
Pg0KPC9kaXY+PGJyPjwvYmxvY2txdW90ZT48L2Rpdj48YnI+PC9kaXY+DQo=
--001a11336a9cdf034205157b5f9e--"""

    b = email.message_from_string(a)
    if b.is_multipart():
        for payload in b.get_payload():
            # if payload.is_multipart(): ...
            print payload.get_payload()
    else:
        print b.get_payload()
