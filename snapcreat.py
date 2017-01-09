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
vol_id = config['prod_vol_id']
tag_name = config['tag_name']
tag_value = config['tag_value']
region = RegionInfo(name=ec2_region_name, endpoint=ec2_region_endpoint)

utc_datetime = datetime.datetime.utcnow()
utc_datetime.strftime("%Y-%m-%d-%H%MZ")

value = tag_value+str(utc_datetime)
conn = EC2Connection(aws_access_key,aws_secret_key,region=region)
snapshot = conn.create_snapshot(vol_id)
snapshot.add_tags({'key': tag_name, 'value': value})
print snapshot.tags
