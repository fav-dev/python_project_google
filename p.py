#!/usr/bin/env python3

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}


from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

report = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A compplet Inventroy of My Fruit", styles["h1"])

report.build([report_title])

table_data = []
for k, v in fruit.items():
  table_data.append([k, v])

report_table = Table(data=table_data)
report.build([report_title, report_table])
