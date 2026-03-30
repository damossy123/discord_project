import discord_webhook
from flask import Flask,request,render_template , jsonify
from discord_webhook import DiscordWebhook
import sqlite3
from datetime import datetime , timedelta

app = Flask(__name__)

# create DataBase
connection = sqlite3.connect("conversation.db")
cursor = connection.cursor()
#cursor.execute('''DROP TABLE IF  EXISTS conversation''')
cursor.execute('''CREATE TABLE IF NOT EXISTS conversation
 (id INTEGER PRIMARY KEY AUTOINCREMENT ,text NOT NULL ,timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);''')
connection.commit()
connection.close()

# save in database
def send_to_database(text_to_send):
    connection = sqlite3.connect("conversation.db")
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO conversation (text) VALUES (?)''',(text_to_send,))
    connection.commit()
    connection.close()

# send to discord functions
discordwebhook_url = "your discord webhook url"
def send_to_discord(text):
    webhook = DiscordWebhook(url=discordwebhook_url , content=text)
    webhook.execute()


@app.route('/')
def hello():
    return render_template('main.html')


#Endpoint 1
@app.route('/input_text',methods=["POST"])
def input_text():
    user_text = request.form.get("text")
    if user_text:
        send_to_database(user_text)
        send_to_discord(user_text)
        return f"your message sent successfully {user_text}"
    return "Please enter a text"


#Endpoint 2
@app.route('/discord_integration')
def discord_integration():
    return discord_webhook.DiscordWebhook(url=discordwebhook_url)

#Endpoint 3
@app.route('/message_retrieval')
def get_message():
    try:
        connection = sqlite3.connect("conversation.db")
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM conversation WHERE timestamp > datetime('now','-30 minutes');''')
        #('''SELECT text ,timestamp FROM conversation WHERE timestamp >= datetime('now','-30 minutes');''')
        rows = cursor.fetchall()
        return jsonify(rows)
    except Exception as e:
        return f"error retrieving messages {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)

