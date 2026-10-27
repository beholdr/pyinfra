hosts = [
    (
        "example.com", {
            "ssh_user": "root",
            "deploy_user": "deploy",
            "timezone": "Europe/Moscow",
            # "backup_enabled": True, # modify config at ~/.autorestic.yml
            "docker_rollout_enabled": True,
            "yandex_registry_enabled": True,
        },
    ),
]
