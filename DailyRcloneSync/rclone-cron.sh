#!/bin/bash

# Run the sync
SYNC_OUTPUT=$(rclone sync gdrive: ~/gdrive/ 2>&1)
SYNC_STATUS=$?

# Determine if there is an error or a success
if [ "$SYNC_STATUS" -ne 0 ]; then
    MAIL_SUBJECT="Error"
else
    MAIL_SUBJECT="Success"
fi

# Send mail
echo "Sending mail for $MAIL_SUBJECT"
(
  echo "Subject: Script $MAIL_SUBJECT"
  echo ""
  echo "Timestamp: $(date)"
  echo "Sync Status: $SYNC_STATUS"
  echo "Message dump: $SYNC_OUTPUT"
) | /usr/bin/msmtp loisinger.r@gmail.com
