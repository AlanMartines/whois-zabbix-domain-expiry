#!/usr/bin/env python3
import re
from subprocess import Popen, PIPE, STDOUT
import datetime
import sys

def execCommand(command):
    popen = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, universal_newlines=True)
    retStdOut = list(popen.stdout.read().split('\n'))
    retStatus = True if popen.wait() == 0 else False
    popen.stdout.close()
    return retStdOut

cmd_output=execCommand("whois "+sys.argv[1])
# cmd_output=execCommand("whois argohost.net")

for line in cmd_output:
    m = re.match(".*Expiry\sDate\:\s(\d{4})\-(\d{2})\-(\d{2})T.*",line)
    if m:
        ano=m.group(1)
        mes=m.group(2)
        dia=m.group(3)
    m = re.match(".*expires\:\s+(\d{4})(\d{2})(\d{2}).*",line)
    if m:
        ano=m.group(1)
        mes=m.group(2)
        dia=m.group(3)
    m = re.match("Expires on\.+\s*:\s*(\d{4})-(\w{3})-(\d{2})\.",line)
    if m:
        ano=m.group(1)
        mes=m.group(2)
        dia=m.group(3)

stringdate=ano+"-"+mes+"-"+dia
try:
   expiration_date=datetime.datetime.strptime(stringdate,"%Y-%m-%d")
except:
   expiration_date=datetime.datetime.strptime(stringdate,"%Y-%b-%d")
now=datetime.datetime.now()
remaining_time=expiration_date-now
remaining_days=str(remaining_time.total_seconds()/86400).split(".")[0]

print (remaining_days)
