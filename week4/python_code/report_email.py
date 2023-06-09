#!/usr/bin/env python3

#!/usr/bin/env python3

from emails import emails
import os
import reports
import json
import sys

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Complete - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"

message = emails.generate(sender, receiver, subject, body, "processed.pdf")
emails.send(message)

def load_data(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def process_data(data):
    summary = []
    for item in data:
        # Process the data and generate a summary
        # Append the summary to the list
        summary.append(item)
    return summary

def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("car_sales.json")
    summary = process_data(data)
    # Generate a PDF report
    report_title = "Sales Summary"
    report_body = "<br/><br/>".join(summary)
    reports.generate_report("/tmp/sales.pdf", report_title, report_body)
    # Send the PDF report as an email attachment
    message = emails.generate(sender, receiver, subject, body, "/tmp/sales.pdf")
    emails.send(message)

if __name__ == "__main__":
    main(sys.argv)


