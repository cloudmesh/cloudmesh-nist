# Libcloud objbects returned by clouds

## AWS



```
{'_uuid': None,
 'created_at': datetime.datetime(2018, 11, 9, 16, 44, 4, tzinfo=<libcloud.utils.iso8601.Utc object at 0x1038ffe80>),
 'driver': <libcloud.compute.drivers.ec2.EC2NodeDriver object at 0x10250c588>,
 'extra': {'architecture': 'x86_64',
           'availability': 'us-west-2a',
           'block_device_mapping': [{'device_name': '/dev/sda1',
                                     'ebs': {'attach_time': datetime.datetime(2018, 10, 25, 19, 0, tzinfo=<libcloud.utils.iso8601.Utc object at 0x1038ffe80>),
                                             'delete': 'true',
                                             'status': 'attached',
                                             'volume_id': 'vol-0081afab5b6fbe25a'}}],
           'client_token': '',
           'dns_name': 'ec2-52-89-23-7.us-west-2.compute.amazonaws.com',
           'ebs_optimized': 'false',
           'groups': [{'group_id': 'sg-1f8ae364',
                       'group_name': 'launch-wizard-2'}],
           'hypervisor': 'xen',
           'iam_profile': None,
           'image_id': 'ami-0bbe6b35405ecebdb',
           'instance_id': 'i-0fad7e92ffea8b345',
           'instance_lifecycle': None,
           'instance_tenancy': 'default',
           'instance_type': 't2.micro',
           'kernel_id': None,
           'key_name': 'ec2',
           'launch_index': 0,
           'launch_time': '2018-11-09T16:44:04.000Z',
           'monitoring': 'disabled',
           'network_interfaces': [<EC2NetworkInterface: id=eni-0dfc8e30289e6aa34, name=eni-0dfc8e30289e6aa34],
           'platform': None,
           'private_dns': 'ip-172-31-28-147.us-west-2.compute.internal',
           'product_codes': [],
           'ramdisk_id': None,
           'reason': '',
           'root_device_name': '/dev/sda1',
           'root_device_type': 'ebs',
           'source_dest_check': 'true',
           'status': 'running',
           'subnet_id': 'subnet-219fd246',
           'tags': {'Name': 'p1'},
           'virtualization_type': 'hvm',
           'vpc_id': 'vpc-52182935'},
 'id': 'i-0fad7e92ffea8b345',
 'image': None,
 'name': 'p1',
 'private_ips': ['172.31.28.147'],
 'public_ips': ['52.89.23.7'],
 'size': None,
 'state': 'running'}
 ```
 
 ## Azure

