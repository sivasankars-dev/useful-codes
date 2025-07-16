class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, name, email):
        mailService = EmailService()
        fileService = FileService()
        self.users.append({'name': name, 'email': email})
        mailService.send_welcome_email(email)
        fileService.save_to_file(name, email)

class EmailService:
    def send_welcome_email(self, email):
        print(f"Sending welcome email to {email}")

class FileService:
    def save_to_file(self, name, email):
        with open("users.txt", "a") as f:
            f.write(f"{name} - {email}\n")

