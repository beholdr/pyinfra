from pyinfra import config, host
from pyinfra.facts.server import LinuxDistribution

from packages.backup import backup_setup
from packages.base import base_setup
from packages.deploy_key import deploy_key
from packages.deploy_user import deploy_user
from packages.docker import docker_install
from packages.docker_rollout import docker_rollout_install
from packages.lazydocker import lazydocker_install
from packages.yandex_registry import yandex_registry

config.INHERIT_ENV = ["YANDEX_S3_ACCESS_KEY", "YANDEX_S3_SECRET_ACCESS_KEY"]

distro = host.get_fact(LinuxDistribution)

if distro["name"] not in ("Ubuntu", "Debian"):
    raise RuntimeError(f"Unsupported distribution: {distro['name']}")

base_setup()

docker_install()

if host.data.get("ssh_user") != host.data.get("deploy_user"):
    deploy_user()

deploy_key()

lazydocker_install()

if host.data.get("docker_rollout_enabled"):
    docker_rollout_install()

if host.data.get("yandex_registry_enabled"):
    yandex_registry()

if host.data.get("backup_enabled"):
    backup_setup()
