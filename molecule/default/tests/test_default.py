# molecule/default/tests/test_default.py

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_docker_is_installed(host):
    docker = host.package('docker-ce')
    assert docker.is_installed


def test_docker_running_and_enabled(host):
    docker = host.service("docker")
    assert docker.is_running
    assert docker.is_enabled


def test_docker_directories_exist(host):
    docker_dirs = ['/opt/docker_data', '/etc/docker',
                   '/etc/systemd/system/docker.service.d']
    for dir in docker_dirs:
        assert host.file(dir).is_directory


def test_docker_config_files_exist(host):
    docker_files = ['/etc/systemd/system/docker.service.d/docker.conf',
                    '/etc/docker/daemon.json']
    for fl in docker_files:
        assert host.file(fl).is_file
        assert host.file(fl).exists


def test_docker_group_exists(host):
    assert host.group('docker').exists
