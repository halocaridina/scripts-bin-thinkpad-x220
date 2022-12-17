#!/usr/bin/env bash

# Optional icon to display before the text
# Insert the absolute path of the icon
# Recommended size is 24x24 px
readonly FAN_OFF_ICON="/etc/icons/indicator-sensors-fan.svg"
readonly FAN_ON_ICON="/etc/icons/indicator-sensors-fan_red.svg"

# Kernel values
readonly FAN="`/usr/bin/sensors | /usr/bin/grep fan | /usr/bin/awk '{print $2, $3}'`"
readonly NOT_RUNNING="0 RPM"

# Panel
if [[ $FAN == $NOT_RUNNING ]]; then
  INFO="<img>${FAN_OFF_ICON}</img>"
#  INFO+="<txt>${CURRENT_KERNEL}</txt>"
  MORE_INFO="<tool>"
  MORE_INFO+="Fan is off"
  MORE_INFO+="</tool>"
else 
  INFO="<img>${FAN_ON_ICON}</img>"
#  INFO+="<txt>${CURRENT_KERNEL}</txt>"
  MORE_INFO="<tool>"
  MORE_INFO+="Speed: ${FAN}"
  MORE_INFO+="</tool>"
fi

# Panel Print
echo -e "${INFO}"

# Tooltip Print
echo -e "${MORE_INFO}"

