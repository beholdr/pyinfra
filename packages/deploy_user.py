from pyinfra import host
from pyinfra.api import deploy
from pyinfra.operations import files, server


@deploy('Deploy user')
def deploy_user():
    user = host.data.get("deploy_user")

    server.user(
        name="Create deploy user",
        user=user,
        shell="/bin/bash",
        group="docker",
        create_home=True,
    )

    files.directory(
        name="Change /srv owner",
        path="/srv",
        user=user,
    )
