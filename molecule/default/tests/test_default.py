import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_jq_package_installed(host):
    assert host.package("jq").is_installed


def test_jq_binary_exists(host):
    assert host.file('/usr/bin/jq').exists


def test_jq_binary_file(host):
    assert host.file('/usr/bin/jq').is_file


def test_jq_binary_which(host):
    assert host.check_output('which jq') == '/usr/bin/jq'
