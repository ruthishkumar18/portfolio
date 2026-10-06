import os
import re
import html

import resend

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv


# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------

load_dotenv()


# ---------------------------------------------------------
# Flask application
# ---------------------------------------------------------

app = Flask(__name__)


# ---------------------------------------------------------
# CORS
# ---------------------------------------------------------

frontend_origin = os.getenv("FRONTEND_ORIGIN", "*")

CORS(
    app,
    resources={
        r"/api/*": {
            "origins": frontend_origin
        }
    }
)


# ---------------------------------------------------------
# Resend email configuration
# ---------------------------------------------------------

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
RESEND_FROM_EMAIL = os.getenv(
    "RESEND_FROM_EMAIL",
    "onboarding@resend.dev"
)
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")


# ---------------------------------------------------------
# Configure Resend
# ---------------------------------------------------------

if RESEND_API_KEY:
    resend.api_key = RESEND_API_KEY


# ---------------------------------------------------------
# Email validation
# ---------------------------------------------------------

def valid_email(value):
    return bool(
        re.fullmatch(
            r"^[^\s@]+@[^\s@]+\.[^\s@]{2,}$",
            value or ""
        )
    )


# ---------------------------------------------------------
# Portfolio frontend
# ---------------------------------------------------------

@app.get("/")
def home():
    return send_from_directory(
        os.path.dirname(os.path.abspath(__file__)),
        "index.html"
    )


# ---------------------------------------------------------
# Contact form API
# ---------------------------------------------------------

@app.post("/api/contact")
def contact():

    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()
    sender_email = str(data.get("email", "")).strip()
    subject = str(data.get("subject", "")).strip()
    message = str(data.get("message", "")).strip()


    # -----------------------------------------------------
    # Validate form fields
    # -----------------------------------------------------

    if len(name) < 2:
        return jsonify({
            "success": False,
            "message": "Enter your name."
        }), 400


    if not valid_email(sender_email):
        return jsonify({
            "success": False,
            "message": "Enter a valid email address."
        }), 400


    if len(subject) < 3:
        return jsonify({
            "success": False,
            "message": "Enter a subject."
        }), 400


    if len(message) < 10:
        return jsonify({
            "success": False,
            "message": "Message must be at least 10 characters."
        }), 400


    # -----------------------------------------------------
    # Check environment configuration
    # -----------------------------------------------------

    if not RESEND_API_KEY:
        app.logger.error(
            "RESEND_API_KEY is missing."
        )

        return jsonify({
            "success": False,
            "message": "Mail service is not configured."
        }), 500


    if not RECEIVER_EMAIL:
        app.logger.error(
            "RECEIVER_EMAIL is missing."
        )

        return jsonify({
            "success": False,
            "message": "Receiver email is not configured."
        }), 500


    if not RESEND_FROM_EMAIL:
        app.logger.error(
            "RESEND_FROM_EMAIL is missing."
        )

        return jsonify({
            "success": False,
            "message": "Sender email is not configured."
        }), 500


    # -----------------------------------------------------
    # Check maximum field lengths
    # -----------------------------------------------------

    if (
        len(name) > 120
        or len(sender_email) > 254
        or len(subject) > 200
        or len(message) > 10000
    ):
        return jsonify({
            "success": False,
            "message": "One or more fields are too long."
        }), 400


    # -----------------------------------------------------
    # Escape user input for HTML email
    # -----------------------------------------------------

    safe_name = html.escape(name)
    safe_email = html.escape(sender_email)
    safe_subject = html.escape(subject)
    safe_message = html.escape(message).replace("\n", "<br>")


    # -----------------------------------------------------
    # HTML email design
    # -----------------------------------------------------

    html_content = f"""
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Portfolio Contact Message</title>

    <style>

        body {{
            margin: 0;
            padding: 0;
            background-color: #f4f7fb;
            font-family: Arial, Helvetica, sans-serif;
            color: #1f2937;
        }}

        .wrapper {{
            width: 100%;
            padding: 40px 15px;
            box-sizing: border-box;
        }}

        .container {{
            max-width: 680px;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid #e5e7eb;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        }}

        .header {{
            background: linear-gradient(
                135deg,
                #0f172a 0%,
                #172554 100%
            );
            padding: 32px;
            color: #ffffff;
        }}

        .brand {{
            font-size: 14px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: #38bdf8;
            margin-bottom: 12px;
        }}

        .title {{
            margin: 0;
            font-size: 28px;
            line-height: 1.3;
            font-weight: 700;
        }}

        .subtitle {{
            margin: 10px 0 0;
            font-size: 14px;
            line-height: 1.6;
            color: #cbd5e1;
        }}

        .content {{
            padding: 32px;
        }}

        .section-title {{
            margin: 0 0 20px;
            font-size: 16px;
            font-weight: 700;
            color: #111827;
        }}

        .info-grid {{
            display: block;
            margin-bottom: 28px;
        }}

        .info-item {{
            padding: 16px 18px;
            margin-bottom: 10px;
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
        }}

        .label {{
            display: block;
            margin-bottom: 6px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: #64748b;
        }}

        .value {{
            font-size: 15px;
            line-height: 1.5;
            color: #111827;
            word-break: break-word;
        }}

        .email-link {{
            color: #0284c7;
            text-decoration: none;
        }}

        .message-box {{
            margin-top: 10px;
            padding: 20px;
            background: #f8fafc;
            border-left: 4px solid #38bdf8;
            border-radius: 8px;
            font-size: 15px;
            line-height: 1.8;
            color: #334155;
            word-break: break-word;
        }}

        .reply-section {{
            margin-top: 28px;
            text-align: center;
        }}

        .reply-button {{
            display: inline-block;
            padding: 13px 24px;
            background: #0284c7;
            color: #ffffff !important;
            text-decoration: none;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 700;
        }}

        .footer {{
            padding: 22px 32px;
            background: #f8fafc;
            border-top: 1px solid #e5e7eb;
            text-align: center;
        }}

        .footer-text {{
            margin: 0;
            font-size: 12px;
            line-height: 1.6;
            color: #64748b;
        }}

        @media only screen and (max-width: 600px) {{

            .wrapper {{
                padding: 15px;
            }}

            .header {{
                padding: 25px 20px;
            }}

            .content {{
                padding: 25px 20px;
            }}

            .footer {{
                padding: 20px;
            }}

            .title {{
                font-size: 23px;
            }}

        }}

    </style>

</head>


<body>

<div class="wrapper">

    <div class="container">

        <!-- Header -->

        <div class="header">

            <div class="brand">
                Portfolio Contact
            </div>

            <h1 class="title">
                New Contact Message
            </h1>

            <p class="subtitle">
                Someone has submitted a message through your
                portfolio website.
            </p>

        </div>


        <!-- Content -->

        <div class="content">

            <h2 class="section-title">
                Contact Information
            </h2>


            <div class="info-grid">

                <!-- Name -->

                <div class="info-item">

                    <span class="label">
                        Name
                    </span>

                    <div class="value">
                        {safe_name}
                    </div>

                </div>


                <!-- Email -->

                <div class="info-item">

                    <span class="label">
                        Email
                    </span>

                    <div class="value">

                        <a
                            href="mailto:{safe_email}"
                            class="email-link"
                        >
                            {safe_email}
                        </a>

                    </div>

                </div>


                <!-- Subject -->

                <div class="info-item">

                    <span class="label">
                        Subject
                    </span>

                    <div class="value">
                        {safe_subject}
                    </div>

                </div>

            </div>


            <!-- Message -->

            <h2 class="section-title">
                Message
            </h2>

            <div class="message-box">
                {safe_message}
            </div>


            <!-- Reply -->

            <div class="reply-section">

                <a
                    href="mailto:{safe_email}?subject=Re: {safe_subject}"
                    class="reply-button"
                >
                    Reply to {safe_name}
                </a>

            </div>

        </div>


        <!-- Footer -->

        <div class="footer">

            <p class="footer-text">
                This message was sent from the contact form
                on your portfolio website.
            </p>

            <p class="footer-text">
                Portfolio Contact System
            </p>

        </div>

    </div>

</div>

</body>

</html>
"""


    # -----------------------------------------------------
    # Plain text fallback
    # -----------------------------------------------------

    plain_text = f"""
NEW PORTFOLIO CONTACT MESSAGE

Name:
{name}

Email:
{sender_email}

Subject:
{subject}

Message:
{message}

----------------------------------------

Reply directly to:
{sender_email}

This message was sent from the portfolio contact form.
"""


    # -----------------------------------------------------
    # Send email using Resend HTTPS API
    # -----------------------------------------------------

    try:

        email_response = resend.Emails.send({
            "from": f"Portfolio Contact <{RESEND_FROM_EMAIL}>",
            "to": [RECEIVER_EMAIL],
            "subject": f"Portfolio Contact: {subject}",
            "reply_to": sender_email,
            "html": html_content,
            "text": plain_text
        })

        app.logger.info(
            "Portfolio email sent successfully: %s",
            email_response
        )

        return jsonify({
            "success": True,
            "message": "Message sent successfully."
        }), 200


    # -----------------------------------------------------
    # Resend / API error
    # -----------------------------------------------------

    except Exception:

        app.logger.exception(
            "Resend error while sending portfolio message."
        )

        return jsonify({
            "success": False,
            "message": "Unable to send the message right now."
        }), 500


# ---------------------------------------------------------
# Run Flask server
# ---------------------------------------------------------

if __name__ == "__main__":

    port = int(
        os.getenv("PORT", 5000)
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
