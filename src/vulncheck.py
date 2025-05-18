#!/usr/bin/env python3

__author__     = "Maxime Reynaud"
__license__    = "GNU General Public License"
__version__    = "0.1.0"
__maintainer__ = "Maxime Reynaud"
__status__     = "Testing"

import click

@click.command()
@click.option('-s', '--scan', is_flag=True, help='scan the target')
@click.option('-u', '--url', type=str, help='Unique CVE-ID')
def main():
    pass
