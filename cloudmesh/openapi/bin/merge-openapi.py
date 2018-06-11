import click
import re
import os

def read(dir, service):
    with open(os.path.join(dir, service, service +".yaml"), "r") as f:
        content = f.read()
    return content

def read_header(dir, service):
    with open(os.path.join(dir, service +".yaml"), "r") as f:
        content = f.read()
    return content

def parse_definitions(content):
    return content.split("definitions:")[1]

def parse_paths(content):
    return content.split("paths:")[1].split("definitions:")[0]


def merge_yaml(services):
    out = ""
    out = out + "definitions:"
    for service in services:
        content = read("services", service)
        out = out + parse_paths (content)

    out = out + "paths:"
    for service in services:
        content = read("services", service)
        out = out + parse_definitions (content)
    return out



@click.command()
@click.argument('services', nargs=-1)
def merge(services):

    header = read_header("service","header")
    out = header + "definitions:"

    for service in services:
        content = read("services", service)
        out = out + parse_paths (content)

    out = out + "paths:"
    for service in services:
        content = read("services", service)
        out = out + parse_definitions (content)
    out = re.sub(r'\n+', '\n', out)
    print(out)


if __name__ == '__main__':

    merge()