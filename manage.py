import pytest


# testinfra_hosts = ["centos74"]


@pytest.mark.parametrize('pkg', [
  'docker-py',
  'molecule'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed
