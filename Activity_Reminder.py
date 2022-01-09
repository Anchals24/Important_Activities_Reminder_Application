#code for the reminder.
from pynotifier import Notification
from datetime import datetime, timezone, timedelta
from time import sleep

utc_dt = datetime.now(timezone.utc)
is_notification_sent = [0]*24


def send_reminder(msg):
    Notification(title='Urgent Reminder',
                 description=msg,
                 duration=5).send()


def schedule(date):
    hour = date.hour

    # Remind for lunch+water time at 1 PM
    if hour == 13 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("It's time for lunch and water!!")

    # Remind for snacks at 4 PM
    if hour == 16 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("It's time for snacks and water!!")

    # Remind to log out from work
    if hour == 18 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("It's time to log off from work!!")

    # Remind for drinking water during office time
    for i in range(9, 18):
        if hour == i and hour not in [13, 16] \
                and is_notification_sent[hour] == 0:
            is_notification_sent[hour] = 1
            send_reminder("It's time to drink water!!")


if __name__ == "__main__":
    prev_date = utc_dt.astimezone() - timedelta(days=1)
    while True:
        date = utc_dt.astimezone()
        if date.day == 1 or date.day > prev_date.day:
            is_notification_sent = [0 for x in is_notification_sent]
            prev_date = date
        schedule(date)
        sleep(300)
