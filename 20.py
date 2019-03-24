# -*- coding: utf-8 -*- 
import DRAGON
from DRAGON import *
from dkbot.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from humanfriendly import format_timespan, format_size, format_number, format_length
from time import sleep
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse
from datetime import timedelta, date
from datetime import datetime
from gtts import gTTS
import html5lib,shutil
import wikipedia,goslate
import ffmpy
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
#import pyimgflip

cl = LineClient()
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

ki = LineClient()
ki.log("Auth Token : " + str(ki.authToken))
ki.log("Channel Access Token : " + str(channel.channelAccessToken))

kk = LineClient()
kk.log("Auth Token : " + str(kk.authToken))
kk.log("Channel Access Token : " + str(channel.channelAccessToken))

kc = LineClient()
kc.log("Auth Token : " + str(kc.authToken))
kc.log("Channel Access Token : " + str(channel.channelAccessToken))

kb = LineClient()
kb.log("Auth Token : " + str(kb.authToken))
kb.log("Channel Access Token : " + str(channel.channelAccessToken))

kd = LineClient()
kd.log("Auth Token : " + str(kd.authToken))
kd.log("Channel Access Token : " + str(channel.channelAccessToken))

ke = LineClient()
ke.log("Auth Token : " + str(ke.authToken))
ke.log("Channel Access Token : " + str(channel.channelAccessToken))

kf = LineClient()
kf.log("Auth Token : " + str(kf.authToken))
kf.log("Channel Access Token : " + str(channel.channelAccessToken))

k8 = LineClient()
k8.log("Auth Token : " + str(k8.authToken))
k8.log("Channel Access Token : " + str(channel.channelAccessToken))

k9 = LineClient()
k9.log("Auth Token : " + str(k9.authToken))
k9.log("Channel Access Token : " + str(channel.channelAccessToken))

k10 = LineClient()
k10.log("Auth Token : " + str(k10.authToken))
k10.log("Channel Access Token : " + str(channel.channelAccessToken))

k11 = LineClient()
k11.log("Auth Token : " + str(k11.authToken))
k11.log("Channel Access Token : " + str(channel.channelAccessToken))

k12 = LineClient()
k12.log("Auth Token : " + str(k12.authToken))
k12.log("Channel Access Token : " + str(channel.channelAccessToken))

k13 = LineClient()
k13.log("Auth Token : " + str(k13.authToken))
k13.log("Channel Access Token : " + str(channel.channelAccessToken))

k14 = LineClient()
k14.log("Auth Token : " + str(k14.authToken))
k14.log("Channel Access Token : " + str(channel.channelAccessToken))

k15 = LineClient()
k15.log("Auth Token : " + str(k15.authToken))
k15.log("Channel Access Token : " + str(channel.channelAccessToken))

k16 = LineClient()
k16.log("Auth Token : " + str(k16.authToken))
k16.log("Channel Access Token : " + str(channel.channelAccessToken))

k17 = LineClient()
k17.log("Auth Token : " + str(k17.authToken))
k17.log("Channel Access Token : " + str(channel.channelAccessToken))

k18 = LineClient()
k18.log("Auth Token : " + str(k18.authToken))
k18.log("Channel Access Token : " + str(channel.channelAccessToken))

k19 = LineClient()
k19.log("Auth Token : " + str(k19.authToken))
k19.log("Channel Access Token : " + str(channel.channelAccessToken))

k20 = LineClient()
k20.log("Auth Token : " + str(k20.authToken))
k20.log("Channel Access Token : " + str(channel.channelAccessToken))

kj = LineClient()
kj.log("Auth Token : " + str(kj.authToken))
kj.log("Channel Access Token : " + str(channel.channelAccessToken))

sw = LineClient()
sw.log("Auth Token : " + str(sw.authToken))
sw.log("Channel Access Token : " + str(channel.channelAccessToken))
print("\nBY: SELFBOT-BY:MAI\n")

poll = LinePoll(cl)
call = cl
creator = ["uc66e45201d1612eb4ce7b3a86bac4685"]
owner = ["uc66e45201d1612eb4ce7b3a86bac4685"]
admin = ["uc66e45201d1612eb4ce7b3a86bac4685"]
staff = ["uc66e45201d1612eb4ce7b3a86bac4685"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kb.getProfile().mid
Emid = kd.getProfile().mid
Fmid = ke.getProfile().mid
Gmid = kf.getProfile().mid
mid8 = k8.getProfile().mid
mid9 = k9.getProfile().mid
mid10 = k10.getProfile().mid
mid11 = k11.getProfile().mid
mid12 = k12.getProfile().mid
mid13 = k13.getProfile().mid
mid14 = k14.getProfile().mid
mid15 = k15.getProfile().mid
mid16 = k16.getProfile().mid
mid17 = k17.getProfile().mid
mid18 = k18.getProfile().mid
mid19 = k19.getProfile().mid
mid20 = k20.getProfile().mid
Jmid = kj.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl,ki,kk,kc,kb,kd,ke,kf,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20,kj,sw]
ABC = [cl,ki,kk,kc,kb,kd,ke,kf,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20,kj,sw]
GHOST = [kj,sw]
Bots = [mid,Amid,Bmid,Dmid,Emid,Fmid,Gmid,mid8,mid9,mid10,mid11,mid12,mid13,mid14,mid15,mid16,mid17,mid18,mid19,mid20,Jmid,Zmid]
Saints = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectantijs = []
protectinvite = []
protectcancel = []
ghost = []
welcome = []
left = []
msg_dict = {}
msg_dict1 = {}

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = kb.getProfile().displayName
responsename5 = kd.getProfile().displayName
responsename6 = ke.getProfile().displayName
responsename7 = kf.getProfile().displayName
responsename8 = k8.getProfile().displayName
responsename9 = k9.getProfile().displayName
responsename10 = k10.getProfile().displayName
responsename11 = k11.getProfile().displayName
responsename12 = k12.getProfile().displayName
responsename13 = k13.getProfile().displayName
responsename14 = k14.getProfile().displayName
responsename15 = k15.getProfile().displayName
responsename16 = k16.getProfile().displayName
responsename17 = k17.getProfile().displayName
responsename18 = k18.getProfile().displayName
responsename19 = k19.getProfile().displayName
responsename20 = k20.getProfile().displayName
responsename21 = kj.getProfile().displayName
responsename22 = sw.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "SpamInvite":False,
    "changeCover":False,
    "changeVideo":False,
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userMention":{},
    "timeRestart": {},
    "server": {},
    "simiSimi":{},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
}

wait = {
    "Limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "contact":False,
    "invite":False,
    'autoJoin':False,
    'autoAdd':False,
    'autoBlock':True,
    'Timeline':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "mentionKick":False,
    "welcomeOn":False,
    "likeOn":True,
    "stickerOn":False,
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
            "displayName": "",
            "coverId": "",
            "pictureStatus": "",
            "statusMessage": ""
            },
    "unsend":False,
    "mention":"BY:MAI",
    "Respontag":"BY:MAI",
    "welcome":"BY:MAI",
    "leave":"Slamat tinggal sobat\nsmoga ktmu di lain hari nanti",
    "comment":"BY:MAI",
    "message":"[ Auto block ]\n ผมบล็อกคุนไว้แล้วกรุนารอผมมา 😭",
}
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

coverId = {}


lineProfile = cl.getProfile()
backup = cl.getProfile()
backup.displayName = lineProfile.displayName
backup.statusMessage = lineProfile.statusMessage
backup.pictureStatus = lineProfile.pictureStatus


with open('creator.json', 'r') as fp:
     creator = json.load(fp)
with open('owner.json', 'r') as fp:
     owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
Setmain = json.load(Setbot)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "「 Daftar Member 」\n\n1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "「✭」{}. ".format(str(no))
            else:
                textx += "\n「 Total {} Member 」".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
           
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Auto Welcome 」\nɦαℓℓσ.......  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+" Di "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Respon Leave 」\nBaper Ya Kak ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ki.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict1[msg_id]

def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "🇹🇭❂͜͡➣      「 💘 คำสั่ง 💘 」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คำสั่ง\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คำสั่ง1\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คำสั่ง2\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คำสั่ง3\n" + \
                  "🇹🇭❂͜͡➣ " + key + "!mai\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เช็ค\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ข้อมูล\n" + \
                  "🇹🇭❂͜͡➣ " + key + "รีบอท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ออน\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ผส\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Sp\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Spb\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ประกาศ:「ข้อความ」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งบอทคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งเชลคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งแอดมินคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ลบบอทคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ลบเชลคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ลบแอดมินคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดข้อความ\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เชคบอท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คิกมา\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คิกออก\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ผีมา\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ผีออก\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เชิญผี\n" + \
                  "🇹🇭         💘 คำสั่งบอท 💘\n" + \
                  "🇹🇭❂͜͡➣ " + key + "บอท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เชิญบอท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เชคดำ\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ล้างดำ\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งแอดมิน @\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ลบแอดมิน @\n" + \
                  "🇹🇭❂͜͡➣ " + key + "รูป1-20\n" + \
                  "🇹🇭❂͜͡➣ " + key + "protectkick on\off\n" + \
                  "🇹🇭❂͜͡➣ " + key + "protectjoin on\off\n" + \
                  "🇹🇭❂͜͡➣ " + key + "protectinvite on\off\n" + \
                  "🇹🇭❂͜͡➣ " + key + "protecturl on\off\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Ghost on\off\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Allpro on\off\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Antijs on\n" + \
                  "🇹🇭❂͜͡➣ BY:MAI"

    return helpMessage

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return

        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventJoinByTicket = False
                            cl.updateGroup(X)
                            Ti = cl.reissueGroupTicket(op.param1)
                            kj.acceptGroupInvitationByTicket(op.param1,Ti)
                            kj.kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                            X = kj.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            kj.updateGroup(X)
                            kj.leaveGroup(op.param1)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            kb.reissueGroupTicket(op.param1)
                                            X = kb.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            cl.updateGroup(X)
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if kd.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                kd.reissueGroupTicket(op.param1)
                                                X = kd.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                kd.updateGroup(X)
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    ke.reissueGroupTicket(op.param1)
                                                    X = ke.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    ke.updateGroup(X)
                                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)            
                                        except:
                                            try:
                                                if kf.getGroup(op.param1).preventedJoinByTicket == False:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        kf.reissueGroupTicket(op.param1)
                                                        X = kf.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        kf.updateGroup(X)
                                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)           
                                            except:
                                                try:
                                                    if k20.getGroup(op.param1).preventedJoinByTicket == False:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            k20.reissueGroupTicket(op.param1)
                                                            X = k20.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            k20.updateGroup(X)
                                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)          
                                                except:
                                                    try:
                                                        if sw.getGroup(op.param1).preventedJoinByTicket == False:
                                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                sw.reissueGroupTicket(op.param1)
                                                                X = sw.getGroup(op.param1)
                                                                X.preventedJoinByTicket = True
                                                                sw.updateGroup(X)
                                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)             
                                                    except:
                                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)           
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.leaveGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
            if mid8 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k8.acceptGroupInvitation(op.param1)
                        ginfo = k8.getGroup(op.param1)
                    else:
                        k8.acceptGroupInvitation(op.param1)
                        ginfo = k8.getGroup(op.param1)
            if mid9 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k9.acceptGroupInvitation(op.param1)
                        ginfo = k9.getGroup(op.param1)
                        k9.leaveGroup(op.param1)
                    else:
                        k9.acceptGroupInvitation(op.param1)
                        ginfo = k9.getGroup(op.param1)
            if mid10 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k10.acceptGroupInvitation(op.param1)
                        ginfo = k10.getGroup(op.param1)
                        k10.leaveGroup(op.param1)
                    else:
                        k10.acceptGroupInvitation(op.param1)
                        ginfo = k10.getGroup(op.param1)
            if mid11 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k11.acceptGroupInvitation(op.param1)
                        ginfo = k11.getGroup(op.param1)
                        k11.leaveGroup(op.param1)
                    else:
                        k11.acceptGroupInvitation(op.param1)
                        ginfo = k11.getGroup(op.param1)
            if mid12 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k12.acceptGroupInvitation(op.param1)
                        ginfo = k12.getGroup(op.param1)
                        k12.leaveGroup(op.param1)
                    else:
                        k12.acceptGroupInvitation(op.param1)
                        ginfo = k12.getGroup(op.param1)
            if mid13 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k13.acceptGroupInvitation(op.param1)
                        ginfo = k13.getGroup(op.param1)
                        k13.leaveGroup(op.param1)
                    else:
                        k13.acceptGroupInvitation(op.param1)
                        ginfo = k13.getGroup(op.param1)
            if mid14 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k14.acceptGroupInvitation(op.param1)
                        ginfo = k14.getGroup(op.param1)
                        k14.leaveGroup(op.param1)
                    else:
                        k14.acceptGroupInvitation(op.param1)
                        ginfo = k14.getGroup(op.param1)           
            if mid15 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k15.acceptGroupInvitation(op.param1)
                        ginfo = k15.getGroup(op.param1)
                        k15.leaveGroup(op.param1)
                    else:
                        k15.acceptGroupInvitation(op.param1)
                        ginfo = k15.getGroup(op.param1)
            if mid16 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k16.acceptGroupInvitation(op.param1)
                        ginfo = k16.getGroup(op.param1)
                        k16.leaveGroup(op.param1)
                    else:
                        k16.acceptGroupInvitation(op.param1)
                        ginfo = k16.getGroup(op.param1)
            if mid17 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k17.acceptGroupInvitation(op.param1)
                        ginfo = k17.getGroup(op.param1)
                        k17.leaveGroup(op.param1)
                    else:
                        k17.acceptGroupInvitation(op.param1)
                        ginfo = k17.getGroup(op.param1)
            if mid18 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k18.acceptGroupInvitation(op.param1)
                        ginfo = k18.getGroup(op.param1)
                        k18.leaveGroup(op.param1)
                    else:
                        k18.acceptGroupInvitation(op.param1)
                        ginfo = k18.getGroup(op.param1)
            if mid19 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k19.acceptGroupInvitation(op.param1)
                        ginfo = k19.getGroup(op.param1)
                        k19.leaveGroup(op.param1)
                    else:
                        k19.acceptGroupInvitation(op.param1)
                        ginfo = k19.getGroup(op.param1)
            if mid20 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k20.acceptGroupInvitation(op.param1)
                        ginfo = k20.getGroup(op.param1)
                        k20.leaveGroup(op.param1)
                    else:
                        k20.acceptGroupInvitation(op.param1)
                        ginfo = k20.getGroup(op.param1)                       

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = kb.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            kb.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = kd.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                kd.cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = ke.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    ke.cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = kf.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            kf.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = k8.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                k8.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = k9.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    k9.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = k10.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        k10.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = k11.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            k11.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = k12.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                k12.cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = k13.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    k13.cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                pass 
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = k14.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            k14.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = k15.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                k15.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = k16.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    k16.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = k17.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        k17.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = k18.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            k18.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = k19.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                k19.cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = k20.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    k20.cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                pass                                            

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                    
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                    
        if op.type == 13:
            if op.param3 in wait["blacklist"]:
                    try:
                        random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                    except:
                        pass
 
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
                
        if op.type == 17:
            if op.param1 in left:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leftMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
                sendMention(to, "ãAuto Mentionã\nâ«@!", [sender])
                cl.sendContact(to, sender)    
                
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k9.kickoutFromGroup(op.param1,[op.param2])          
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                kb.kickoutFromGroup(op.param1,[op.param2])         
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                               try:
                                                   if op.param3 not in wait["blacklist"]:
                                                       ke.kickoutFromGroup(op.param1,[op.param2])      
                                               except:
                                                  try:
                                                      if op.param3 not in wait["blacklist"]:
                                                          kf.kickoutFromGroup(op.param1,[op.param2]) 
                                                  except:
                                                     try:
                                                         if op.param3 not in wait["blacklist"]:
                                                             k17.kickoutFromGroup(op.param1,[op.param2])        
                                                     except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                if op.param3 not in wait["blacklist"]:
                                                                    k11.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                               try:
                                                                   if op.param3 not in wait["blacklist"]:
                                                                       k12.kickoutFromGroup(op.param1,[op.param2])
                                                               except:
                                                                  try:
                                                                      if op.param3 not in wait["blacklist"]:
                                                                          k13.kickoutFromGroup(op.param1,[op.param2])  
                                                                  except:
                                                                     try:
                                                                         if op.param3 not in wait["blacklist"]:
                                                                             k14.kickoutFromGroup(op.param1,[op.param2])
                                                                     except:
                                                                        try:
                                                                            if op.param3 not in wait["blacklist"]:
                                                                                k15.kickoutFromGroup(op.param1,[op.param2])  
                                                                        except:
                                                                           try:
                                                                               if op.param3 not in wait["blacklist"]:
                                                                                    k16.kickoutFromGroup(op.param1,[op.param2])        
                                                                           except:
                                                                               pass  
                return

        if op.type == 5:
              if wait["autoAdd"] == True:
                  cl.findAndAddContactsByMid(op.param1)
                  sendMention(op.param1, op.param1, "Haii ", ", terimakasih sudah add saya")
                  cl.sendText(op.param1, wait["message"])
                  cl.sendContact(op.param1, "uc66e45201d1612eb4ce7b3a86bac4685")

        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wait["autoBlock"] == True:
                cl.sendText(op.param1, wait["message"])
                cl.sendContact(op.param1, "uc66e45201d1612eb4ce7b3a86bac4685")
                cl.blockContact(op.param1)

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                	pass

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = kb.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            kb.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = kd.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                kd.cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = kf.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    kf.cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = k8.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            k8.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = k9.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                k9.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = k10.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    k10.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = k11.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        k11.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = k12.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            k12.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = k13.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                k13.cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = k14.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    k14.cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = k15.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            k15.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = k16.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                k16.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = k17.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    k17.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = k18.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        k18.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = k19.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            k19.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = k20.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                k20.cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = kj.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    kj.cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                pass                                            

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
                
        if op.type == 19:
            if op.param1 in ghost:
                try:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        sw.sendMessage(op.param1,"Wah kiker tempe mai kick orang minta di hajar")
                        sw.leaveGroup(op.param1)
                        kj.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                except:
                    try:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ki.updateGroup(G)
                            invsend = 0
                            Ticket = ki.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                            sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                            sw.leaveGroup(op.param1)
                            kj.leaveGroup(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            ki.updateGroup(X)
                    except:
                        try:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kk.updateGroup(G)
                                invsend = 0
                                Ticket = kk.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                                sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                sw.leaveGroup(op.param1)
                                kj.leaveGroup(op.param1)
                                X = kk.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                kk.updateGroup(X)
                        except:
                            try:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.updateGroup(G)
                                    invsend = 0
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                    sw.sendMessage(op.param1,"Wah kiker tempe mai kick orang minta di hajar")
                                    sw.leaveGroup(op.param1)
                                    kj.leaveGroup(op.param1)
                                    X = kc.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kc.updateGroup(X)
                            except:
                                try:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        G = kb.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kb.updateGroup(G)
                                        invsend = 0
                                        Ticket = kb.reissueGroupTicket(op.param1)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                        sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                        sw.leaveGroup(op.param1)
                                        kj.leaveGroup(op.param1)
                                        X = kb.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kb.updateGroup(X)
                                except:
                                    try:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kd.updateGroup(G)
                                            invsend = 0
                                            Ticket = kd.reissueGroupTicket(op.param1)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                            sw.sendMessage(op.param1,"Terdeteksi Kicker,Maaf anda melangar")
                                            sw.leaveGroup(op.param1)
                                            kj.leaveGroup(op.param1)
                                            X = kd.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            kd.updateGroup(X)
                                    except:
                                        try:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                G = ke.getGroup(op.param1)
                                                G.preventedJoinByTicket = False
                                                ke.updateGroup(G)
                                                invsend = 0
                                                Ticket = ke.reissueGroupTicket(op.param1)
                                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True
                                                sw.sendMessage(op.param1,"Terdeteksi kicker\nMaaf anda mepanggar")
                                                sw.leaveGroup(op.param1)
                                                kj.leaveGroup(op.param1)
                                                X = ke.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ke.updateGroup(X)
                                        except:
                                            try:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    G = kf.getGroup(op.param1)
                                                    G.preventedJoinByTicket = False
                                                    kf.updateGroup(G)
                                                    invsend = 0
                                                    Ticket = kf.reissueGroupTicket(op.param1)
                                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True
                                                    sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                                    sw.leaveGroup(op.param1)
                                                    kj.leaveGroup(op.param1)
                                                    X = kf.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    kf.updateGroup(X)      
                                            except:
                                                try:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        G = k8.getGroup(op.param1)
                                                        G.preventedJoinByTicket = False
                                                        k8.updateGroup(G)
                                                        invsend = 0
                                                        Ticket = k8.reissueGroupTicket(op.param1)
                                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                        wait["blacklist"][op.param2] = True
                                                        sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                                        sw.leaveGroup(op.param1)
                                                        kj.leaveGroup(op.param1)
                                                        X = k8.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        k8.updateGroup(X)  
                                                except:
                                                    try:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            G = k9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            k9.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = k9.reissueGroupTicket(op.param1)
                                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                            wait["blacklist"][op.param2] = True
                                                            sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                                            sw.leaveGroup(op.param1)
                                                            kj.leaveGroup(op.param1)
                                                            X = k9.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            k9.updateGroup(X)     
                                                    except:
                                                        pass
                  
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        cl.findAndAddContactsByMid(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                if op.param3 in Jmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Jmid])
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Jmid])                                        
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                else:
                    pass
            except:
                pass
                
        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
         
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                k11.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            k12.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k13.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k14.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k15.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k16.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                k17.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            k18.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k19.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k20.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kj.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass                                           
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    passl
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])                   
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            G = cl.getGroup(op.param1)
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                        k8.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                                            k9.inviteIntoGroup(op.param1,[op.param3])
                                                            cl.acceptGroupInvitation(op.param1)
                                                        except:
                                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = ki.getGroup(op.param1)
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                                        k9.inviteIntoGroup(op.param1,[op.param3])
                                                        ki.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                                            k10.inviteIntoGroup(op.param1,[op.param3])
                                                            ki.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kk.getGroup(op.param1)
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k8.kickoutFromGroup(op.param1,[op.param2])
                                                k8.inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k9.kickoutFromGroup(op.param1,[op.param2])
                                                    k9.inviteIntoGroup(op.param1,[op.param3])
                                                    kk.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                                        k10.inviteIntoGroup(op.param1,[op.param3])
                                                        kk.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k11.kickoutFromGroup(op.param1,[op.param2])
                                                            k11.inviteIntoGroup(op.param1,[op.param3])
                                                            kk.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                    kf.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                        k8.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kc.getGroup(op.param1)
                                            G = kb.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.updateGroup(G)
                                            Ticket = kb.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kb.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kb.updateGroup(G)
                                            Ticket = kb.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k9.kickoutFromGroup(op.param1,[op.param2])
                                                k9.inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                                    k10.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k11.kickoutFromGroup(op.param1,[op.param2])
                                                        k11.inviteIntoGroup(op.param1,[op.param3])
                                                        kc.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k12.kickoutFromGroup(op.param1,[op.param2])
                                                            k12.inviteIntoGroup(op.param1,[op.param3])
                                                            kc.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                    kb.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                        k9.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kb.getGroup(op.param1)
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.updateGroup(G)
                                            Ticket = kd.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kd.updateGroup(G)
                                            Ticket = kd.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                                k10.inviteIntoGroup(op.param1,[op.param3])
                                                kb.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k11.kickoutFromGroup(op.param1,[op.param2])
                                                    k11.inviteIntoGroup(op.param1,[op.param3])
                                                    kb.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k12.kickoutFromGroup(op.param1,[op.param2])
                                                        k12.inviteIntoGroup(op.param1,[op.param3])
                                                        kb.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k13.kickoutFromGroup(op.param1,[op.param2])
                                                            k13.inviteIntoGroup(op.param1,[op.param3])
                                                            kb.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            k9.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                    kd.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                        k10.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kd.getGroup(op.param1)
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.updateGroup(G)
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ke.updateGroup(G)
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k11.kickoutFromGroup(op.param1,[op.param2])
                                                k11.inviteIntoGroup(op.param1,[op.param3])
                                                kd.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k12.kickoutFromGroup(op.param1,[op.param2])
                                                    k12.inviteIntoGroup(op.param1,[op.param3])
                                                    kd.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k13.kickoutFromGroup(op.param1,[op.param2])
                                                        k13.inviteIntoGroup(op.param1,[op.param3])
                                                        kd.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k14.kickoutFromGroup(op.param1,[op.param2])
                                                            k14.inviteIntoGroup(op.param1,[op.param3])
                                                            kd.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        kf.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k8.kickoutFromGroup(op.param1,[op.param2])
                            k8.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k9.kickoutFromGroup(op.param1,[op.param2])
                                k9.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                    k10.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k11.kickoutFromGroup(op.param1,[op.param2])
                                        k11.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = ke.getGroup(op.param1)
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.updateGroup(G)
                                            Ticket = kf.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kf.updateGroup(G)
                                            Ticket = kf.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k12.kickoutFromGroup(op.param1,[op.param2])
                                                k12.inviteIntoGroup(op.param1,[op.param3])
                                                ke.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k13.kickoutFromGroup(op.param1,[op.param2])
                                                    k13.inviteIntoGroup(op.param1,[op.param3])
                                                    ke.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k14.kickoutFromGroup(op.param1,[op.param2])
                                                        k14.inviteIntoGroup(op.param1,[op.param3])
                                                        ke.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k15.kickoutFromGroup(op.param1,[op.param2])
                                                            k15.inviteIntoGroup(op.param1,[op.param3])
                                                            ke.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if mid8 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k8.kickoutFromGroup(op.param1,[op.param2])
                        k8.inviteIntoGroup(op.param1,[op.param3])
                        kf.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            k9.inviteIntoGroup(op.param1,[op.param3])
                            kf.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k10.kickoutFromGroup(op.param1,[op.param2])
                                k10.inviteIntoGroup(op.param1,[op.param3])
                                kf.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k11.kickoutFromGroup(op.param1,[op.param2])
                                    k11.inviteIntoGroup(op.param1,[op.param3])
                                    kf.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k12.kickoutFromGroup(op.param1,[op.param2])
                                        k12.inviteIntoGroup(op.param1,[op.param3])
                                        kf.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kf.getGroup(op.param1)
                                            G = k8.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k8.kickoutFromGroup(op.param1,[op.param2])
                                            k8.updateGroup(G)
                                            Ticket = k8.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k8.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k8.updateGroup(G)
                                            Ticket = k8.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k13.kickoutFromGroup(op.param1,[op.param2])
                                                k13.inviteIntoGroup(op.param1,[op.param3])
                                                kf.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k14.kickoutFromGroup(op.param1,[op.param2])
                                                    k14.inviteIntoGroup(op.param1,[op.param3])
                                                    kf.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k15.kickoutFromGroup(op.param1,[op.param2])
                                                        k15.inviteIntoGroup(op.param1,[op.param3])
                                                        kf.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k16.kickoutFromGroup(op.param1,[op.param2])
                                                            k16.inviteIntoGroup(op.param1,[op.param3])
                                                            kf.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass                                    
                return

            if mid9 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k9.kickoutFromGroup(op.param1,[op.param2])
                        k9.inviteIntoGroup(op.param1,[op.param3])
                        k8.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k10.kickoutFromGroup(op.param1,[op.param2])
                            k10.inviteIntoGroup(op.param1,[op.param3])
                            k8.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k11.kickoutFromGroup(op.param1,[op.param2])
                                k11.inviteIntoGroup(op.param1,[op.param3])
                                k8.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k12.kickoutFromGroup(op.param1,[op.param2])
                                    k12.inviteIntoGroup(op.param1,[op.param3])
                                    k8.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k13.kickoutFromGroup(op.param1,[op.param2])
                                        k13.inviteIntoGroup(op.param1,[op.param3])
                                        k8.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k8.getGroup(op.param1)
                                            G = k9.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                            k9.updateGroup(G)
                                            Ticket = k9.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k9.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k9.updateGroup(G)
                                            Ticket = k9.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k14.kickoutFromGroup(op.param1,[op.param2])
                                                k14.inviteIntoGroup(op.param1,[op.param3])
                                                k8.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k15.kickoutFromGroup(op.param1,[op.param2])
                                                    k15.inviteIntoGroup(op.param1,[op.param3])
                                                    k8.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k16.kickoutFromGroup(op.param1,[op.param2])
                                                        k16.inviteIntoGroup(op.param1,[op.param3])
                                                        k8.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k17.kickoutFromGroup(op.param1,[op.param2])
                                                            k17.inviteIntoGroup(op.param1,[op.param3])
                                                            k8.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if mid10 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.inviteIntoGroup(op.param1,[op.param3])
                        k9.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k11.kickoutFromGroup(op.param1,[op.param2])
                            k11.inviteIntoGroup(op.param1,[op.param3])
                            k9.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k12.kickoutFromGroup(op.param1,[op.param2])
                                k12.inviteIntoGroup(op.param1,[op.param3])
                                k9.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k13.kickoutFromGroup(op.param1,[op.param2])
                                    k13.inviteIntoGroup(op.param1,[op.param3])
                                    k9.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k14.kickoutFromGroup(op.param1,[op.param2])
                                        k14.inviteIntoGroup(op.param1,[op.param3])
                                        k9.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k9.getGroup(op.param1)
                                            G = k10.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                            k10.updateGroup(G)
                                            Ticket = k10.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k10.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k10.updateGroup(G)
                                            Ticket = k10.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k15.kickoutFromGroup(op.param1,[op.param2])
                                                k15.inviteIntoGroup(op.param1,[op.param3])
                                                k9.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k16.kickoutFromGroup(op.param1,[op.param2])
                                                    k16.inviteIntoGroup(op.param1,[op.param3])
                                                    k9.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k17.kickoutFromGroup(op.param1,[op.param2])
                                                        k17.inviteIntoGroup(op.param1,[op.param3])
                                                        k9.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k18.kickoutFromGroup(op.param1,[op.param2])
                                                            k18.inviteIntoGroup(op.param1,[op.param3])
                                                            k9.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid11 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k11.kickoutFromGroup(op.param1,[op.param2])
                        k11.inviteIntoGroup(op.param1,[op.param3])
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k12.kickoutFromGroup(op.param1,[op.param2])
                            k12.inviteIntoGroup(op.param1,[op.param3])
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k13.kickoutFromGroup(op.param1,[op.param2])
                                k13.inviteIntoGroup(op.param1,[op.param3])
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k14.kickoutFromGroup(op.param1,[op.param2])
                                    k14.inviteIntoGroup(op.param1,[op.param3])
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k15.kickoutFromGroup(op.param1,[op.param2])
                                        k15.inviteIntoGroup(op.param1,[op.param3])
                                        k10.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k10.getGroup(op.param1)
                                            G = k11.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k11.kickoutFromGroup(op.param1,[op.param2])
                                            k11.updateGroup(G)
                                            Ticket = k11.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k11.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k11.updateGroup(G)
                                            Ticket = k11.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k16.kickoutFromGroup(op.param1,[op.param2])
                                                k16.inviteIntoGroup(op.param1,[op.param3])
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k17.kickoutFromGroup(op.param1,[op.param2])
                                                    k17.inviteIntoGroup(op.param1,[op.param3])
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k18.kickoutFromGroup(op.param1,[op.param2])
                                                        k18.inviteIntoGroup(op.param1,[op.param3])
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k19.kickoutFromGroup(op.param1,[op.param2])
                                                            k19.inviteIntoGroup(op.param1,[op.param3])
                                                            k10.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid12 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k12.kickoutFromGroup(op.param1,[op.param2])
                        k12.inviteIntoGroup(op.param1,[op.param3])
                        k11.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k13.kickoutFromGroup(op.param1,[op.param2])
                            k13.inviteIntoGroup(op.param1,[op.param3])
                            k11.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k14.kickoutFromGroup(op.param1,[op.param2])
                                k14.inviteIntoGroup(op.param1,[op.param3])
                                k11.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k15.kickoutFromGroup(op.param1,[op.param2])
                                    k15.inviteIntoGroup(op.param1,[op.param3])
                                    k11.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k16.kickoutFromGroup(op.param1,[op.param2])
                                        k16.inviteIntoGroup(op.param1,[op.param3])
                                        k11.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k11.getGroup(op.param1)
                                            G = k12.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k12.kickoutFromGroup(op.param1,[op.param2])
                                            k12.updateGroup(G)
                                            Ticket = k12.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k12.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k12.updateGroup(G)
                                            Ticket = k12.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k17.kickoutFromGroup(op.param1,[op.param2])
                                                k17.inviteIntoGroup(op.param1,[op.param3])
                                                k11.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k18.kickoutFromGroup(op.param1,[op.param2])
                                                    k18.inviteIntoGroup(op.param1,[op.param3])
                                                    k11.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k19.kickoutFromGroup(op.param1,[op.param2])
                                                        k19.inviteIntoGroup(op.param1,[op.param3])
                                                        k11.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k20.kickoutFromGroup(op.param1,[op.param2])
                                                            k20.inviteIntoGroup(op.param1,[op.param3])
                                                            k11.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid13 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k13.kickoutFromGroup(op.param1,[op.param2])
                        k13.inviteIntoGroup(op.param1,[op.param3])
                        k12.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k14.kickoutFromGroup(op.param1,[op.param2])
                            k14.inviteIntoGroup(op.param1,[op.param3])
                            k12.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k15.kickoutFromGroup(op.param1,[op.param2])
                                k15.inviteIntoGroup(op.param1,[op.param3])
                                k12.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k16.kickoutFromGroup(op.param1,[op.param2])
                                    k16.inviteIntoGroup(op.param1,[op.param3])
                                    k12.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k17.kickoutFromGroup(op.param1,[op.param2])
                                        k17.inviteIntoGroup(op.param1,[op.param3])
                                        k12.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k12.getGroup(op.param1)
                                            G = k13.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k13.kickoutFromGroup(op.param1,[op.param2])
                                            k13.updateGroup(G)
                                            Ticket = k13.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k13.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k13.updateGroup(G)
                                            Ticket = k13.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k18.kickoutFromGroup(op.param1,[op.param2])
                                                k18.inviteIntoGroup(op.param1,[op.param3])
                                                k12.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k19.kickoutFromGroup(op.param1,[op.param2])
                                                    k19.inviteIntoGroup(op.param1,[op.param3])
                                                    k12.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k20.kickoutFromGroup(op.param1,[op.param2])
                                                        k20.inviteIntoGroup(op.param1,[op.param3])
                                                        k12.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                                            k12.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid14 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k14.kickoutFromGroup(op.param1,[op.param2])
                        k14.inviteIntoGroup(op.param1,[op.param3])
                        k13.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k15.kickoutFromGroup(op.param1,[op.param2])
                            k15.inviteIntoGroup(op.param1,[op.param3])
                            k13.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k16.kickoutFromGroup(op.param1,[op.param2])
                                k16.inviteIntoGroup(op.param1,[op.param3])
                                k13.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k17.kickoutFromGroup(op.param1,[op.param2])
                                    k17.inviteIntoGroup(op.param1,[op.param3])
                                    k13.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k18.kickoutFromGroup(op.param1,[op.param2])
                                        k18.inviteIntoGroup(op.param1,[op.param3])
                                        k13.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k13.getGroup(op.param1)
                                            G = k14.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k14.kickoutFromGroup(op.param1,[op.param2])
                                            k14.updateGroup(G)
                                            Ticket = k14.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k14.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k14.updateGroup(G)
                                            Ticket = k14.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k19.kickoutFromGroup(op.param1,[op.param2])
                                                k19.inviteIntoGroup(op.param1,[op.param3])
                                                k13.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k20.kickoutFromGroup(op.param1,[op.param2])
                                                    k20.inviteIntoGroup(op.param1,[op.param3])
                                                    k13.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                                        k13.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                                            k13.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid15 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k15.kickoutFromGroup(op.param1,[op.param2])
                        k15.inviteIntoGroup(op.param1,[op.param3])
                        k14.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k16.kickoutFromGroup(op.param1,[op.param2])
                            k16.inviteIntoGroup(op.param1,[op.param3])
                            k14.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k17.kickoutFromGroup(op.param1,[op.param2])
                                k17.inviteIntoGroup(op.param1,[op.param3])
                                k14.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k18.kickoutFromGroup(op.param1,[op.param2])
                                    k18.inviteIntoGroup(op.param1,[op.param3])
                                    k14.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k19.kickoutFromGroup(op.param1,[op.param2])
                                        k19.inviteIntoGroup(op.param1,[op.param3])
                                        k14.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k14.getGroup(op.param1)
                                            G = k15.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k15.kickoutFromGroup(op.param1,[op.param2])
                                            k15.updateGroup(G)
                                            Ticket = k15.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k15.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k15.updateGroup(G)
                                            Ticket = k15.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k20.kickoutFromGroup(op.param1,[op.param2])
                                                k20.inviteIntoGroup(op.param1,[op.param3])
                                                k14.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                    k14.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                                        k14.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                            k14.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass 
                return

            if mid16 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k16.kickoutFromGroup(op.param1,[op.param2])
                        k16.inviteIntoGroup(op.param1,[op.param3])
                        k15.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k17.kickoutFromGroup(op.param1,[op.param2])
                            k17.inviteIntoGroup(op.param1,[op.param3])
                            k15.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k18.kickoutFromGroup(op.param1,[op.param2])
                                k18.inviteIntoGroup(op.param1,[op.param3])
                                k15.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k19.kickoutFromGroup(op.param1,[op.param2])
                                    k19.inviteIntoGroup(op.param1,[op.param3])
                                    k15.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k20.kickoutFromGroup(op.param1,[op.param2])
                                        k20.inviteIntoGroup(op.param1,[op.param3])
                                        k15.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k15.getGroup(op.param1)
                                            G = k16.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k16.kickoutFromGroup(op.param1,[op.param2])
                                            k16.updateGroup(G)
                                            Ticket = k16.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k16.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k16.updateGroup(G)
                                            Ticket = k16.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                                k15.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                    k15.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        k15.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                                            k15.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid17 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k17.kickoutFromGroup(op.param1,[op.param2])
                        k17.inviteIntoGroup(op.param1,[op.param3])
                        k16.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k18.kickoutFromGroup(op.param1,[op.param2])
                            k18.inviteIntoGroup(op.param1,[op.param3])
                            k16.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k19.kickoutFromGroup(op.param1,[op.param2])
                                k19.inviteIntoGroup(op.param1,[op.param3])
                                k16.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k20.kickoutFromGroup(op.param1,[op.param2])
                                    k20.inviteIntoGroup(op.param1,[op.param3])
                                    k16.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        k16.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k16.getGroup(op.param1)
                                            G = k17.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k17.kickoutFromGroup(op.param1,[op.param2])
                                            k17.updateGroup(G)
                                            Ticket = k17.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k17.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k17.updateGroup(G)
                                            Ticket = k17.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                k16.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                    k16.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                        k16.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                            k16.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid18 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k18.kickoutFromGroup(op.param1,[op.param2])
                        k18.inviteIntoGroup(op.param1,[op.param3])
                        k17.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k19.kickoutFromGroup(op.param1,[op.param2])
                            k19.inviteIntoGroup(op.param1,[op.param3])
                            k17.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k20.kickoutFromGroup(op.param1,[op.param2])
                                k20.inviteIntoGroup(op.param1,[op.param3])
                                k17.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                    k17.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        k17.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k17.getGroup(op.param1)
                                            G = k18.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k18.kickoutFromGroup(op.param1,[op.param2])
                                            k18.updateGroup(G)
                                            Ticket = k18.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k18.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k18.updateGroup(G)
                                            Ticket = k18.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                k17.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                    k17.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                                        k17.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                                            k17.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid19 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k19.kickoutFromGroup(op.param1,[op.param2])
                        k19.inviteIntoGroup(op.param1,[op.param3])
                        k18.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k20.kickoutFromGroup(op.param1,[op.param2])
                            k20.inviteIntoGroup(op.param1,[op.param3])
                            k18.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                k18.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    k18.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        k18.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k18.getGroup(op.param1)
                                            G = k19.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k19.kickoutFromGroup(op.param1,[op.param2])
                                            k19.updateGroup(G)
                                            Ticket = k19.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k19.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k19.updateGroup(G)
                                            Ticket = k19.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                k18.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                                    k18.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                                        k18.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                                            k18.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid20 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.inviteIntoGroup(op.param1,[op.param3])
                        k9.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k20.kickoutFromGroup(op.param1,[op.param2])
                            k20.inviteIntoGroup(op.param1,[op.param3])
                            k19.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                k19.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    k19.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        k19.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k19.getGroup(op.param1)
                                            G = k20.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k20.kickoutFromGroup(op.param1,[op.param2])
                                            k20.updateGroup(G)
                                            Ticket = k20.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k20.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k20.updateGroup(G)
                                            Ticket = k20.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                k19.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                    k19.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                                        k19.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                                            k19.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Jmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kj.kickoutFromGroup(op.param1,[op.param2])
                        kj.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k10.kickoutFromGroup(op.param1,[op.param2])
                            k10.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k11.kickoutFromGroup(op.param1,[op.param2])
                                k11.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k12.kickoutFromGroup(op.param1,[op.param2])
                                    k13.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k14.kickoutFromGroup(op.param1,[op.param2])
                                        k14.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k20.getGroup(op.param1)
                                            G = kj.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kj.kickoutFromGroup(op.param1,[op.param2])
                                            kj.updateGroup(G)
                                            Ticket = kj.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kj.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kj.updateGroup(G)
                                            Ticket = kj.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k15.kickoutFromGroup(op.param1,[op.param2])
                                                k15.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k16.kickoutFromGroup(op.param1,[op.param2])
                                                    k16.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k17.kickoutFromGroup(op.param1,[op.param2])
                                                        k17.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k18.kickoutFromGroup(op.param1,[op.param2])
                                                            k18.inviteIntoGroup(op.param1,[op.param3])
                                                            cl.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass 
                return

            if Zmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k19.kickoutFromGroup(op.param1,[op.param2])
                            k19.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k20.kickoutFromGroup(op.param1,[op.param2])
                                k20.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = cl.getGroup(op.param1)
                                            G = sw.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                            kj.updateGroup(G)
                                            Ticket = sw.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = sw.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            sw.updateGroup(G)
                                            Ticket = sw.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                                            cl.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass                                                        
                return
                
#####################

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    passl
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])                   
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            G = cl.getGroup(op.param1)
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                        k8.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                                            k9.inviteIntoGroup(op.param1,[op.param3])
                                                            cl.acceptGroupInvitation(op.param1)
                                                        except:
                                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = ki.getGroup(op.param1)
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                                        k9.inviteIntoGroup(op.param1,[op.param3])
                                                        ki.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                                            k10.inviteIntoGroup(op.param1,[op.param3])
                                                            ki.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kk.getGroup(op.param1)
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k8.kickoutFromGroup(op.param1,[op.param2])
                                                k8.inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k9.kickoutFromGroup(op.param1,[op.param2])
                                                    k9.inviteIntoGroup(op.param1,[op.param3])
                                                    kk.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                                        k10.inviteIntoGroup(op.param1,[op.param3])
                                                        kk.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k11.kickoutFromGroup(op.param1,[op.param2])
                                                            k11.inviteIntoGroup(op.param1,[op.param3])
                                                            kk.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                    kf.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                        k8.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kc.getGroup(op.param1)
                                            G = kb.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.updateGroup(G)
                                            Ticket = kb.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kb.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kb.updateGroup(G)
                                            Ticket = kb.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k9.kickoutFromGroup(op.param1,[op.param2])
                                                k9.inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                                    k10.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k11.kickoutFromGroup(op.param1,[op.param2])
                                                        k11.inviteIntoGroup(op.param1,[op.param3])
                                                        kc.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k12.kickoutFromGroup(op.param1,[op.param2])
                                                            k12.inviteIntoGroup(op.param1,[op.param3])
                                                            kc.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                    kb.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                        k9.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kb.getGroup(op.param1)
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.updateGroup(G)
                                            Ticket = kd.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kd.updateGroup(G)
                                            Ticket = kd.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                                k10.inviteIntoGroup(op.param1,[op.param3])
                                                kb.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k11.kickoutFromGroup(op.param1,[op.param2])
                                                    k11.inviteIntoGroup(op.param1,[op.param3])
                                                    kb.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k12.kickoutFromGroup(op.param1,[op.param2])
                                                        k12.inviteIntoGroup(op.param1,[op.param3])
                                                        kb.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k13.kickoutFromGroup(op.param1,[op.param2])
                                                            k13.inviteIntoGroup(op.param1,[op.param3])
                                                            kb.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            k9.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                    kd.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                        k10.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kd.getGroup(op.param1)
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.updateGroup(G)
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ke.updateGroup(G)
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k11.kickoutFromGroup(op.param1,[op.param2])
                                                k11.inviteIntoGroup(op.param1,[op.param3])
                                                kd.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k12.kickoutFromGroup(op.param1,[op.param2])
                                                    k12.inviteIntoGroup(op.param1,[op.param3])
                                                    kd.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k13.kickoutFromGroup(op.param1,[op.param2])
                                                        k13.inviteIntoGroup(op.param1,[op.param3])
                                                        kd.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k14.kickoutFromGroup(op.param1,[op.param2])
                                                            k14.inviteIntoGroup(op.param1,[op.param3])
                                                            kd.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        kf.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k8.kickoutFromGroup(op.param1,[op.param2])
                            k8.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k9.kickoutFromGroup(op.param1,[op.param2])
                                k9.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                    k10.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k11.kickoutFromGroup(op.param1,[op.param2])
                                        k11.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = ke.getGroup(op.param1)
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.updateGroup(G)
                                            Ticket = kf.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kf.updateGroup(G)
                                            Ticket = kf.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k12.kickoutFromGroup(op.param1,[op.param2])
                                                k12.inviteIntoGroup(op.param1,[op.param3])
                                                ke.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k13.kickoutFromGroup(op.param1,[op.param2])
                                                    k13.inviteIntoGroup(op.param1,[op.param3])
                                                    ke.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k14.kickoutFromGroup(op.param1,[op.param2])
                                                        k14.inviteIntoGroup(op.param1,[op.param3])
                                                        ke.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k15.kickoutFromGroup(op.param1,[op.param2])
                                                            k15.inviteIntoGroup(op.param1,[op.param3])
                                                            ke.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if mid8 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k8.kickoutFromGroup(op.param1,[op.param2])
                        k8.inviteIntoGroup(op.param1,[op.param3])
                        kf.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            k9.inviteIntoGroup(op.param1,[op.param3])
                            kf.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k10.kickoutFromGroup(op.param1,[op.param2])
                                k10.inviteIntoGroup(op.param1,[op.param3])
                                kf.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k11.kickoutFromGroup(op.param1,[op.param2])
                                    k11.inviteIntoGroup(op.param1,[op.param3])
                                    kf.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k12.kickoutFromGroup(op.param1,[op.param2])
                                        k12.inviteIntoGroup(op.param1,[op.param3])
                                        kf.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kf.getGroup(op.param1)
                                            G = k8.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k8.kickoutFromGroup(op.param1,[op.param2])
                                            k8.updateGroup(G)
                                            Ticket = k8.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k8.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k8.updateGroup(G)
                                            Ticket = k8.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k13.kickoutFromGroup(op.param1,[op.param2])
                                                k13.inviteIntoGroup(op.param1,[op.param3])
                                                kf.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k14.kickoutFromGroup(op.param1,[op.param2])
                                                    k14.inviteIntoGroup(op.param1,[op.param3])
                                                    kf.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k15.kickoutFromGroup(op.param1,[op.param2])
                                                        k15.inviteIntoGroup(op.param1,[op.param3])
                                                        kf.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k16.kickoutFromGroup(op.param1,[op.param2])
                                                            k16.inviteIntoGroup(op.param1,[op.param3])
                                                            kf.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass                                    
                return

            if mid9 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k9.kickoutFromGroup(op.param1,[op.param2])
                        k9.inviteIntoGroup(op.param1,[op.param3])
                        k8.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k10.kickoutFromGroup(op.param1,[op.param2])
                            k10.inviteIntoGroup(op.param1,[op.param3])
                            k8.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k11.kickoutFromGroup(op.param1,[op.param2])
                                k11.inviteIntoGroup(op.param1,[op.param3])
                                k8.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k12.kickoutFromGroup(op.param1,[op.param2])
                                    k12.inviteIntoGroup(op.param1,[op.param3])
                                    k8.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k13.kickoutFromGroup(op.param1,[op.param2])
                                        k13.inviteIntoGroup(op.param1,[op.param3])
                                        k8.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k8.getGroup(op.param1)
                                            G = k9.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                            k9.updateGroup(G)
                                            Ticket = k9.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k9.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k9.updateGroup(G)
                                            Ticket = k9.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k14.kickoutFromGroup(op.param1,[op.param2])
                                                k14.inviteIntoGroup(op.param1,[op.param3])
                                                k8.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k15.kickoutFromGroup(op.param1,[op.param2])
                                                    k15.inviteIntoGroup(op.param1,[op.param3])
                                                    k8.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k16.kickoutFromGroup(op.param1,[op.param2])
                                                        k16.inviteIntoGroup(op.param1,[op.param3])
                                                        k8.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k17.kickoutFromGroup(op.param1,[op.param2])
                                                            k17.inviteIntoGroup(op.param1,[op.param3])
                                                            k8.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if mid10 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.inviteIntoGroup(op.param1,[op.param3])
                        k9.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k11.kickoutFromGroup(op.param1,[op.param2])
                            k11.inviteIntoGroup(op.param1,[op.param3])
                            k9.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k12.kickoutFromGroup(op.param1,[op.param2])
                                k12.inviteIntoGroup(op.param1,[op.param3])
                                k9.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k13.kickoutFromGroup(op.param1,[op.param2])
                                    k13.inviteIntoGroup(op.param1,[op.param3])
                                    k9.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k14.kickoutFromGroup(op.param1,[op.param2])
                                        k14.inviteIntoGroup(op.param1,[op.param3])
                                        k9.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k9.getGroup(op.param1)
                                            G = k10.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                            k10.updateGroup(G)
                                            Ticket = k10.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k10.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k10.updateGroup(G)
                                            Ticket = k10.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k15.kickoutFromGroup(op.param1,[op.param2])
                                                k15.inviteIntoGroup(op.param1,[op.param3])
                                                k9.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k16.kickoutFromGroup(op.param1,[op.param2])
                                                    k16.inviteIntoGroup(op.param1,[op.param3])
                                                    k9.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k17.kickoutFromGroup(op.param1,[op.param2])
                                                        k17.inviteIntoGroup(op.param1,[op.param3])
                                                        k9.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k18.kickoutFromGroup(op.param1,[op.param2])
                                                            k18.inviteIntoGroup(op.param1,[op.param3])
                                                            k9.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid11 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k11.kickoutFromGroup(op.param1,[op.param2])
                        k11.inviteIntoGroup(op.param1,[op.param3])
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k12.kickoutFromGroup(op.param1,[op.param2])
                            k12.inviteIntoGroup(op.param1,[op.param3])
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k13.kickoutFromGroup(op.param1,[op.param2])
                                k13.inviteIntoGroup(op.param1,[op.param3])
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k14.kickoutFromGroup(op.param1,[op.param2])
                                    k14.inviteIntoGroup(op.param1,[op.param3])
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k15.kickoutFromGroup(op.param1,[op.param2])
                                        k15.inviteIntoGroup(op.param1,[op.param3])
                                        k10.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k10.getGroup(op.param1)
                                            G = k11.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k11.kickoutFromGroup(op.param1,[op.param2])
                                            k11.updateGroup(G)
                                            Ticket = k11.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k11.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k11.updateGroup(G)
                                            Ticket = k11.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k16.kickoutFromGroup(op.param1,[op.param2])
                                                k16.inviteIntoGroup(op.param1,[op.param3])
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k17.kickoutFromGroup(op.param1,[op.param2])
                                                    k17.inviteIntoGroup(op.param1,[op.param3])
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k18.kickoutFromGroup(op.param1,[op.param2])
                                                        k18.inviteIntoGroup(op.param1,[op.param3])
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k19.kickoutFromGroup(op.param1,[op.param2])
                                                            k19.inviteIntoGroup(op.param1,[op.param3])
                                                            k10.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid12 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k12.kickoutFromGroup(op.param1,[op.param2])
                        k12.inviteIntoGroup(op.param1,[op.param3])
                        k11.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k13.kickoutFromGroup(op.param1,[op.param2])
                            k13.inviteIntoGroup(op.param1,[op.param3])
                            k11.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k14.kickoutFromGroup(op.param1,[op.param2])
                                k14.inviteIntoGroup(op.param1,[op.param3])
                                k11.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k15.kickoutFromGroup(op.param1,[op.param2])
                                    k15.inviteIntoGroup(op.param1,[op.param3])
                                    k11.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k16.kickoutFromGroup(op.param1,[op.param2])
                                        k16.inviteIntoGroup(op.param1,[op.param3])
                                        k11.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k11.getGroup(op.param1)
                                            G = k12.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k12.kickoutFromGroup(op.param1,[op.param2])
                                            k12.updateGroup(G)
                                            Ticket = k12.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k12.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k12.updateGroup(G)
                                            Ticket = k12.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k17.kickoutFromGroup(op.param1,[op.param2])
                                                k17.inviteIntoGroup(op.param1,[op.param3])
                                                k11.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k18.kickoutFromGroup(op.param1,[op.param2])
                                                    k18.inviteIntoGroup(op.param1,[op.param3])
                                                    k11.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k19.kickoutFromGroup(op.param1,[op.param2])
                                                        k19.inviteIntoGroup(op.param1,[op.param3])
                                                        k11.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k20.kickoutFromGroup(op.param1,[op.param2])
                                                            k20.inviteIntoGroup(op.param1,[op.param3])
                                                            k11.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid13 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k13.kickoutFromGroup(op.param1,[op.param2])
                        k13.inviteIntoGroup(op.param1,[op.param3])
                        k12.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k14.kickoutFromGroup(op.param1,[op.param2])
                            k14.inviteIntoGroup(op.param1,[op.param3])
                            k12.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k15.kickoutFromGroup(op.param1,[op.param2])
                                k15.inviteIntoGroup(op.param1,[op.param3])
                                k12.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k16.kickoutFromGroup(op.param1,[op.param2])
                                    k16.inviteIntoGroup(op.param1,[op.param3])
                                    k12.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k17.kickoutFromGroup(op.param1,[op.param2])
                                        k17.inviteIntoGroup(op.param1,[op.param3])
                                        k12.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k12.getGroup(op.param1)
                                            G = k13.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k13.kickoutFromGroup(op.param1,[op.param2])
                                            k13.updateGroup(G)
                                            Ticket = k13.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k13.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k13.updateGroup(G)
                                            Ticket = k13.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k18.kickoutFromGroup(op.param1,[op.param2])
                                                k18.inviteIntoGroup(op.param1,[op.param3])
                                                k12.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k19.kickoutFromGroup(op.param1,[op.param2])
                                                    k19.inviteIntoGroup(op.param1,[op.param3])
                                                    k12.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k20.kickoutFromGroup(op.param1,[op.param2])
                                                        k20.inviteIntoGroup(op.param1,[op.param3])
                                                        k12.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                                            k12.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid14 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k14.kickoutFromGroup(op.param1,[op.param2])
                        k14.inviteIntoGroup(op.param1,[op.param3])
                        k13.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k15.kickoutFromGroup(op.param1,[op.param2])
                            k15.inviteIntoGroup(op.param1,[op.param3])
                            k13.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k16.kickoutFromGroup(op.param1,[op.param2])
                                k16.inviteIntoGroup(op.param1,[op.param3])
                                k13.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k17.kickoutFromGroup(op.param1,[op.param2])
                                    k17.inviteIntoGroup(op.param1,[op.param3])
                                    k13.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k18.kickoutFromGroup(op.param1,[op.param2])
                                        k18.inviteIntoGroup(op.param1,[op.param3])
                                        k13.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k13.getGroup(op.param1)
                                            G = k14.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k14.kickoutFromGroup(op.param1,[op.param2])
                                            k14.updateGroup(G)
                                            Ticket = k14.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k14.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k14.updateGroup(G)
                                            Ticket = k14.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k19.kickoutFromGroup(op.param1,[op.param2])
                                                k19.inviteIntoGroup(op.param1,[op.param3])
                                                k13.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k20.kickoutFromGroup(op.param1,[op.param2])
                                                    k20.inviteIntoGroup(op.param1,[op.param3])
                                                    k13.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                                        k13.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                                            k13.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid15 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k15.kickoutFromGroup(op.param1,[op.param2])
                        k15.inviteIntoGroup(op.param1,[op.param3])
                        k14.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k16.kickoutFromGroup(op.param1,[op.param2])
                            k16.inviteIntoGroup(op.param1,[op.param3])
                            k14.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k17.kickoutFromGroup(op.param1,[op.param2])
                                k17.inviteIntoGroup(op.param1,[op.param3])
                                k14.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k18.kickoutFromGroup(op.param1,[op.param2])
                                    k18.inviteIntoGroup(op.param1,[op.param3])
                                    k14.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k19.kickoutFromGroup(op.param1,[op.param2])
                                        k19.inviteIntoGroup(op.param1,[op.param3])
                                        k14.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k14.getGroup(op.param1)
                                            G = k15.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k15.kickoutFromGroup(op.param1,[op.param2])
                                            k15.updateGroup(G)
                                            Ticket = k15.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k15.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k15.updateGroup(G)
                                            Ticket = k15.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k20.kickoutFromGroup(op.param1,[op.param2])
                                                k20.inviteIntoGroup(op.param1,[op.param3])
                                                k14.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                    k14.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                                        k14.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                            k14.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass 
                return

            if mid16 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k16.kickoutFromGroup(op.param1,[op.param2])
                        k16.inviteIntoGroup(op.param1,[op.param3])
                        k15.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k17.kickoutFromGroup(op.param1,[op.param2])
                            k17.inviteIntoGroup(op.param1,[op.param3])
                            k15.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k18.kickoutFromGroup(op.param1,[op.param2])
                                k18.inviteIntoGroup(op.param1,[op.param3])
                                k15.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k19.kickoutFromGroup(op.param1,[op.param2])
                                    k19.inviteIntoGroup(op.param1,[op.param3])
                                    k15.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k20.kickoutFromGroup(op.param1,[op.param2])
                                        k20.inviteIntoGroup(op.param1,[op.param3])
                                        k15.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k15.getGroup(op.param1)
                                            G = k16.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k16.kickoutFromGroup(op.param1,[op.param2])
                                            k16.updateGroup(G)
                                            Ticket = k16.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k16.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k16.updateGroup(G)
                                            Ticket = k16.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                                k15.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                    k15.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        k15.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                                            k15.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid17 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k17.kickoutFromGroup(op.param1,[op.param2])
                        k17.inviteIntoGroup(op.param1,[op.param3])
                        k16.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k18.kickoutFromGroup(op.param1,[op.param2])
                            k18.inviteIntoGroup(op.param1,[op.param3])
                            k16.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k19.kickoutFromGroup(op.param1,[op.param2])
                                k19.inviteIntoGroup(op.param1,[op.param3])
                                k16.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k20.kickoutFromGroup(op.param1,[op.param2])
                                    k20.inviteIntoGroup(op.param1,[op.param3])
                                    k16.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        k16.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k16.getGroup(op.param1)
                                            G = k17.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k17.kickoutFromGroup(op.param1,[op.param2])
                                            k17.updateGroup(G)
                                            Ticket = k17.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k17.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k17.updateGroup(G)
                                            Ticket = k17.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                k16.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                    k16.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                        k16.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                            k16.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid18 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k18.kickoutFromGroup(op.param1,[op.param2])
                        k18.inviteIntoGroup(op.param1,[op.param3])
                        k17.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k19.kickoutFromGroup(op.param1,[op.param2])
                            k19.inviteIntoGroup(op.param1,[op.param3])
                            k17.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k20.kickoutFromGroup(op.param1,[op.param2])
                                k20.inviteIntoGroup(op.param1,[op.param3])
                                k17.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                    k17.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        k17.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k17.getGroup(op.param1)
                                            G = k18.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k18.kickoutFromGroup(op.param1,[op.param2])
                                            k18.updateGroup(G)
                                            Ticket = k18.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k18.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k18.updateGroup(G)
                                            Ticket = k18.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                k17.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                    k17.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                                        k17.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                                            k17.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid19 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k19.kickoutFromGroup(op.param1,[op.param2])
                        k19.inviteIntoGroup(op.param1,[op.param3])
                        k18.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k20.kickoutFromGroup(op.param1,[op.param2])
                            k20.inviteIntoGroup(op.param1,[op.param3])
                            k18.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                k18.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    k18.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        k18.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k18.getGroup(op.param1)
                                            G = k19.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k19.kickoutFromGroup(op.param1,[op.param2])
                                            k19.updateGroup(G)
                                            Ticket = k19.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k19.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k19.updateGroup(G)
                                            Ticket = k19.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                k18.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                                    k18.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                                        k18.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                                            k18.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid20 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.inviteIntoGroup(op.param1,[op.param3])
                        k9.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k20.kickoutFromGroup(op.param1,[op.param2])
                            k20.inviteIntoGroup(op.param1,[op.param3])
                            k19.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                k19.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    k19.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        k19.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k19.getGroup(op.param1)
                                            G = k20.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k20.kickoutFromGroup(op.param1,[op.param2])
                                            k20.updateGroup(G)
                                            Ticket = k20.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k20.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k20.updateGroup(G)
                                            Ticket = k20.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                k19.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                    k19.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                                        k19.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                                            k19.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Jmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kj.kickoutFromGroup(op.param1,[op.param2])
                        kj.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k10.kickoutFromGroup(op.param1,[op.param2])
                            k10.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k11.kickoutFromGroup(op.param1,[op.param2])
                                k11.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k12.kickoutFromGroup(op.param1,[op.param2])
                                    k13.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k14.kickoutFromGroup(op.param1,[op.param2])
                                        k14.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k20.getGroup(op.param1)
                                            G = kj.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kj.kickoutFromGroup(op.param1,[op.param2])
                                            kj.updateGroup(G)
                                            Ticket = kj.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kj.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kj.updateGroup(G)
                                            Ticket = kj.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k15.kickoutFromGroup(op.param1,[op.param2])
                                                k15.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k16.kickoutFromGroup(op.param1,[op.param2])
                                                    k16.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k17.kickoutFromGroup(op.param1,[op.param2])
                                                        k17.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k18.kickoutFromGroup(op.param1,[op.param2])
                                                            k18.inviteIntoGroup(op.param1,[op.param3])
                                                            cl.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass 
                return

            if Zmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k19.kickoutFromGroup(op.param1,[op.param2])
                            k19.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k20.kickoutFromGroup(op.param1,[op.param2])
                                k20.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = cl.getGroup(op.param1)
                                            G = sw.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                            kj.updateGroup(G)
                                            Ticket = sw.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = sw.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            sw.updateGroup(G)
                                            Ticket = sw.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                                            cl.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass                                                        
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,admin)
                                                ke.inviteIntoGroup(op.param1,admin)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param1,admin)
                                                    kf.inviteIntoGroup(op.param1,admin)
                                                except:
                                                    try:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                        k8.findAndAddContactsByMid(op.param1,admin)
                                                        k8.inviteIntoGroup(op.param1,admin)  
                                                    except:
                                                        try:
                                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                                            k9.findAndAddContactsByMid(op.param1,admin)
                                                            k9.inviteIntoGroup(op.param1,admin)  
                                                        except:
                                                            pass

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.findAndAddContactsByMid(op.param1,admin)
                        k10.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            k11.kickoutFromGroup(op.param1,[op.param2])
                            k11.findAndAddContactsByMid(op.param1,admin)
                            k11.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                k12.kickoutFromGroup(op.param1,[op.param2])
                                k12.findAndAddContactsByMid(op.param1,admin)
                                k12.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    k13.kickoutFromGroup(op.param1,[op.param2])
                                    k13.findAndAddContactsByMid(op.param1,admin)
                                    k13.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        k14.kickoutFromGroup(op.param1,[op.param2])
                                        k14.findAndAddContactsByMid(op.param1,admin)
                                        k14.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            k15.kickoutFromGroup(op.param1,[op.param2])
                                            k15.findAndAddContactsByMid(op.param1,admin)
                                            k15.nviteIntoGroup(op.param1,admin)
                                        except:
                                            try:
                                                k16.kickoutFromGroup(op.param1,[op.param2])
                                                k16.findAndAddContactsByMid(op.param1,admin)
                                                k16.inviteIntoGroup(op.param1,admin)
                                            except:
                                                 try:
                                                     k17.kickoutFromGroup(op.param1,[op.param2])
                                                     k17.findAndAddContactsByMid(op.param1,admin)
                                                     k17.inviteIntoGroup(op.param1,admin)
                                                 except:
                                                     try:
                                                         k18.kickoutFromGroup(op.param1,[op.param2])
                                                         k18.findAndAddContactsByMid(op.param1,admin)
                                                         k18.inviteIntoGroup(op.param1,admin)  
                                                     except:
                                                        try:
                                                            k19.kickoutFromGroup(op.param1,[op.param2])
                                                            k19.findAndAddContactsByMid(op.param1,admin)
                                                            k19.inviteIntoGroup(op.param1,admin)  
                                                        except:
                                                            pass
                                                           
            
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k20.kickoutFromGroup(op.param1,[op.param2])
                        k20.findAndAddContactsByMid(op.param1,admin)
                        k20.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k20.kickoutFromGroup(op.param1,[op.param2])
                                                       k20.findAndAddContactsByMid(op.param1,admin)
                                                       k20.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k8.kickoutFromGroup(op.param1,[op.param2])
                                                           k8.findAndAddContactsByMid(op.param1,admin)
                                                           k8.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass          

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k9.kickoutFromGroup(op.param1,[op.param2])
                        k9.findAndAddContactsByMid(op.param1,admin)
                        k9.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            k10.kickoutFromGroup(op.param1,[op.param2])
                            k10.findAndAddContactsByMid(op.param1,admin)
                            k10.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                k11.kickoutFromGroup(op.param1,[op.param2])
                                k11.findAndAddContactsByMid(op.param1,admin)
                                k11.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    k12.kickoutFromGroup(op.param1,[op.param2])
                                    k12.findAndAddContactsByMid(op.param1,admin)
                                    k12.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        k13.kickoutFromGroup(op.param1,[op.param2])
                                        k13.findAndAddContactsByMid(op.param1,admin)
                                        k13.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            k14.kickoutFromGroup(op.param1,[op.param2])
                                            k14.findAndAddContactsByMid(op.param1,admin)
                                            k14.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               k15.kickoutFromGroup(op.param1,[op.param2])
                                               k15.findAndAddContactsByMid(op.param1,admin)
                                               k15.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   k16.kickoutFromGroup(op.param1,[op.param2])
                                                   k16.findAndAddContactsByMid(op.param1,admin)
                                                   k16.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k17.kickoutFromGroup(op.param1,[op.param2])
                                                       k17.findAndAddContactsByMid(op.param1,admin)
                                                       k17.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k18.kickoutFromGroup(op.param1,[op.param2])
                                                           k18.findAndAddContactsByMid(op.param1,admin)
                                                           k18.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k19.kickoutFromGroup(op.param1,[op.param2])
                                                       k19.findAndAddContactsByMid(op.param1,admin)
                                                       k19.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k20.kickoutFromGroup(op.param1,[op.param2])
                                                           k20.findAndAddContactsByMid(op.param1,admin)
                                                           k20.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass       
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k8.kickoutFromGroup(op.param1,[op.param2])
                                                       k8.findAndAddContactsByMid(op.param1,admin)
                                                       k8.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k9.kickoutFromGroup(op.param1,[op.param2])
                                                           k9.findAndAddContactsByMid(op.param1,admin)
                                                           k9.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass         

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k10.kickoutFromGroup(op.param1,[op.param2])
                                                       k10.findAndAddContactsByMid(op.param1,admin)
                                                       k10.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k11.kickoutFromGroup(op.param1,[op.param2])
                                                           k11.findAndAddContactsByMid(op.param1,admin)
                                                           k11.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k13.kickoutFromGroup(op.param1,[op.param2])
                                                       k13.findAndAddContactsByMid(op.param1,admin)
                                                       k13.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k14.kickoutFromGroup(op.param1,[op.param2])
                                                           k14.findAndAddContactsByMid(op.param1,admin)
                                                           k14.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass          

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k15.kickoutFromGroup(op.param1,[op.param2])
                                                       k15.findAndAddContactsByMid(op.param1,admin)
                                                       k15.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k16.kickoutFromGroup(op.param1,[op.param2])
                                                           k16.findAndAddContactsByMid(op.param1,admin)
                                                           k16.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass          

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k17.kickoutFromGroup(op.param1,[op.param2])
                                                       k17.findAndAddContactsByMid(op.param1,admin)
                                                       k17.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k18.kickoutFromGroup(op.param1,[op.param2])
                                                           k18.findAndAddContactsByMid(op.param1,admin)
                                                           k18.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k19.kickoutFromGroup(op.param1,[op.param2])
                                                       k19.findAndAddContactsByMid(op.param1,admin)
                                                       k19.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k20.kickoutFromGroup(op.param1,[op.param2])
                                                           k20.findAndAddContactsByMid(op.param1,admin)
                                                           k20.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass           
                                
                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)

        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot saints")
                                            
                        elif cmd == "คำสั่ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage = help()
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「My Name 'S」\n• User : "
                                ret_ = str(helpMessage)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "คำสั่ง1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage1 = help1()
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「MY Name 'S」\n• User : "
                                ret_ = str(helpMessage1)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "คำสั่ง2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage2 = help2()
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「MY Nme 'S」\n• User : "
                                ret_ = str(helpMessage2)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "คำสั่ง3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage3 = help3()
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「MY Name 'S」\n• User : "
                                ret_ = str(helpMessage3)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "เชค":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "\n   「 Mai 」\n"
                                if wait["stickerOn"] == True: md+="「🇹🇭」 Sticker「ON」📲\n"
                                else: md+="「🇹🇭」 Sticker「OFF」📵\n"
                                if wait["contact"] == True: md+="「🇹🇭」 Contact「ON」📲\n"
                                else: md+="「🇹🇭」 Contact「OFF」📵\n"
                                if wait["talkban"] == True: md+="「🇹🇭」 Talkban「ON」📲\n"
                                else: md+="「🇹🇭」 Talkban「OFF」📵\n"
                                if wait["unsend"] == True: md+="「🇹🇭」 Unsend「ON」📲\n"
                                else: md+="「🇹🇭」 Unsend「OFF」📵\n"
                                if settings["SpamInvite"] == True: md+="「🇹🇭」 Spaminvite「ON」📲\n"
                                else: md+="「🇹🇭」 Spaminvite「OFF」📵\n"
                                if wait["detectMention"] == True: md+="「🇹🇭」 Respon「ON」📲\n"
                                else: md+="「🇹🇭」 Respon「OFF」📵\n"
                                if wait["Timeline"] == True: md+="「🇹🇭」 Timeline「ON」📲\n"
                                else: md+="「🇹🇭」 Timeline「OFF」📵\n"
                                if wait["autoJoin"] == True: md+="「🇹🇭」 Autojoin「ON」📲\n"
                                else: md+="「🇹🇭」 Autojoin「OFF」📵\n"
                                if wait["autoAdd"] == True: md+="「🇹🇭」 Autoadd「ON」📲\n"
                                else: md+="「🇹🇭」 Autoadd「OFF」📵\n"
                                if settings["autoJoinTicket"] == True: md+="「🇹🇭」 Jointicket「ON」📲\n"
                                else: md+="「🇹🇭」 Jointicket「OFF」📵\n"
                                if msg.to in welcome: md+="「🇹🇭」 Welcome「ON」📲\n"
                                else: md+="「🇹🇭」 Welcome「OFF」📵\n"
                                if wait["autoLeave"] == True: md+="「🇹🇭」 Autoleave「ON」📲\n"
                                else: md+="「🇹🇭」 Autoleave「OFF」📵\n"
                                if msg.to in protectqr: md+="「🇹🇭」Protecturl「ON」📲\n"
                                else: md+="「🇹🇭」Protecturl「OFF」📵\n"
                                if msg.to in protectjoin: md+="「🇹🇭」Protectjoin「ON」📲\n"
                                else: md+="「🇹🇭」Protectjoin「OFF」📵\n"
                                if msg.to in protectjoin: md+="「🇹🇭」Protectinvite「ON」📲\n"
                                else: md+="「🇹🇭」Protectinvite「OFF」📵\n"
                                if msg.to in protectkick: md+="「🇹🇭」Protectkick「ON」📲\n"
                                else: md+="「🇹🇭」Protectkick「OFF」📵\n"
                                if msg.to in protectcancel: md+="「🇹🇭」Protectcancel「ON」📲\n"
                                else: md+="「🇹🇭」Protectcancel「OFF」📵\n"
                                if msg.to in protectantijs: md+="「🇹🇭」Antijs「ON」📲\n"
                                else: md+="「🇹🇭」Antijs「OFF」📵\n"  
                                if msg.to in ghost: md+="「🇹🇭」Ghost「ON」📲\n"
                                else: md+="「🇹🇭」Ghost「OFF」📵\n"
                                ginfo = cl.getGroup(msg.to)
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 BY:MAI  」\n• User : "
                                ret_ = "• Group : {}\n".format(str(ginfo.name))
                                ret_ += str(md)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + "\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                
                        elif cmd == "มี" or text.lower() == 'aim':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 User Selfbot 」\n", "")
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
                        elif text.lower() == "ลบแชท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "ลบแชทคิก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   kd.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   kf.removeAllMessages(op.param2)
                                   k8.removeAllMessages(op.param2)
                                   k9.removeAllMessages(op.param2)
                                   k10.removeAllMessages(op.param2)
                                   k11.removeAllMessages(op.param2)
                                   k12.removeAllMessages(op.param2)
                                   k13.removeAllMessages(op.param2)
                                   k14.removeAllMessages(op.param2)
                                   k15.removeAllMessages(op.param2)
                                   k16.removeAllMessages(op.param2)
                                   k17.removeAllMessages(op.param2)
                                   k18.removeAllMessages(op.param2)
                                   k19.removeAllMessages(op.param2)
                                   k20.removeAllMessages(op.param2)
                                   kj.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   ki.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   kk.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   kc.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   kb.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   kd.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   ke.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   kf.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k8.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k9.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k10.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k11.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k12.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k13.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k14.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k15.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k16.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k17.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k18.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k19.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k20.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                               except:
                                   pass

                        elif cmd.startswith("ประกาศ "):
                           if msg._from in admin:
                             sep = text.split(" ")
                             bc = text.replace(sep[0] + " ","")
                             saya = cl.getGroupIdsJoined()
                             for group in saya:
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 ประกาศกลุ่ม 」\nประกาศ โดย "
                                ret_ = "{}".format(str(bc))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)


                        elif cmd == "ออน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 เวลาทำงานของบอท 」\n• ชื่อผู้ใช้ : "
                                ret_ = "• {}".format(str(bot))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "กลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ กลุ่มที่มีทั้งหมด ]\n║\n"+ma+"║\n╚══[ จำนวน「"+str(len(gid))+"」กลุ่ม ]")
                        elif cmd == "เปิดลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "เปิดลิ้งเรียบร้อย...")

                        elif cmd == "ปิดลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "ปิดลิ้งเรียบร้อย...")

                        elif cmd == "ลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "กลุ่ม "+str(x.name)+ "\nลิ้งกลุ่ม \nhttp://line.me/R/ti/g/"+gurl)
#KICKALL
                        elif "!mai" in msg.text:
                          if msg._from in admin:
                           if msg.toType == 2:
                              print("ok")
                              _name = msg.text.replace("!mai","")
                              gs = kj.getGroup(msg.to)
                              gs = kj.getGroup(msg.to)
                              gs = kj.getGroup(msg.to)
                              targets = []
                              for g in gs.members:
                                 if _name in g.displayName:
                                     targets.append(g.mid)
                              if targets == []:
                                 kj.sendText(msg.to,"Tidak Ditemukan.")
                              else:
                                  for target in targets:
                                   if not target in admin and Bots:
                                      try:
                                          klist=[kj]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except Exception as e:
                                          break
 
                        elif ("Vk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif cmd == "ดึงคิก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,mid8,mid9,mid10,mid11,mid12,mid13,mid14,mid15,mid16,mid17,mid18,mid19,mid20]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kf.acceptGroupInvitation(msg.to)
                                    k8.acceptGroupInvitation(msg.to)
                                    k9.acceptGroupInvitation(msg.to)
                                    k10.acceptGroupInvitation(msg.to)
                                    k11.acceptGroupInvitation(msg.to)
                                    k12.acceptGroupInvitation(msg.to)
                                    k13.acceptGroupInvitation(msg.to)
                                    k14.acceptGroupInvitation(msg.to)
                                    k15.acceptGroupInvitation(msg.to)
                                    k16.acceptGroupInvitation(msg.to)
                                    k17.acceptGroupInvitation(msg.to)
                                    k18.acceptGroupInvitation(msg.to)
                                    k19.acceptGroupInvitation(msg.to)
                                    k20.acceptGroupInvitation(msg.to)
                                    cl.sendMessage(msg.to,"Grup "+str(ginfo.name)+"Aman Dari JS")
                                except:
                                    pass

                        elif cmd == "ck":
                            if msg._from in admin or msg._from in owner:
                               try:cl.inviteIntoGroup(to, ["uc66e45201d1612eb4ce7b3a86bac4685"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["uc66e45201d1612eb4ce7b3a86bac4685"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               cl.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:ki.inviteIntoGroup(to, ["uff4bd67e5bc6ab62760b1ff78d89dfe4"]);has = "OK"
                               except:has = "NOT"
                               try:ki.kickoutFromGroup(to, ["uff4bd67e5bc6ab62760b1ff78d89dfe4"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               ki.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:kk.inviteIntoGroup(to, ["u5db69e110e5c7a468584632c6472bb66"]);has = "OK"
                               except:has = "NOT"
                               try:kk.kickoutFromGroup(to, ["u5db69e110e5c7a468584632c6472bb66"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kk.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:kc.inviteIntoGroup(to, ["u7fed37def4d8e3bcef59b1e8af11da3a"]);has = "OK"
                               except:has = "NOT"
                               try:kc.kickoutFromGroup(to, ["u7fed37def4d8e3bcef59b1e8af11da3a"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low  0%"
                               kc.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:kb.inviteIntoGroup(to, ["u21f2166935c999fe450ce5ea5aa42652"]);has = "OK"
                               except:has = "NOT"
                               try:kb.kickoutFromGroup(to, ["u21f2166935c999fe450ce5ea5aa42652"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kb.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                              
                               try:kd.inviteIntoGroup(to, ["u2739569d28dfd03972f92bc4508d5b95"]);has = "OK"
                               except:has = "NOT"
                               try:kd.kickoutFromGroup(to, ["u2739569d28dfd03972f92bc4508d5b95"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kd.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:ke.inviteIntoGroup(to, ["ue093b1293a087794a6750a77b5ec3990"]);has = "OK"
                               except:has = "NOT"
                               try:ke.kickoutFromGroup(to, ["ue093b1293a087794a6750a77b5ec3990"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               ke.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:kf.inviteIntoGroup(to, ["u6756e5a6ec421fbe85b3173d2c32a16a"]);has = "OK"
                               except:has = "NOT"
                               try:kf.kickoutFromGroup(to, ["u6756e5a6ec421fbe85b3173d2c32a16a"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kf.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:k8.inviteIntoGroup(to, ["ua747585a5201be67956b55bcfe662466"]);has = "OK"
                               except:has = "NOT"
                               try:k8.kickoutFromGroup(to, ["ua747585a5201be67956b55bcfe662466"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k8.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k9.inviteIntoGroup(to, ["u252bef6cbe92d5682068c6b07a3659db"]);has = "OK"
                               except:has = "NOT"
                               try:k9.kickoutFromGroup(to, ["u252bef6cbe92d5682068c6b07a3659db"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low  0%"
                               k9.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:k10.inviteIntoGroup(to, ["u971c92c69915f75f6d427d580b8ee7a2"]);has = "OK"
                               except:has = "NOT"
                               try:k10.kickoutFromGroup(to, ["u971c92c69915f75f6d427d580b8ee7a2"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k10.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                              
                               try:k11.inviteIntoGroup(to, ["u4783b96f646f7ee4f77912aaf2fc16c8"]);has = "OK"
                               except:has = "NOT"
                               try:k11.kickoutFromGroup(to, ["u4783b96f646f7ee4f77912aaf2fc16c8"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k11.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k12.inviteIntoGroup(to, ["u9a7763fdf967b345d935c7e06b632ad7"]);has = "OK"
                               except:has = "NOT"
                               try:k12.kickoutFromGroup(to, ["u9a7763fdf967b345d935c7e06b632ad7"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k12.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k13.inviteIntoGroup(to, ["u26d534ff9575a209224834af584ddc5a"]);has = "OK"
                               except:has = "NOT"
                               try:k13.kickoutFromGroup(to, ["u26d534ff9575a209224834af584ddc5a"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k13.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:k14.inviteIntoGroup(to, ["u601169a39deea005cb054f6df3a1be01"]);has = "OK"
                               except:has = "NOT"
                               try:k14.kickoutFromGroup(to, ["u601169a39deea005cb054f6df3a1be01"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k14.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k15.inviteIntoGroup(to, ["u608398e513e31d10a748f7976c06ca6e"]);has = "OK"
                               except:has = "NOT"
                               try:k15.kickoutFromGroup(to, ["u608398e513e31d10a748f7976c06ca6e"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low  0%"
                               k15.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:k16.inviteIntoGroup(to, ["u0cb657723b765e0294eaaee08be417ae"]);has = "OK"
                               except:has = "NOT"
                               try:k16.kickoutFromGroup(to, ["u0cb657723b765e0294eaaee08be417ae"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k16.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                              
                               try:k17.inviteIntoGroup(to, ["uda15719071a4e30a0ed3b1fce2f695ab"]);has = "OK"
                               except:has = "NOT"
                               try:k17.kickoutFromGroup(to, ["uda15719071a4e30a0ed3b1fce2f695ab"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k17.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k18.inviteIntoGroup(to, ["u36b501abe0dff8c6767724ed32c0a140"]);has = "OK" 
                               except:has = "NOT"
                               try:k18.kickoutFromGroup(to, ["u36b501abe0dff8c6767724ed32c0a140"]);has1 = "OK"
                               except:has1 = "NOT" 
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%" 
                               k18.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k19.inviteIntoGroup(to, ["u77d0f412a5d3d8f75baf86a9170a7b83"]);has = "OK" 
                               except:has = "NOT"
                               try:k19.kickoutFromGroup(to, ["u77d0f412a5d3d8f75baf86a9170a7b83"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k19.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))  
                               try:k20.inviteIntoGroup(to, ["u12876a2278a9b14d042c632d15ee0480"]);has = "OK"  
                               except:has = "NOT"                     
                               try:k20.kickoutFromGroup(to, ["u12876a2278a9b14d042c632d15ee0480"]);has1 = "OK"
                               except:has1 = "NOT"                     
                               if has == "OK":sil = "🔋██ full 100%"                     
                               else:sil = "🔌█▒ Low 0%"                     
                               if has1 == "OK":sil1 = "🔋██ full 100%"                     
                               else:sil1 = "🔌█▒ Low 0%"
                               k20.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))

                        elif cmd == "ผีมา":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "ผีออก":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kj.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               sendMention(msg.to, sender, "「 Selfbot Speed 」\n• User ", "")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "spb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                cl.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ki.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kk.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kc.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kb.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kd.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ke.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kf.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k8.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k9.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k10.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k11.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k12.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k13.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k14.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k15.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k16.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k17.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k18.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k19.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k20.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3)) 
                        elif cmd.startswith("ดึง "):
                          if msg._from in admin:
                               sep = text.split(" ")
                               idnya = text.replace(sep[0] + " ","")
                               conn = cl.findContactsByUserid(idnya)
                               cl.findAndAddContactsByMid(conn.mid)
                               cl.inviteIntoGroup(msg.to,[conn.mid])
                               group = cl.getGroup(msg.to)
                               xname = cl.getContact(conn.mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan = '「 Sukses Diinvite 」\nNama contact '
                               recky = str(xname.displayName)
                               pesan = ''
                               pesan2 = pesan+"@a\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':xname.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan+ zxc + "ke grup " + str(group.name) +""
                               cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                               
                        elif cmd == "เชคบอท" or cmd == "ชบ":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                kk.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                kc.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                kb.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                kd.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                ke.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                kf.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k8.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k9.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k10.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k11.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k12.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k13.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k14.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k15.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k16.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k17.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k18.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k19.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                k20.sendMessage(msg.to, "อยู่ค้าบเจ้านาย ")
                                
                        elif cmd == "คิกมา":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k11.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k12.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k13.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k14.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k15.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k16.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k17.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k18.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k19.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k20.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k20.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k20.updateGroup(G)

                        elif cmd == "คิกออก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                k8.leaveGroup(msg.to)
                                k9.leaveGroup(msg.to)
                                k10.leaveGroup(msg.to)
                                k11.leaveGroup(msg.to)
                                k12.leaveGroup(msg.to)
                                k13.leaveGroup(msg.to)
                                k14.leaveGroup(msg.to)
                                k15.leaveGroup(msg.to)
                                k16.leaveGroup(msg.to)
                                k17.leaveGroup(msg.to)
                                k18.leaveGroup(msg.to)
                                k19.leaveGroup(msg.to)
                                k20.leaveGroup(msg.to)
                        elif cmd == "ผีมา":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "ผีออก":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kj.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif ("ผี2เตะ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass
                        elif ("ผี1เตะ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           kj.kickoutFromGroup(msg.to, [target])
                                           kj.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass                 

                        elif cmd == "เชคดำ" or text.lower() == 'bc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cb" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"ล้างดำหมดแล้วคัฟเจ้านาย " +mc)

                        elif 'Antijs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Antijs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Anti JS Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Anti JS Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua sudah diaktifkan"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protection diaktifkan"
                                  cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)




    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
