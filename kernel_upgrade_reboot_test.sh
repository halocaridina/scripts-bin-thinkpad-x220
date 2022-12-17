#!/usr/bin/env bash

# Optional icon to display before the text
# Insert the absolute path of the icon
# Recommended size is 24x24 px
readonly OK_ICON="/etc/icons/update-none.svg"
readonly REBOOT_ICON="/etc/icons/reload.svg"

# Kernel values
readonly CURRENT_KERNEL=`/usr/bin/uname -r`

# Panel
if [[ -d "/lib/modules/${CURRENT_KERNEL}" && -f "/lib/modules/${CURRENT_KERNEL}/vmlinuz" ]]; then
  INFO="<img>${OK_ICON}</img>"
#  INFO+="<txt>${CURRENT_KERNEL}</txt>"
  MORE_INFO="<tool>"
  MORE_INFO+="Running: ${CURRENT_KERNEL}"
  MORE_INFO+="</tool>"
else 
  INFO="<img>${REBOOT_ICON}</img>"
#  INFO+="<txt>${CURRENT_KERNEL}</txt>"
  MORE_INFO="<tool>"
  MORE_INFO+="Kernel Upgraded - Reboot Required"
  MORE_INFO+="</tool>"
fi

# Tooltip
#MORE_INFO="<tool>"
#MORE_INFO+="Kernel Upgraded - Reboot Required"
#MORE_INFO+="</tool>"

# Panel Print
echo -e "${INFO}"

# Tooltip Print
echo -e "${MORE_INFO}"

