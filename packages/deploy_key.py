from pyinfra import host
from pyinfra.api import deploy
from pyinfra.facts.files import File
from pyinfra.facts.server import Home, Hostname
from pyinfra.operations import files, server


@deploy('Deploy key')
def deploy_key():
    user = host.data.get("deploy_user")
    homedir = "/root" if user == "root" else f"/home/{user}"
    directory = f"{homedir}/.ssh"
    authorized_keys = f"{directory}/authorized_keys"
    private_key = f"{directory}/id_ed25519"
    public_key = f"{private_key}.pub"
    comment = f"{user}@{host.get_fact(Hostname)}"

    files.directory(
        name="Ensure the ~/.ssh folder exist",
        path=directory,
    )

    key_generated = server.shell(
        name="Generate SSH key",
        commands=f"ssh-keygen -t ed25519 -N '' -C '{comment}' -f {private_key}",
        _if=lambda: not host.get_fact(File, path=private_key),
    )

    server.shell(
        name="Add SSH public key to authorized_keys",
        commands=f"cat {public_key} >> {authorized_keys}",
        _if=key_generated.did_change,
    )
