from pyinfra import host
from pyinfra.api import deploy
from pyinfra.facts.server import LinuxDistribution
from pyinfra.operations import apt


@deploy('Docker')
def docker_install():
    distro = host.get_fact(LinuxDistribution)

    codename = distro["release_meta"]["VERSION_CODENAME"]

    match distro["name"]:
        case "Ubuntu":
            docker_base_url = "https://download.docker.com/linux/ubuntu"
        case "Debian":
            docker_base_url = "https://download.docker.com/linux/debian"
        case _:
            raise RuntimeError(f"Unsupported distribution: {distro['name']}")

    apt.packages(
        name="Install Docker prerequisites",
        packages=[
            "ca-certificates",
            "curl",
        ],
        update=True,
    )

    apt.key(
        name="Add Docker GPG key",
        src=f"{docker_base_url}/gpg",
        dest="docker.gpg",
    )

    apt.sources_file(
        name="Add Docker APT repository",
        filename="docker",
        types="deb",
        uris=docker_base_url,
        suites=codename,
        components="stable",
        signed_by="/etc/apt/keyrings/docker.gpg",
    )

    apt.packages(
        name="Install Docker",
        packages=[
            "docker-ce",
            "docker-ce-cli",
            "containerd.io",
            "docker-buildx-plugin",
            "docker-compose-plugin",
        ],
        update=True,
    )
