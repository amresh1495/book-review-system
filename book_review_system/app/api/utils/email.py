from fastapi import BackgroundTasks, FastAPI
from fastapi.testclient import TestClient
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Background task for sending confirmation email
def send_email(email: str, book_title: str, review_text: str):
    subject = "Review Confirmation"
    body = f"Thank you for submitting a review for '{book_title}'.\n\nYour review: {review_text}"
    sender_email = "your_email@gmail.com"  # Replace with your email
    receiver_email = email

    msg = MIMEMultipart()
    msg.attach(MIMEText(body, "plain"))
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        # Replace with your email password
        server.login(sender_email, "your_password")
        server.sendmail(sender_email, receiver_email, msg.as_string())
