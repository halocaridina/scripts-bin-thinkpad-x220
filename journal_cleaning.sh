#!/usr/bin/env sh

/usr/bin/journalctl --vacuum-time=1d &>/dev/null

/usr/bin/systemd-cat -t "journalctl_cleaning" /usr/bin/echo "***** OUTDATED JOURNALS PURGED - $(date) *****"

exit 0
