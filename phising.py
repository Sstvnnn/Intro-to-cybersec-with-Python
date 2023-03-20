import re
#regex

# Define the criteria for identifying phishing emails
sender_address = "example.com"
subject_line = r"\d{6}|\d{8}"
content_keywords = r"password|credit card|SSN"
link_url = "example.com"

# Open the email file and read its contents
with open("email2.txt", "r") as f:
    email_lines = f.read()
    email_lines = email_lines.split('\n')
email = {}
for line in email_lines:
    if line.startswith("From:"):
        email["From"] = line.split(":")[1].strip()
    elif line.startswith("Subject:"):
        email["Subject"] = line.split(":")[1].strip()
    elif line.startswith("Content:"):
        email["Content"] = line.split(":")[1].strip()
    elif line.startswith("Links:"):
        email["Links"] = line.split(":")[1].strip()
# Check the sender address
if re.search(sender_address, email["From"]):
    print("WARNING: Suspicious sender address")

# Check the subject line
if re.search(subject_line, email["Subject"]):
    print("WARNING: Suspicious subject line")

# Check the content
if re.search(content_keywords, email["Content"]):
    print("WARNING: Suspicious content")

# Check the links
if re.search(link_url, email["Links"]):
    print("WARNING: Suspicious links")
