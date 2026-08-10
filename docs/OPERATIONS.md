# OICO Operations

The public repository is frozen for maintenance and external validation. Operational state that could contain professional contact details is kept outside Git under `~/Library/Application Support/OICO/operations/` and is never committed.

## Monitoring

The optional local monitor is `com.oico.validation-monitor`. It uses unauthenticated public GitHub endpoints, checks every six hours, records only issue/pull-request/release titles and URLs, and caps its event log. It does not read email, browser cookies, private repositories, or repository credentials.

```bash
sh scripts/status_monitor.sh
sh scripts/uninstall_monitor.sh
```

The monitor can be reinstalled with `sh scripts/install_monitor.sh`. Its state and bounded logs live under `~/Library/Application Support/OICO/monitor/`.

## Evidence discipline

Internal CI, repository existence, stars, download counts, and author-created issues are not external validation. A reproduction, critique, contribution, course use, lab use, or citation is recorded only when there is a public, auditable source and an identifiable external actor.
