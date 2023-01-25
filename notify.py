from notifypy import Notify

notification = Notify(
  default_notification_title="You have been sitting for too long",
  default_application_name="Anti Office Syndrome",
  default_notification_icon=".\stuffnotify\workplace.png",
  default_notification_audio=".\stuffnotify\dtry.wav"
)

def notify():
  # stuff happening here.
  notification.message = "time to stand up and walk around"
  notification.send()