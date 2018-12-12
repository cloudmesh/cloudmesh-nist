from random import randint

clouds = ["aws", "azure", "chameleon"]
statuses = ["running", "stopped", "paused"]
rams = [4294967296, 8589934592, 12884901888, 17179869184, 34359738368]
disks = [10737418240, 21474836480, 32212254720, 53687091200, 1099511627776]
tags = ["web server", "db", "compute", "proxy"]
os = ["linux", "windows", "darwin"]


vm_data = {
    "azure": {
        "regions": [
            "usnorthcentral",
            "useast",
            "uswest",
            "ussouth",
        ],
        "images": [
            "Canonical:UbuntuServer:16.04-LTS:latest"
        ],
        "sizes": [
            "Basic_A0",
        ]
    },
    "aws": {
        "regions": [
            "us-west-2",
            "us-west-1",
            "us-east-1"
        ],
        "images": [
            "ami-0bbe6b35405ecebdb"
        ],
        "sizes": [
            "t2.micro",
            "m1.small"
        ]
    },

    "chameleon": {
        "regions": [
            "us-west-2",
            "us-west-1",
            "us-east-1"
        ],
        "images": [
            "CC-Ubuntu16.04"
        ],
        "sizes": [
            "t2.micro",
            "Basic_A0",
            "m1.small"
        ]
    }
}


def random_ip():
    return f"{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}"
