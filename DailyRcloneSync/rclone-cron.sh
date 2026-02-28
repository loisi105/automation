#!/bin/bash
rclone sync gdrive: ~/gdrive/

# Capture the exit status
STATUS=$?
echo "$STATUS"
if [ $STATUS -ne 0 ]; then
    (
      echo "Subject: Alert: Script Failure"
      echo ""
      echo "The shell script failed with return value $STATUS at $(date)."
    ) | /usr/bin/msmtp loisinger.r@gmail.com
fi