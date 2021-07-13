import os
from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib
import random
import songdata
from songdata import *

load_dotenv(".env")
SENDER = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PASSWORD")
RECIPIENT = os.environ.get("EMAIL_RECIPIENT")
SUBJECT = os.environ.get("EMAIL_SUBJECT_LINE")
EMAIL_ENABLED = (os.environ.get("EMAIL_ENABLED", 'False') == 'True')

# GENERATE A TRACK TEMPO
bpm = str(random.randint(bpm_range[0]/10,bpm_range[1]/10)*10)

# WEIGHTED PROBABILITY FOR SONG LENGTH
# 1:00 => 10%
# 2:00 => 20%
# 3:00 => 40%
# 4:00 => 20%
# 5:00 => 10%
length = ["1:00"] + ["2:00"] * 2 + ["3:00"] * 4 + ["4:00"] * 2 + ["5:00"]

genre = random.choice(genre_list)
i = random.choice(range(len(key_list)))
key = key_list[i]
pitches = pitch_list[i]

# WEIGHTED PROBABILITY FOR SYSTEM SELECTION,
# BASED ON # OF ITEMS IN EACH SYSTEM LIST
# (THE MORE GEAR IN A SYSTEM, THE HIGHER THE WEIGHTING)
# SYSTEM 0 : BIG RIG (CIRKLON OR NERDSEQ OR TELETYPE)
# SYSTEM 1 : MIDI DEVICES (CIRKLON OR NERDSEQ)
# SYSTEM 2 : SOUND TOYS (NO SEQUENCER)
# SYSTEM 3 : STANDALONE (NO SEQUENCER)
# SYSTEM 4 : HIGH LEVEL (CIRKLON OR NERDSEQ OR TELETYPE OR NO SEQUENCER)
system_weights = [0] * len(system_list[0]) + [1] * len(system_list[1]) + [2] * len(system_list[2]) + [3] * len(system_list[3]) + [4] * len(system_list[4])

system_selection = random.choice(system_weights)
sounds = random.sample(system_list[system_selection], random.randint(1, 3))

sequencer_prepend = ""
sequencer = random.choice(sequencer_list[system_selection])

# IF SYSTEM 0 BIG RIG IS SELECTED, CHECK IF 
# THERE ARE ANY MIDI DEVICES IN SOUND SOURCES
# IF THERE ARE AND THE SEQUENCER IS TELETYPE,
# RANDOMLY RESELECT SEQUENCER FROM SYSTEM 1 SEQUENCER OPTIONS
if system_selection == 0 :
	check = any(item in sounds for item in system_list[1])
	if check is True and sequencer == "Teletype" :
		sequencer = random.choice(sequencer_list[1])

# IF NO SEQUENCER IS SELECTED, DO NOT LIST IT
# IN THE FULL PRINTOUT OF THE RAVE STRATEGY
if sequencer == "none" :
	sequencer = ""
else :
	sequencer_prepend = " sequenced by "

# ASSEMBLE THE RAVE STRATEGY
strategy = "Write a " + bpm + "bpm " + genre + " track in " + key + " using " + " / ".join(sounds) + sequencer_prepend + sequencer + " with a duration of ~" + random.choice(length) + ". \n\nIt should " + random.choice(action_list) + " like " + random.choice(thing_list) + " " + random.choice(context_list) + ". \n\n" + pitches

# CONSTRUCT THE EMAIL
def send_email(recipient, subject, body) :
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = recipient
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(SENDER, PASSWORD)
    server.send_message(msg)
    server.quit()

if EMAIL_ENABLED:
    try:
        send_email(RECIPIENT, subject=SUBJECT, body=strategy)
        print("Message sent to", RECIPIENT)
    except smtplib.SMTPAuthenticationError as e:
        print("Authentication error. Update email credentials in .env.\n", e)
else:
    print(strategy);
