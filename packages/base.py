from pyinfra import host
from pyinfra.api import deploy
from pyinfra.operations import apt, server


@deploy('Base setup')
def base_setup():
    server.timezone(
        name="Set timezone",
        timezone=host.data.get("timezone"),
    )

    apt.packages(
        name="Install system packages",
        packages=["aptitude", "htop", "mc"],
        update=True,
    )
