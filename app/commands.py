#!/usr/bin/env python
# -*-coding:utf-8 -*-
import ansible.runner

def ansiblecommand(commands,host):
    results = ansible.runner.Runner(
        pattern=host, forks=10,
        module_name='command', module_args=commands,
        ).run()
    return results
