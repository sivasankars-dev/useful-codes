from Factory.notification_factory import NotificationFactory

if __name__ == "__main__":
    for notification_type in ['email', 'sms', 'push']:
        notification = NotificationFactory.create_notification(notification_type)
        print(notification.notify("123456"))


