# Security Policy

Do not commit API keys, OAuth tokens, passwords, private URLs with credentials,
browser cookies, or local machine identifiers.

Before each release, run:

```bash
python scripts/scan_secrets.py
```

If a credential is found, remove it from the repository history before public
release and rotate the credential at the provider.

