Specification
=============

Several objects defined in this document are used across the NBDRA.
Therefore, the objects have not been organized by NBDRA components, as
shown in Figure 1, but rather grouped by functional use as summarized in
Figure 2.

![Figure 2: NIST Big Data Reference Architecture Interfaces](media/image4.jpeg)



Identity
--------

In a multiuser environment, a simple mechanism is used in this document
for associating objects and data to a particular person or group. While
these efforts do not intend to replace more elaborate solutions such as
proposed by eduPerson [5] or others, a very simple way was chosen to
distinguish users. Therefore, the following sections introduce a number
of simple objects including a profile and a user.

### Profile

A profile defines the identity of an individual. It contains name and
email information. It may have an optional unique user identification
(uuid) and/or use a unique email to distinguish a user. Profiles are
used to identify different users.


```
{
    'profile': {
        'description': 'The Profile of a user',
        'uuid': 'jshdjkdh\...',
        'context:': 'resource',
        'email': 'laszewski\@gmail.com',
        'firstname': 'Gregor',
        'lastname': 'von Laszewski',
        'username': 'gregor',
        'publickey': 'ssh \....'
    }
}
```

Object 4.1: Profile

### User

In contrast to the profile, a user contains additional attributes that
define the role of the user within the multiuser system. The user
associates different roles to individuals. These roles potentially have
gradations of responsibility and privilege.


```
{
    'user': {
        'profile': 'objectid:profile',
        'roles': ['admin']
    }
}
```

Object 4.2: User

### Organization

An important concept in many applications is the management of a group
of users in an organization that manages a Big Data application or
infrastructure. User group management can be achieved through three
concepts. First, it can be achieved by using the profile and user
resources itself as they contain the ability to manage multiple users as
part of the REST interface. The second concept is to create a (virtual)
organization that lists all users within the virtual organization. The
third concept is to introduce groups and roles either as part of the
user definition or as part of a simple list similar to the organization.



```
{
    'organization': {
        'users': [
            'objectid:user'
        ]
    }
}
```

Object 4.3: Organization

The profile, user, and organization concepts allow for the clear
definition of various roles such as data provider, data consumer, data
curator, and others. These concepts also allow for the creation of
services that restrict data access by role or organizational
affiliation.

### Group/Role

A group contains a number of users. It is used to manage authorized
services.


```
{
    'group': {
        'name': 'users',
        'description': 'This group contains all users',
        'users': [
            'objectid:user'
        ]
    }
}
```

Object 4.4: Group

A role is a further refinement of a group. Group members can have
specific roles. For example, a group of users can be assigned a role
that allows access to a repository. More specifically, the role would
define a user's read and write privileges to the data within the
repository.

```
{
    'role': {
        'name': 'editor',
        'description': 'This role contains all editors',
        'users': [
            'objectid:user'
        ]
    }
}
```
Object 4.5: Role

Data
----

Data for Big Data applications are delivered through data providers.
They can be either local data providers, data contributed by a user, or
distributed data providers, data on the Internet. Currently, the focus
is on an elementary set of abstractions related to data providers that
offer the ability to utilize variables, files, virtual data directories,
data streams, and data filters.

-***Variables*** are used to hold specific contents that are
 associated in programming language as variables. A variable has a
 name, value, and type.

-***Defaults*** are a special type of variables that allow adding of
 a context. Defaults can be created for different contexts.

-***Files*** are used to represent information collected within the
 context of classical files in an operating system.

-***Directories*** are locations for storing and organizing multiple
 files on a compute resource.

-***Virtual Directories*** are collections of endpoints to files.
 Files in a virtual directory may be located on different resources.
 For this initial purpose, the distinction between virtual and
 non-virtual directories is nonessential, and the focus will be on
 abstracting all directories to be virtual. Therefore, the files
 could be physically hosted on different disks. However, it is
 important to note that virtual data directories can hold more than
 files; they can also contain data streams and data filters.

-***Streams*** are services that offer the consumer a flow of data.
 Streams may allow the initiation of filters to reduce the amount of
 data requested by the consumer. Stream filters operate in streams or
 on files converting them to streams.

-***Batch Filters*** operate on streams and on files, working in the
 background and delivering files as output. In contrast to streams,
 batch filters process the data set and return an output after all
 operations have been applied.

-***Indexed Stores*** are storage systems for objects that can be
 accessed by an index for each object. Search and filter functions
 are integrated into indexed stores to allow identification of
 objects.

-***Databases*** refer to traditional databases but also to NoSQL.

-***Collections*** are an agglomeration of any type of data.

-***Replicas*** are duplication of data objects created to avoid
 overhead due to network or other physical restrictions on a remote
 resource.

### TimeStamp

Often data needs to be timestamped to indicate when it has been
accessed, created, or modified. All objects defined in this document
will have, in their final version, a timestamp.

```
{
    'timestamp': {
        'accessed': '1.1.2017:05:00:00:EST',
        'created': '1.1.2017:05:00:00:EST',
        'modified': '1.1.2017:05:00:00:EST'
    }
}
```
Object 4.6: TimeStamp

### Variables

Variables are used to store simple values. Each variable can have a
type, which is also provided as demonstrated in the object below. The
variable value format is defined as string to allow maximal probability.


```
{
    'var': {
        'name': 'name of the variable',
        'value': 'the value of the variable as string',
        'type': 'the datatype of the variable such as int, str, float, \...'
    }
}
```

Object 4.7: Variables

### Default

A default is a special variable that has a context associated with it.
This allows one to define values that can be easily retrieved based on
the associated context. For example, a default could be the image name
for a cloud where the context is defined by the cloud name.


```
{
    'default': {
        'value': 'string',
        'name': 'string',
        'context': 'string - defines the context of the default (user, cloud, \...)'
    }
}
```

Object 4.8: Default

![Figure 3: Booting a VM from Defaults](media/image5.jpeg)


### File

A file is a computer resource allowing storage of data that is being
processed. The interface to a file provides the mechanism to
appropriately locate a file in a distributed system. File identification
includes the name, endpoint, checksum, and size. Additional parameters,
such as the last access time, could also be stored. The interface only
describes the location of the file.

The *file* object has *name*, *endpoint* (location), *size* in GB, MB,
Byte, *checksum* for integrity check, and last *accessed* timestamp.


```
{
    'file': {
        'name': 'report.dat',
        'endpoint': 'file://gregor\@machine.edu:/data/report.dat',
        'checksum': {'sha256':'c01b39c7a35ccc \...\.... ebfeb45c69f08e17dfe3ef375a7b'},
        'accessed': '1.1.2017:05:00:00:EST',
        'created': '1.1.2017:05:00:00:EST',
        'modified': '1.1.2017:05:00:00:EST',
        'size': ['GB', 'Byte']
    }
}
```


Object 4.9: File

### Alias

A data object could have one alias or even multiple ones. The reason for
an alias is that a file may have a complex name but a user may want to
refer to that file in a name space that is suitable for the user's
application.


```
{
    'alias': {
        'name': 'a better name for the object',
        'origin': 'the original object name'
    }
}
```

Object 4.10: File Alias

### Replica

In many distributed systems, it is important that a file can be
replicated among different systems to provide faster access. It is
important to provide a mechanism to trace the pedigree of the file while
pointing to its original source. A replica can be applied to all data
types introduced in this document.


```
{
    'replica': {
        'name': 'replica_report.dat',
        'replica': 'report.dat',
        'endpoint': 'file://gregor\@machine.edu:/data/replica_report.dat',
        'checksum': {
           `md5': '8c324f12047dc2254b74031b8f029ad0'
         },
        'accessed': '1.1.2017:05:00:00:EST',
        'size': [
            'GB',
            'Byte'
        ]
    }
}
```

Object 4.11: Replica

### Virtual Directory

A virtual directory is a collection of files or replicas of the files. A
virtual directory can contain a number of entities including files,
streams, and other virtual directories as part of a collection. The
element in the collection can either be defined by uuid or by name.


```
{
    'virtual_directory': {
    'name': 'data',
    'endpoint': 'http://\.../data/',
    'protocol': 'http',
    'collection': [
            'report.dat',
            'file2'
        ]
    }
}
```

Object 4.12: Virtual Directory


### Database

A *database* could have a name, an *endpoint* (e.g., host, port), and a
protocol used (e.g., SQL, mongo).


```
{
    'database': {
        'name': 'data',
        'endpoint': 'http://\.../data/',
        'protocol': 'mongo'
    }
}
```

Object 4.13: Database

### Stream

The stream object describes a data flow, providing information about the
rate and number of items exchanged while issuing requests to the stream.
A stream may return data items in a specific format that is defined by
the stream.


```
{
    'stream': {
        'name': 'name of the variable',
        'format': 'the format of the data exchanged in the stream',
        'attributes': {
            'rate': 10,
            'limit': 1000
            }
    }
}
```

Object 4.14: Stream

### Filter

Filters can operate on a variety of objects and reduce the information
received based on a search criterion.


```
{
  'filter': {
      'name': 'name of the filter',
      'function': 'the function of the data exchanged in the stream'
    }
}
```

Object 4.15: Filter


Virtual Cluster
---------------

One of the essential features for Big Data is the creation of a Big Data
analysis cluster. A virtual cluster combines resources that generally
are used to serve the Big Data application and can constitute a variety
of data analysis nodes that together build the virtual cluster. Instead
of focusing only on the deployment of a physical cluster, the creation
of a virtual cluster can be instantiated on a number of different
platforms. Such platforms include clouds, containers, physical hardware,
or a mix thereof to support different aspects of the Big Data
application.

Figure 4 illustrates the process for allocating and provisioning a
virtual cluster. The user defines the desired physical properties of the
cluster (e.g., CPU, memory, disk) and the intended configuration (e.g.,
software, users). After requesting the stack to be deployed, cloudmesh
allocates the machines by matching the desired properties with the
available images and booting. The stack definition is then parsed and
then evaluated to provision the cluster.

![Figure 4: Allocating and Provisioning a Virtual Cluster](media/image6.jpeg){width="3.16in" height="1.74in"}


### Virtual Cluster

A virtual cluster is an agglomeration of virtual compute nodes that
constitute the cluster. Nodes can be assembled to be bare metal, VMs,
and containers. A virtual cluster contains a number of virtual compute
nodes.

The virtual cluster object has name, label, endpoint, and provider. The
*endpoint* defines a mechanism to connect to it. The *provider* defines
the nature of the cluster (e.g., it is a virtual cluster on an OpenStack
cloud, or from AWS, or a bare metal cluster).

To manage the cluster, it can have a frontend node that is used to
manage other nodes. Authorized keys within the definition of the cluster
allow administrative functions, while authorized keys on a compute node
allow login and use functionality of the virtual nodes.

  []{#_Toc497917211 .anchor}

```
{
  'virtual_cluster': {
      'name': 'myvirtualcluster',
      'label': 'C0',
      'uuid': 'sgdlsjlaj\....',
      'endpoint': {
          'passwd': 'secret',
          'url': 'https:\...'
      },
      'provider': 'virtual_cluster_provider:openstack',
      'frontend': 'objectid:virtual_machine',
      'authorized_keys': ['objectid:sshkey'],
      'nodes': [
            'objectid:virtual_machine'
      ]
  }
}
```

Object 4.16: Virtual Cluster


```
virtual_cluster_provider': 'aws' | 'azure' | 'google' | 'comet' | 'openstack'
```

Object 4.17: Virtual Cluster Provider

### Compute Node

Compute nodes are used to conduct compute and data functions. They are
of a specific *kind*. For example, compute nodes could be a virtual
machine (VM), bare metal, or part of a predefined virtual cluster
framework.

Compute nodes are a representation of a computer system (physical or
virtual). A very basic set of information about the compute node is
maintained in this document. It is expected that, through the endpoint,
the VM can be introspected and more detailed information can be
retrieved. A compute node has name, label, a flavor, network interface
cards (NICs), and other relevant information.


```
{
    'compute_node': {
        'name': 'vm1',
        'label': 'gregor-vm001',
        'uuid': 'sgklfgslakj\....',
        'kind': 'vm',
        'flavor': ['objectid:flavor'],
        'image': 'Ubuntu-16.04',
        'secgroups': ['objectid:secgroup'],
        'nics': ['objectid:nic'],
        'status': '',
        'loginuser': 'ubuntu',
        'status': 'active',
        'authorized_keys': ['objectid:sshkey'],
        'metadata': {
            'owner':'gregor',
            'experiment': 'exp-001'
        }
    }
}
```

Object 4.18: Compute Node of a Virtual Cluster

### Flavor

The flavor specifies elementary information about the compute node, such
as memory and number of cores, as well as other attributes that can be
added. Flavors are essential to size a virtual cluster appropriately.


```
{
    'flavor': {
        'name': 'flavor1',
        'label': '2-4G-40G',
        'uuid': 'sgklfgslakj\....',
        'ncpu': 2,
        'ram': '4G',
        'disk': '40G'
    }
}
```

Object 4.19: Flavor

### Network Interface Card

To interact between the nodes, a network interface is needed. Such a
network interface, specified on a virtual machine with a NIC object, is
showcased in Object 4.20.


```
{
    'nic': {
        'name': 'eth0',
        'type': 'ethernet',
        'mac': '00:00:00:11:22:33',
        'ip': '123.123.1.2',
        'mask': '255.255.255.0',
        'broadcast': '123.123.1.255',
        'gateway': '123.123.1.1',
        'mtu': 1500,
        'bandwidth': '10Gbps'
    }
}
```

Object 4.20: Network Interface Card


### Key

Many services and frameworks use Secure Shell (SSH) keys to
authenticate. To allow the convenient storage of the public key, the
sshkey object can be used (see Object 4.21).


```
{
    'sshkey': {
        'comment': 'string',
        'source': 'string',
        'uri': 'string',
        'value': 'ssh-rsa AAA\...\...',
        'fingerprint': 'string, unique'
    }
}
```

Object 4.21: Key

### Security Groups

To allow secure communication between the nodes, security groups are
introduced. They define the typical security groups that will be
deployed once a compute node is specified. The security group object is
depicted in Object 4.22.


```
{
    'secgroup': {
            'ingress': '0.0.0.0/32',
            'egress': '0.0.0.0/32',
            'ports': 22,
            'protocols': 'tcp'
        }
}
```

Object 4.22: Security Groups

IaaS
----

Although Section 4.3 defines a general virtual cluster useful for Big
Data, sometimes the need exists to specifically utilize Infrastructure
as a Service (IaaS) frameworks, such as Openstack, Azure, and others. To
do so, it is beneficial to be able to define virtual clusters using
these frameworks. Hence, this subsection defines interfaces related to
IaaS frameworks. This includes specific objects useful for OpenStack,
Azure, and AWS, as well as others. The definition of the objects used
between the clouds to manage them, are different and not standardized.
In this case, the objects support functions such as starting, stopping,
suspending resuming, migration, network configuration, assigning of
resources, assigning of operating systems for and others for the VMs.

Inspecting other examples, such as *LibCloud*, shows the definition of
generalized objects are discovered, which are augmented with extra
fields to specifically integrate with the various frameworks. When
working with cloudmesh, it is sufficient to be able to specify a cloud
based on a cloud-specific action. Actions include boot, terminate,
suspend, resume, assign network intrusion prevention system, and add
users.

To support such actions, objects can be selected based on the IaaS type
in use when invoked. The following subsections list these objects as
used in LibCloud, OpenStack, and Azure.

### LibCloud

Libcloud is a Python library for interacting with different cloud
service providers. It uses a unified API that exposes similar access to
a variety of clouds. Internally, it uses objects that can interface with
different IaaS frameworks. However, as these frameworks are different
from each other, specific adaptations are done for each IaaS, mostly
reflected in the LibCloud Node (see Section 4.4.1.5).

#### Challenges

For time considerations, LibCloud was used for some time practically in
various versions of cloudmesh. However, it became apparent that at
times, the representation and functionality provided by LibCloud, for
reference implementations, did not support some advanced aspects
provided by the native cloud objects. Depending on the application,
libraries for interfacing with different frameworks, direct utilization
of the native objects, and interfaces provided by a particular IaaS
framework could all be viable options. Additional interfaces have been
introduced in Sections 4.4.2 and 4.4.3. Additional sections addressing
other IaaS frameworks may be integrated in the future.

#### LibCloud Flavor

The object referring to flavors is listed in Object 4.23.


```
{
    'libcloud_flavor': {
        'bandwidth': 'string',
        'disk': 'string',
        'uuid': 'string',
        'price': 'string',
        'ram': 'string',
        'cpu': 'string',
        'flavor_id': 'string'
    }
}
```

Object 4.23: Libcloud Flavor

#### LibCloud Image

The object referring to images is listed in Object 4.24.


```
{
    'libcloud_image': {
        'username': 'string',
        'status': 'string',
        'updated': 'string',
        'description': 'string',
        'owner_alias': 'string',
        'kernel_id': 'string',
        'ramdisk_id': 'string',
        'image_id': 'string',
        'is_public': 'string',
        'image_location': 'string',
        'uuid': 'string',
        'created': 'string',
        'image_type': 'string',
        'hypervisor': 'string',
        'platform': 'string',
        'state': 'string',
        'architecture': 'string',
        'virtualization_type': 'string',
        'owner_id': 'string'
    }
}
```

Object 4.24: Libcloud Image

#### LibCloud VM

The object referring to virtual machines is listed in the Object 4.25.

```
{
  'libcloud_vm': {
      'username': 'string',
      'status': 'string',
      'root_device_type': 'string',
      'image': 'string',
      'image_name': 'string',
      'image_id': 'string',
      'key': 'string',
      'flavor': 'string',
      'availability': 'string',
      'private_ips': 'string',
      'group': 'string',
      'uuid': 'string',
      'public_ips': 'string',
      'instance_id': 'string',
      'instance_type': 'string',
      'state': 'string',
      'root_device_name': 'string',
      'private_dns': 'string'
  }
}
```

Object 4.25: LibCloud VM

#### LibCloud Node

Virtual machines for the various clouds have additional attributes that
are summarized in Object 4.25. These attributes will be integrated into
the VM object in the future.


```
{
 'LibCLoudNode': {
     'id': 'instance_id',
     'name': 'name',
     'state': 'state',
     'public_ips': ['111.222.111.1'],
     'private_ips': ['192.168.1.101'],
     'driver': 'connection.driver',
     'created_at': 'created_timestamp',
     'extra': { }
 },
 'ec2NodeExtra': {
     'block_device_mapping': 'deviceMapping',
     'groups': ['security_group1', 'security_group2'],
     'network_interfaces': ['nic1', 'nic2'],
     'product_codes': 'product_codes',
     'tags': ['tag1', 'tag2']
     },
 'OpenStackNodeExtra': {
     'addresses': ['addresses'],
     'hostId': 'hostId',
     'access_ip': 'accessIPv4',
     'access_ipv6': 'accessIPv6',
     'tenantId': 'tenant_id',
     'userId': 'user_id',
     'imageId': 'image_id',
     'flavorId': 'flavor_id',
     'uri': '',
     'service_name': '',
     'metadata': ['metadata'],
     'password': 'adminPass',
     'created': 'created',
     'updated': 'updated',
     'key_name': 'key_name',
     'disk_config': 'diskConfig',
     'config_drive': 'config_drive',
     'availability_zone': 'availability_zone',
     'volumes_attached': 'volumes_attached',
     'task_state': 'task_state',
     'vm_state': 'vm_state',
     'power_state': 'power_state',
     'progress': 'progress',
     'fault': 'fault'
     },
 'AzureNodeExtra': {
     'instance_endpoints': 'instance_endpoints',
     'remote_desktop_port': 'remote_desktop_port',
     'ssh_port': 'ssh_port',
     'power_state': 'power_state',
     'instance_size': 'instance_size',
     'ex_cloud_service_name': 'ex_cloud_service_name'
     },
 'GCENodeExtra': {
     'status': 'status',
     'statusMessage': 'statusMessage',
     'description': 'description',
     'zone': 'zone',
     'image': 'image',
     'machineType': 'machineType',
     'disks': 'disks',
     'networkInterfaces': 'networkInterfaces',
     'id': 'node_id',
     'selfLink': 'selfLink',
     'kind': 'kind',
     'creationTimestamp': 'creationTimestamp',
     'name': 'name',
     'metadata': 'metadata',
     'tags_fingerprint': 'fingerprint',
     'scheduling': 'scheduling',
     'deprecated': 'True or False',
     'canIpForward': 'canIpForward',
     'serviceAccounts': 'serviceAccounts',
     'boot_disk': 'disk'
     }
 }
```

Object 4.26: LibCloud Node

### OpenStack

Objects related to OpenStack VMs are summarized in this section.

#### OpenStack Flavor

The object referring to flavors is listed in Object 4.27.


```
 {
 'openstack_flavor': {
     'os_flv_disabled': 'string',
     'uuid': 'string',
     'os_flv_ext_data': 'string',
     'ram': 'string',
     'os_flavor_acces': 'string',
     'vcpus': 'string',
     'swap': 'string',
     'rxtx_factor': 'string',
     'disk': 'string'
     }
 }
```

Object 4.27: OpenStack Flavor

#### OpenStack Image

The object referring to images is listed in Object 4.28.


```
{
    'openstack_image': {
        'status': 'string',
        'username': 'string',
        'updated': 'string',
        'uuid': 'string',
        'created': 'string',
        'minDisk': 'string',
        'progress': 'string',
        'minRam': 'string',
        'os_image_size': 'string',
        'metadata': {
        'image_location': 'string',
        'image_state': 'string',
        'description': 'string',
        'kernel_id': 'string',
        'instance_type_id': 'string',
        'ramdisk_id': 'string',
        'instance_type_name': 'string',
        'instance_type_rxtx_factor': 'string',
        'instance_type_vcpus': 'string',
        'user_id': 'string',
        'base_image_ref': 'string',
        'instance_uuid': 'string',
        'instance_type_memory_mb': 'string',
        'instance_type_swap': 'string',
        'image_type': 'string',
        'instance_type_ephemeral_gb': 'string',
        'instance_type_root_gb': 'string',
        'network_allocated': 'string',
        'instance_type_flavorid': 'string',
        'owner_id': 'string'
        }
    }
}
```

Object 4.28: OpenStack Image

#### OpenStack VM

The object referring to VMs is listed in Object 4.29.


```
{
    'openstack_vm': {
        'username': 'string',
        'vm_state': 'string',
        'updated': 'string',
        'hostId': 'string',
        'availability_zone': 'string',
        'terminated_at': 'string',
        'image': 'string',
        'floating_ip': 'string',
        'diskConfig': 'string',
        'key': 'string',
        'flavor__id': 'string',
        'user_id': 'string',
        'flavor': 'string',
        'static_ip': 'string',
        'security_groups': 'string',
        'volumes_attached': 'string',
        'task_state': 'string',
        'group': 'string',
        'uuid': 'string',
        'created': 'string',
        'tenant_id': 'string',
        'accessIPv4': 'string',
        'accessIPv6': 'string',
        'status': 'string',
        'power_state': 'string',
        'progress': 'string',
        'image__id': 'string',
        'launched_at': 'string',
        'config_drive': 'string'
    }
}
```

Object 4.29: OpenStack VM

### Azure

Objects related to Azure virtual machines are summarized in this
section.

#### Azure Size

The object referring to the image size machines is listed in Object
4.30.


```
{
    'azure-size': {
        '_uuid': 'None',
        'name': 'D14 Faster Compute Instance',
        'extra': {
            'cores': 16,
            'max_data_disks': 32
        },
        'price': 1.6261,
        'ram': 114688,
        'driver': 'libcloud',
        'bandwidth': 'None',
        'disk': 127,
        'id': 'Standard_D14'
    }
}
```


Object 4.30: Azure-Size

#### Azure Image

The object referring to the images machines is listed in Object 4.31.


```
{
    'azure_image': {
      '_uuid': 'None',
      'driver': 'libcloud',
      'extra': {
          'affinity_group': '',
          'category': 'Public',
          'description': 'Linux VM image with coreclr-x64-beta5-11624 installed to /opt/dnx. This image is based on Ubuntu 14.04 LTS, with prerequisites of CoreCLR installed. It also contains PartsUnlimited demo app which runs on the installed coreclr. The demo app is installed to /opt/demo. To run the demo, please type the command /opt/demo/Kestrel in a terminal window. The website is listening on port 5004. Please enable or map an endpoint of HTTP port 5004 for your azure VM.',
          'location': 'East Asia;Southeast Asia;Australia East;Australia Southeast;Brazil South;North Europe;West Europe;Japan East;Japan West;Central US;East US 2; North Central US;South Central US;West US',
          'media_link': '',
          'os': 'Linux',
          'vm_image': 'False'
          },
      'id': '03f55de797f546a1b29d1\....',
      'name': 'CoreCLR x64 Beta5 (11624) with PartsUnlimited Demo App on Ubuntu Server 14.04 LTS'
    }
}
```

Object 4.31: Azure-Image

#### Azure VM

The object referring to the virtual machines is listed in Object 4.32.


```
{
    'azure-vm': {
        'username': 'string',
        'status': 'string',
        'deployment_slot': 'string',
        'cloud_service': 'string',
        'image': 'string',
        'floating_ip': 'string',
        'image_name': 'string',
        'key': 'string',
        'flavor': 'string',
        'resource_location': 'string',
        'disk_name': 'string',
        'private_ips': 'string',
        'group': 'string',
        'uuid': 'string',
        'dns_name': 'string',
        'instance_size': 'string',
        'instance_name': 'string',
        'public_ips': 'string',
        'media_link': 'string'
    }
}
```

Object 4.32: Azure VM

Compute Services
----------------

### Batch Queue

Computing jobs that can run without end user interaction, or are
scheduled based on resource permission, are called batch jobs. Batch
jobs are used to minimize human interaction and allow the submission and
scheduling of many jobs in parallel while attempting to utilize the
resources through a resource scheduler more efficiently or simply in
sequential order. Batch processing is not to be underestimated even in
today's shifting Internet of Things environment towards clouds and
containers. This is based on the fact that for some applications,
resources managed by batch queues are highly optimized and in many
cases, provide significant performance advantages. Disadvantages include
the limited and preinstalled software stacks that, in some cases, do not
allow the latest applications to run.


```
{
    'batchjob': {
        'output_file': 'string',
        'group': 'string',
        'job_id': 'string',
        'script': 'string, the batch job script',
        'cmd': 'string, executes the cmd, if None path is used',
        'queue': 'string',
        'cluster': 'string',
        'time': 'string',
        'path': 'string, path of the batchjob, if non cmd is used',
        'nodes': 'string',
        'dir': 'string'
    }
}
```

Object 4.33: Batch Job

### Reservation

Some services may consume a considerable amount of resources,
necessitating the reservation of resources. For this purpose, a
reservation object (Object 4.34) has been introduced.


```
{
    'reservation': {
        'service': 'name of the service',
        'description': 'what is this reservation for',
        'start_time': ['date', 'time'],
        'end_time': ['date', 'time']
    }
}
```

Object 4.34: Reservation

Containers
----------

The following defines the container object.

```
{
    'container': {
        'name': 'container1',
        'endpoint': 'http://\.../container/',
        'ip': '127.0.0.1',
        'label': 'server-001',
        'memoryGB': 16
    }
}
```

Object 4.35: Container

Deployment
----------

A *deployment* consists of the resource *cluster*, the location
*provider* (e.g., OpenStack), and software *stack* to be deployed (e.g.,
Hadoop, Spark).


```
{
    'deployment': {
        'cluster': [
            { 'name': 'myCluster'},
            { 'id' : 'cm-0001'}
        ],
        'stack': {
            'layers': [
                'zookeeper',
                'hadoop',
                'spark',
                'postgresql'
                ],
            'parameters': {
                'hadoop': { 'zookeeper.quorum': [ 'IP', 'IP', 'IP']
        }
        }
        }
    }
}
```

Object 4.36: Deployment

Map/Reduce
----------

The *Map/Reduce* deployment has as inputs parameters defining the
applied function and the input data. Both function and data objects
define a *source* parameter, which specifies the location from which it
is retrieved. For instance, the \`\`file://'' Uniform Resource
Identifier (URI) indicates sending a directory structure from the local
file system, and the \`\`ftp://'' indicates that the data should be
fetched from a File Transfer Protocol (FTP) resource. It is the
framework's responsibility to materialize an instantiation of the
desired environment along with the function and data.


```
{
    'mapreduce': {
        'function': {
            'source': 'file://.',
            'args': {}
        },
        'data': {
            'source': 'ftp:///\...',
            'dest': '/data'
        },
        'fault_tolerant': true,
        'backend': {'type': 'hadoop'}
    }
}
```

Object 4.37: Map/Reduce

Additional parameters include the *fault\\_tolerant* and *backend*
parameters. The former flag indicates if the *Map/Reduce* deployment
should operate in a fault tolerant mode. For instance, in the case of
Hadoop, this may mean configuring automatic failover of name nodes using
Zookeeper. The *backend* parameter accepts an object describing the
system providing the *Map/Reduce* workflow. This may be a native
deployment of Hadoop, or a special instantiation using other frameworks
such as Mesos.

A function prototype is defined earlier. Key properties are that
functions describe their input parameters and generated results. For
input parameters, the *buildInputs* and *systemBuildInputs* respectively
describe the objects that should be evaluated and system packages that
should be present before this function can be installed. The *eval*
attribute describes how to apply this function to its input data.
Parameters affecting the evaluation of the function may be passed in as
the *args* attribute. The results of the function application can be
accessed via the *outputs* object, which is a mapping from arbitrary
keys (e.g., data, processed, model) to an object representing the
result.



```
{
    'mapreduce_function': {
        'name': 'name of this function',
        'description': 'These should be self-describing',
        'source': 'a URI to obtain the resource',
        'install': {
            'description': 'instructions to install the source if needed',
            'script': 'source://install.sh'
        },
        'eval': {
            'description': 'How to evaluate this function',
            'script': 'source://run.sh'
        },
        'args': [
            {
                'argument': 'value'
            }
            ],
            'buildInputs': [
                'list of dependent objects'
            ],
            'systemBuildInputs': [
            '   list of packages'
            ],
            'outputs': {
                'key': 'value'
            }
    }
}
```

Object 4.38: Map/Reduce Function


One example function is the *NoOp* function shown in Object 4.39. In the
case of undefined arguments, the parameters default to an identity
element. In the case of mappings, the identity element is the empty
mapping while for lists, the identity element is the empty list.


```
{
    'mapreduce_noop': {
        'name': 'noop',
        'description': 'A function with no effect'
    }
}
```

Object 4.39: Map/Reduce NoOp

### Hadoop

A *Hadoop* definition defines which *deployer* to use, the *parameters*
of the deployment, and the system packages *required*. For each
requirement, it could have attributes such as the library origin,
version, and other attributes (see Object 4.40).


```
{
    'hadoop': {
        'deployers': {
            'ansible': 'git://github.com/cloudmesh_roles/hadoop'
        },
        'requires': {
            'java': {
            'implementation': 'OpenJDK',
            'version': '1.8',
            'zookeeper': 'TBD',
            'supervisord': 'TBD'
            }
        },
        'parameters': {
            'num_resourcemanagers': 1,
            'num_namenodes': 1,
            'use_yarn': false,
            'use_hdfs': true,
            'num_datanodes': 1,
            'num_historyservers': 1,
            'num_journalnodes': 1
        }
    }
}
```

Object 4.40: Hadoop

Microservice
------------

As part of microservices, a function with parameters that can be invoked
has been defined. To describe such services, the Object 4.41 was
created. Defining multiple services facilitates the finding of the
microservices and the use as part of a microservice-based
implementation.


```
{
    'microservice' :{
        'name': 'ms1',
        'endpoint': 'http://\.../ms/',
        'function': 'microservice spec'
    }
}
```

Object 4.41: Microservice
