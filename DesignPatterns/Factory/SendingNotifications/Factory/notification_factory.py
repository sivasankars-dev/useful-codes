from Notifications.EmailNotification import EmailNotification
from Notifications.SMSNotification import SMSNotification
from Notifications.PushNotification import PushNotification

class NotificationFactory:
    _creators = {
        'sms': SMSNotification,
        'email': EmailNotification,
        'push': PushNotification
    }

    @classmethod
    def create_notification(cls, notification_type):
        if notification_type not in cls._creators:
            raise ValueError(f"Unknown notification type: {notification_type}")
        return cls._creators[notification_type]()

    