import pytest


# testinfra_hosts = ["centos74"]


@pytest.mark.parametrize('pkg', [
  'ruby-full'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed
