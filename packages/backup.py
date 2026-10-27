from pyinfra import host
from pyinfra.api import deploy
from pyinfra.facts.server import Home
from pyinfra.operations import crontab, files, server


@deploy('Backup')
def backup_setup():
    home = host.get_fact(Home)
    backup_bucket = f"{host.name.replace(".", "-")}-backup"

    server.shell(
        name="Install Autorestic",
        commands="curl https://raw.githubusercontent.com/cupcakearmy/autorestic/master/install.sh | bash",
    )

    files.template(
        name="Add autorestic config",
        src="templates/autorestic/.autorestic.yml.j2",
        dest=f"{home}/.autorestic.yml",
        backup_bucket=backup_bucket,
    )

    crontab.crontab(
        name="Add cron",
        cron_name="autorestic-backup",
        command="autorestic cron --ci --lean",
        minute="*/5",
    )
