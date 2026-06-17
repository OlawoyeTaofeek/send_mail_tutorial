from utils import email, my_password, modify, read_file
from build_html import build_birthday_email
from send import send_birthday_email
import os


print(email)

def main():
    content = modify(read_file("data/Birthday_Wish_Template.txt"), "Teejay", "Taofeek")
    # print(content)
    html = build_birthday_email(name="Teejay", body_text=content, sender_name="Taofeek")
    # print(html)
    send_birthday_email("jtee71708@gmail.com", "Happy Birthday, Teejay! 🎉", html, email, my_password)

main()