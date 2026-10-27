# Pyinfra helpers

## Provision

1. Add your ssh-key to the target server:
  - `ssh-copy-id root@example.com` from your computer OR
  - `ssh-import-id gh:<your-username>` from server

2. Copy `.env.example` → `.env` and fill the secrets

3. Set up your host and other settings in the `inventory.py`

4. Run `task provision`
