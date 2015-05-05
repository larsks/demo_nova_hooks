#!/usr/bin/env python

import setuptools

setuptools.setup(
    name="demo_nova_hooks",
    version=5,
    packages=['demo_nova_hooks'],
    entry_points={
        'nova.hooks': [
            'create_instance=demo_nova_hooks.simple:SimpleHookCreate',
            'instance_network_info=demo_nova_hooks.simple:SimpleHookNetwork',
            'delete_instance=demo_nova_hooks.simple:SimpleHookDelete',
        ]
    },
)
