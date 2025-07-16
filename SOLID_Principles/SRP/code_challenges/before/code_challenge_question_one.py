# 1. UserManager – Too Many Responsibilities
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, email):
        self.users.append({'name': name, 'email': email})
        self.send_welcome_email(email)
        self.save_to_file(name, email)

    def send_welcome_email(self, email):
        print(f"Sending welcome email to {email}")

    def save_to_file(self, name, email):
        with open("users.txt", "a") as f:
            f.write(f"{name} - {email}\n")

