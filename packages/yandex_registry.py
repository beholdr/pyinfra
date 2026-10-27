from pyinfra import host
from pyinfra.api import deploy
from pyinfra.operations import docker


@deploy('Yandex registry')
def yandex_registry():
    user = host.data.get("deploy_user")
    password = host.data.get("YANDEX_REGISTRY_PASSWORD")

    docker.login(
        name="Login to Yandex Registry (root)",
        server="registry.yandexcloud.net",
        username="api_key",
        password=password,
    )

    if host.data.get("ssh_user") != host.data.get("deploy_user"):
        docker.login(
            name="Login to Yandex Registry (deploy user)",
            server="registry.yandexcloud.net",
            username="api_key",
            password=password,
            force=True, # because the deploy_user may not have been created yet
            _sudo=True,
            _sudo_user=user,
        )
