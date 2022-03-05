# (BETA) python-telegram-bot
Alerts to telegram group (with a bot), when someone logs in to a server via ssh

# Work in progres

## How to get your telegram_token and CHAT_ID
**in progress**  
....  
....  
....  

# Create executable

/etc/ssh/login_notification.sh
```
#!/usr/bin/env bash

sshd-telegram-alert > /tmp/sshd.log
```

```
$ chown root:root /etc/ssh/login_notification.sh 
$ chmod 700 /etc/ssh/login_notification.sh
```

vim /etc/pam.d/sshd

# Login Telegram Notification
# session optional pam_exec.so /etc/ssh/login_notify.sh


requirements:

```
python3-pip
```