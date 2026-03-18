#!/bin/bash

# Probe the remote directory
MSG_DUMP=rclone lsd gdrive: > /dev/null 2>&1 --log-level ERROR
PROBE_STATUS=$?

# Run the sync
rclone sync gdrive: ~/gdrive/ -v
SYNC_STATUS=$?

# Determine if there is an error or a success
if [ "$PROBE_STATUS" -ne 0 ] || [ "$SYNC_STATUS" -ne 0 ]; then
    MAIL_SUBJECT="Error"
else
    MAIL_SUBJECT="Success"
fi

# Send mail
echo "Sending mail for $MAIL_SUBJECT"
(
  echo "Subject: Script $MAIL_SUBJECT"
  echo ""
  echo "Probe Status: $PROBE_STATUS"
  echo "Sync Status: $SYNC_STATUS"
  echo "Timestamp: $(date)"
  echo "Message dump: $MSG_DUMP"
) | /usr/bin/msmtp loisinger.r@gmail.com
