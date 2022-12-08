#20-20-20 Rule to keep our eyes health

#Import time library
#Import notification for notification


import time
from plyer import notification


def notification_me(notification_title, notification_message):
    # Notify the message
    notification.notify(
        title=notification_title,
        message=notification_message,
        #Import the icons for message
        app_icon="/home/aparna/Desktop/Gaurav_rem/Alarm.ico",
        timeout=10,
        toast=False
    )


if __name__ == "__main__":
    while True:
    	#Message display on screen
        notification_me("Hii Bestie..!  It's Break Time",
                        "You should follow 20-20-20 rule to keep your eyes health..!!")
        time.sleep(1500)
