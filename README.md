# Zabbix Domain Expiry

## Description

Zabbix template to check domain registration expiry

Tested on:
* Zabbix 7.0

## Requirements:
* Zabbix v7.0
* whois installed on zabbix server
* python installed on zabbix server

## Setup:

1. Copy shell script domain.py to your Zabbix server external scripts dir (default: /usr/lib/zabbix/externalscripts/)
2. Make it executable (e.g. chmod +x /usr/lib/zabbix/externalscripts/domain.py)
2. Import yaml template to your zabbix server
3. Create a host with a domain name as the Host name and attach the template to the host. Make sure required macros are filled out
