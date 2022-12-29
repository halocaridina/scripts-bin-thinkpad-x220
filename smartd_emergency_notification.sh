#!/usr/bin/env bash

read -d '' TERMINAL_MESSAGE << EOF

-------------------------------------------------
Smartd has detected an error!

Error type: $SMARTD_FAILTYPE
Device node: $SMARTD_DEVICESTRING
Date occurred: $SMARTD_TFIRST
-------------------------------------------------

EOF

for pts in /dev/pts/*; do
  echo "$TERMINAL_MESSAGE" > $pts
done

sudo -u srsantos DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
notify-send "S.M.A.R.T Error ($SMARTD_FAILTYPE)" "$SMARTD_MESSAGE" --icon=dialog-warning -u critical
