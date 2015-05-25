# mail
A basic program should take a path to an e-mail message file as a command line parameter and print all found e-mail addresses and URLs as well as their source (either From, To, Cc, Bcc or body).  Also print the total number of found e-mail addresses and URLs.  For example:

ostas@softservecom.com From
ober@softservecom.com  To
http://www.google.com body
Total e-mail addresses 2
Total URLs 1

For now concentrate on e-mail messages having a plain text body (skip multi-part messages or messages having HTML body).  Use regular expressions to split a message and collect e-mail addresses and URLs (aim to collect 99% of valid e-mail addresses and URLs).  Dont remove found duplicates.

Print an error when:
a)  there is no path to a message;
b) a message file not found;
c)  it's not a valid e-mail message. 
Print a warning when:
a)  it doesn't have a body, From or To field;
b)  From or To field doesn't have a valid e-mail address;
c)  a body doesn't contain any URL or e-mail address. 

Time to accomplish it - one week.
