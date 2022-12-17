#!/usr/bin/env sh

/usr/bin/notify-send -t 10000 -i battery "Battery Status" "$(/usr/local/bin/battery.rb)"
