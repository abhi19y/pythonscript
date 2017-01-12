import boto
import datetime
import dateutil
from dateutil import parser
from boto import ec2
from boto.ec2.connection import EC2Connection
from boto.ec2.regioninfo import RegionInfo
import os
import time
import sys
import logging
from config import config


aws_access_key = config['aws_access_key']
aws_secret_key = config['aws_secret_key']
ec2_region_name = config['ec2_region_name']
ec2_region_endpoint = config['ec2_region_endpoint']
region = RegionInfo(name=ec2_region_name, endpoint=ec2_region_endpoint)


conn = EC2Connection(aws_access_key,aws_secret_key,region=region)

ebsAllSnapshots=conn.get_all_snapshots(owner='self',filters={'volume_id':'vol_id'})

timeLimit=datetime.datetime.now() - datetime.timedelta(days = 20)  

for snapshot in ebsAllSnapshots:
    print snapshot.id
    
    if parser.parse(snapshot.start_time).date() <= timeLimit.date():
        print " Deleting Snapshot %s  %s "  %(snapshot.id,snapshot.tags)
        conn.delete_snapshot(snapshot.id) 
	# Setup logging
	logging.basicConfig(filename=config['log_file'], level=logging.INFO)
	start_message = 'Started deleting %(period)s snapshots at %(date)s' % {
	   'period': period,
	   'date': datetime.today().strftime('%d-%m-%Y %H:%M:%S')
		}
    else:
	print "No snapshot earlier than ", timeLimit
	quit()

