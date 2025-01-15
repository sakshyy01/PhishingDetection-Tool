import tkinter as tk
from tkinter import messagebox
import re
import urllib.parse

# Function to check for suspicious URL patterns
def check_url(url):
    # Check if the URL uses HTTP instead of HTTPS (less secure)
    if url.startswith("http://"):
        return "Suspicious: HTTP protocol (should use HTTPS)"

    # Check for excessive use of subdomains (a common phishing technique)
    subdomains = url.split(".")
    if len(subdomains) > 3:
        return "Suspicious: Too many subdomains"

    # Check if the domain name contains unusual characters (common in phishing)
    domain = urllib.parse.urlparse(url).netloc
    if not re.match(r'^[a-zA-Z0-9.-]+$', domain):
        return "Suspicious: Unusual characters in domain name"

    # Check if the URL contains keywords commonly associated with phishing
    phishing_keywords = ["login", "update", "verify", "password", "account", "secure"]
    if any(keyword in url.lower() for keyword in phishing_keywords):
        return "Suspicious: Contains phishing keywords"

    return "Legitimate URL"


# Function to check email content for phishing attempts
def check_email_content(content):
    # Check for common phishing words
    phishing_keywords = ["urgent", "account suspended", "confirm your identity", "reset password", "suspicious activity"]
    if any(keyword in content.lower() for keyword in phishing_keywords):
        return "Suspicious: Contains phishing-related phrases"

    # Check for requests for personal information (e.g., passwords, usernames)
    if "password" in content.lower() or "social security number" in content.lower():
        return "Suspicious: Asks for sensitive information"

    return "Legitimate Email"


# Function to process URL input from the GUI
def process_url():
    url = url_entry.get()
    if url:
        result = check_url(url)
        result_label.config(text=f"URL Check Result: {result}")
    else:
        messagebox.showerror("Error", "Please enter a URL.")


# Function to process email content input from the GUI
def process_email():
    email_content = email_entry.get()
    if email_content:
        result = check_email_content(email_content)
        result_label.config(text=f"Email Content Check Result: {result}")
    else:
        messagebox.showerror("Error", "Please enter email content.")


# Create the main GUI window
root = tk.Tk()
root.title("Phishing Detection Tool")

# Create a label and entry for URL input
url_label = tk.Label(root, text="Enter URL to Check:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create a button to check the URL
url_button = tk.Button(root, text="Check URL", command=process_url)
url_button.pack(pady=10)

# Create a label and entry for email content input
email_label = tk.Label(root, text="Enter Email Content to Check:")
email_label.pack(pady=5)
email_entry = tk.Entry(root, width=50)
email_entry.pack(pady=5)

# Create a button to check the email content
email_button = tk.Button(root, text="Check Email Content", command=process_email)
email_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="Result will be shown here", wraplength=400)
result_label.pack(pady=20)

# Run the GUI main loop
root.mainloop()