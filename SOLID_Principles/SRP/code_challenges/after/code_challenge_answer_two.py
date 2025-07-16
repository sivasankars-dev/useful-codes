class ReportAnalyser:
    def __init__(self, data):
        self.data = data

    def analyze(self):
        # Some complex analysis
        return sum(self.data) / len(self.data)

class ReportGenerator:
    def generate_pdf(self):
        print("Generating PDF report...")

class EmailService:
    def send_report_email(self):
        print("Sending report via email...")
