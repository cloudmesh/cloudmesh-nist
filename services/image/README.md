# Azure

```    
{   '_uuid': None,
    'driver': <libcloud.compute.drivers.azure_arm.AzureNodeDriver object at 0x000001DDAE20A588>,
    'extra': {},
    'id': 'Canonical:UbuntuServer:16.04-LTS:latest',
    'location': 'northcentralus',
    'name': 'Canonical UbuntuServer 16.04-LTS latest',
    'offer': 'UbuntuServer',
    'publisher': 'Canonical',
    'sku': '16.04-LTS',
    'version': 'latest'}
```

# AWS

```
{'_uuid': None,
 'driver': <libcloud.compute.drivers.ec2.EC2NodeDriver object at 0x11056fc50>,
 'extra': {'architecture': 'x86_64',
           'billing_products': [],
           'block_device_mapping': [{'device_name': '/dev/sda1',
                                     'ebs': {'delete': 'true',
                                             'iops': None,
                                             'snapshot_id': 'snap-0576704bcf883d5ee',
                                             'volume_id': None,
                                             'volume_size': 8,
                                             'volume_type': 'gp2'},
                                     'virtual_name': None},
                                    {'device_name': '/dev/sdb',
                                     'virtual_name': 'ephemeral0'},
                                    {'device_name': '/dev/sdc',
                                     'virtual_name': 'ephemeral1'}],
           'description': 'Canonical, Ubuntu, 18.04 LTS, amd64 bionic image '
                          'build on 2018-09-12',
           'ena_support': 'true',
           'hypervisor': 'xen',
           'image_location': '099720109477/ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-20180912',
           'image_type': 'machine',
           'is_public': 'true',
           'kernel_id': None,
           'owner_alias': None,
           'owner_id': '099720109477',
           'platform': None,
           'ramdisk_id': None,
           'root_device_type': 'ebs',
           'sriov_net_support': 'simple',
           'state': 'available',
           'tags': {},
           'virtualization_type': 'hvm'},
 'id': 'ami-0bbe6b35405ecebdb',
 'name': 'ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-20180912'}
```

# OPenSTack



```
{'_uuid': None,
 'driver': <libcloud.compute.drivers.openstack.OpenStack_1_1_NodeDriver object at 0x1045d32b0>,
 'extra': {'created': '2018-10-24T17:48:11Z',
           'metadata': {'build-os': 'ubuntu-trusty',
                        'build-os-base-image-revision': '20181022',
                        'build-repo': 'https://github.com/ChameleonCloud/CC-Ubuntu16.04',
                        'build-repo-commit': 'f87a840fb0d7b0530696e751e42060decc6087be',
                        'build-tag': 'jenkins-cc-ubuntu-trusty-builder-2',
                        'build-variant': 'base'},
           'minDisk': 0,
           'minRam': 0,
           'progress': 100,
           'serverId': None,
           'status': 'ACTIVE',
           'updated': '2018-10-24T17:48:21Z'},
 'id': '1eabad70-eaa9-4724-b64d-67176066f9b1',
 'name': 'CC-Ubuntu14.04'}
```
