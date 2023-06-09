#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, additional_info):
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    empty_line = Spacer(1, 20)

    try:
        report = SimpleDocTemplate(filename)
        report.build([report_title, empty_line, report_info, empty_line])
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")