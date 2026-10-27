from pyinfra import host
from pyinfra.api import deploy
from pyinfra.facts.server import Home
from pyinfra.operations import files, server


@deploy('Lazydocker')
def lazydocker_install():
    home = host.get_fact(Home)

    server.shell(
        name="Install Lazydocker",
        commands="curl https://raw.githubusercontent.com/jesseduffield/lazydocker/master/scripts/install_update_linux.sh | bash",
        _env={"DIR": "/usr/local/bin"},
    )

    # TODO: add config for the app user too?
    files.put(
        name="Add lazydocker config",
        src="templates/lazydocker/config.yml",
        dest=f"{home}/.config/lazydocker/config.yml",
    )
