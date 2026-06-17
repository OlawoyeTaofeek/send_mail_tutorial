# AIJobPartner

A lightweight Python birthday email generator that personalizes a template, builds a styled HTML email, and sends it via SMTP.

## ✅ What this project does

- Reads a birthday message template from `data/Birthday_Wish_Template.txt`
- Replaces placeholders like `{name}` and `[Your Name]`
- Builds a polished HTML birthday email using `build_html.py`
- Sends the email through SMTP using `send.py`

## 🌟 Why it exists

This project demonstrates how to combine template personalization with HTML email creation and SMTP delivery in Python. It is ideal for sending custom birthday greetings with a professional, modern email design.

## 🚀 Files

- `app.py` — project entry point; personalizes the template, builds the HTML, and sends the email
- `build_html.py` — generates the HTML email body with a birthday banner, paragraphs, and footer
- `send.py` — sends the email via SMTP (default is Gmail)
- `utils.py` — loads environment variables and personalizes the template
- `data/Birthday_Wish_Template.txt` — the birthday message template with placeholder fields
- `WhatsApp Image 2026-06-17 at 12.50.19.jpeg` — preview screenshot showing the email output

## 🛠️ Requirements

- Python 3.8+
- `python-dotenv`

Install dependencies:

```bash
pip install python-dotenv
```

## ⚙️ Setup

1. Create a `.env` file at the project root.
2. Add your SMTP credentials:

```env
my_email=youremail@example.com
my_password=YOUR_SMTP_PASSWORD
```

> If you use Gmail, create an App Password and use that value for `my_password`.

## ▶️ Run the app

```bash
python app.py
```

The script uses the built-in template, replaces `{name}` with the recipient name, replaces `[Your Name]` with the sender name, generates the HTML email, and sends it to the recipient configured in `app.py`.

## ✏️ Customization

- Edit `data/Birthday_Wish_Template.txt` to change the message.
- Modify `app.py` to send to a different email address or use a different recipient name.
- Update the HTML styling in `build_html.py` for a custom visual theme.

## 📸 Output Preview

The screenshot below shows the generated birthday email HTML rendered in an email client, including the festive banner, personalized greeting, and footer.

![Birthday email preview](WhatsApp%20Image%202026-06-17%20at%2012.50.19.jpeg)

## 💡 Notes

- The current example in `app.py` sends to `jtee71708@gmail.com`.
- The app is built for demonstration and can be extended into a reusable email automation tool.
