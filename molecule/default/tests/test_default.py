import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'jq'
PACKAGE_BINARY = '/usr/bin/jq'


def test_jq_package_installed(host):
    """
    Tests if jq packages is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_jq_binary_exists(host):
    """
    Tests if jq binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_jq_binary_file(host):
    """
    Tests if jq binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_jq_binary_which(host):
    """
    Tests the output to confirm jq's binary location.
    """
    assert host.check_output('which jq') == PACKAGE_BINARY
