from snap_rem_v3 import snapshot_create, snapshot_delete
from config import config

# keys
aws_access_key = config['aws_access_key']
aws_secret_key = config['aws_secret_key']
ec2_region_name = config['ec2_region_name']
ec2_region_endpoint = config['ec2_region_endpoint']

# volume ids and days
qa_vol_id = config['qa_vol_id']
uat_vol_id = config['uat_vol_id']
qa_days_del = config['qa_days_old']
uat_days_del = config['uat_days_old']

# tags for creation of snapshot
uat_tag_value = config['tag_value1']
qa_tag_value = config['tag_value']


create_snap = snapshot_create (qa_vol_id, uat_tag_value)
del_snap = snapshot_delete(uat_vol_id, qa_days_del)
