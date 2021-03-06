from util import hook, strip_formatting
from datetime import datetime
import re

taned = False

@hook.event('*')
def tane_event(paraml, conn=None):
    global taned
    today = datetime.today()
    if today.weekday() == 4 and today.hour == 18 and not taned:
        taned = True
        conn.cmd('PRIVMSG #sa-minecraft ' + rainbow("I CAN'T WAIT"))
        conn.cmd('PRIVMSG #sa-minecraft http://tane.us/weekend.html')
        conn.cmd('PRIVMSG #sa-minecraft ' + rainbow("FOR THE WEEKEND TO BEGIN"))

    if today.weekday() != 4:
        taned = False

@hook.command
def tane(inp, say=None):
    say(rainbow('death comes to us all'))
    return
    say(rainbow("I CAN'T WAIT"))
    say('http://tane.us/weekend.html')
    say(rainbow("FOR THE WEEKEND TO BEGIN"))

def rainbow(text):
    c =['\x0304', '\x0307', '\x0309', '\x0310', '\x0306']
    text = strip_formatting.strip(text)
    out = ""
    l = len(c)
    for i, t in enumerate(text):
        out += c[i % l] + t
    return out
