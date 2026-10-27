from pyinfra import host
from pyinfra.api import deploy
from pyinfra.operations import files


@deploy('Docker-rollout')
def docker_rollout_install():
    version = "0.14"
    plugins_dir = "/usr/local/lib/docker/cli-plugins"

    files.directory(
        name="Ensure the cli-plugins folder exist",
        path=plugins_dir,
        present=True,
    )

    files.download(
        name="Install docker-rollout",
        src=f"https://raw.githubusercontent.com/wowu/docker-rollout/refs/tags/v{version}/docker-rollout",
        dest=f"{plugins_dir}/docker-rollout",
        mode="0755",
    )
