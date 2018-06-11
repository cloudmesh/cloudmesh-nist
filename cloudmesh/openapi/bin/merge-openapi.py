import click

import os

def read(dir, service):
    with open(os.path.join(dir, service, service +".yaml"), "r") as f:
        content = f.read()
    return content

def parse_definitions(content):
    print (content.split("definitions:")[1])

def parse_paths(content):
    print(content.split("paths:")[1].split("definitions:")[0])



@click.command()
@click.argument('services', nargs=-1)
def merge(services):
    print ("definitions:")
    for service in services:
        content = read("services", service)
        parse_paths (content)

    print ("paths:")
    for service in services:
        content = read("services", service)
        parse_definitions (content)


if __name__ == '__main__':
    merge()