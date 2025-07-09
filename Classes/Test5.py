class Logger:
    def __init__(self, logname):
        self.logname = logname

    def log(self, message):
        print(f"Log: {message}")

class AdvancedLogger(Logger):
    def __init__(self, logname):
        super().__init__(logname)

    def log(self, message):
        super().log(message)
        print(f"Advanced logging enabled")

advanced = AdvancedLogger("Logfile")
advanced.log("This is a test message")

