#!/usr/bin/env python3.9

import getopt 
import socket
import ssl
import sys


if len(sys.argv) < 2:
    exit("Usage: check-cert.py -h hostname")
else:
    pass 

argumentList = sys.argv[1:]

options = "h:"

long_options = ["host"]

def check_ssl_expiry(host):
    context = ssl.create_default_context()
    with socket.create_connection((host, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as sslsock:
            cert = sslsock.getpeercert()
            expiry_date = cert['notAfter']
            #return expiry_date
            print("Certificate Expiry date: " + expiry_date)

            

try: 
    arguments, values = getopt.getopt(argumentList, options, long_options)

    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--host"):
            check_ssl_expiry(currentValue)

except getopt.error as err:
    # output error, and return with an error code
    print (str(err))





