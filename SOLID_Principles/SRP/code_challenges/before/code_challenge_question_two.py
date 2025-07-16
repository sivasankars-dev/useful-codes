# 2. ReportGenerator – Mixed Logic 
class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def analyze(self):
        # Some complex analysis
        return sum(self.data) / len(self.data)

    def generate_pdf(self):
        print("Generating PDF report...")

    def send_report_email(self):
        print("Sending report via email...")
