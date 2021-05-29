import os
from linode_api4 import LinodeClient

TOKEN = os.environ.get('TOKEN')
CLIENT = LinodeClient(TOKEN)


def main():
    enum_file = f'from enum import Enum{add_instance_enums()}{add_region_and_az_enums()}'

    # Create file
    with open("linode_enums/linode_enums.py", 'w') as output_file:
        output_file.write(enum_file)


def add_instance_enums() -> str:

    instance_blob = f"\n\nclass LinodeInstanceTypes(Enum):"

    instances = CLIENT.linode.types()

    for instance in instances:
        instance_type = instance.id

        instance_enum = instance_type.upper().replace('-', '_')
        instance_type = f"'{instance_type}'"

        instance_blob = f"{instance_blob}\n    {instance_enum} = {instance_type}"

    return instance_blob


def add_region_and_az_enums() -> str:
    region_blob = f"\n\nclass LinodeRegions(Enum):"

    regions = CLIENT.regions()

    for region in regions:
        region = region.id

        region_enum = region.upper().replace('-', '_')
        region_str = f"'{region}'"

        region_blob = f"{region_blob}\n    {region_enum} = {region_str}"

    return region_blob


if __name__ == '__main__':
    main()
