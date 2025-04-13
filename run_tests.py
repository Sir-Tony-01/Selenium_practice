import subprocess
import webbrowser
import os

report_file = "report.html"

subprocess.run([
    "pytest",
    "--html=" + report_file,
    "--self-contained-html"
])

if os.path.exists(report_file):
    webbrowser.open("file://" + os.path.abspath(report_file))

