import random
from mongoengine import connect
from db.models import Vm, Image, Flavor
from db.mock_info import statuses, clouds, vm_data, random_ip


connect("cloudmesh-mock", alias="default")


class MongoDb:

    def check_db(self):
        """
        Call build_db to generate a mock database if
        none exists.
        """
        vm_count = Vm.objects.count()

        if vm_count < 1:
            self.build_db()

    def build_db(self, vm_count=1000):
        """
        Generate entries into a mock mongodb
        """

        # Build Vm collection
        for i in range(1, vm_count + 1):
            cloud = random.choice(clouds)
            cloud_data = vm_data[cloud]

            vm = Vm(
                cloud_id=f"CLOUD-ID-{i}",
                cloud=cloud,
                name=f"base-cloudmesh-user-{i}",
                image=random.choice(cloud_data["images"]),
                region=random.choice(cloud_data["regions"]),
                size=random.choice(cloud_data["sizes"]),
                state=random.choice(statuses),
                private_ips=[random_ip()],
                public_ips=[random_ip()],
                metadata=f"Metadata-{i}"
            )

            vm.save()
