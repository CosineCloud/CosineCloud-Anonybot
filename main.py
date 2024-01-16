import os
import sys
import telebot
import datetime
import time
import requests
import random
import psutil
import subprocess
import pickle
import platform
import shutil
import random
import qrcode
import base64
import ast
from sys import exit
from threading import Thread
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton ,ReplyKeyboardMarkup
import pandas as pd    
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from pyzbar import pyzbar
from better_profanity import profanity
import sqlite3
from tabulate import tabulate
#import builtins
from keep_alive import keep_alive
keep_alive()

bot = telebot.TeleBot("5768243722:AAGuPYWlGCH9x7I-N5bJ3u6royTuEfQ5ZFw")
bot.send_message('584429967', '🌀Welcome to Anonymous Chats!!')
print('🌀Welcome to Anonymous Chats!!')

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Auto Start DB Manager
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def start_db():
  print("Started DB")

if __name__ == "__main__":
  start_db()
  bot.send_message('584429967', 'Starting DB Manager')

  # Run the db_manager.1.2.py file in the background without capturing output
  process = subprocess.Popen(['python', 'db_manager.2.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
  bot.send_message('584429967', 'DB Manager Started')


    # Add a delay or other operations if needed
  time.sleep(1)
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Disable print Command
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 

#def empty_print(*args, **kwargs):
#    pass

# Redefine the print function to do nothing
#builtins.print = empty_print

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                      Time stemp
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||   

def timestemp():
        import time
        from datetime import datetime
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       List module
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
def listfiles(path):
    try:
        folder_path = str("info_files/"+str(path))
        for file in os.scandir(folder_path):
            if file.is_file():
                time.sleep(2)
                return(file.name)
    except Exception as e:
        return ("Error:/ "+str(e))
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Open AI Module slots
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def AIslots(S):
    conn = sqlite3.connect('Anonychatdb_5.0v.db')
    # create a cursor to execute SQL commands
    cursor = conn.cursor()
    # execute the query to count the occurrences of "AI" in the "Status" column
    cursor.execute("SELECT COUNT(*) FROM my_table WHERE Status=?", (S,))
    # retrieve the result of the query
    result = cursor.fetchone()
    # print the number of occurrences of "AI" in the "Status" column
    print("Number of occurrences of 'AI' in the 'Status' column:", result[0])
    # close the connection
    cursor.close()
    conn.close()
    return result[0]

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Nicknames Module
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||  
def nick():
    import nick_names
    result = nick_names.nick()
    return(result)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Open AI Module
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||     
def OPnAI(Q):
    import OpenAI
    #Q = (input("Enter a Question: "))
    result = OpenAI.OPAI(Q)
    print(result)
    return(result)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Open AI Module
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||     
def Blocklistchk(Q):
    import OpenAI
    #Q = (input("Enter a Question: "))
    result = OpenAI.OPAI(Q)
    return(result)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Open AI Module
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||     
def Blocklistadd(A,B,C):
    df = pd.read_csv('info_files/Blocklist.csv')
    i2 = df.ID[df.ID == int(A)].index.tolist()
    x=str(i2)
    x=x.replace("[","")
    x=x.replace("]","")
    #print(A)
    if x == "":
        #print('not found')
        #print("Original DataFrame:\n",df)
        df1 = pd.DataFrame({"BID":[int(A)],"WhoID":[B],"Remarks":[C]})
        s = df.append(df1)
        s2 = s.to_csv(r'info_files/Blocklist.csv', index=False)
        #print("Modified DataFrame:\n",s)
        return "✅  Block ID add"

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Encoding Decoding
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    

def encode(S):
    l1 = ':'.join([str(elem) for elem in S])
    S1 = l1.encode("ascii")
    S2 = base64.b64encode(S1)
    S3 = S2.decode("ascii")
    #print(f"Encoded string: {base64_string}")
    return S3


def decode(S):
    S1 = S.encode("ascii")
    S2 = base64.b64decode(S1)
    S3 = S2.decode("ascii")
    l1 = list(S3.split(":"))
    print ('<< decoding done >>')
    return l1

def SignalRead(mid,l):
    D1a = finder('ID',int(mid))
    D1b = get(D1a,'Signals')
    S1 = decode(D1b)
    print ('<< signal read >>')
    return (S1[l])

def SignalWrite(mid,P,V):
    D1a = finder('ID',int(mid))
    D1b = get(D1a,'Signals')
    S1 = decode(D1b)
    S1[P] = V
    print (S1)
    S3 = encode(S1)
    anych_modify('Signals',S3,mid)
    print ('<< signal write >>')
    return S3




#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Register User
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def reg(mid):
    try:
        Anid = AnonyID()
        print(Anid)
        a = anych_entry(str(mid),str(timestemp()),'100',str(Anid),0,'paused',0,str(encode([0,0,10,0,1])),0)
        b = anych_para_entry(str(mid),'Free',0,3,0,0,1,0,0,1,500,100,0,0,0,0,0,0,100)
        #tin = timestemp()

        return "✅  𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 !!"
    except Exception as e:
        print('xx error in registeration xx :/'+str(e))
        return 'Error while a registering user'

    #signal = picture sharing(on/off):block:picquality:broadcaster:censor

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Add Parameters
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def anych_para_entry(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S):
    # Connect to the database
    conn = sqlite3.connect('parameter1.0v.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Check if the ID already exists in the database
    cursor.execute("SELECT COUNT(*) FROM my_table WHERE MID=?", (A,))
    result = cursor.fetchone()

    if result[0] > 0:
        # ID already exists in the database, print a message and return
        print("⚠️ 𝗣𝗮𝗿𝗮𝗺𝗲𝘁𝗲𝗿 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗲𝘅𝗶𝘀𝘁!!")
    else:
        # ID does not exist in the database, insert a new row
        cursor.execute("INSERT INTO my_table (MID,MEM,NTI,REG,BLK,PIX,MSG,VDO,VCN,CEN,BAL,SPD,QOS,MSGIN,MSGOUT,PYMNT,HLD,OTP,ANBAL) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S))
        conn.commit()

        # Print a message to indicate successful registration
        print("✅ 𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆!!")

    # Close the cursor and the connection
    cursor.close()
    conn.close()


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Add Entry
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def anych_entry(A,B,C,D,E,F,G,H,I):
    J = nick()
    # Connect to the database
    conn = sqlite3.connect('Anonychatdb_5.0v.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Check if the ID already exists in the database
    cursor.execute("SELECT COUNT(*) FROM my_table WHERE ID=?", (A,))
    result = cursor.fetchone()

    if result[0] > 0:
        # ID already exists in the database, print a message and return
        print("⚠️ 𝗨𝘀𝗲𝗿 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗲𝘅𝗶𝘀𝘁!!")
    else:
        # ID does not exist in the database, insert a new row
        cursor.execute("INSERT INTO my_table (ID, tin, tout, AnonyID, Peer, Status, OTP, Signals, Timer, Nickname) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (A, B, C, D, E, F, G, H, I, J))
        conn.commit()

        # Print a message to indicate successful registration
        print("✅ 𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆!!")

    # Close the cursor and the connection
    cursor.close()
    conn.close()

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Verify User
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def verifyuser(C,mid):
    try:
        # Connect to the database
        conn = sqlite3.connect('Anonychatdb_5.0v.db')

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a SELECT query to retrieve the 'Status' column value
        cursor.execute("SELECT Status FROM my_table WHERE {}=?".format(C), (MID,))
        result = cursor.fetchone()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        # Return the 'Status' column value if found, or 'unregistered' otherwise
        if result is not None:
            return result[0]
        else:
            return 'unregistered'
    except Exception as e:
        print('xx verify user error :/'+str(e))

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Authentication
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


def auth(V1,mid):
    try:
        a = finder('AnonyID',mid)
        print('finder_auth : '+str(a))
        V2 = get((a),'OTP')
        print('auth_V2 :'+str(V2))
        if str(V1) == str(V2):
            #print('OK')
            return 'OK'
        else:
            #print('NOT OK')
            return 'NOT OK'
    except Exception as e:
        print(e)

#auth('12112','12112')

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Chat recorder
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def chtrecord(nm,mid,msg,reqmid):
    msg1 = msg.replace("\n", " ")
    with open('info_files/AI_chatlogs/'+str(reqmid)+'_logs.txt', 'a') as f:
        print(str(nm)+"["+str(mid)+']-('+timestemp()+')- '+str(msg1), file=f)
        #print(dt_string+'-MAN-CCLE Manager will restart the bot in 5 sec.', file=f)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Renew Leasing
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def leasing(mid,t):
    try:
        # Connect to the database
        conn = sqlite3.connect('Anonychatdb_5.0v.db')
        # Create a cursor object
        cursor = conn.cursor()
        # Execute an UPDATE query to set the 'tout' column value for the specified ID
        cursor.execute("UPDATE my_table SET tout=? WHERE ID=?", (t, mid))
        # Commit the changes to the database
        conn.commit()
        # Close the cursor and the connection
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)


#print(leasing(int('2346439302')))


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Modify Entry
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def anych_modify(C,V,mid):
    try:
        conn = sqlite3.connect('Anonychatdb_5.0v.db')
        cursor = conn.cursor()
        cursor.execute(f"UPDATE my_table SET {C}=? WHERE ID=?", (V, mid))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

#anych_modify('Status','Value','5370406979')

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Modify parameter
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def anych_para_modify(C,V,mid):
    try:
        conn = sqlite3.connect('parameter1.0v.db')
        cursor = conn.cursor()
        cursor.execute(f"UPDATE my_table SET {C}=? WHERE MID=?", (V, mid))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

#anych_modify('Status','Value','5370406979')

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def QRDCode(PID):
    decoded = pyzbar.decode(Image.open(PID))
    data = decoded[0].data
    xdata = str(data).replace("b'", "")
    fdata = str(xdata).replace("'", "")
    print (fdata)
    return fdata

def dataQ(mid,V):
    D1a = finder('ID',int(mid))
    D1b = get(D1a,V)
    print(D1b)
    return D1b



#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

def flush(mid):
    conn = sqlite3.connect('Anonychatdb_5.0v.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM my_table WHERE ID = ?", (mid,))
    row = cursor.fetchone()
    if row is not None:
        cursor.execute(f"DELETE FROM my_table WHERE ID = ?", (mid,))
        conn.commit()
        conn.close()
        return "ID Flushed"
    else:
        conn.close()
        return "User not registered !!"

def status(MID):
    try:
        C = 'ID'
        # Connect to the database
        conn = sqlite3.connect('Anonychatdb_5.0v.db')

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a SELECT query to retrieve the 'Status' column value
        cursor.execute("SELECT Status FROM my_table WHERE {}=?".format(C), (MID,))
        result = cursor.fetchone()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        # Return the 'Status' column value if found, or 'unregistered' otherwise
        if result is not None:
            return result[0]
        else:
            return 'unregistered'
    except Exception as e:
        print('Status checking error :/'+str(e))
        return '𝚞𝚗𝚔𝚗𝚘𝚠𝚗'

def channel(mid):

    a = find(mid)
    b = status(mid)
    #print (a)
    if a == 'User Not Registered':
        return 'You are not registered to connected with anyone\n\nPlease register first!!'
    elif b != 'linked':
        return 'You are registered but not linked with anyone\n\nPlease try again!!'
    elif b == 'linked':
        c = chk('mid','Peer')
        return c
    else:
        return 'Unable to send message to your peer\n\nPlease try again!!'

def inspector():
    state = '0'
    cmd = 'ps -fA | grep python'
    x = os.popen(cmd)
    o = x.read()
    #print(o)
    x2 = str(o.find('db_manager.2.py'))
    #print('find :'+str(x2))
    try:
        x3 = x2.isnumeric()
        print('x3 ::: '+str(x3))
        if x2 == '-1':
            if state == 'down':
                state = 'down'
            else:
                state = 'down'
                #bot.send_message('584429967', '𝙳𝙱 𝙼𝙰𝙽𝙰𝙶𝙴𝚁 : 𝙰𝚗𝚘𝚗𝚢𝙲𝚑𝚊𝚝 𝚋𝚘𝚝 𝚒𝚜 𝙳𝚘𝚠𝚗 🔴')
            return 'Random Connection Service is currently under maintenance\n\nPlease Try Later \nor\nUse Other Services'
        elif x3 == True:
            if state == 'up':
                state = 'up'
            else:
                state = 'up'
                #bot.send_message('584429967', '𝙳𝙱 𝙼𝙰𝙽𝙰𝙶𝙴𝚁 : 𝙰𝚗𝚘𝚗𝚢𝙲𝚑𝚊𝚝 𝚋𝚘𝚝 𝚒𝚜 𝚄𝚙 🟢')
            #print('up')
            return 'Random Connection Manager is trying to find partner!!\n\nPlease Wait...'
        else :
            if state == 'down':
                state = 'down'
            else:
                state = 'down'
                #bot.send_message('584429967', '𝙳𝙱 𝙼𝙰𝙽𝙰𝙶𝙴𝚁 : 𝙰𝚗𝚘𝚗𝚢𝙲𝚑𝚊𝚝 𝚋𝚘𝚝 𝚒𝚜 𝙳𝚘𝚠𝚗 🔴')
            #print('error')
            return 'Random Connection Manager is unresponsive\n\nPlease Try Later or Use Other Services '
    except Exception as e:
        try:
            if state == 'error':
                state = 'error'
            else:
                state = 'error'
                #bot.send_message('584429967', '𝙳𝙱 𝙼𝙰𝙽𝙰𝙶𝙴𝚁 : 𝙷𝚊𝚟𝚒𝚗𝚐 𝚎𝚛𝚛𝚘𝚛 𝚝𝚘 𝚌𝚑𝚎𝚌𝚔 𝙰𝚗𝚘𝚗𝚢𝙲𝚑𝚊𝚝 𝚋𝚘𝚝 𝚑𝚎𝚊𝚛𝚝𝚋𝚎𝚊𝚝 ‼️.')
            #print('error /: '+str(e))
            return 'Random Connection Service is currently under maintenance\n\nPlease Try Later \nor\nUse Other Services '
        except:
            return 'Error'
            print('Error')

def find(V):
    df = db()
    i2 = df.ID[df.ID == int(V)].index.tolist()
    x=str(i2)
    x=x.replace("[","")
    x=x.replace("]","")
    if x == "":
        return ('not found')
    else:
        #print ('index is : '+x)
        return i2

def db():
    conn = sqlite3.connect('Anonychatdb_5.0v.db')
    df = pd.read_sql_query("SELECT * FROM my_table", conn)
    conn.close()
    return df

def db1():
    conn = sqlite3.connect('Anonychatdb_5.0v.db')
    df = pd.read_sql_query("SELECT * FROM my_table", conn)
    print(df)
    conn.close()
    output_df = df
    table = tabulate(df, headers='keys', tablefmt='fancy_grid')
    with open('db1.txt', 'w') as f:
        f.write(table)
    return df

def dbp():
    conn = sqlite3.connect('parameter1.0v.db')
    df = pd.read_sql_query("SELECT * FROM my_table", conn)
    conn.close()
    return df

def dbp1():
    conn = sqlite3.connect('parameter1.0v.db')
    df = pd.read_sql_query("SELECT * FROM my_table", conn)
    print(df)
    conn.close()
    return df

def emoji(In):
    if In == 1:
        return '🟢'
    else:
        return '🔴'
def invert(In):
    if str(In) == '1':
        return 0
    elif str(In) == '0':
        return 1
    else:
        print ('error')

def photoconverter(img):
    image_path = img
    image_file = Image.open(image_path)
    image_file.save("image_name.jpg", quality=95)

    image_file.save("image_name2.jpg", quality=25)

    # Example-2
    image_file.save("image_name3.jpg", quality=1)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                           Switch
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def switch(V):   
    if V == '1':
        return '0'
    elif V == '0':
        return '1'

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       AnonyID 
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def AnonyID():
    try:
        IDi = True
        while IDi :
            aID = (str(random.randint(9,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,0))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
            print('Proposed Aid :'+str(aID))
            f = finder('AnonyID',int(aID))
            #print
            if f == "not found":
                IDi = False
                #print('Proposed Aid :'+str(aID))
                return aID
            else:
                #print('Proposed Aid :'+str(aID))
                IDi = True
    except Exception as e:
        #print('error')
        print(e)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Find module
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def finder(C,Q):
    try:
        df = db()
        x = df.index[df[C]==Q].tolist()
        p = str(x)
        p=p.replace("[","")
        p=p.replace("]","")
        if p == "" :
            return 'not found'
        else:
            return p
    except Exception as e:
        print(e)

#print(finder('ID',int('2346439310')))

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       QR Code Generator 
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def QRCode(link,mID):
    try:
        os.remove('temp/qrcode'+str(mID)+'.png')
    except:
        print('no QRcode')
    img = qrcode.make(link)
    img.save('temp/qrcode'+str(mID)+'.png')
    return 'qrcode done'

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Get module
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def get(index,C):
    try:
        df = db()
        p = df._get_value(int(index), C)
        return p 
    except Exception as e:
        return '-invalid-'
        #print('Get:'+str(e))

#print (get(10,'ID'))

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Count waitings
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def findw(S):
    conn = sqlite3.connect('Anonychatdb_5.0v.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM my_table WHERE Status=?", (S,))
    count = c.fetchone()[0]
    conn.close()
    return count

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Lookup Module
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def lookup(RC,LC,Q):
    try:
        df = dbp()
        x = df.index[df[RC]==Q].tolist()
        p = str(x)
        p=p.replace("[","")
        p=p.replace("]","")
        p2 = df._get_value(int(p), LC)
        if p2 == "" :
            return 'not found'
        else:
            return p2
    except Exception as e:
        print(e)

#print(loopup('ID',int('2346439310')))

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       OTP Generator 
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def OTP(mid):
    try:
        oID = (str(random.randint(1,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
        #print(oID)
        anych_modify('OTP',oID,mid)
        f = finder('OTP',oID)
        return oID
    except Exception as e:
        print(e)
        #bot.send_message((message.chat.id),'Unable to complete the operation')

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Switch Module
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def SW(S,V):
    W11a = 'ON'
    W11b = 'ON'
    W11c = 'ON'
    W11d = 'ON'
    W11e = 'ON'



#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Broadcast subscriber number
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def broadcast(l):
    import Broadcasting
    result = Broadcasting.subscribers_count(l)
    print(result)
    return (result)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Broadcast subscribers IDs
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def broadcastIDs(l,n):
    import Broadcasting
    result = Broadcasting.subscribers_ID(l,n)
    return (result)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                       Image Converter
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def photoconverter(img):
        image_path = img
        image_file = Image.open(image_path)
        image_file.save("image_name.jpg", quality=95)

        image_file.save("image_name2.jpg", quality=25)

        # Example-2
        image_file.save("image_name3.jpg", quality=1)


@bot.message_handler(content_types=['sticker'])
def handle_sticker_message(message):
    print("ANONYCHATBOT--User "+str(message.chat.id)+" attemping to send  sticker")
    A1a = finder('ID',int(message.chat.id))
    A1b = str(get(A1a,'Peer'))
    peer_status = get((A1a),'Status')
    anych_modify('Status','paused',int(str(message.chat.id)))
    if A1b == 0:
        msgpdc1a = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝗻𝗼𝘁 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 !!")
        time.sleep(2)
        bot.delete_message(message.chat.id, msgpdc1a.message_id)
        print("ANONYCHATBOT--User "+str(message.chat.id)+" failed to send sticker (no partner found)")
    else:
        try:
            A1a = get((finder('ID',int(message.chat.id))),'Peer')
            file_id = message.sticker.file_id
            bot.send_sticker(chat_id=A1a, sticker=file_id)
            #msgpic = bot.send_message(message.chat.id, '✅ 𝘀𝗲𝗻𝘁!!')
            #time.sleep(1)
            #bot.delete_message(message.chat.id, msgpic.message_id)
            print("ANONYCHATBOT--User "+str(message.chat.id)+" sucessfully send sticker")
        except Exception as e:
            print('Sending document error /: '+str(e))
            bot.send_message((message.chat.id), "❌ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 !")
            print("ANONYCHATBOT--User "+str(message.chat.id)+" failed to send sticker (system process error)")
    anych_modify('Status',str(peer_status),int(str(message.chat.id)))        


@bot.message_handler(content_types=['poll'])
def handle_poll_message(message):
    print("ANONYCHATBOT--User "+str(message.chat.id)+" attemping to send  poll")
    A1a = finder('ID',int(message.chat.id))
    A1b = str(get(A1a,'Peer'))
    peer_status = get((A1a),'Status')
    anych_modify('Status','paused',int(str(message.chat.id)))
    if A1b == 0:
        msgpdc1a = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝗻𝗼𝘁 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 !!")
        time.sleep(2)
        bot.delete_message(message.chat.id, msgpdc1a.message_id)
        print("ANONYCHATBOT--User "+str(message.chat.id)+" failed to send poll (no partner found)")
    else:
        try:
            A1a = get((finder('ID',int(message.chat.id))),'Peer')
            question = message.poll.question
            options = [option.text for option in message.poll.options]
            is_quiz = message.poll.type == 'poll'
            #bot.send_poll(A1a, question, options=options, is_quiz=is_quiz)
            #msgpic = bot.send_message(message.chat.id, '✅ 𝘀𝗲𝗻𝘁!!')
            #time.sleep(1)
            bot.delete_message(message.chat.id, msgpic.message_id)
            print("ANONYCHATBOT--User "+str(message.chat.id)+" sucessfully send poll")
        except Exception as e:
            print('Sending document error /: '+str(e))
            bot.send_message((message.chat.id), "❌ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 !")
            print("ANONYCHATBOT--User "+str(message.chat.id)+" failed to send poll (system process error)")
    anych_modify('Status',str(peer_status),int(str(message.chat.id)))


@bot.message_handler(content_types=['animation'])
def handle_gif_message(message):
    A1a = finder('ID',int(message.chat.id))
    A1b = str(get(A1a,'Peer'))
    bot.send_chat_action(int(message.chat.id), 'upload_photo')
    bot.send_chat_action(int(A1b), 'upload_photo')
    VDOchk = lookup('MID','PIX',int(A1b))
    if VDOchk == 0:
        bot.send_message((message.chat.id), "❌  𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗵𝗮𝘀 𝗯𝗹𝗼𝗰𝗸𝗲𝗱 𝘁𝗵𝗲 𝗽𝗶𝗰𝘁𝘂𝗿𝗲𝘀 𝗿𝗲𝗰𝗲𝗶𝘃𝗶𝗻𝗴 !!")
        bot.send_message((A1b), "❌  𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗮𝘁𝘁𝗲𝗺𝗽𝘁 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘆𝗼𝘂 𝗮 𝗽𝗶𝗰𝘁𝘂𝗿𝗲! 𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝗮𝗯𝗹𝗲 𝗽𝗶𝗰𝘁𝘂𝗿𝗲 𝗿𝗲𝗰𝗲𝗶𝘃𝗶𝗻𝗴 𝗳𝗿𝗼𝗺 𝘆𝗼𝘂𝗿 𝘀𝗲𝘁𝘁𝗶𝗻𝗴𝘀!!")
        with open("setting_help.gif", "rb") as gif:
            bot.send_animation((A1b), animation=gif, caption="How to change settings:")
    else:
        print("ANONYCHATBOT--User "+str(message.chat.id)+" attemping to send  gif")
        A1a = finder('ID',int(message.chat.id))
        A1b = str(get(A1a,'Peer'))
        peer_status = get((A1a),'Status')
        anych_modify('Status','paused',int(str(message.chat.id)))
        if A1b == 0:
            msgpdc1a = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝗻𝗼𝘁 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 !!")
            time.sleep(2)
            bot.delete_message(message.chat.id, msgpdc1a.message_id)
            print("ANONYCHATBOT--User "+str(message.chat.id)+" failed to send gif (no partner found)")
        else:
            try:
                A1a = get((finder('ID',int(message.chat.id))),'Peer')
                file_id = message.animation.file_id
                bot.send_animation(A1a, file_id)
                msgpic = bot.send_message(message.chat.id, '✅ 𝗚𝗶𝗳 𝗻𝗼𝘁𝗲 𝘀𝗲𝗻𝘁!!')
                time.sleep(1)
                bot.delete_message(message.chat.id, msgpic.message_id)
                anych_para_modify('BAL',(lookup('MID','BAL',message.chat.id))-0.5,message.chat.id)
                bot.delete_message(message.chat.id, msgpic.message_id)
                anych_para_modify('MSGOUT',int(lookup('MID','MSGOUT',message.chat.id))+1,message.chat.id)
                anych_para_modify('MSGIN',int(lookup('MID','MSGIN',int(A1a)))+1,int(A1a))
                print("ANONYCHATBOT--User "+str(message.chat.id)+" sucessfully send gif")
            except Exception as e:
                print('Sending document error /: '+str(e))
                bot.send_message((message.chat.id), "❌ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘆𝗼𝘂𝗿 𝗴𝗶𝗳!")
                print("ANONYCHATBOT--User "+str(message.chat.id)+" failed to send gif (system process error)")
        anych_modify('Status',str(peer_status),int(str(message.chat.id)))



@bot.message_handler(content_types=['document'])
def on_document(message):
    print("ANONYCHATBOT--User "+str(message.chat.id)+" attemping to send  document")
    A1a = finder('ID',int(message.chat.id))
    A1b = str(get(A1a,'Peer'))
    bot.send_chat_action(int(message.chat.id), 'upload_document')
    bot.send_chat_action(int(A1b), 'upload_document')
    peer_status = get((A1a),'Status')
    anych_modify('Status','paused',int(str(message.chat.id)))
    if A1b == 0:
        msgpdc1a = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝗻𝗼𝘁 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 !!")
        time.sleep(2)
        bot.delete_message(message.chat.id, msgpdc1a.message_id)
        print("ANONYCHATBOT--User "+str(message.chat.id)+" failed to send document (no partner found)")
    else:
        try:
            A1a = get((finder('ID',int(message.chat.id))),'Peer')
            file_id = message.document.file_id
            #bot.send_video(A1a, file_id)
            bot.send_document(chat_id=A1a, document=file_id)
            msgpic = bot.send_message(message.chat.id, '✅ 𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁 𝗻𝗼𝘁𝗲 𝘀𝗲𝗻𝘁!!')
            time.sleep(1)
            bot.delete_message(message.chat.id, msgpic.message_id)
            anych_para_modify('BAL',(lookup('MID','BAL',message.chat.id))-10,message.chat.id)
            anych_para_modify('MSGOUT',int(lookup('MID','MSGOUT',message.chat.id))+1,message.chat.id)
            anych_para_modify('MSGIN',int(lookup('MID','MSGIN',int(A1a)))+1,int(A1a))
            print("ANONYCHATBOT--User "+str(message.chat.id)+" sucessfully send document")
        except Exception as e:
            print('Sending document error /: '+str(e))
            bot.send_message((message.chat.id), "❌ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘆𝗼𝘂𝗿 𝗱𝗼𝗰𝘂𝗺𝗲𝗻𝘁 !!")
            print("ANONYCHATBOT--User "+str(message.chat.id)+" failed to send document (system process error)")
    anych_modify('Status',str(peer_status),int(str(message.chat.id)))


@bot.message_handler(content_types=['video'])
def on_video(message):
    print("ANONYCHATBOT--User "+str(message.chat.id)+" attemping to send video message")
    A1a = finder('ID',int(message.chat.id))
    A1b = str(get(A1a,'Peer'))
    bot.send_chat_action(int(message.chat.id), 'upload_video')
    bot.send_chat_action(int(A1b), 'upload_video')
    VDOchk = lookup('MID','VDO',int(A1b))
    if VDOchk == 0:
        bot.send_message((message.chat.id), "❌  𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗵𝗮𝘀 𝗯𝗹𝗼𝗰𝗸𝗲𝗱 𝘁𝗵𝗲 𝘃𝗶𝗱𝗲𝗼𝘀 𝗿𝗲𝗰𝗲𝗶𝘃𝗶𝗻𝗴 !!")
        bot.send_message((A1b), "❌  𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗮𝘁𝘁𝗲𝗺𝗽𝘁 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘆𝗼𝘂 𝗮 𝘃𝗶𝗱𝗲𝗼𝘀!! 𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝗮𝗯𝗹𝗲 𝘃𝗶𝗱𝗲𝗼 𝗿𝗲𝗰𝗲𝗶𝘃𝗶𝗻𝗴 𝗳𝗿𝗼𝗺 𝘆𝗼𝘂𝗿 𝘀𝗲𝘁𝘁𝗶𝗻𝗴𝘀!!")
        with open("setting_help.gif", "rb") as gif:
            bot.send_animation((A1b), animation=gif, caption="How to change settings:")
    else:
        A1a = finder('ID',int(message.chat.id))
        A1b = str(get(A1a,'Peer'))
        peer_status = get((A1a),'Status')
        anych_modify('Status','paused',int(str(message.chat.id)))
        if A1b == 0:
            msgpdc1a = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝗻𝗼𝘁 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 !!")
            time.sleep(2)
            bot.delete_message(message.chat.id, msgpdc1a.message_id)
            print("ANONYCHATBOT--User "+str(message.chat.id)+" failed to send video message (no partner found)")
        else:
            try:
                A1a = get((finder('ID',int(message.chat.id))),'Peer')
                file_id = message.video.file_id
                bot.send_video(A1a, file_id)
                msgpic = bot.send_message(message.chat.id, '✅ 𝗩𝗶𝗱𝗲𝗼 𝗻𝗼𝘁𝗲 𝘀𝗲𝗻𝘁!!')
                time.sleep(1)
                anych_para_modify('BAL',(lookup('MID','BAL',message.chat.id))-5,message.chat.id)
                bot.delete_message(message.chat.id, msgpic.message_id)
                anych_para_modify('MSGOUT',int(lookup('MID','MSGOUT',message.chat.id))+1,message.chat.id)
                anych_para_modify('MSGIN',int(lookup('MID','MSGIN',int(A1a)))+1,int(A1a))
                print("ANONYCHATBOT--User "+str(message.chat.id)+" sucessfully send video message")
            except Exception as e:
                print('Sending video error /: '+str(e))
                bot.send_message((message.chat.id), "❌ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘆𝗼𝘂𝗿 𝘃𝗶𝗱𝗲𝗼 !!")
                print("ANONYCHATBOT--User "+str(message.chat.id)+" failed to send video message (system process error)")
        anych_modify('Status',str(peer_status),int(str(message.chat.id)))

@bot.message_handler(content_types=['voice'])
def on_voice(message):
    print("ANONYCHATBOT--User "+str(message.chat.id)+" attemping to send voice message")
    A1a = finder('ID',int(message.chat.id))
    A1b = str(get(A1a,'Peer'))
    bot.send_chat_action(int(message.chat.id), 'upload_audio')
    bot.send_chat_action(int(A1b), 'record_audio')
    VDOchk = lookup('MID','VNC',int(A1b))
    if VDOchk == 0:
        bot.send_message((message.chat.id), "❌  𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗵𝗮𝘀 𝗯𝗹𝗼𝗰𝗸𝗲𝗱 𝘁𝗵𝗲 𝘃𝗼𝗶𝗰𝗲 𝗻𝗼𝘁𝗲𝘀 𝗿𝗲𝗰𝗲𝗶𝘃𝗶𝗻𝗴 !!")
        with open("setting_help.gif", "rb") as gif:
            bot.send_animation((A1b), animation=gif, caption="How to change settings:")
        bot.send_message((A1b), "❌  𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗮𝘁𝘁𝗲𝗺𝗽𝘁 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘆𝗼𝘂 𝗮 𝘃𝗼𝗶𝗰𝗲 𝗻𝗼𝘁𝗲! 𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝗮𝗯𝗹𝗲 𝘃𝗼𝗶𝗰𝗲 𝗻𝗼𝘁𝗲 𝗿𝗲𝗰𝗲𝗶𝘃𝗶𝗻𝗴 𝗳𝗿𝗼𝗺 𝘆𝗼𝘂𝗿 𝘀𝗲𝘁𝘁𝗶𝗻𝗴𝘀!!")
    else:
        A1a = finder('ID',int(message.chat.id))
        A1b = str(get(A1a,'Peer'))
        peer_status = get((A1a),'Status')
        anych_modify('Status','paused',int(str(message.chat.id)))
        if A1b == 0:
            msgpdc1a = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝗻𝗼𝘁 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 !!")
            time.sleep(2)
            bot.delete_message(message.chat.id, msgpdc1a.message_id)
            print("ANONYCHATBOT--User "+str(message.chat.id)+" failed to send voice message (no partner found)")
        else:
            try:
                A1a = get((finder('ID',int(message.chat.id))),'Peer')
                file_id = message.voice.file_id
                bot.send_voice(A1a, file_id)
                msgpic = bot.send_message(message.chat.id, '✅  𝗩𝗼𝗶𝗰𝗲 𝗻𝗼𝘁𝗲 𝘀𝗲𝗻𝘁!!')
                time.sleep(1)
                anych_para_modify('BAL',(lookup('MID','BAL',message.chat.id))-2.5,message.chat.id)
                bot.delete_message(message.chat.id, msgpic.message_id)
                anych_para_modify('MSGOUT',int(lookup('MID','MSGOUT',message.chat.id))+1,message.chat.id)
                anych_para_modify('MSGIN',int(lookup('MID','MSGIN',int(A1a)))+1,int(A1a))
                print("ANONYCHATBOT--User "+str(message.chat.id)+" sucessfully send voice message")

            except Exception as e:
                print('Sending voice error /: '+str(e))
                bot.send_message((message.chat.id), "❌  𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘆𝗼𝘂𝗿 𝘃𝗼𝗶𝗰𝗲 𝗻𝗼𝘁𝗲 !!")
                print("ANONYCHATBOT--User "+str(message.chat.id)+" failed to send voice message (system process error)")
        anych_modify('Status',str(peer_status),int(str(message.chat.id)))

@bot.message_handler(content_types=['photo'])
def on_photo(message):
    A1a = finder('ID',int(message.chat.id))
    A1b = str(get(A1a,'Peer'))
    VDOchk = lookup('MID','PIX',int(A1b))
    if VDOchk == 0:
        bot.send_message((message.chat.id), "❌  𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗵𝗮𝘀 𝗯𝗹𝗼𝗰𝗸𝗲𝗱 𝘁𝗵𝗲 𝗽𝗶𝗰𝘁𝘂𝗿𝗲𝘀 𝗿𝗲𝗰𝗲𝗶𝘃𝗶𝗻𝗴 !!")
        bot.send_message((A1b), "❌  𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗮𝘁𝘁𝗲𝗺𝗽𝘁 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘆𝗼𝘂 𝗮 𝗽𝗶𝗰𝘁𝘂𝗿𝗲! 𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝗮𝗯𝗹𝗲 𝗽𝗶𝗰𝘁𝘂𝗿𝗲 𝗿𝗲𝗰𝗲𝗶𝘃𝗶𝗻𝗴 𝗳𝗿𝗼𝗺 𝘆𝗼𝘂𝗿 𝘀𝗲𝘁𝘁𝗶𝗻𝗴𝘀!!")
        with open("setting_help.gif", "rb") as gif:
            bot.send_animation((A1b), animation=gif, caption="How to change settings:")
    else:
        try:
            A1a = finder('ID',int(message.chat.id))
            peer_status = get((A1a),'Status')
            anych_modify('Status','paused',int(str(message.chat.id)))
            if str(dataQ(message.chat.id,'Peer')) == '0':
                try:
                    msgpic = bot.send_message(message.chat.id, '𝙲𝚑𝚎𝚌𝚔𝚒𝚗𝚐 𝚀𝚁 𝙲𝚘𝚍𝚎...')
                    file_id = message.photo[-1].file_id
                    file_info = bot.get_file(file_id)
                    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format('5768243722:AAGuPYWlGCH9x7I-N5bJ3u6royTuEfQ5ZFw', file_info.file_path))
                    with open('temp/img/'+str(message.chat.id)+'_photo.jpg','wb') as f:
                        f.write(file.content)
                    linkq = QRDCode('temp/img/'+str(message.chat.id)+'_photo.jpg')
                    if str(linkq)[:4] == "/pvt":
                         msgpic = bot.send_message(message.chat.id, '𝙲𝚕𝚒𝚌𝚔 𝚘𝚗 𝚝𝚑𝚒𝚜 𝚕𝚒𝚗𝚔𝚒𝚗𝚐 𝚝𝚘 𝚌𝚘𝚗𝚗𝚎𝚌𝚝 :\n '+str(linkq))
                    else:
                        msgpic = bot.send_message(message.chat.id, '❌ 𝚆𝚛𝚘𝚗𝚐𝚎 𝚀𝚁 𝙲𝚘𝚍𝚎 ')
                except:
                    msgpic = bot.send_message(message.chat.id, "𝚈𝚘𝚞𝚛 𝚙𝚊𝚛𝚝𝚗𝚎𝚛 𝚒𝚜 𝚗𝚘𝚝 𝚕𝚒𝚗𝚔𝚎𝚍 𝚠𝚒𝚝𝚑 𝚢𝚘𝚞 !!")
                    time.sleep(2)
                    bot.delete_message(message.chat.id, msgpic.message_id)
            elif (str(SignalRead(dataQ(message.chat.id,'Peer'),0))) == '1':
                msgpic = bot.send_message(message.chat.id, '❌ 𝚈𝚘𝚞𝚛 𝚕𝚒𝚗𝚔𝚎𝚍 𝚙𝚊𝚛𝚝𝚗𝚎𝚛 𝚑𝚊𝚟𝚎 𝚗𝚘𝚝 𝚎𝚗𝚊𝚋𝚕𝚎𝚍 𝚝𝚑𝚎 𝚙𝚒𝚌𝚝𝚞𝚛𝚎 𝚛𝚎𝚌𝚎𝚒𝚟𝚒𝚗𝚐.')
                time.sleep(2)
                bot.delete_message(message.chat.id, msgpic.message_id)
            elif (str(SignalRead(dataQ(message.chat.id,'Peer'),0))) == '0':
                try:
                    D1a = finder('ID',int(message.chat.id))
                    D1b = get(D1a,'Peer')
                    bot.send_chat_action(int(message.chat.id), 'upload_photo')
                    bot.send_chat_action(int(D1b), 'upload_photo')
                    file_id = message.photo[-1].file_id
                    file_info = bot.get_file(file_id)
                    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format('5768243722:AAGuPYWlGCH9x7I-N5bJ3u6royTuEfQ5ZFw', file_info.file_path))
                    with open('temp/img/'+str(message.chat.id)+'_photo.jpg','wb') as f:
                        f.write(file.content)
                    img = Image.open('temp/img/'+str(message.chat.id)+'_photo.jpg')
                    photoconverter('temp/img/'+str(message.chat.id)+'_photo.jpg')
                    draw = ImageDraw.Draw(img)
                    # font = ImageFont.truetype(<font-file>, <font-size>)
                    text = "Sent via :\n@CCLE_anonychatbot\n[https://t.me/CCLE_anonychatbot]\n"+str(timestemp())
                    font = ImageFont.truetype("Aaargh.ttf", 25)
                    # draw.text((x, y),"Sample Text",(r,g,b))
                    fill_color = (0, 0, 0)
                    stroke_color = (50, 50, 50)
                  #=================
                    im = Image.new(mode="P", size=(0, 0))
                    draw = ImageDraw.Draw(im)
                    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
                    #textwidth, textheight = draw.textsize(text, font)
                  #=================
                    width, height = img.size 
                    x=width/2-width/2
                    y=height-height-600
                    #draw.text((x, y), text,(255,255,255), font=font)
                    draw.text((x, y), text, font=font, fill=fill_color, stroke_width=2, stroke_fill=stroke_color)



                    draw.text((0, 0),"Sent via :\nhttps://t.me/CCLE_anonychatbot\n @CCLE_anonychatbot",(255,255,255),font=font)

                    img.save('temp/img/'+str(message.chat.id)+'_photo.jpg',dpi=(600,600)) 

                    try:
                        D1a = finder('ID',int(message.chat.id))
                        D1b = get(D1a,'Peer')
                        D2a = finder('ID',int(D1b))
                        D2b = get((D2a),'tout')
                        #print ('D2a : '+str(D2a))
                        #print ('D2b : '+str(D2b))
                        if int(D2b) <= 0 :
                            msgLE = bot.send_message((message.chat.id), "❌ 𝚈𝚘𝚞𝚛 𝚕𝚎𝚊𝚜𝚎 𝚒𝚜 𝚎𝚡𝚙𝚒𝚛𝚎𝚍 !!")
                            time.sleep(2)
                            bot.delete_message(message.chat.id, msgLE.message_id)
                        else:

                            try:
                                anych_modify('Status',str(peer_status),int(str(message.chat.id)))
                                E1a = finder('ID',int(message.chat.id))
                                E1b = str(get(E1a,'Status'))
                                print('test1'+str(E1b))
                                if E1b == 'private':
                                    anych_modify('Status','paused',int(str(message.chat.id)))
                                    bot.send_photo(str(D1b), photo=open('temp/img/'+str(message.chat.id)+'_photo.jpg', 'rb'))
                                    os.remove('temp/img/'+str(message.chat.id)+'_photo.jpg')
                                    leasing(int(message.chat.id),10000)
                                    anych_para_modify('BAL',(lookup('MID','BAL',message.chat.id))-2.5,message.chat.id)
                                    anych_para_modify('MSGOUT',int(lookup('MID','MSGOUT',message.chat.id))+1,message.chat.id)
                                    anych_para_modify('MSGIN',int(lookup('MID','MSGIN',int(D1b)))+1,int(D1b))
                                    msgpic = bot.send_message(message.chat.id, '✅ 𝗣𝗶𝗰𝘁𝘂𝗿𝗲 𝘀𝗲𝗻𝘁 !!')
                                    time.sleep(1)
                                    bot.delete_message(message.chat.id, msgpic.message_id)
                                    anych_modify('Status',str(peer_status),int(str(message.chat.id)))
                                elif E1b == 'permanent':
                                    anych_modify('Status','paused',int(str(message.chat.id)))
                                    bot.send_photo(str(D1b), photo=open('temp/img/'+str(message.chat.id)+'_photo.jpg', 'rb'))
                                    os.remove('temp/img/'+str(message.chat.id)+'_photo.jpg')
                                    leasing(int(message.chat.id),10000)
                                    anych_para_modify('BAL',(lookup('MID','BAL',message.chat.id))-2.5,message.chat.id)
                                    anych_para_modify('MSGOUT',int(lookup('MID','MSGOUT',message.chat.id))+1,message.chat.id)
                                    anych_para_modify('MSGIN',int(lookup('MID','MSGIN',int(D1b)))+1,int(D1b))
                                    msgpic = bot.send_message(message.chat.id, '✅ 𝗣𝗶𝗰𝘁𝘂𝗿𝗲 𝘀𝗲𝗻𝘁 !!')
                                    time.sleep(1)
                                    bot.delete_message(message.chat.id, msgpic.message_id)
                                elif E1b == 'linked':
                                    anych_modify('Status','paused',int(str(message.chat.id)))
                                    bot.send_photo(str(D1b), photo=open('temp/img/'+str(message.chat.id)+'_photo.jpg', 'rb'))
                                    os.remove('temp/img/'+str(message.chat.id)+'_photo.jpg')
                                    leasing(int(message.chat.id),120)
                                    anych_para_modify('BAL',(lookup('MID','BAL',message.chat.id))-2.5,message.chat.id)
                                    anych_para_modify('MSGOUT',int(lookup('MID','MSGOUT',message.chat.id))+1,message.chat.id)
                                    anych_para_modify('MSGIN',int(lookup('MID','MSGIN',int(D1b)))+1,int(D1b))
                                    msgpic = bot.send_message(message.chat.id, '✅ 𝗣𝗶𝗰𝘁𝘂𝗿𝗲 𝘀𝗲𝗻𝘁 !!')
                                    time.sleep(1)
                                    bot.delete_message(message.chat.id, msgpic.message_id)
                                    anych_modify('Status',str(peer_status),int(str(message.chat.id)))
                                else:
                                    msgpic = bot.send_message(message.chat.id, '𝚈𝚘𝚞𝚛 𝚊𝚛𝚎 𝚛𝚎𝚐𝚒𝚜𝚝𝚎𝚛𝚎𝚍 𝚠𝚒𝚝𝚑 𝚞𝚗𝚔𝚗𝚘𝚠𝚗 𝚜𝚝𝚊𝚝𝚞𝚜 , \n\n𝚆𝚎 𝚌𝚊𝚗𝚗𝚘𝚝 𝚙𝚎𝚛𝚏𝚘𝚛𝚖 𝚊𝚗𝚢 𝚘𝚙𝚎𝚛𝚊𝚝𝚒𝚘𝚗.\n\n𝙿𝚕𝚎𝚊𝚜𝚎 𝚌𝚕𝚘𝚜𝚎 𝚊𝚕𝚕 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗𝚜 𝚏𝚒𝚛𝚜𝚝 𝚊𝚗𝚍 𝚝𝚛𝚢 𝚊𝚐𝚊𝚒𝚗 !!')
                                    time.sleep(2)
                                    bot.delete_message(message.chat.id, msgpic.message_id)
                                    leasing(int(message.chat.id),0)
                            except Exception as e:
                                msgpic = bot.send_message(message.chat.id, "❌ 𝚄𝚗𝚊𝚋𝚕𝚎 𝚝𝚘 𝚙𝚛𝚘𝚌𝚎𝚜𝚜 𝚙𝚒𝚌𝚞𝚝𝚛𝚎𝚜 𝚊𝚝 𝚝𝚑𝚎 𝚖𝚘𝚖𝚎𝚗𝚝 !!")
                                time.sleep(2)
                                bot.delete_message(message.chat.id, msgpic.message_id)
                    except Exception as e:
                        msgpic = bot.send_message(message.chat.id, "𝚈𝚘𝚞𝚛 𝚙𝚊𝚛𝚝𝚗𝚎𝚛 𝚒𝚜 𝚗𝚘𝚝 𝚕𝚒𝚗𝚔𝚎𝚍 𝚠𝚒𝚝𝚑 𝚢𝚘𝚞 !!")
                        print('Img error /: '+str(e))
                        time.sleep(2)
                        bot.delete_message(message.chat.id, msgpic.message_id)
                except Exception as e:
                    msgpic = bot.send_message(message.chat.id, "❌ 𝚄𝚗𝚊𝚋𝚕𝚎 𝚝𝚘 𝚙𝚛𝚘𝚌𝚎𝚜𝚜 𝚙𝚒𝚌𝚞𝚝𝚛𝚎𝚜 𝚊𝚝 𝚝𝚑𝚎 𝚖𝚘𝚖𝚎𝚗𝚝 !!")
                    print('Img error /: '+str(e))
                    time.sleep(2)
                    bot.delete_message(message.chat.id, msgpic.message_id)
            else :
                print('error')
            anych_modify('Status',str(peer_status),int(str(message.chat.id)))
        except Exception as e:
            msgcon = bot.send_message(message.chat.id, "𝚈𝚘𝚞𝚛 𝙸𝙳 𝚒𝚜 𝚗𝚘𝚝 𝚛𝚎𝚐𝚒𝚜𝚝𝚎𝚛𝚎𝚍!!\n\n𝙿𝚕𝚎𝚊𝚜𝚎 𝚠𝚊𝚒𝚝 𝚠𝚑𝚒𝚕𝚎 𝚛𝚎𝚐𝚒𝚜𝚝𝚛𝚊𝚝𝚒𝚘𝚗 𝚒𝚗 𝚙𝚛𝚘𝚐𝚛𝚎𝚜𝚜!!")
            anych_modify('Status',str(peer_status),int(str(message.chat.id)))




@bot.message_handler(content_types=['text'])
#@bot.message_handler(commands=['start'])

def start(message):
    if str(message.text) == '/start':
        bot.send_chat_action(str(message.chat.id), 'typing')
        #print("connecting")
        mid = str(message.chat.id)
        a = find(mid)
        b = lookup('MID','MID',message.chat.id)
        print(mid)
        print('finder result : '+str(a))
        if str(b) == 'None':
            anych_para_entry(str(message.chat.id),'Free',0,3,0,0,1,0,0,1,500,100,0,0,0,0,0,0,100)
        else:
            if str(a) == 'not found':
                if (os.stat("info_files/notice.txt").st_size == 0) :
                            return 0
                else:
                    time.sleep(0)
                    with open('info_files/notice.txt') as f:
                        f = f.read()
                    bot.send_chat_action(str(message.chat.id), 'typing')
                    keyboard = types.InlineKeyboardMarkup()
                    button_a = types.InlineKeyboardButton(text='Open Text Message', callback_data='check_t')
                    button_b = types.InlineKeyboardButton(text='Open Voice Message', callback_data='check_v')
                    button_c = types.InlineKeyboardButton(text='Ignore', callback_data='ignore')
                    keyboard.add(button_a,button_b)
                    keyboard.add(button_c)
                    bot.send_message(message.chat.id, "📥 𝟮 𝗨𝗻𝘀𝗲𝗲𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲", reply_markup=keyboard)
                    #msgnotice = bot.send_message(message.chat.id, "📥 𝟭 𝗨𝗻𝘀𝗲𝗲𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲")
                    bot.send_chat_action(str(message.chat.id), 'typing')
                    time.sleep(0)
                    #msgnotice = bot.send_message(message.chat.id, "⚠️ Important Notice!! ⚠️\n\n"+str(f))
                    #msgnotice2 = bot.edit_message_text("⚠️ Important Notice!! ⚠️\n\n"+str(f) , message.chat.id, msgnotice.message_id)
                    bot.send_chat_action(str(message.chat.id), 'typing')
                    #time.sleep(23)
                    #bot.delete_message(message.chat.id, msgnotice2.message_id)
                msgcon = bot.send_message(message.chat.id, "⚠️ 𝗬𝗼𝘂𝗿 𝗶𝗱 𝗶𝘀 𝗻𝗼𝘁 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝘄𝗵𝗶𝗹𝗲 𝘄𝗲 𝗮𝗿𝗲 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗶𝗻𝗴 𝘆𝗼𝘂 !!")
                a = reg(str(message.chat.id))
                with open('info_files/Anonychat_reg_logs.txt', 'a') as f:
                    print('USER Registered : cID('+str(message.chat.id)+') : nID('+str(message.from_user.first_name)+') : tIN('+str(timestemp())+')', file=f)
                bot.send_chat_action(str(message.chat.id), 'typing')
                time.sleep(0)
                msgcon2 = bot.edit_message_text(str(a), message.chat.id, msgcon.message_id)
                bot.send_chat_action(str(message.chat.id), 'typing')
                time.sleep(0)
                bot.send_message('584429967', 'USER Registered: '+str(message.from_user.first_name)+' ('+get((finder('ID',int(message.chat.id))),'Nickname')+')')
                bot.send_chat_action(str(message.chat.id), 'typing')
                #with open('info_files/anonymouschats_message01.ogg', 'rb') as audio:
                #    bot.send_voice(str(message.chat.id), audio,caption="Amenda , Camilla and Jeff want to tell you somthing!")
                anych_modify('Status','waiting',int(str(message.chat.id)))


            else:
                bot.send_message('584429967', 'USER Online: '+str(message.from_user.first_name)+' ('+get((finder('ID',int(message.chat.id))),'Nickname')+')')

            keyboard = types.InlineKeyboardMarkup()
            button_a = types.InlineKeyboardButton(text='🔐 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗖𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻', callback_data='A1')
            button_b = types.InlineKeyboardButton(text='🔀 𝗥𝗮𝗻𝗱𝗼𝗺 𝗖𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻', callback_data='B1')
            button_c = types.InlineKeyboardButton(text='📲 𝗔𝗻𝗼𝗻𝘆 𝗡𝘂𝗺𝗯𝗲𝗿', callback_data='C1')
            button_d = types.InlineKeyboardButton(text='❇️ 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗖𝗹𝘂𝗯𝘀', callback_data='D1')
            button_e = types.InlineKeyboardButton(text='🔊 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁𝗶𝗻𝗴', callback_data='E1')
            button_f = types.InlineKeyboardButton(text='🔆 𝗔𝗜 𝗖𝗵𝗮𝘁 𝗕𝗼𝘁', callback_data='F1')
            button_g = types.InlineKeyboardButton(text='🚹 𝗔𝗯𝗼𝘂𝘁', callback_data='G1')
            button_h = types.InlineKeyboardButton(text='📝 𝗣𝗿𝗶𝘃𝗮𝗰𝘆 𝗣𝗼𝗹𝗶𝗰𝘆', callback_data='H1')
            button_i = types.InlineKeyboardButton(text='⏏️', callback_data='I1')
            button_i1 = types.InlineKeyboardButton(text='⏹️', callback_data='I2')
            button_i2 = types.InlineKeyboardButton(text='⏩️', callback_data='I3')
            button_j = types.InlineKeyboardButton(text='𝗠𝗼𝗿𝗲  >>', callback_data='J1')
            if str(message.chat.id) == '584429967':
                button_Ks1 = types.InlineKeyboardButton(text='📛 𝗖𝗵𝗮𝗻𝗴𝗲 𝗻𝗶𝗰𝗸𝗻𝗮𝗺𝗲', callback_data='Ks1')
                keyboard.add(button_a)
                keyboard.add(button_b)
                keyboard.add(button_i,button_i1,button_i2)
                keyboard.add(button_c)
                keyboard.add(button_d)
                keyboard.add(button_e)
                keyboard.add(button_f)
                keyboard.add(button_g,button_h)
                keyboard.add(button_Ks1)
                keyboard.add(button_j)
            else:
                keyboard.add(button_a)
                keyboard.add(button_b)
                keyboard.add(button_i,button_i1,button_i2)
                keyboard.add(button_c)
                keyboard.add(button_d)
                keyboard.add(button_e)
                keyboard.add(button_f)
                keyboard.add(button_g,button_h)
                keyboard.add(button_j)
            #bot.send_photo(message.chat.id, photo=open('info_files/Anonychat_banner.jpg', 'rb'),caption= ".            𝔄 𝔫 𝔬 𝔫 𝔶 𝔪 𝔬 𝔲 𝔰    ℭ 𝔥 𝔞 𝔱 𝔰", reply_markup=keyboard)
            bot.send_message(message.chat.id, "||             𝓐𝓷𝓸𝓷𝔂𝓶𝓸𝓾𝓼 𝓒𝓱𝓪𝓽𝓼.          ", reply_markup=keyboard)

            @bot.callback_query_handler(func=lambda call: call.data in ['A1','B1','C1','D1','E1','F1','G1','H1','J1','I1','I2','I3','check_t','check_v','ignore','Ks1'])
            def callback_inline(call):
                #================================================
                #               Private Connection                    
                #================================================
                if call.data == 'A1':
                    A1botp = get((finder('ID',int(call.from_user.id))),'OTP')
                    A1bstatus = get((finder('ID',int(call.from_user.id))),'Status')
                    print('the OTP is:'+str(A1botp))
                    if A1bstatus == 'private' :
                        bot.send_message(call.from_user.id, '⚠️ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝗽𝗿𝗼𝗰𝗲𝘀𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 (𝘆𝗼𝘂𝗿 𝗰𝘂𝗿𝗿𝗲𝗻𝘁 𝘀𝘁𝗮𝘁𝘂𝘀 𝗶𝘀 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗽𝗹𝗲𝗮𝘀𝗲 𝗰𝗹𝗼𝘀𝗲 𝘁𝗵𝗲 𝗰𝘂𝗿𝗿𝗲𝗻𝘁 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝗯𝘆 𝗰𝗹𝗶𝗰𝗸𝗶𝗻𝗴 𝗼𝗻 ⏹️  𝘁𝗼 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗻𝗲𝘄 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗹𝗶𝗻𝗸)')
                    elif str(A1botp) == '0' or str(A1botp) == '-' :
                        MA1a = finder('ID',int(call.from_user.id))
                        if str(MA1a) == 'not found':
                            bot.answer_callback_query(callback_query_id=call.id,
                                                  show_alert=True,
                                                  text='⚠️\n\nYour ID is not registered\nPlease register first')
                        else:
                            bot.answer_callback_query(callback_query_id=call.id,
                                                 show_alert=True,
                                                 text='⚠️\n\nPlease share the generated QR code or the link starting with  "/pvt" with the person you wish to connect.')    
                            #bot.answer_callback_query(call.id, "Requesting private link...")
                            #bot.delete_message(call.from_user.id, msgM2.message_id)
                            cid = call.from_user.id
                            chk = finder('ID',int(call.from_user.id))
                            print(str(call.from_user.id))
                            print(chk)
                            if str(chk) == 'not found':
                                msgnt1a = bot.send_message(call.from_user.id, '⚠️ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘂𝘀𝗲𝗿..\n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝗰𝗹𝗶𝗰𝗸 𝗼𝗻 /𝘀𝘁𝗮𝗿𝘁 𝘁𝗼 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝗮𝗻𝗱 𝗲𝘅𝗽𝗹𝗼𝗿𝗲')
                                bot.delete_message(call.from_user.id, msgM2.message_id)
                                time.sleep(10)
                                bot.delete_message(call.from_user.id, msgnt1a.message_id)
                            else:
                                try:
                                    try:
                                        print(int(call.from_user.id))
                                        A1a = finder('ID',int(call.from_user.id))
                                        A1b = get((A1a),'Peer')
                                        print('Peer Index : '+str(A1b))
                                        print('Peer : '+str(A1b))
                                        B1a = finder('ID',int(A1b))
                                        B1b = get((B1a),'Peer')
                                        #anych_modify('Peer',0,int(str(call.from_user.id)))
                                        #anych_modify('Status','closed',int(str(call.from_user.id)))
                                        #anych_modify('OTP',0,int(str(call.from_user.id)))
                                        ##anych_modify('Peer',0,int(A1b))
                                        #anych_modify('Status','open',int(A1b))
                                        ##anych_modify('OTP',0,int(A1b))
                                        if A1b == 0 :
                                            D = OTP(int(str(call.from_user.id)))
                                            D1a = finder('ID',int(str(call.from_user.id)))
                                            D1b = get((D1a),'AnonyID')
                                            #print(str(call.from_user.id))
                                            if str(D1b) == '-invalid-':
                                                msgpvt = bot.send_message(call.from_user.id, 'Error to generate link,\n\nPlease try again!!')
                                            else:
                                                xcode = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
                                                xcode2 = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
                                                QRL = '/pvt'+str(xcode)+str(D)+str(xcode2)+str(D1b)
                                                mID = str(call.from_user.id)
                                                if QRCode(QRL,mID) == 'qrcode done':
                                                    msgpvt = bot.send_photo(call.from_user.id, photo=open('temp/qrcode'+str(mID)+'.png', 'rb'),caption= '𝗕𝗲𝗹𝗼𝘄 𝗶𝘀 𝘆𝗼𝘂𝗿 𝘃𝗮𝗹𝗶𝗱 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝗹𝗶𝗻𝗸: \n\n/pvt'+str(xcode)+str(D)+str(xcode2)+str(D1b)+"\n\n\n𝗡𝗼𝘁𝗲: 𝗧𝗼 𝗲𝘀𝘁𝗮𝗯𝗹𝗶𝘀𝗵 𝗮 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗹𝗶𝗻𝗸, 𝗸𝗶𝗻𝗱𝗹𝘆 𝘀𝗵𝗮𝗿𝗲 𝘁𝗵𝗲 𝗮𝗯𝗼𝘃𝗲 𝗹𝗶𝗻𝗸 𝗼𝗿 𝗤𝗥 𝗰𝗼𝗱𝗲 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿. 𝗙𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲 𝗹𝗶𝗻𝗸, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗮𝘀𝗸 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝘁𝗼 𝗰𝗹𝗶𝗰𝗸 𝗼𝗻 𝗶𝘁 𝗮𝗻𝗱 𝘁𝘆𝗽𝗲 𝗶𝗻 𝘁𝗵𝗲 𝗰𝗵𝗮𝘁 𝗯𝗼𝘅. 𝗜𝗻 𝗰𝗮𝘀𝗲 𝗼𝗳 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲 𝗤𝗥 𝗰𝗼𝗱𝗲, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗮𝘀𝗸 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝘁𝗼 𝘁𝗮𝗸𝗲 𝗮 𝗽𝗶𝗰𝘁𝘂𝗿𝗲 𝗮𝗻𝗱 𝘀𝗲𝗻𝗱 𝗶𝘁 𝘁𝗼 𝘁𝗵𝗲𝗶𝗿 𝗮𝗻𝗼𝗻𝘆𝗺𝗼𝘂𝘀 𝗰𝗵𝗮𝘁.\n\n\n(𝗧𝗵𝗶𝘀 𝗹𝗶𝗻𝗸 𝘄𝗶𝗹𝗹 𝗲𝘅𝗽𝗶𝗿𝗲 𝗶𝗻 𝟲𝟬𝘀𝗲𝗰)")
                                                    os.remove('temp/qrcode'+str(mID)+'.png')
                                                #msgpvt = bot.send_message(call.from_user.id, '𝚈𝚘𝚞𝚛 𝙸𝙳 𝚁𝚎𝚊𝚍𝚢 𝚏𝚘𝚛 𝚙𝚛𝚒𝚟𝚊𝚝𝚎 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 : \n\n/pvt'+str(xcode)+str(D)+str(xcode2)+str(D1b)+"\n\n\n𝚈𝚘𝚞𝚛 𝚙𝚛𝚒𝚟𝚊𝚝𝚎 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 𝚕𝚒𝚗𝚔 𝚠𝚒𝚕𝚕 𝚎𝚡𝚙𝚒𝚛𝚎 𝚒𝚗 𝟼𝟶𝚜𝚎𝚌.")
                                            D2a = finder('ID',int(str(call.from_user.id)))
                                            D2b = get((D1a),'Status')
                                            time.sleep(60)
                                            bot.delete_message(call.from_user.id, msgpvt.message_id)
                                            anych_modify('OTP','-',call.from_user.id)
                                            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                        else:
                                            D1a = finder('ID',int(str(call.from_user.id)))
                                            D1b = get((D1a),'AnonyID')
                                            D1c = get((D1a),'Peer')
                                            print("D1c is :"+str(D1c))
                                            keyboard = types.InlineKeyboardMarkup()
                                            button_a0 = types.InlineKeyboardButton(text='↖️ Send to partner ', callback_data='link_yes')
                                            button_b0 = types.InlineKeyboardButton(text='⤵️ Show here ', callback_data='link_no')
                                            button_c0 = types.InlineKeyboardButton(text='❌ Cancel ', callback_data='link_Cancel')
                                            keyboard.add(button_a0,button_b0)
                                            keyboard.add(button_c0)
                                            bot.send_message(call.from_user.id, "⚠️ 𝗗𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝘀𝗵𝗮𝗿𝗲 𝘁𝗵𝗲 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗹𝗶𝗻𝗸 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 ??", reply_markup=keyboard)
                                            @bot.callback_query_handler(func=lambda call: call.data in ['link_yes','link_no','link_Cancel'])
                                            def callback_inline(call):
                                                if call.data == 'link_yes':
                                                    D = OTP(int(str(call.from_user.id)))
                                                    D1a = finder('ID',int(str(call.from_user.id)))
                                                    D1b = get((D1a),'AnonyID')
                                                    D1c = get((D1a),'Peer')
                                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                                    #print(str(call.from_user.id))
                                                    if str(D1b) == '-invalid-':
                                                        msgpvt = bot.send_message(call.from_user.id, 'Error to generate link,\n\nPlease try again!!')
                                                    else:
                                                        xcode = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
                                                        xcode2 = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
                                                        QRL = '/pvt'+str(xcode)+str(D)+str(xcode2)+str(D1b)
                                                        mID = str(call.from_user.id)
                                                        if QRCode(QRL,mID) == 'qrcode done':
                                                            msgpvt = bot.send_photo(D1c, photo=open('temp/qrcode'+str(mID)+'.png', 'rb'),caption= '𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝘄𝗮𝗻𝘁𝘀 𝘁𝗼 𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂 𝗮𝘀 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝘀𝘁𝗮𝘁𝘂𝘀 !! 𝗣𝗹𝗲𝗮𝘀𝗲 𝗰𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝗲𝗹𝗼𝘄 𝗹𝗶𝗻𝗸 𝗼𝗿 𝘁𝘆𝗽𝗲 𝗶𝗻 𝗰𝗵𝗮𝘁 𝗯𝗼𝘅 𝗼𝗿 𝗿𝗲𝘀𝗲𝗻𝗱 𝘁𝗵𝗲 𝗤𝗥 𝗰𝗼𝗱𝗲 𝗶𝗻 𝗮𝗻𝗼𝗻𝘆𝗺𝗼𝘂𝘀 𝗰𝗵𝗮𝘁 𝘁𝗼 𝗰𝗵𝗮𝗻𝗴𝗲 𝘆𝗼𝘂𝗿 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝘀𝘁𝗮𝘁𝘂𝘀 : \n\n/pvt'+str(xcode)+str(D)+str(xcode2)+str(D1b)+"\n\n\n𝗡𝗢𝗧𝗘: 𝗘𝘀𝘁𝗮𝗯𝗹𝗶𝘀𝗵𝗶𝗻𝗴 𝗮 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝘄𝗶𝗹𝗹 𝗻𝗼𝘁 𝗰𝗼𝗺𝗽𝗿𝗼𝗺𝗶𝘀𝗲 𝘆𝗼𝘂𝗿 𝗮𝗻𝗼𝗻𝘆𝗺𝗶𝘁𝘆, 𝗯𝘂𝘁 𝗶𝘁 𝘄𝗶𝗹𝗹 𝗲𝗻𝘀𝘂𝗿𝗲 𝗮 𝘀𝗲𝗰𝘂𝗿𝗲 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗮𝗻𝗱 𝗽𝗿𝗲𝘃𝗲𝗻𝘁 𝗮𝗻𝘆 𝗸𝗶𝗻𝗱 𝗼𝗳 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻𝘀.")
                                                            os.remove('temp/qrcode'+str(mID)+'.png')
                                                        #msgpvt = bot.send_message(call.from_user.id, '𝚈𝚘𝚞𝚛 𝙸𝙳 𝚁𝚎𝚊𝚍𝚢 𝚏𝚘𝚛 𝚙𝚛𝚒𝚟𝚊𝚝𝚎 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 : \n\n/pvt'+str(xcode)+str(D)+str(xcode2)+str(D1b)+"\n\n\n𝚈𝚘𝚞𝚛 𝚙𝚛𝚒𝚟𝚊𝚝𝚎 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 𝚕𝚒𝚗𝚔 𝚠𝚒𝚕𝚕 𝚎𝚡𝚙𝚒𝚛𝚎 𝚒𝚗 𝟼𝟶𝚜𝚎𝚌.")
                                                    D2a = finder('ID',int(str(call.from_user.id)))
                                                    D2b = get((D1a),'Status')
                                                    msgpic = bot.send_message(call.from_user.id, '✅ 𝗟𝗶𝗻𝗸𝘀𝗲𝗻𝘁 !!')
                                                    time.sleep(1)
                                                    bot.delete_message(call.from_user.id, msgpic.message_id)
                                                    time.sleep(60)
                                                    bot.delete_message(call.from_user.id, msgpvt.message_id)
                                                    anych_modify('OTP','-',call.from_user.id)
                                                    msgpic = bot.send_message(call.from_user.id, '❌ 𝗟𝗶𝗻𝗸 𝗲𝘅𝗽𝗶𝗿𝗲𝗱!!')
                                                    msgpic2 = bot.send_message(D1c, '❌ 𝗟𝗶𝗻𝗸 𝗲𝘅𝗽𝗶𝗿𝗲𝗱!!')


                                                    print('Yes selected !!')
                                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                                elif call.data == 'link_no':
                                                    D = OTP(int(str(call.from_user.id)))
                                                    D1a = finder('ID',int(str(call.from_user.id)))
                                                    D1b = get((D1a),'AnonyID')
                                                    D1c = get((D1a),'Peer')
                                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                                    #print(str(call.from_user.id))
                                                    if str(D1b) == '-invalid-':
                                                        msgpvt = bot.send_message(call.from_user.id, 'Error to generate link,\n\nPlease try again!!')
                                                    else:
                                                        xcode = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
                                                        xcode2 = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
                                                        QRL = '/pvt'+str(xcode)+str(D)+str(xcode2)+str(D1b)
                                                        mID = str(call.from_user.id)
                                                        if QRCode(QRL,mID) == 'qrcode done':
                                                            msgpvt = bot.send_photo(call.from_user.id, photo=open('temp/qrcode'+str(mID)+'.png', 'rb'),caption= '𝗕𝗲𝗹𝗼𝘄 𝗶𝘀 𝘆𝗼𝘂𝗿 𝘃𝗮𝗹𝗶𝗱 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝗹𝗶𝗻𝗸: \n\n/pvt'+str(xcode)+str(D)+str(xcode2)+str(D1b)+"\n\n\n𝗡𝗼𝘁𝗲: 𝗧𝗼 𝗲𝘀𝘁𝗮𝗯𝗹𝗶𝘀𝗵 𝗮 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗹𝗶𝗻𝗸, 𝗸𝗶𝗻𝗱𝗹𝘆 𝘀𝗵𝗮𝗿𝗲 𝘁𝗵𝗲 𝗮𝗯𝗼𝘃𝗲 𝗹𝗶𝗻𝗸 𝗼𝗿 𝗤𝗥 𝗰𝗼𝗱𝗲 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿. 𝗙𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲 𝗹𝗶𝗻𝗸, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗮𝘀𝗸 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝘁𝗼 𝗰𝗹𝗶𝗰𝗸 𝗼𝗻 𝗶𝘁 𝗮𝗻𝗱 𝘁𝘆𝗽𝗲 𝗶𝗻 𝘁𝗵𝗲 𝗰𝗵𝗮𝘁 𝗯𝗼𝘅. 𝗜𝗻 𝗰𝗮𝘀𝗲 𝗼𝗳 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲 𝗤𝗥 𝗰𝗼𝗱𝗲, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗮𝘀𝗸 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝘁𝗼 𝘁𝗮𝗸𝗲 𝗮 𝗽𝗶𝗰𝘁𝘂𝗿𝗲 𝗮𝗻𝗱 𝘀𝗲𝗻𝗱 𝗶𝘁 𝘁𝗼 𝘁𝗵𝗲𝗶𝗿 𝗮𝗻𝗼𝗻𝘆𝗺𝗼𝘂𝘀 𝗰𝗵𝗮𝘁.\n\n\n(𝗧𝗵𝗶𝘀 𝗹𝗶𝗻𝗸 𝘄𝗶𝗹𝗹 𝗲𝘅𝗽𝗶𝗿𝗲 𝗶𝗻 𝟲𝟬𝘀𝗲𝗰)")
                                                            os.remove('temp/qrcode'+str(mID)+'.png')
                                                        #msgpvt = bot.send_message(call.from_user.id, '𝚈𝚘𝚞𝚛 𝙸𝙳 𝚁𝚎𝚊𝚍𝚢 𝚏𝚘𝚛 𝚙𝚛𝚒𝚟𝚊𝚝𝚎 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 : \n\n/pvt'+str(xcode)+str(D)+str(xcode2)+str(D1b)+"\n\n\n𝚈𝚘𝚞𝚛 𝚙𝚛𝚒𝚟𝚊𝚝𝚎 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 𝚕𝚒𝚗𝚔 𝚠𝚒𝚕𝚕 𝚎𝚡𝚙𝚒𝚛𝚎 𝚒𝚗 𝟼𝟶𝚜𝚎𝚌.")
                                                    D2a = finder('ID',int(str(call.from_user.id)))
                                                    D2b = get((D1a),'Status')
                                                    time.sleep(60)
                                                    bot.delete_message(call.from_user.id, msgpvt.message_id)
                                                    anych_modify('OTP','-',call.from_user.id)
                                                    msgpic = bot.send_message(call.from_user.id, '❌ 𝗟𝗶𝗻𝗸 𝗲𝘅𝗽𝗶𝗿𝗲𝗱!!')
                                                elif call.data == 'link_Cancel':
                                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                                else:
                                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                    except Exception as e:
                                            print('cb_PrivateConnection error [410-433] /: '+str(e))
                                            anych_modify('OTP',0,int(str(call.from_user.id)))
                                            mid = str(call.from_user.id)

                                except Exception as e:
                                    print('Exception [408-415] /:'+str(e))
                                    bot.send_message(call.from_user.id, '⚠️ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝗽𝗿𝗼𝗰𝗲𝘀𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 !!')

                    else :
                        bot.send_message(call.from_user.id, '⚠️ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗹𝗶𝗻𝗸 (𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝗮𝗰𝘁𝗶𝘃𝗲 𝗹𝗶𝗻𝗸 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝗳𝗼𝗿 𝗶𝘁𝘀 𝗲𝘅𝗽𝗶𝗿𝘆)')
                #================================================
                #               Text Message                    
                #================================================
                elif call.data == 'check_t':
                    with open('info_files/notice.txt') as f:
                        f = f.read()
                    msgnotice = bot.send_message(call.from_user.id, "📩 Text Messgae :\n\n"+str(f))
                    time.sleep(2)
                    msgnotice2 = bot.edit_message_text("⚠️ Important Notice!! ⚠️\n\n"+str(f) , call.from_user.id, msgnotice.message_id)
                #================================================
                #               Vocie Message                    
                #================================================
                elif call.data == 'check_v':
                    with open('info_files/anonymouschats_message01.ogg', 'rb') as audio:
                        bot.send_voice(str(call.from_user.id), audio,caption="📼 Voice Message from :\nAmenda , Camilla and Jeff want to tell you somthing!")
                #================================================
                #               Random Connection                    
                #================================================
                elif call.data == 'ignore':
                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                #================================================
                #               Random Connection                    
                #================================================
                elif call.data == 'B1':
                    status = get((finder('ID',int(call.from_user.id))),'Status')
                    if status == 'waiting':
                        bot.answer_callback_query(callback_query_id=call.id,
                                              show_alert=True,
                                              text='⚠️\n\nYou are with waiting status\nWe will notify you once we have found your partner')
                    elif status == "linked":
                        bot.answer_callback_query(callback_query_id=call.id,
                                              show_alert=True,
                                              text='⚠️\n\nYou are already linked with random partner\nplease select below operations:\n⏹️ Close connection\n⏩️ Search new partner')
                    elif status == "private":
                        bot.answer_callback_query(callback_query_id=call.id,
                                              show_alert=True,
                                              text='⚠️\n\nYou are connected with your partner as private connection:\n⏹️ Close your connection before connecting to random partner')
                    else:
                        checkdb = inspector()
                        print(checkdb)
                        print("inspector status:"+str(checkdb))
                        #if str(checkdb) == "error" or str(checkdb) == "Random Connection Service is currently under maintenance\n\nPlease Try Later \nor\nUse Other Services" or str(checkdb) == "Random Connection Manager is unresponsive\n\nPlease Try Later or Use Other Services ":
                         #   bot.answer_callback_query(callback_query_id=call.id,
                          #                        show_alert=True,
                           #                       text='⚠️\n\n'+str(checkdb))
                            #print ("Db manager is not working!!")
                        #else:
                        print(checkdb)
                        print ("Db manager is working")
                        MA1a = finder('ID',int(call.from_user.id))
                        if str(MA1a) == 'not found':
                            bot.answer_callback_query(callback_query_id=call.id,
                                                  show_alert=True,
                                                  text='⚠️\n\nYour ID is not registered\nPlease register first')
                        else:
                            A1a = finder('ID',int(call.from_user.id))
                            A1b = get((A1a),'Peer')
                            print('Test value:'+str(A1b))
                            if A1b == 0:
                                tout1 = (get((A1a),'tout'))
                            else:
                                tout1 = (get((A1a),'tout'))
                                B1a = finder('ID',int(A1b))
                                B1b = get((B1a),'Peer')
                                tout1 = (get((B1a),'tout'))

                            try:
                                anych_modify('Peer',0,int(str(call.from_user.id)))
                                anych_modify('Status','open',int(str(call.from_user.id)))
                                anych_modify('OTP',0,int(str(call.from_user.id)))
                                anych_modify('Peer',0,int(A1b))
                                anych_modify('Status','closed',int(A1b))
                                anych_modify('tout',1728,int(A1b))
                                anych_modify('OTP',0,int(A1b))
                            except:
                                anych_modify('Peer',0,int(str(call.from_user.id)))
                                anych_modify('Status','open',int(str(call.from_user.id)))
                                anych_modify('OTP',0,int(str(call.from_user.id)))
                            time.sleep(2)
                            df = pd.read_csv('info_files/Anonychatdb01.2.csv')
                            try:
                                df=db()
                                L = (df['Status'].value_counts()['waiting'])
                            except:
                                L = 0
                            print ('L is '+str(L))
                            if (L) < 1 :
                                anych_modify('Status','waiting',int(str(call.from_user.id)))
                                anych_modify('tout',120,int(str(call.from_user.id)))
                                anych_modify('OTP',0,int(str(call.from_user.id)))
                                #bot.answer_callback_query(call.id, "Searching for channel...")
                                bot.answer_callback_query(callback_query_id=call.id,
                                                      show_alert=True,
                                                      text="⚠️\n\nYOUR IN QUEUE!!\n\nCurrently all slots are fully occupied!!\nYou'll be connected with random partner once a slot is available\n\n\n Try later!!")
                                bot.send_message(str(call.from_user.id),"Hi, I am your assistant while random chats slots are fully occupied, i am free to talk with you, you can ask me any thing if you want, i will answer you :)")
                            else:
                                #bot.delete_message(call.from_user.id, msgM2.message_id)
                                cid = call.from_user.id
                                chk = finder('ID',int(call.from_user.id))
                                if chk == 'not found':
                                    msgnf = bot.send_message(call.from_user.id, '⚠️ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘂𝘀𝗲𝗿..\n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝗰𝗹𝗶𝗰𝗸 𝗼𝗻 /start 𝘁𝗼 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝗮𝗻𝗱 𝗲𝘅𝗽𝗹𝗼𝗿𝗲')
                                    time.sleep(10)
                                    bot.delete_message(call.from_user.id, msgnf.message_id)

                                else:
                                    bot.answer_callback_query(callback_query_id=call.id,
                                                 show_alert=True,
                                                 text='⚠️\n\nPARTNER FOUND!!\n\nPlease wait a request has been submitted to the Anonymous Chats connection manager for connecting you with a random person.')
                                    try:
                                        try:
                                            A1a = finder('ID',int(call.from_user.id))
                                            A1b = get((A1a),'Peer')
                                            print('Peer : '+str(A1b))
                                            B1a = finder('ID',int(A1b))
                                            B1b = get((B1a),'Peer')
                                            anych_modify('Peer',0,int(str(call.from_user.id)))
                                            anych_modify('Status','open',int(str(call.from_user.id)))
                                            anych_modify('OTP',0,int(str(call.from_user.id)))
                                            anych_modify('Peer',0,int(A1b))
                                            anych_modify('Status','closed',int(A1b))
                                            anych_modify('tout',1728,int(A1b))
                                            anych_modify('OTP',0,int(A1b))
                                            if A1b == 0 :
                                                print('')
                                            else:
                                                bot.send_message(str(call.from_user.id),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                                                bot.send_message(str(A1b),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                                        except Exception as e:
                                                print('cb_RandomConnection error [431-442] /: '+str(e))
                                                anych_modify('Peer',0,int(str(call.from_user.id)))
                                                anych_modify('Status','open',int(str(call.from_user.id)))
                                                anych_modify('OTP',0,int(str(call.from_user.id)))
                                                mid = str(call.from_user.id)
                                    except Exception as e:
                                        print('Exception [462-485] /:'+str(e))
                                        bot.send_message(cid, '⚠️ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝗽𝗿𝗼𝗰𝗲𝘀𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 !!')

                                #############

                                try:
                                    bot.answer_callback_query(call.id, "⚠️ 𝗥𝗲𝗾𝘂𝗲𝘀𝘁𝗶𝗻𝗴 𝗳𝗼𝗿 𝗿𝗮𝗻𝗱𝗼𝗺 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻..")
                                    D = verifyuser('ID',str(call.from_user.id))
                                    A1a = finder('ID',int(call.from_user.id))
                                    A1b = get((A1a),'Status')
                                    if D == 'unregistered':
                                        msgcon = bot.send_message(call.from_user.id, "⚠️ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘂𝘀𝗲𝗿..\n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝗰𝗹𝗶𝗰𝗸 𝗼𝗻 /start 𝘁𝗼 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝗮𝗻𝗱 𝗲𝘅𝗽𝗹𝗼𝗿𝗲")
                                        a = reg(str(call.from_user.id))
                                        with open('code/Python_Lab/Anonychat/Anonychat_reg_logs.txt', 'a') as f:
                                            print('USER Registered : cID('+str(message.chat.id)+') : nID('+str(message.from_user.first_name)+') : tIN('+str(timestemp())+')', file=f)
                                        bot.send_message('584429967', 'USER Registered: '+str(message.from_user.first_name))
                                        time.sleep(2)
                                        msgcon2 = bot.edit_message_text(str(a), call.from_user.id, msgcon.message_id)
                                        time.sleep(1)
                                        msgcon3 = bot.edit_message_text('𝗣𝗹𝗲𝗮𝘀𝗲 𝗰𝗹𝗶𝗰𝗸 𝗼𝗻  /start 𝘁𝗼 𝗲𝘅𝗽𝗹𝗼𝗿𝗲..' , call.from_user.id, msgcon2.message_id)
                                        time.sleep(10)
                                        bot.delete_message(call.from_user.id, msgcon3.message_id)
                                    elif A1b == "waiting":
                                        msgstwa = bot.send_message(call.from_user.id, "𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝗶𝘀 '𝘄𝗮𝗶𝘁𝗶𝗻𝗴', \n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝘄𝗵𝗶𝗹𝗲 𝘄𝗲 𝗮𝗿𝗲 𝘀𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝗳𝗼𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿..")
                                        time.sleep(3)
                                        bot.delete_message(call.from_user.id, msgstwa.message_id)
                                    elif A1b == "blocked":
                                        msgstbk = bot.send_message(call.from_user.id, "𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝗶𝘀 '𝗯𝗹𝗼𝗰𝗸𝗲𝗱', \n\n𝗦𝗼𝗿𝗿𝘆 𝘆𝗼𝘂 𝘄𝗶𝗹𝗹 𝘂𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝘂𝘁𝗶𝗹𝗶𝘀𝗲 𝘁𝗵𝗶𝘀 𝘀𝗲𝗿𝘃𝗶𝗰𝗲 𝗮𝘁 𝘁𝗵𝗲 𝗺𝗼𝗺𝗲𝗻𝘁..")
                                        time.sleep(3)
                                        bot.delete_message(call.from_user.id, msgstbk.message_id)
                                    elif A1b == "private":
                                        msgstpvt = bot.send_message(call.from_user.id, "𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝗶𝘀 '𝗽𝗿𝗶𝘃𝗮𝘁𝗲', \n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝗰𝗹𝗼𝘀𝗲 𝘁𝗵𝗲 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝗳𝗶𝗿𝘀𝘁..")
                                        time.sleep(3)
                                        bot.delete_message(call.from_user.id, msgstpvt.message_id)
                                    elif A1b == "permanent":
                                        msgstpvt = bot.send_message(call.from_user.id, "𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝗶𝘀 '𝗽𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁', \n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝗰𝗹𝗼𝘀𝗲 𝘁𝗵𝗲 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝗳𝗶𝗿𝘀𝘁..")
                                        time.sleep(3)
                                        bot.delete_message(call.from_user.id, msgstpvt.message_id)
                                    elif A1b == "open":
                                        bot.answer_callback_query(callback_query_id=call.id,
                                                              show_alert=True,
                                                              text="Your lease is updated!!\nYour Status Changed to : Waiting\n\n\nAnonymous Chats manager will connect you with someone in a while\n\n\nPlease wait!!")                                                
                                        bot.send_message(call.from_user.id, '𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝗶𝘀 "𝗼𝗽𝗲𝗻" \n\n𝗪𝗲 𝗮𝗿𝗲 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝘁𝗼 𝗲𝘀𝘁𝗮𝗯𝗹𝗶𝘀𝗵 𝗮 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝘄𝗶𝘁𝗵 𝗿𝗮𝗻𝗱𝗼𝗺 𝗽𝗮𝗿𝘁𝗻𝗲𝗿.')
                                        anych_modify('Status','waiting',int(str(call.from_user.id)))
                                        leasing(int(call.from_user.id),120)
                                        #msgser = bot.send_message(call.from_user.id, '🔎 𝚂𝚎𝚊𝚛𝚌𝚑𝚒𝚗𝚐 𝚏𝚘𝚛 𝚙𝚊𝚛𝚝𝚗𝚎𝚛 𝚙𝚕𝚎𝚊𝚜𝚎 𝚠𝚊𝚒𝚝...')
                                    elif A1b == "closed":
                                        msgstcl = bot.send_message(call.from_user.id, '𝚈𝚘𝚞𝚛 𝙰𝚗𝚘𝚗𝚢𝙸𝙳 𝚒𝚜 𝚗𝚘𝚝 𝚟𝚊𝚕𝚒𝚍 , \n\n𝚈𝚘𝚞 𝚗𝚎𝚎𝚍 𝚝𝚘 𝚌𝚕𝚘𝚜𝚎 𝚢𝚘𝚞𝚛 𝚎𝚡𝚒𝚜𝚝𝚒𝚗𝚐 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 𝚊𝚗𝚍 𝚛𝚎𝚐𝚒𝚜𝚝𝚎𝚛 𝚊𝚐𝚊𝚒𝚗 !!')
                                        time.sleep(3)
                                        bot.delete_message(call.from_user.id, msgstcl.message_id)
                                    elif A1b == "locked":
                                        msgstlk = bot.send_message(call.from_user.id, '𝚈𝚘𝚞𝚛 𝚜𝚝𝚊𝚝𝚞𝚜 𝚒𝚜 "𝚕𝚘𝚌𝚔𝚎𝚍" , \n\n𝚃𝚑𝚒𝚜 𝚒𝚜 𝚋𝚎𝚌𝚊𝚞𝚜𝚎 𝚢𝚘𝚞𝚛 𝚐𝚎𝚗𝚎𝚛𝚊𝚝𝚎𝚍 𝙾𝚃𝙿 𝚒𝚜 𝚊𝚌𝚝𝚒𝚟𝚎 !!')
                                        time.sleep(3)
                                        bot.delete_message(call.from_user.id, msgstlk.message_id)
                                    else:
                                        bot.send_message(call.from_user.id, '𝚈𝚘𝚞𝚛 𝚊𝚛𝚎 𝚛𝚎𝚐𝚒𝚜𝚝𝚎𝚛𝚎𝚍 𝚠𝚒𝚝𝚑 𝚞𝚗𝚔𝚗𝚘𝚠𝚗 𝚜𝚝𝚊𝚝𝚞𝚜 , \n\n𝚆𝚎 𝚌𝚊𝚗𝚗𝚘𝚝 𝚙𝚎𝚛𝚏𝚘𝚛𝚖 𝚊𝚗𝚢 𝚘𝚙𝚎𝚛𝚊𝚝𝚒𝚘𝚗.\n\n𝙿𝚕𝚎𝚊𝚜𝚎 𝚌𝚕𝚘𝚜𝚎 𝚊𝚕𝚕 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗𝚜 𝚏𝚒𝚛𝚜𝚝 𝚊𝚗𝚍 𝚝𝚛𝚢 𝚊𝚐𝚊𝚒𝚗 !!')
                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                except Exception as e:
                                    print('cb_RandomConnection error [451-480] /: '+str(e))
                            #except Exception as e:
                            #        print('cb_RandomConnection error [451-480] /: '+str(e))


                #================================================
                #               Anony Number                    
                #================================================
                elif call.data == 'C1':
                    bot.answer_callback_query(callback_query_id=call.id,
                                                              show_alert=True,
                                                              text='⚠️ Currently Not Available')
                #================================================
                #               Anony Number                    
                #================================================
                elif call.data == 'C1x':
                    bot.answer_callback_query(callback_query_id=call.id,
                                                              show_alert=True,
                                                              text='✅️\n\nAnony Number\n\nPlease be mindful when sharing your anonymous number with anyone!!')    
                    keyboard = types.InlineKeyboardMarkup()
                    button_a0 = types.InlineKeyboardButton(text='🟩 User specified anonymous Number ', callback_data='link_yes0')
                    button_b0 = types.InlineKeyboardButton(text='🟨 Open Anonymous Number ', callback_data='link_no0')
                    button_c0 = types.InlineKeyboardButton(text='❌ Cancel ', callback_data='link_Cancel0')
                    keyboard.add(button_a0)
                    keyboard.add(button_b0)
                    keyboard.add(button_c0)
                    bot.send_message(call.from_user.id, "⚠️ 𝗗𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝘀𝗵𝗮𝗿𝗲 𝘁𝗵𝗲 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗹𝗶𝗻𝗸 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 ??", reply_markup=keyboard)
                    @bot.callback_query_handler(func=lambda call: call.data in ['link_yes0','link_no0','link_Cancel0'])
                    def callback_inline(call):
                        if call.data == 'link_yes0':
                            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                        #finder('ID',int(str(Peer)))
                        #D1a = finder('ID',int(str(call.from_user.id)))
                            YourAnonyID = get((finder('ID',int(str(call.from_user.id)))),'AnonyID')
                            YourAnonyName = get((finder('ID',int(str(call.from_user.id)))),'Nickname')
                            Peer = get((finder('ID',int(str(call.from_user.id)))),'Peer')
                            PeerAnonyID = get((finder('ID',int(str(Peer)))),'AnonyID')
                            PeerAnonyName = get((finder('ID',int(str(Peer)))),'Nickname')
                            AnonyNumber = (encode(str(YourAnonyID)+str(':')+str(YourAnonyName)+str(':')+str(PeerAnonyID)+str(':')+str(PeerAnonyName)))
                            print('Anony Number :'+str(AnonyNumber))
                            keyboard = types.InlineKeyboardMarkup()
                            button_a0 = types.InlineKeyboardButton(text='↖️ Send to partner ', callback_data='link_yes1')
                            button_b0 = types.InlineKeyboardButton(text='⤵️ Show here ', callback_data='link_no1')
                            button_c0 = types.InlineKeyboardButton(text='❌ Cancel ', callback_data='link_Cancel1')
                            keyboard.add(button_a0,button_b0)
                            keyboard.add(button_c0)
                            bot.send_message(call.from_user.id, "⚠️ 𝗗𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝘀𝗵𝗮𝗿𝗲 𝘆𝗼𝘂𝗿 𝗮𝗻𝗼𝗻𝘆𝗺𝗼𝘂𝘀 𝗻𝘂𝗺𝗯𝗲𝗿 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 ??", reply_markup=keyboard)
                            @bot.callback_query_handler(func=lambda call: call.data in ['link_yes1','link_no1','link_Cancel1'])
                            def callback_inline(call):
                                if call.data == 'link_yes1':
                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                    bot.send_message(str(Peer),"/99"+str(AnonyNumber))

                                elif call.data == 'link_no1':
                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                    bot.send_message(str(call.from_user.id),"/99"+str(AnonyNumber))
                                    OriAnonyNumber = decode(str(AnonyNumber))
                                    print('Ori Code :')
                                elif call.data == 'link_Cancel1':
                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

                                else:
                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


                        elif call.data == 'link_no0':
                            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                        #finder('ID',int(str(Peer)))
                        #D1a = finder('ID',int(str(call.from_user.id)))
                            YourAnonyID = get((finder('ID',int(str(call.from_user.id)))),'AnonyID')
                            YourAnonyName = get((finder('ID',int(str(call.from_user.id)))),'Nickname')
                            Peer = get((finder('ID',int(str(call.from_user.id)))),'Peer')
                            PeerAnonyID =get((finder('ID',int(str(Peer)))),'AnonyID')
                            PeerAnonyName =get((finder('ID',int(str(Peer)))),'Nickname')
                            AnonyNumber = (encode(str(YourAnonyID)+str(':')+str(YourAnonyName)))
                            print('Anony Number :'+str(AnonyNumber))
                            keyboard = types.InlineKeyboardMarkup()
                            button_a0 = types.InlineKeyboardButton(text='↖️ Send to partner ', callback_data='link_yes2')
                            button_b0 = types.InlineKeyboardButton(text='⤵️ Show here ', callback_data='link_no2')
                            button_c0 = types.InlineKeyboardButton(text='❌ Cancel ', callback_data='link_Cancel2')
                            keyboard.add(button_a0,button_b0)
                            keyboard.add(button_c0)
                            bot.send_message(call.from_user.id, "⚠️ 𝗗𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝘀𝗵𝗮𝗿𝗲 𝘆𝗼𝘂𝗿 𝗮𝗻𝗼𝗻𝘆𝗺𝗼𝘂𝘀 𝗻𝘂𝗺𝗯𝗲𝗿 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 ??", reply_markup=keyboard)
                            @bot.callback_query_handler(func=lambda call: call.data in ['link_yes2','link_no2','link_Cancel2'])
                            def callback_inline(call):
                                if call.data == 'link_yes2':
                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                    bot.send_message(str(Peer),"/99"+str(AnonyNumber))

                                elif call.data == 'link_no2':
                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                    bot.send_message(str(call.from_user.id),"/99"+str(AnonyNumber))

                                elif call.data == 'link_Cancel2':
                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

                                else:
                                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                        elif call.data == 'link_Cancel0':
                            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                #================================================
                #               Private Clubs                    
                #================================================
                elif call.data == 'D1':
                    bot.answer_callback_query(callback_query_id=call.id,
                                                              show_alert=True,
                                                              text='⚠️ Currently Not Available')


                #================================================
                #               Broadcasting                    
                #================================================
                elif call.data == 'E1':
                    bot.answer_callback_query(callback_query_id=call.id,
                                                              show_alert=True,
                                                              text='⚠️ Currently Not Available')

                #================================================
                #               Broadcasting (testing)          
                #================================================
                elif call.data == 'E1i':
                    A1a = finder('ID',int(call.from_user.id))
                    A1b = get((A1a),'Status')
                    if A1b == 'broadcaster' or A1b == 'subscribers': 
                     bot.answer_callback_query(callback_query_id=call.id,
                                                                  show_alert=True,
                                                                  text='❌ ️\nBroadcasting\n\nUnable to cretate your broadcast link\nPlease close your current connection first by click on ⏏️')
                    else:
                        bot.answer_callback_query(callback_query_id=call.id,
                                                                  show_alert=True,
                                                                  text='🔊️\\Broadcasting\n\nThis feature will allow you to create the broadcasting link and allow uptp 20 subscribers to receive your messages')
                        MA1a = finder('ID',int(call.from_user.id))
                        if str(MA1a) == 'not found':
                            bot.answer_callback_query(callback_query_id=call.id,
                                                  show_alert=True,
                                                  text='⚠️\n\nYour ID is not registered\nPlease register first')
                        else:
                            bot.answer_callback_query(callback_query_id=call.id,
                                                 show_alert=True,
                                                 text='⚠️\n\nPlease share the generated QR code or the link starting with  "/brc" with the person you wish to add in broadcast list.')
                            cid = call.from_user.id
                            chk = finder('ID',int(call.from_user.id))
                            try:
                                try:
                                    A1a = finder('ID',int(call.from_user.id))
                                    A1b = get((A1a),'Peer')
                                    B1a = finder('ID',int(A1b))
                                    B1b = get((B1a),'Peer')
                                    anych_modify('Peer',0,int(str(call.from_user.id)))
                                    anych_modify('Status','closed',int(str(call.from_user.id)))
                                    anych_modify('tout',1728,int(str(call.from_user.id)))
                                    anych_modify('OTP',0,int(str(call.from_user.id)))
                                    if A1b == 0 :
                                        print('')
                                    else:
                                        anych_modify('Peer',0,int(A1b))
                                        anych_modify('Status','closed',int(A1b))
                                        anych_modify('tout',1728,int(A1b))
                                        anych_modify('OTP',0,int(A1b))
                                        bot.send_message(str(call.from_user.id),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                                        bot.send_message(str(A1b),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                                except Exception as e:
                                        print('cb_PrivateConnection error [410-433] /: '+str(e))
                                        #anych_modify('Peer',0,int(str(call.from_user.id)))
                                        #anych_modify('Status','closed',int(str(call.from_user.id)))
                                        anych_modify('OTP',0,int(str(call.from_user.id)))
                                        mid = str(call.from_user.id)
                                #D = OTP(int(str(call.from_user.id)))
                                D1a = finder('ID',int(str(call.from_user.id)))
                                D1b = get((D1a),'AnonyID')
                                #print(str(call.from_user.id))
                                if str(D1b) == '-invalid-':
                                    msgpvt = bot.send_message(call.from_user.id, 'Error to generate link,\n\nPlease try again!!')
                                else:
                                    mID = str(call.from_user.id)
                                    xcode = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
                                    xcode2 = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
                                    QRL = '/brc'+str(xcode)+str(D1b)+str(mID)+str(xcode2)
                                    if QRCode(QRL,(str(D1b)+str(mID))) == 'qrcode done':
                                        msgpvt = bot.send_photo(call.from_user.id, photo=open('temp/qrcode'+str(D1b)+str(mID)+'.png', 'rb'),caption= '𝚈𝚘𝚞𝚛 𝙸𝙳 𝚁𝚎𝚊𝚍𝚢 𝚏𝚘𝚛 𝚙𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 (𝟷 𝚍𝚊𝚢 𝚙𝚊𝚜𝚜) 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 : \n\n/brc'+str(xcode)+str(D1b)+str(mID)+str(xcode2)+"\n\n\n𝙽͟𝙾͟𝚃͟𝙴͟: 𝚂𝚎𝚗𝚍 𝚝𝚑𝚎 𝚊𝚋𝚘𝚟𝚎 𝚕𝚒𝚗𝚔 𝚘𝚛 𝚀𝚁 𝚌𝚘𝚍𝚎 𝚘𝚛 𝚙𝚎𝚎𝚛 𝚊𝚕𝚜𝚘 𝚌𝚊𝚗 𝚞𝚜𝚎 𝚌𝚊𝚖𝚎𝚛𝚊 𝚝𝚘 𝚜𝚌𝚊𝚗 𝚒𝚝 𝚊𝚗𝚍 𝚜𝚎𝚗𝚍 𝚝𝚘 𝚑𝚒𝚜/𝚑𝚎𝚛  '𝙰𝚗𝚘𝚗𝚢𝚖𝚘𝚞𝚜 𝙲𝚑𝚊𝚝' 𝚝𝚘 𝚎𝚜𝚝𝚊𝚋𝚕𝚒𝚜𝚑 𝚝𝚑𝚎 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗\n\n\n(𝚈𝚘𝚞𝚛 𝚙𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 (𝟷 𝚍𝚊𝚢 𝚙𝚊𝚜𝚜) 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 𝚕𝚒𝚗𝚔 𝚠𝚒𝚕𝚕 𝚎𝚡𝚙𝚒𝚛𝚎 𝚒𝚗 𝟼𝟶𝚜𝚎𝚌.")
                                        os.remove('temp/qrcode'+str(D1b)+str(mID)+'.png')
                                        with open('info_files/Broadcasting/Broadcasting_'+str(D1b)+str(mID)+'.txt', "w") as f:
                                            f.write("")
                                    #msgpvt = bot.send_message(call.from_user.id, '𝚈𝚘𝚞𝚛 𝙸𝙳 𝚁𝚎𝚊𝚍𝚢 𝚏𝚘𝚛 𝚙𝚛𝚒𝚟𝚊𝚝𝚎 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 : \n\n/pvt'+str(xcode)+str(D)+str(xcode2)+str(D1b)+"\n\n\n𝚈𝚘𝚞𝚛 𝚙𝚛𝚒𝚟𝚊𝚝𝚎 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 𝚕𝚒𝚗𝚔 𝚠𝚒𝚕𝚕 𝚎𝚡𝚙𝚒𝚛𝚎 𝚒𝚗 𝟼𝟶𝚜𝚎𝚌.")
                                D2a = finder('ID',int(str(call.from_user.id)))
                                D2b = get((D1a),'Status')
                                time.sleep(60)
                                bot.delete_message(call.from_user.id, msgpvt.message_id)
                                anych_modify('OTP','-',call.from_user.id)
                                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                            except Exception as e:
                                print('cb_PrivateConnection error [547-589] /: '+str(e))
                                msgplk = bot.send_message(str(call.from_user.id),"❌ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝗰𝗿𝗲𝗮𝘁𝗲 𝗹𝗶𝗻𝗸 !!")
                                time.sleep(2)
                                bot.delete_message(call.from_user.id, msgplk.message_id)

                #================================================
                #               AI Assistant                    
                #================================================
                elif call.data == 'F1':
                    if AIslots('AI') > 4 :
                        bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=True,
                                  text='⚠️\n\nSorry!!\n\nNo Free slot for AI assistant is available\nYou will able to use once someone leave the slot\n\nPlease try later!!') 
                    else:
                        try:
                            A1a = finder('ID',int(call.from_user.id))
                            A1b = get((A1a),'Peer')
                            print('Peer : '+str(A1b))
                            B1a = finder('ID',int(A1b))
                            B1b = get((B1a),'Peer')
                            if A1b == 0 :
                                anych_modify('Peer',0,int(str(call.from_user.id)))
                                anych_modify('Status','AI',int(str(call.from_user.id)))
                                anych_modify('OTP',0,int(str(call.from_user.id)))
                                anych_modify('tout',120,int(str(call.from_user.id)))
                                bot.send_message(str(call.from_user.id),"⚠️ 𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝗰𝗵𝗮𝗻𝗴𝗲𝘀 𝘁𝗼 '𝗔𝗜'. 𝗙𝗿𝗲𝗲 𝗺𝗲𝗺𝗯𝗲𝗿 𝗰𝗮𝗻 𝗴𝗲𝘁 𝘂𝗽𝘁𝗼 𝟱 𝗿𝗲𝘀𝗽𝗼𝗻𝘀𝗲𝘀 𝗳𝗿𝗼𝗺 𝘆𝗼𝘂 𝗚𝗣𝗧𝟯 𝗔𝗜 𝗮𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝘁.")
                            else:
                                anych_modify('Peer',0,int(str(call.from_user.id)))
                                anych_modify('Status','AI',int(str(call.from_user.id)))
                                anych_modify('OTP',0,int(str(call.from_user.id)))
                                anych_modify('tout',120,int(str(call.from_user.id)))
                                anych_modify('Peer',0,int(A1b))
                                anych_modify('Status','closed',int(A1b))
                                anych_modify('tout',1728,int(A1b))
                                anych_modify('OTP',0,int(A1b))
                                bot.send_message(str(call.from_user.id),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                                bot.send_message(str(A1b),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                                bot.send_message(str(call.from_user.id),"⚠️ 𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝗰𝗵𝗮𝗻𝗴𝗲𝘀 𝘁𝗼 '𝗔𝗜'. 𝗙𝗿𝗲𝗲 𝗺𝗲𝗺𝗯𝗲𝗿 𝗰𝗮𝗻 𝗴𝗲𝘁 𝘂𝗽𝘁𝗼 𝟱 𝗿𝗲𝘀𝗽𝗼𝗻𝘀𝗲𝘀 𝗳𝗿𝗼𝗺 𝘆𝗼𝘂 𝗚𝗣𝗧𝟯 𝗔𝗜 𝗮𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝘁.")
                        except Exception as e:
                            print('Exception [1177-1192] /:'+str(e))
                            anych_modify('Peer',0,int(str(call.from_user.id)))
                            anych_modify('Status','AI',int(str(call.from_user.id)))
                            anych_modify('OTP',0,int(str(call.from_user.id)))
                            anych_modify('tout',120,int(str(call.from_user.id)))
                            bot.send_message(str(call.from_user.id),"⚠️ 𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝗰𝗵𝗮𝗻𝗴𝗲𝘀 𝘁𝗼 '𝗔𝗜'. 𝗙𝗿𝗲𝗲 𝗺𝗲𝗺𝗯𝗲𝗿 𝗰𝗮𝗻 𝗴𝗲𝘁 𝘂𝗽𝘁𝗼 𝟱 𝗿𝗲𝘀𝗽𝗼𝗻𝘀𝗲𝘀 𝗳𝗿𝗼𝗺 𝘆𝗼𝘂 𝗚𝗣𝗧𝟯 𝗔𝗜 𝗮𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝘁.")
                        bot.answer_callback_query(callback_query_id=call.id,
                                          show_alert=True,
                                          text='ℹ️\n\nGPT3 AI BOT \n\nYour status changed to [AI] from now all replies will be given by AI bot, Unless you have close the connection.')

                #================================================
                #                     About                   
                #================================================
                elif call.data == 'G1':
                    A1a = finder('ID',int(call.from_user.id))
                    peer_status = get((A1a),'Status')
                    anych_modify('Status','paused',int(str(call.from_user.id)))
                    with open('info_files/about.txt') as f:
                            privacy = f.read()

                    msghelp = bot.send_message(call.message.chat.id, str(privacy))
                    anych_modify('Status',str(peer_status),int(str(call.from_user.id)))
                    bot.answer_callback_query(callback_query_id=call.id,
                                          show_alert=True,
                                          text='ℹ️\n\nAnonychat Bot Version 5.2.1\nSecurity Version 2.0.1\nAddon Version 2.0.3\nPatch Verion 21.0.3')
                #================================================
                #               Privacy Statement                    
                #================================================
                elif call.data == 'H1':
                    A1a = finder('ID',int(call.from_user.id))
                    peer_status = get((A1a),'Status')
                    anych_modify('Status','paused',int(str(call.from_user.id)))
                    with open('info_files/privacystatement.txt') as f:
                            privacy = f.read()
                    msghelp = bot.send_message(call.message.chat.id, str(privacy))
                    anych_modify('Status',str(peer_status),int(str(call.from_user.id)))
                #================================================
                #               ID Flushing                    
                #================================================
                elif call.data == 'I1':
                    if str(call.from_user.id) == '584429967' or str(call.from_user.id) == '5370406970':
                        keyboard = types.InlineKeyboardMarkup()
                        button_a0 = types.InlineKeyboardButton(text=' 𝗬𝗘𝗦 ', callback_data='IDF_yes')
                        button_b0 = types.InlineKeyboardButton(text=' 𝗡𝗢 ', callback_data='IDF_no')
                        keyboard.add(button_a0,button_b0)
                        bot.send_message(call.from_user.id, "⚠️ 𝗔𝗿𝗲 𝘆𝗼𝘂 𝘀𝘂𝗿𝗲 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗲𝗹𝗲𝘁𝗲/𝗲𝗿𝗮𝘀𝗲 𝘆𝗼𝘂𝗿 𝗜𝗗??", reply_markup=keyboard)
                        @bot.callback_query_handler(func=lambda call: call.data in ['IDF_yes','IDF_no'])
                        def callback_inline(call):
                            if call.data == 'IDF_yes':
                                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                poll = bot.send_poll(chat_id=int(call.from_user.id), question="Please rate our service",open_period=10,options=["⭐️⭐️⭐️Excellent", "⭐️⭐️Good", "⭐️Bad"])
                                MA1a = finder('ID',int(call.from_user.id))
                                if str(MA1a) == 'not found':
                                    bot.answer_callback_query(callback_query_id=call.id,
                                                          show_alert=True,
                                                          text='⚠️\n\nYour ID is not registered')
                                else:
                                    bot.answer_callback_query(call.id, "Requesting....")
                                    try:
                                        #bot.delete_message(call.from_user.id, msgM2.message_id)
                                        try:
                                            bot.answer_callback_query(call.id, "Closing you connection...")
                                            A1a = finder('ID',int(call.from_user.id))
                                            print('ok 1')
                                            A1b = str(int(round(get((A1a),'Peer'))))
                                            B1a = finder('ID',int(A1b))
                                            B1b = get((B1a),'Peer')
                                            B1c = get((B1a),'Status')
                                            print('ok 2')
                                            anych_modify('Peer',0,int(str(call.from_user.id)))
                                            anych_modify('Status','closed',int(str(call.from_user.id)))
                                            anych_modify('tout',1728,int(str(call.from_user.id)))
                                            anych_modify('OTP',0,int(str(call.from_user.id)))
                                            anych_modify('Peer',0,int(A1b))
                                            if B1c == 'linked':
                                                anych_modify('Status','waiting',int(A1b))
                                            else:
                                                anych_modify('Status','open',int(A1b))
                                            anych_modify('OTP',0,int(A1b))
                                            print('ok 3')
                                            bot.answer_callback_query(call.id, "Deleting your ID..")
                                            flush(str(call.from_user.id))
                                            print('ok 4')
                                            print(str(A1b))
                                            print(str(call.from_user.id))
                                            msgcl1b = bot.send_message(str(A1b),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                                            msgcl1a = bot.send_message(str(call.from_user.id),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                                            time.sleep(6)
                                            print('ok 5')
                                            bot.delete_message(str(A1b), msgcl1b.message_id)
                                            msgcl1a2 = bot.edit_message_text("❌ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼 𝗺𝗼𝗿𝗲 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘂𝘀𝗲𝗿 !!", call.from_user.id, msgcl1a.message_id)
                                            bot.delete_message(call.from_user.id, msgcl1a2.message_id)
                                            print('ok 6')
                                            time.sleep(6)
                                            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                        except Exception as e:
                                            print('cb_CloseConnection error [1289-1331] /: '+str(e))
                                            bot.answer_callback_query(call.id, "Closing you connections...")
                                            flush(str(call.from_user.id))
                                            msgcl2 = bot.send_message(str(call.from_user.id),"❌ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼 𝗺𝗼𝗿𝗲 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘂𝘀𝗲𝗿 !!")
                                            time.sleep(2)
                                            bot.delete_message(call.from_user.id, msgcl2.message_id)
                                            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                                    except Exception as e:
                                        print('cb_CloseConnection error [501-529] /: '+str(e))
                            elif call.data == 'IDF_no':
                                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                            else:
                                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                    else:
                        bot.answer_callback_query(callback_query_id=call.id,
                                              show_alert=True,
                                              text='⚠️\n\nUnable to process your request!!\n\nPlease click on ⏹️ to closed your connection')
                #================================================
                #           Closing your connection                    
                #================================================
                elif call.data == 'I2':
                    keyboard = types.InlineKeyboardMarkup()
                    button_a0 = types.InlineKeyboardButton(text=' 𝗬𝗘𝗦 ', callback_data='IDC_yes')
                    button_b0 = types.InlineKeyboardButton(text=' 𝗡𝗢 ', callback_data='IDC_no')
                    keyboard.add(button_a0,button_b0)
                    bot.send_message(call.from_user.id, "⚠️ 𝗔𝗿𝗲 𝘆𝗼𝘂𝗿 𝘀𝘂𝗿𝗲 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗰𝗹𝗼𝘀𝗲 𝘆𝗼𝘂𝗿 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 ??", reply_markup=keyboard)
                    @bot.callback_query_handler(func=lambda call: call.data in ['IDC_yes','IDC_no'])
                    def callback_inline(call):
                        if call.data == 'IDC_yes':
                            bot.answer_callback_query(callback_query_id=call.id,
                                                    show_alert=True,
                                                    text='❌\n\nYour connection has been closed and will remain closed for the next 24 hours or until you wish to connect with someone within this period.')
                            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                            A0a = finder('ID',int(call.from_user.id))
                            A0b = str(get((A0a),'Status'))
                            #A0c = str(int(round(get((A0a),'AnonyID'))))
                            if A0b == "subscriber":
                                msgcl1a = bot.send_message(str(call.from_user.id),broadcast_subcancel('info_files/Broadcasting/brc'+str(A0c),int(call.from_user.id)))
                                time.sleep(6)
                                bot.delete_message(call.from_user.id, msgcl1a.message_id)
                            #elif A0b == "broadcaster":

                            else:
                                #delete_row("file.txt", 3234)
                                MA1a = finder('ID',int(call.from_user.id))
                                if str(MA1a) == 'not found':
                                    bot.answer_callback_query(callback_query_id=call.id,
                                                          show_alert=True,
                                                          text='⚠️\n\nYour ID is not registered')
                                else:
                                    bot.answer_callback_query(call.id, "Requesting...")
                                    try:
                                        #bot.delete_message(call.from_user.id, msgM2.message_id)
                                        try:
                                            bot.answer_callback_query(callback_query_id=call.id,
                                                                show_alert=True,
                                                                text='❌\n\nYour anonymous connection has been closed on your request!!\n\nYour Membership ID is still valid for new connections!!')
                                            bot.answer_callback_query(call.id, "Closing your connections..")
                                            A1a = finder('ID',int(call.from_user.id))
                                            A1b = str(int(round(get((A1a),'Peer'))))
                                            if A1b == 0 :
                                                anych_modify('Peer',0,int(str(call.from_user.id)))
                                                anych_modify('Status','closed',int(str(call.from_user.id)))
                                                anych_modify('tout',14400,int(str(call.from_user.id)))
                                                anych_modify('OTP',0,int(str(call.from_user.id)))
                                                msgcl1a = bot.send_message(str(call.from_user.id),"❌ 𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝗰𝗵𝗮𝗻𝗴𝗲𝗱 𝘁𝗼 '𝗰𝗹𝗼𝘀𝗲𝗱' !!")
                                                time.sleep(6)
                                                bot.delete_message(call.from_user.id, msgcl1a.message_id)
                                                bot.answer_callback_query(callback_query_id=call.id,
                                                                      show_alert=True,
                                                                      text='❌\n\nYour anonymous connection has been closed on your request!!\n\nYour Membership ID is still valid for new connections!!')
                                            else:
                                                B1a = finder('ID',int(A1b))
                                                B1b = get((B1a),'Peer')
                                                peer_status = get((B1a),'Status')
                                                anych_modify('Peer',0,int(str(call.from_user.id)))
                                                anych_modify('Status','closed',int(str(call.from_user.id)))
                                                anych_modify('OTP',0,int(str(call.from_user.id)))
                                                anych_modify('Peer',0,int(A1b))
                                                anych_modify('OTP',0,int(A1b))
                                                anych_modify('Status','closed',int(A1b))
                                                leasing(int(call.from_user.id),14400)
                                                leasing(int(A1b),200)
                                                msgcl1a = bot.send_message(str(call.from_user.id),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                                                msgcl1b = bot.send_message(str(A1b),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                                                msgcl1bi = bot.send_message(str(A1b),"🔍  𝗪𝗲 𝗮𝗿𝗲 𝘀𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝗳𝗼𝗿 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝘂𝘀𝗲𝗿 𝘁𝗼 𝗵𝗮𝘃𝗲 𝗮 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂 !!")
                                                if str(peer_status) == "linked":
                                                    anych_modify('Status',str('waiting'),int(A1b))
                                                    anych_modify('tout',200,int(A1b))
                                                else:
                                                    anych_modify('Status',str('closed'),int(A1b))
                                                    #anych_modify('tout',0,int(A1b))
                                                    leasing(int(A1b),200)
                                                time.sleep(6)
                                                bot.delete_message(call.from_user.id, msgcl1a.message_id)
                                                bot.delete_message(str(A1b), msgcl1b.message_id)
                                                bot.delete_message(str(A1b), msgcl1bi.message_id)

                                        except Exception as e:
                                            bot.answer_callback_query(callback_query_id=call.id,
                                                                show_alert=True,
                                                                text='❌\n\nYour anonymous connection has been closed on your request!!\n\nYour Membership ID is still valid for new connections!!')

                                            print('cb_CloseConnection error [1366-1406] /: '+str(e))
                                            bot.answer_callback_query(call.id, "Changing your status...")
                                            anych_modify('Peer',0,int(str(call.from_user.id)))
                                            anych_modify('Status','closed',int(str(call.from_user.id)))
                                            leasing(int(call.from_user.id),14400)
                                            anych_modify('OTP',0,int(str(call.from_user.id)))
                                            msgcl1a = bot.send_message(str(call.from_user.id),"❌ 𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝗰𝗵𝗮𝗻𝗴𝗲𝗱 𝘁𝗼 '𝗰𝗹𝗼𝘀𝗲𝗱' !!")
                                            time.sleep(2)
                                            bot.delete_message(call.from_user.id, msgcl1a.message_id)

                                    except Exception as e:
                                        print('cb_CloseConnection error [501-529] /: '+str(e))
                        elif call.data == 'IDC_no':
                            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                        else:
                            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                #================================================
                #           Searching new partner                    
                #================================================
                elif call.data == 'I3':
                    print('-close connection-')
                    status = get((finder('ID',int(call.from_user.id))),'Status')
                    if status == 'privte':
                        bot.answer_callback_query(callback_query_id=call.id,
                                              show_alert=True,
                                              text='⚠️\n\nYour status is private\n\nPlease ⏹️ close your connection first')
                    elif status == 'waiting':
                        bot.answer_callback_query(callback_query_id=call.id,
                                              show_alert=True,
                                              text='⚠️\nPlease wait!!\n\nYou are with waiting status\nWe will notify you once we have found your partner')
                    else:
                        MA1a = finder('ID',int(call.from_user.id))
                        if str(MA1a) == 'not found':
                            bot.answer_callback_query(callback_query_id=call.id,
                                                  show_alert=True,
                                                  text='⚠️\n\nYour ID is not registered')
                        else:
                            bot.answer_callback_query(call.id, "Requesting...")
                            try:
                                #bot.delete_message(call.from_user.id, msgM2.message_id)
                                try:
                                    bot.answer_callback_query(call.id, "Searching for another partner..")
                                    A1a = finder('ID',int(call.from_user.id))
                                    A1b = str(int(round(get((A1a),'Peer'))))
                                    A1c = str(get((A1a),'Status'))
                                    print('A1a >>> '+str(A1a))
                                    print('A1b >>> '+str(A1b))
                                    print('A1s >>> '+str(A1c))
                                    if A1c == 'private' or A1c == 'broadcaster' or A1c == 'subscribers' or A1c == 'permanent' or A1c == 'AI' :
                                        msgcl1b = bot.send_message(str(call.from_user.id),"❌  𝗬𝗼𝘂 𝗮𝗿𝗲 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝘂𝘁𝗶𝗹𝗶𝘀𝗶𝗻𝗴 𝗼𝘁𝗵𝗲𝗿 𝘀𝗲𝗿𝘃𝗶𝗰𝗲, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗰𝗹𝗼𝘀𝗲 𝘆𝗼𝘂𝗿 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝗯𝘆 𝗰𝗹𝗶𝗰𝗸𝗶𝗻𝗴 𝗼𝗻 ⏹️ .")
                                    elif A1c == 'paused':
                                        msgcl1b = bot.send_message(str(call.from_user.id),"❌ 𝗦𝘆𝘀𝘁𝗲𝗺 𝗶𝘀 𝗯𝘂𝘀𝘆 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗽𝗿𝗲𝘃𝗶𝗼𝘂𝘀 𝗿𝗲𝗾𝘂𝗲𝘀𝘁, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝗼𝗿 𝗰𝗹𝗼𝘀𝗲 𝘆𝗼𝘂𝗿 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝗯𝘆 𝗰𝗹𝗶𝗰𝗸𝗶𝗻𝗴 𝗼𝗻 ⏹️ .")
                                    elif A1c == 'waiting':
                                        msgcl1b = bot.send_message(str(call.from_user.id),"⚠️ 𝗬𝗼𝘂 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗵𝗮𝘃𝗲 '𝘄𝗮𝗶𝘁𝗶𝗻𝗴' 𝘀𝘁𝗮𝘁𝘂𝘀.𝗣𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝘄𝗵𝗶𝗹𝗲 𝘄𝗲'𝗿 𝘀𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗳𝗼𝗿 𝘆𝗼𝘂.𝗧𝗵𝗶𝘀 𝗺𝗶𝗴𝗵𝘁 𝘁𝗮𝗸𝗲 𝗹𝗼𝗻𝗴 𝘁𝗶𝗺𝗲 𝘀𝘂𝗯𝗷𝗲𝗰𝘁𝗲𝗱 𝘁𝗼 𝘁𝗵𝗲 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝘀𝗹𝗼𝘁𝘀.")

                                    elif str(A1b) == '0' :
                                        print('>>>YES HERE>>>>')
                                        anych_modify('Peer',0,int(str(call.from_user.id)))
                                        anych_modify('Status','waiting',int(str(call.from_user.id)))
                                        anych_modify('OTP',0,int(str(call.from_user.id)))
                                        msgcl1b = bot.send_message(str(call.from_user.id),"🔍 𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝗳𝗼𝗿 𝗿𝗮𝗻𝗱𝗼𝗺 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 !!")
                                    else:
                                        B1a = finder('ID',int(A1b))
                                        B1b = get((B1a),'Peer')
                                        anych_modify('Peer',0,int(str(call.from_user.id)))
                                        anych_modify('Status','waiting',int(str(call.from_user.id)))
                                        anych_modify('OTP',0,int(str(call.from_user.id)))
                                        anych_modify('Peer',0,int(A1b))
                                        anych_modify('OTP',0,int(A1b))
                                        anych_modify('Status','closed',int(A1b))
                                        leasing(int(A1b),200)
                                        msgcl1b = bot.send_message(str(A1b),"❌𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                                        msgcl1bi = bot.send_message(str(A1b),"𝗣𝗹𝗲𝗮𝘀𝗲 𝗰𝗹𝗶𝗰𝗸 𝗼𝗻 ⏩️ 𝗶𝗳 𝘆𝗼𝘂𝗿 𝘄𝗶𝘀𝗵𝗶𝗻𝗴 𝘁𝗼 𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝘄𝗶𝘁𝗵 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗿𝗮𝗻𝗱𝗼𝗺 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 !!")
                                        msgcl1a = bot.send_message(str(call.from_user.id),"❌𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                                        #time.sleep(6)
                                        #bot.delete_message(call.from_user.id, msgcl1a.me�ssage_id)
                                        #bot.delete_message(str(A1b), msgcl1b.message_id)
                                        #bot.delete_message(str(A1b), msgcl1bi.message_id)
                                        bot.answer_callback_query(callback_query_id=call.id,
                                                        show_alert=True,
                                                        text='❌\n\nYour anonymous connection has been closed on your request!!\n\nAnonymous chats manager is finding another partner for you!!')
                                except Exception as e:
                                    print('cb_CloseConnection error [1436-1480] /: '+str(e))
                                    bot.answer_callback_query(call.id, "System having error..")
                                    msgcl1b = bot.send_message(str(call.from_user.id),"⚠️ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝗽𝗿𝗼𝗰𝗲𝘀𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 !!")
                                    bot.answer_callback_query(callback_query_id=call.id,
                                                        show_alert=True,
                                                        text='❌\n\nYour anonymous connection has been closed on your request!!\n\nAnonymous chats manager is finding another partner for you!!')
                                    #time.sleep(2)
                                    #bot.delete_message(str(call.from_user.id), msgcl1b.message_id)

                            except Exception as e:
                                print('cb_CloseConnection error [1434-1491] /: '+str(e))
                #================================================
                #               Change Nicename                   
                #================================================
                elif call.data == 'Ks1':
                    try:
                        anych_modify('Nickname',str(nick()),584429967)
                        bot.send_message('584429967','Nickname changed')

                    except Exception as e:
                        bot.send_message(('584429967','Error :/'+str(e)))

                #================================================
                #               More >>                   
                #================================================

                elif call.data == 'J1':
                    keyboard = types.InlineKeyboardMarkup()
                    button_a = types.InlineKeyboardButton(text='🪙 𝗠𝗲𝗺𝗯𝗲𝗿𝘀𝗵𝗶𝗽', callback_data='A11')
                    button_b = types.InlineKeyboardButton(text='⚙️ 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀', callback_data='0B11')
                    button_c = types.InlineKeyboardButton(text='🆘 𝗛𝗲𝗹𝗽', callback_data='C11')
                    button_d = types.InlineKeyboardButton(text='📞 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗨𝘀', callback_data='D11')
                    button_e = types.InlineKeyboardButton(text='<<  𝗕𝗮𝗰𝗸', callback_data='E11')
                    keyboard.add(button_a)
                    keyboard.add(button_b)
                    keyboard.add(button_c,button_d)
                    keyboard.add(button_e)
                    #bot.editMessageCaption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="|   𝓐𝓷𝓸𝓷𝔂𝓶𝓸𝓾𝓼 𝓒𝓱𝓪𝓽𝓼.  |")
                    #bot.edit_message_photo(chat_id=call.message.chat.id, message_id=call.message.message_id, photo=open('info_files/Anonychat_banner.jpg', 'rb'),caption= ".            𝔄 𝔫 𝔬 𝔫 𝔶 𝔪 𝔬 𝔲 𝔰    ℭ 𝔥 𝔞 𝔱 𝔰", reply_markup=keyboard)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="||             𝓐𝓷𝓸𝓷𝔂𝓶𝓸𝓾𝓼 𝓒𝓱𝓪𝓽𝓼.          ", reply_markup=keyboard)
                    #bot.send_message(message.chat.id, "|   𝓐𝓷𝓸𝓷𝔂𝓶𝓸𝓾𝓼 𝓒𝓱𝓪𝓽𝓼.  |", reply_markup=keyboard)
                else:
                    print('Invalid option selection!!')
            @bot.callback_query_handler(func=lambda call: call.data in ['A11','C11','D11','E11'])
            def callback_inline(call):
                if call.data == 'E11':
                    keyboard = types.InlineKeyboardMarkup()
                    button_a = types.InlineKeyboardButton(text='🔐 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗖𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻', callback_data='A1')
                    button_b = types.InlineKeyboardButton(text='🔀 𝗥𝗮𝗻𝗱𝗼𝗺 𝗖𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻', callback_data='B1')
                    button_c = types.InlineKeyboardButton(text='📲 𝗔𝗻𝗼𝗻𝘆 𝗡𝘂𝗺𝗯𝗲𝗿', callback_data='C1')
                    button_d = types.InlineKeyboardButton(text='❇️ 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗖𝗹𝘂𝗯𝘀', callback_data='D1')
                    button_e = types.InlineKeyboardButton(text='🔊 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁𝗶𝗻𝗴', callback_data='E1')
                    button_f = types.InlineKeyboardButton(text='🔆 𝗔𝗜 𝗖𝗵𝗮𝘁 𝗕𝗼𝘁', callback_data='F1')
                    button_g = types.InlineKeyboardButton(text='🚹 𝗔𝗯𝗼𝘂𝘁', callback_data='G1')
                    button_h = types.InlineKeyboardButton(text='📝 𝗣𝗿𝗶𝘃𝗮𝗰𝘆 𝗣𝗼𝗹𝗶𝗰𝘆', callback_data='H1')
                    button_i = types.InlineKeyboardButton(text='⏏️ ', callback_data='I1')
                    button_i1 = types.InlineKeyboardButton(text='⏹️', callback_data='I2')
                    button_i2 = types.InlineKeyboardButton(text='⏩️', callback_data='I3')
                    button_j = types.InlineKeyboardButton(text='𝗠𝗼𝗿𝗲  >>', callback_data='J1')
                    if str(message.chat.id) == '584429967':
                        button_Ks1 = types.InlineKeyboardButton(text='📛 𝗖𝗵𝗮𝗻𝗴𝗲 𝗻𝗶𝗰𝗸𝗻𝗮𝗺𝗲', callback_data='Ks1')
                        keyboard.add(button_a)
                        keyboard.add(button_b)
                        keyboard.add(button_i,button_i1,button_i2)
                        keyboard.add(button_c)
                        keyboard.add(button_d)
                        keyboard.add(button_e)
                        keyboard.add(button_f)
                        keyboard.add(button_g,button_h)
                        keyboard.add(button_Ks1)
                        keyboard.add(button_j)
                    else:
                        keyboard.add(button_a)
                        keyboard.add(button_b)
                        keyboard.add(button_i,button_i1,button_i2)
                        keyboard.add(button_c)
                        keyboard.add(button_d)
                        keyboard.add(button_e)
                        keyboard.add(button_f)
                        keyboard.add(button_g,button_h)
                        keyboard.add(button_j)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="||             𝓐𝓷𝓸𝓷𝔂𝓶𝓸𝓾𝓼 𝓒𝓱𝓪𝓽𝓼.          ", reply_markup=keyboard)
                #================================================
                #                 Membership                    
                #================================================
                elif call.data == 'A11':
                    MA1a = finder('ID',int(call.from_user.id))
                    print(MA1a)
                    if str(MA1a) == 'not found':
                        bot.answer_callback_query(callback_query_id=call.id,
                                              show_alert=True,
                                              text='⚠️\n\nYour ID is not registered\nPlease register first')
                    else:
                        MA1b = get((MA1a),'AnonyID')
                        if str(call.from_user.id) == "584429967":
                            memtype = "Gold Account 🥇 \n\n[AI Credit 5000cr]"
                        else:
                            memtype = "Free Privilege Account \n\n[AI Credit 5cr]"
                        bot.answer_callback_query(callback_query_id=call.id,
                                              show_alert=True,
                                              text='ℹ️\n\n'+str(memtype)+'\n\nMembership ID : '+str(int(round((MA1b)))))
                #================================================
                #                     Help                    
                #================================================
                elif call.data == 'C11':
                    A1a = finder('ID',int(call.from_user.id))
                    peer_status = get((A1a),'Status')
                    anych_modify('Status','paused',int(str(call.from_user.id)))
                    with open('info_files/help.txt') as f:
                            f = f.read()
                    anych_modify('Status',str(peer_status),int(str(call.from_user.id)))
                    msghelp = bot.send_message(call.message.chat.id, str(f))

                #================================================
                #                   Contact us                    
                #================================================

                elif call.data == 'D11':    
                    with open('info_files/contactus.txt') as f:
                            f = f.read()
                    msghelp = bot.send_message(call.message.chat.id, str(f))

            @bot.callback_query_handler(func=lambda call: call.data in ['1', '2'])
            def callback_inline(call):
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

            @bot.callback_query_handler(func=lambda call: call.data in ['0B11'])
            def callback_inline(call):
                if call.data == '0B11':
                    print("Settings called")
                    keyboard = types.InlineKeyboardMarkup()
                    W11a = str(lookup('MID','PIX',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                    W11b = str(lookup('MID','MSG',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                    W11c = str(lookup('MID','VCN',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                    W11d = str(lookup('MID','VDO',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                    W11e = str(lookup('MID','BLK',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                    #W11f = str(lookup('MID','ATR',584429967)).replace("1", "🟢").replace("0", "🔴")
                    W11g = str(lookup('MID','CEN',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                    button_a = types.InlineKeyboardButton(text='𝗣𝗶𝗰𝘁𝘂𝗿𝗲s'+str(W11a), callback_data='1A')
                    button_b = types.InlineKeyboardButton(text='𝗧𝗲𝘅𝘁'+str(W11b), callback_data='1B')
                    button_c = types.InlineKeyboardButton(text='𝗩𝗼𝗶𝗰𝗲'+str(W11c), callback_data='1C')
                    button_d = types.InlineKeyboardButton(text='𝗩𝗶𝗱𝗲𝗼'+str(W11d), callback_data='1D')
                    button_e = types.InlineKeyboardButton(text='𝗔𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗕𝗹𝗼𝗰𝗸 𝗹𝗶𝘀𝘁'+str(W11e), callback_data='1E')
                    button_f = types.InlineKeyboardButton(text='𝗔𝘂𝘁𝗼 𝗧𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗲'+str('⚫️'), callback_data='1F')
                    button_g = types.InlineKeyboardButton(text='𝗖𝗲𝗻𝘀𝗼𝗿'+str(W11g), callback_data='1G')
                    button_z = types.InlineKeyboardButton(text='𝗘𝘅𝗶𝘁', callback_data='1Z')
                    keyboard.add(button_a, button_d)
                    keyboard.add(button_b,button_c)
                    keyboard.add(button_e)
                    keyboard.add(button_f)
                    keyboard.add(button_g)
                    keyboard.add(button_z)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀         [𝗢𝗡/𝗢𝗙𝗙] :", reply_markup=keyboard)
                    #bot.send_message(message.chat.id, "𝗬𝗼𝘂𝗿 𝗰𝗵𝗮𝘁 𝘀𝗲𝘁𝘁𝗶𝗻𝗴𝘀", reply_markup=keyboard)
                else:
                    bot.answer_callback_query(callback_query_id=call.id,
                                                              show_alert=True,
                                                              text='⚠️\n\nThis feature is currently unavailable!!')
                @bot.callback_query_handler(func=lambda call: call.data in ['1A', '1B','1C','1D','1E','1F','1G'])
                def callback_inline(call):
                    if call.data == '1A' or call.data == '1B' or call.data == '1C' or call.data == '1D' or call.data == '1E' or call.data == '1F'or  call.data == '1G':
                        keyboard = types.InlineKeyboardMarkup()
                        if call.data == '1A':
                            anych_para_modify('PIX',1,call.from_user.id)
                        elif call.data == '1B':
                            anych_para_modify('MSG',1,call.from_user.id)
                        elif call.data == '1C':
                            anych_para_modify('VCN',1,call.from_user.id)
                        elif call.data == '1D':
                            anych_para_modify('VDO',1,call.from_user.id)
                        elif call.data == '1E':
                            anych_para_modify('BLK',1,call.from_user.id)
                        elif call.data == '1F':
                            bot.answer_callback_query(callback_query_id=call.id,
                                                                      show_alert=True,
                                                                      text='⚠️\n\nThis feature is currently unavailable!!')
                        elif call.data == '1G':
                            anych_para_modify('CEN',1,call.from_user.id)
                        else:
                            #global W11b,W11c,W11d,W11e
                            W11z = 'OFF'
                        W11a = str(lookup('MID','PIX',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                        W11b = str(lookup('MID','MSG',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                        W11c = str(lookup('MID','VCN',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                        W11d = str(lookup('MID','VDO',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                        W11e = str(lookup('MID','BLK',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                        #W11f = str(lookup('MID','ATR',584429967)).replace("1", "🟢").replace("0", "🔴")
                        W11g = str(lookup('MID','CEN',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                        button_a = types.InlineKeyboardButton(text='𝗣𝗶𝗰𝘁𝘂𝗿𝗲s'+str(W11a), callback_data='1A1')
                        button_b = types.InlineKeyboardButton(text='𝗧𝗲𝘅𝘁'+str(W11b), callback_data='1B1')
                        button_c = types.InlineKeyboardButton(text='𝗩𝗼𝗶𝗰𝗲'+str(W11c), callback_data='1C1')
                        button_d = types.InlineKeyboardButton(text='𝗩𝗶𝗱𝗲𝗼'+str(W11d), callback_data='1D1')
                        button_e = types.InlineKeyboardButton(text='𝗔𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗕𝗹𝗼𝗰𝗸 𝗹𝗶𝘀𝘁'+str(W11e), callback_data='1E1')
                        button_f = types.InlineKeyboardButton(text='𝗔𝘂𝘁𝗼 𝗧𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗲'+str('⚫️'), callback_data='1F1')
                        button_g = types.InlineKeyboardButton(text='𝗖𝗲𝗻𝘀𝗼𝗿'+str(W11g), callback_data='1G1')
                        button_z = types.InlineKeyboardButton(text='𝗘𝘅𝗶𝘁', callback_data='1Z1')
                        keyboard.add(button_a, button_d)
                        keyboard.add(button_b,button_c)
                        keyboard.add(button_e)
                        keyboard.add(button_f)
                        keyboard.add(button_g)
                        keyboard.add(button_z)
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀         [𝗢𝗡/𝗢𝗙𝗙] :", reply_markup=keyboard)
                        #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="𝗬𝗼𝘂𝗿 𝗰𝗵𝗮𝘁 𝘀𝗲𝘁𝘁𝗶𝗻𝗴𝘀", reply_markup=keyboard)
                        #bot.send_message(call.from_user.id, "𝙰𝚗𝚘𝚗𝚢𝚖𝚘𝚞𝚜 𝙲𝚑𝚊𝚝 𝙱𝚘𝚝 𝚂𝚎𝚝𝚝𝚒𝚗𝚐𝚜(SAVED) :", reply_markup=keyboard)

                @bot.callback_query_handler(func=lambda call: call.data in ['�1A1', '1B1','1C1','1D1','1E1','1F1','1G1'])
                def callback_inline(call):
                    if call.data == '1A1' or call.data == '1B1' or call.data == '1C1' or call.data == '1D1' or call.data == '1E1' or call.data == '1F1' or call.data == '1G1':
                        keyboard = types.InlineKeyboardMarkup()
                        if call.data == '1A1':
                            anych_para_modify('PIX',0,call.from_user.id)
                        elif call.data == '1B1':
                            anych_para_modify('MSG',0,call.from_user.id)
                        elif call.data == '1C1':
                            anych_para_modify('VCN',0,call.from_user.id)
                        elif call.data == '1D1':
                            anych_para_modify('VDO',0,call.from_user.id)
                        elif call.data == '1E1':
                            anych_para_modify('BLK',0,call.from_user.id)
                        elif call.data == '1F1':
                            bot.answer_callback_query(callback_query_id=call.id,
                                                                      show_alert=True,
                                                                      text='⚠️\n\nThis feature is currently unavailable!!')
                        elif call.data == '1G1':
                            anych_para_modify('CEN',0,call.from_user.id)
                        else:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀 𝘀𝗮𝘃𝗲𝗱!!")
                            W11z = 'ON'
                        W11a = str(lookup('MID','PIX',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                        W11b = str(lookup('MID','MSG',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                        W11c = str(lookup('MID','VCN',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                        W11d = str(lookup('MID','VDO',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                        W11e = str(lookup('MID','BLK',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                        #W11f = str(lookup('MID','ATR',584429967)).replace("1", "🟢").replace("0", "🔴")
                        W11g = str(lookup('MID','CEN',call.from_user.id)).replace("1", "🟢").replace("0", "🔴")
                        button_a = types.InlineKeyboardButton(text='𝗣𝗶𝗰𝘁𝘂𝗿𝗲s'+str(W11a), callback_data='1A')
                        button_b = types.InlineKeyboardButton(text='𝗧𝗲𝘅𝘁'+str(W11b), callback_data='1B')
                        button_c = types.InlineKeyboardButton(text='𝗩𝗼𝗶𝗰𝗲'+str(W11c), callback_data='1C')
                        button_d = types.InlineKeyboardButton(text='𝗩𝗶𝗱𝗲𝗼'+str(W11d), callback_data='1D')
                        button_e = types.InlineKeyboardButton(text='𝗔𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗕𝗹𝗼𝗰𝗸 𝗹𝗶𝘀𝘁'+str(W11e), callback_data='1E')
                        button_f = types.InlineKeyboardButton(text='𝗔𝘂𝘁𝗼 𝗧𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗲'+str('⚫️'), callback_data='1F')
                        button_g = types.InlineKeyboardButton(text='𝗖𝗲𝗻𝘀𝗼𝗿'+str(W11g), callback_data='1G')
                        button_z = types.InlineKeyboardButton(text='𝗘𝘅𝗶𝘁', callback_data='1Z')
                        keyboard.add(button_a, button_d)
                        keyboard.add(button_b,button_c)
                        keyboard.add(button_e)
                        keyboard.add(button_f)
                        keyboard.add(button_g)
                        keyboard.add(button_z)
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀         [𝗢𝗡/𝗢𝗙𝗙] :", reply_markup=keyboard)
                        #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="𝗬𝗼𝘂𝗿 𝗰𝗵𝗮𝘁 𝘀𝗲𝘁𝘁𝗶𝗻𝗴𝘀", reply_markup=keyboard)
                        #bot.send_message(call.from_user.id, "𝙰𝚗𝚘𝚗𝚢𝚖𝚘𝚞𝚜 𝙲𝚑𝚊𝚝 𝙱𝚘𝚝 𝚂𝚎𝚝𝚝𝚒𝚗𝚐𝚜(SAVED) :", reply_markup=keyboard)

                @bot.callback_query_handler(func=lambda call: call.data in ['1Z','1Z1'])
                def callback_inline(call):
                    if call.data == '1Z1' or call.data == '1Z':
                        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                @bot.callback_query_handler(func=lambda call: call.data in ['1', '2'])
                def callback_inline(call):
                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)




    elif str(message.text) == '/flush':
        if str(message.chat.id) == str('584429967'):
            mid = str(message.chat.id)
            a = find(mid)
            if a == 'not found':
                bot.send_message((message.chat.id), str(a))
            else:
                a = flush(str(mid))
                bot.send_message((message.chat.id), str(a))
        else:
            return 0

    elif str(message.text) == '/logs':
        try:
            if str(message.chat.id) == '584429967':
              bot.send_chat_action(str(message.chat.id), 'typing')
              text_doc = open('Anonychat_reg_logs.txt', 'rb')
              bot.send_document('584429967', text_doc)
            else:
                return 0
        except:
            print('Unable to send logs"')

    elif str(message.text) == '/db':
        if str(message.chat.id) == str('584429967'):
            bot.send_chat_action(str(message.chat.id), 'typing')
            df = db1()
            df1 = dbp1()
            #time.sleep()
            with open('db1.txt', 'rb') as f:
                bot.send_document(chat_id=584429967, document=f)
            bot.send_message('584429967','Database : \n'+str(df))
            bot.send_message('584429967','Parameters : \n'+str(df1))
        else:
            return 0

    elif str(message.text) == '/status':
        a = status(str(message.chat.id))
        bot.send_message((message.chat.id),'Your status is : '+str(a))

    elif str(message.text) == '/balance':
        bal = lookup('MID','BAL',message.chat.id)
        bot.send_message((message.chat.id),'𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗯𝗮𝗹𝗮𝗻𝗰𝗲 : '+str(bal))
    elif str(message.text) == '/usage':
        msgout = lookup('MID','MSGOUT',message.chat.id)
        msgin = lookup('MID','MSGIN',message.chat.id)
        bot.send_message((message.chat.id),'𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝘀𝗲𝗻𝘁 : '+str(msgout)+'\n𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗿𝗲𝗰𝗲𝗶𝘃𝗲𝗱 : '+str(msgin))
    elif str(message.text) == '/anony_name':
        try:
            A1a = get((finder('ID',int(message.chat.id))),'Nickname')
            A1b = get((finder('ID',int(message.chat.id))),'Peer')
            A1c = get((finder('ID',int(A1b))),'Nickname')
            if A1b == 0 :
                bot.send_message((message.chat.id),'𝗬𝗼𝘂𝗿 𝗮𝗻𝗼𝗻𝘆𝗺𝗼𝘂𝘀 𝗻𝗮𝗺𝗲 𝗶𝘀: '+str(A1a))
            else:
                bot.send_message((message.chat.id),'𝗬𝗼𝘂𝗿 𝗮𝗻𝗼𝗻𝘆𝗺𝗼𝘂𝘀 𝗻𝗮𝗺𝗲 𝗶𝘀: '+str(A1a)+"\n𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿'𝘀 𝗮𝗻𝗼𝗻𝘆𝗺𝗼𝘂𝘀 𝗻𝗮𝗺𝗲 𝗶𝘀: "+str(A1c))
        except:
                bot.send_message((message.chat.id),'𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘄𝗶𝘁𝗵 𝘂𝘀 !!')

    elif str(message.text) == '/contactus':
        bot.send_chat_action(str(message.chat.id), 'typing')
        a = status(str(message.chat.id))
        msgcont = bot.send_message((message.chat.id),'Click to below link to contact us : \nhttps://bit.ly/m/AnonymousChats')
        time.sleep(5)
        bot.delete_message(message.chat.id, msgcont.message_id)

    elif str(message.text) == '/test00':
        try:
            print(SignalWrite((message.chat.id),0,0))
        except Exception as e:
            print (e)
            bot.send_message(('584429967','Error :/'+str(e)))

    elif str(message.text) == '/test01':
        try:
            print(SignalWrite((message.chat.id),0,1))
        except Exception as e:
            print (e)
            bot.send_message(('584429967','Error :/'+str(e)))

    elif str(message.text) == '/broadcasting':
        a = (broadcast('info_files/Broadcasting/test.txt'))
    elif str(message.text) == '/test01':
        try:
            print(SignalWrite((message.chat.id),0,1))
        except Exception as e:
            print (e)
            bot.send_message(('584429967','Error :/'+str(e)))

    elif str(message.text) == '/broadcasting':
        a = (broadcast('info_files/Broadcasting/test.txt'))
        bot.send_message('584429967','Number of subscribers :'+str(a))

    elif str(message.text) == '/broadcastingIDs':
        a = (broadcast('info_files/Broadcasting/test.txt'))
        #broadcastIDs(
        b = 0
        while b <= a :
            b+=1
            print(b)
            #print(subscribers_ID(Broadcast_list,b-1))
            #broadcastIDs('info_files/Broadcasting/test.txt',b-1)
            if b == a:
                bot.send_message('584429967','Subscriber no '+str(b)+' is :'+str(broadcastIDs('info_files/Broadcasting/test.txt',b)))
                bot.send_message('584429967','Total of Subscribers :'+str(a))
                break
            else:
                bot.send_message('584429967','Subscriber no '+str(b)+' is :'+str(broadcastIDs('info_files/Broadcasting/test.txt',b)))


    elif str(message.text) == '/test02':
        try:
            print(SignalRead((message.chat.id),0))
        except Exception as e:
            print (e)
            bot.send_message(('584429967','Error :/'+str(e)))

    elif str(message.text) == '/test03':
        context.bot.answer_callback_query(callback_query_id=query.id, text='you chose cat', show_alert=True)


    elif str(message.text) == '/dbstart':
        exec(open('db_manager.py').read())
        bot.send_message(('584429967','db Mamager started !!'))


    elif str(message.text)[0:3] == '/ls':
        try:
            if str(message.chat.id) == '584429967':
                path1 = str(message.text)[3:20].strip()
                print(path1)
                pthmsg = listfiles(path1)
                print(pthmsg)
                bot.send_message('584429967',str(pthmsg))
            else:
                return 0
        except Exception as e:
                bot.send_message('584429967','Error:/'+str(e))

    elif str(message.text)[0:4] == '/msg':
        if str(message.chat.id) == '584429967':
            try:
                print (str(message.text))
                parts = str(message.text).split(":")
                bot.send_message(parts[1],parts[2])
                bot.send_message('584429967','✅  Message sent!')
            except Exception as e:
                bot.send_message('584429967','❌  Failed to send!!'+str(e))
        else:
            return 0

    elif str(message.text)[0:4] == '/fem':
        if str(message.chat.id) == '584429967':
            try:
                print (str(message.text))
                parts = str(message.text).split(":")
                anych_para_modify('CEN',0,parts[1])
                anych_para_modify('CEN',0,parts[2])
                anych_para_modify('NTI',0,parts[1])
                anych_para_modify('NTI',0,parts[2])
                bot.send_message('584429967','✅  Messages change to feminine !!')
            except Exception as e:
                bot.send_message('584429967','❌  Messages change to feminine failed')
        else:
            return 0

    elif str(message.text)[0:5] == '/xfem':
        if str(message.chat.id) == '584429967':
            try:
                print (str(message.text))
                parts = str(message.text).split(":")
                anych_para_modify('CEN',1,parts[1])
                anych_para_modify('CEN',1,parts[2])
                anych_para_modify('NTI',0,parts[1])
                anych_para_modify('NTI',0,parts[2])
                bot.send_message('584429967','✅  Messages change to original!!')
            except Exception as e:
                bot.send_message('584429967','❌  Messages change to original! failed!')
        else:
            return 0


    elif str(message.text)[0:4] == '/ad1':
        if str(message.chat.id) == '584429967':
            msg = str(message.text)[5:1000]
            df = pd.read_csv('info_files/Anonychatdb01.2.csv')

            # Get the number of rows in the DataFrame
            num_ids = len(df)
            # Loop through each row of the DataFrame
            a=0
            for i in range(num_ids):
                try:
                    # Get the ID from the 'ID' column of the current row
                    id_num = df.loc[i, 'ID']
                    # Print the message with the current ID number

                    bot.send_message(int(id_num),str(msg))
                    print(f"Hello--{id_num}")
                except Exception as e:
                    print(e)
                    a-=1
                    #A1a = (finder('ID',int(id_num)))
                    #A1b = (finder('Peer',int(A1a)))
                    #anych_modify('Status','waiting',int(str(A1b)))
                    #bot.send_message(str(A1b),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                    df.drop(df.loc[df['ID'] == str(id_num)].index, inplace=True)
                    df.to_csv('info_files/Anonychatdb01.2.csv', index=False)
                    bot.send_message('584429967',f"❌  User {id_num} is unreachable")

            # Print the total number of IDs in the DataFrame
            usert = num_ids + a
            print(f"Message send to number of Users: {num_ids}")
            bot.send_message('584429967',f"Message send to number of Users: {usert}")
        else:
            return 0
    elif str(message.text)[0:3] == '/ad':
        if str(message.chat.id) == '584429967':
            msg = str(message.text)[4:1000]
            df = db()
            # Get the number of rows in the DataFrame
            num_ids = len(df)
            # Loop through each row of the DataFrame
            a=0
            for i in range(num_ids):
                try:
                    # Get the ID from the 'ID' column of the current row
                    id_num = df.loc[i, 'ID']
                    # Print the message with the current ID number

                    bot.send_message(int(id_num),str(msg))
                    print(f"Hello--{id_num}")
                except Exception as e:
                    print(e)
                    a-=1
                    #A1a = (finder('ID',int(id_num)))
                    #A1b = (finder('Peer',int(A1a)))
                    #anych_modify('Status','waiting',int(str(A1b)))
                    #bot.send_message(str(A1b),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                    df.drop(df.loc[df['ID'] == str(id_num)].index, inplace=True)
                    df.to_csv('info_files/Anonychatdb01.2.csv', index=False)
                    bot.send_message('584429967',f"❌  User {id_num} is unreachable")

            # Print the total number of IDs in the DataFrame
            usert = num_ids + a
            print(f"Message send to number of Users: {num_ids}")
            bot.send_message('584429967',f"Message send to number of Users: {usert}")
        else:
            return 0


    elif str(message.text)[0:6] == '/stchg':
        if str(message.chat.id) == '584429967':
            try:
                df = db()
                bot.send_message('584429967','Before'+str(df))
                conn = sqlite3.connect('Anonychatdb_5.0v.db')
                c = conn.cursor()
                c.execute("UPDATE my_table SET Status = 'waiting' WHERE Status = 'closed'")
                conn.commit()
                conn.close()
                df2 = db()
                df2 = db()
                bot.send_message('584429967','After'+str(df2))
                bot.send_message('584429967','✅ All closed changes to waiting !!')
            except Exception as e:
                print('stchg error :/ '+str(e))
                bot.send_message('584429967','stchg error :/ '+str(e))
        else:
            return 0


    elif str(message.text)[0:4] == '/pvt':
        peercheck = get((finder('ID',int(message.chat.id))),'Peer')
        Anonycheck = get((finder('ID',int(message.chat.id))),'AnonyID')
        OTPcheck = get((finder('ID',int(message.chat.id))),'OTP')
        D1 = str(message.text)[-12:]
        D2 = str(message.text)[10:14]
        D3 = (finder('OTP',int(D2)))
        D4 = (finder('AnonyID',int(D1)))
        print ("Checking D1: "+str(D1))
        print ("Checking D2: "+str(D2))
        print ("Checking D3: "+str(D3))
        print ("Checking D4: "+str(D4))
        if str(D2) == str(OTPcheck):
                bot.send_chat_action(str(message.chat.id), 'typing')
                msgslflk = bot.send_message((message.chat.id), '❌ 𝗬𝗼𝘂 𝗰𝗮𝗻𝗻𝗼𝘁 𝘂𝘀𝗲 𝘀𝗲𝗹𝗳 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 𝗹𝗶𝗻𝗸 !!')
                time.sleep(2)
                bot.delete_message(message.chat.id, msgslflk.message_id)
        elif str(D1) == str(Anonycheck):
                bot.send_chat_action(str(message.chat.id), 'typing')
                msgslflk = bot.send_message((message.chat.id), '❌ 𝗬𝗼𝘂 𝗰𝗮𝗻𝗻𝗼𝘁 𝘂𝘀𝗲 𝘀𝗲𝗹𝗳 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 𝗹𝗶𝗻𝗸 !!')
                time.sleep(2)
                bot.delete_message(message.chat.id, msgslflk.message_id)
        elif str(D3) == 'not found' and str(D4) == 'not found':
                bot.send_chat_action(str(message.chat.id), 'typing')
                msgslflk = bot.send_message((message.chat.id), '⚠️ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗹𝗶𝗻𝗸 !!')
                time.sleep(2)
                bot.delete_message(message.chat.id, msgslflk.message_id)
        else:
            msgCON1 = bot.send_message((message.chat.id), '⏳ 𝗩𝗲𝗿𝗶𝗳𝘆𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗹𝗶𝗻𝗸 !!')
            getpeer = get((D4),'ID')
            print(str(str(D2)+str(D1)))
            print('matching')
            print(str(str(get(finder('ID',get((D4),'ID')),'OTP'))+str(get(finder('ID',get((D4),'ID')),'AnonyID'))))
            if str(str(D2)+str(D1)) == str(str(get(finder('ID',get((D4),'ID')),'OTP'))+str(get(finder('ID',get((D4),'ID')),'AnonyID'))):
                if str(peercheck) != "0":
                    statuscheck = get((finder('ID',int(message.chat.id))),'Status')
                    if str(statuscheck) == "linked" and str(D1) != str(get((finder('ID',int(peercheck))),'AnonyID')):
                        bot.send_message(str(message.chat.id),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                        bot.send_message(str(peercheck), "❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                        anych_modify('Status','waiting',int(str(peercheck)))
                        bot.send_message(str(peercheck), "🔍 𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝗳𝗼𝗿 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 !!")
                        anych_modify('Peer',0,int(peercheck))
                        anych_modify('OTP',0,int(peercheck))
                    elif str(statuscheck) == "linked" and str(D1) == str(get((finder('ID',int(peercheck))),'AnonyID')) :
                        bot.send_message(str(message.chat.id),"⚠️ 𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝘄𝗶𝘁𝗵 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝗿𝗮𝗻𝗱𝗼𝗺 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗰𝗵𝗮𝗻𝗴𝗲𝗱 𝘁𝗼 '𝗽𝗿𝗶𝘃𝗮𝘁𝗲' !!")
                        bot.send_message(str(peercheck), "⚠️ 𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝘄𝗶𝘁𝗵 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝗿𝗮𝗻𝗱𝗼𝗺 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗰𝗵𝗮𝗻𝗴𝗲𝗱 𝘁𝗼 '𝗽𝗿𝗶𝘃𝗮𝘁𝗲' !!")
                    elif str(get((finder('ID',int(message.chat.id))),'AnonyID')) == 'closed' or str(get((finder('ID',int(message.chat.id))),'AnonyID')) == 'waiting':
                        msgpvt1 = bot.send_message(str(message.chat.id),"⚠️ 𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝗰𝗵𝗮𝗻𝗴𝗲𝗱 𝘁𝗼 '𝗽𝗿𝗶𝘃𝗮𝘁𝗲' !!")
                    else:
                        bot.send_message(str(peercheck),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                        anych_modify('Status','closed',int(peercheck))
                        anych_modify('tout',1728,int(peercheck))
                        print('')
                    #bot.send_message(str(message.chat.id),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                #elif str(D2)+str(D1) == str(get(finder('ID',get((D4),'ID')),'OTP'))+str(get(finder('ID',get((D4),'ID')),'AnonyID'))
                else:
                    print('no peer')
                getpeer = get((D4),'ID')
                print('getpeer is :'+str(getpeer))
                anych_modify('Status','private',int(str(message.chat.id)))
                anych_modify('tout',10000,int(str(message.chat.id)))
                anych_modify('Peer',str(getpeer),int(message.chat.id))
                anych_modify('Status','private',int(str(getpeer)))
                anych_modify('Peer',str(message.chat.id),int(getpeer))
                anych_modify('OTP',0,int(getpeer))
                anych_modify('OTP',0,int(message.chat.id))
                #msgCON = bot.send_message((message.chat.id), '✅  𝗔𝘂𝘁𝗵𝗲𝗻𝘁𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗱𝗼𝗻𝗲 !!')
                msgCON = bot.edit_message_text('✅  𝗔𝘂𝘁𝗵𝗲𝗻𝘁𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗱𝗼𝗻𝗲 !!', message.chat.id, msgCON1.message_id)
                time.sleep(1)
                msgpvt1 = bot.edit_message_text('𝗬𝗼𝘂 𝗮𝗿𝗲 𝐧𝐨𝐰 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝘂𝘀𝗶𝗻𝗴 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗹𝗶𝗻𝗸 !!', message.chat.id, msgCON.message_id)
                msgpvt2 = bot.send_message(str(getpeer), '𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗻𝗼𝘄 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗹𝗶𝗻𝗸 !!')
                time.sleep(5)
                bot.delete_message(message.chat.id, msgpvt1.message_id)
                bot.delete_message(str(getpeer), msgpvt2.message_id)

            else:
                msgCON = bot.edit_message_text( '⚠️ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗹𝗶𝗻𝗸 !!',message.chat.id, msgCON1.message_id)
                time.sleep(2)
                bot.delete_message(message.chat.id, msgCON.message_id)




    elif str(message.text)[0:4] == '/brc':
        bot.send_chat_action(str(message.chat.id), 'typing')
        mid = str(message.chat.id)
        a = find(mid)
        #print('finder result : '+str(a))
        if a == 'not found':
            msgcon = bot.send_message(message.chat.id, "𝚈𝚘𝚞𝚛 𝙸𝙳 𝚒𝚜 𝚗𝚘𝚝 𝚛𝚎𝚐𝚒𝚜𝚝𝚎𝚛𝚎𝚍!!\n\n𝙿𝚕𝚎𝚊𝚜𝚎 𝚠𝚊𝚒𝚝 𝚠𝚑𝚒𝚕𝚎 𝚛𝚎𝚐𝚒𝚜𝚝𝚛𝚊𝚝𝚒𝚘𝚗 𝚒𝚗 𝚙𝚛𝚘𝚐𝚛𝚎𝚜𝚜!!")
            a = reg(str(message.chat.id))
            with open('Anonychat_reg_logs.txt', 'a') as f:
                print('USER Registered : cID('+str(message.chat.id)+') : nID('+str(message.from_user.first_name)+') : tIN('+str(timestemp())+')', file=f)
            bot.send_message('584429967', 'USER Registered: '+str(message.from_user.first_name))
            time.sleep(2)
            msgcon2 = bot.edit_message_text(str(a), message.chat.id, msgcon.message_id)
            time.sleep(1)
            msgcon3 = bot.edit_message_text('𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚠𝚒𝚕𝚕 𝚜𝚝𝚊𝚋𝚕𝚒𝚜𝚑𝚎𝚍 𝚒𝚗 𝚊 𝚠𝚑𝚒𝚕𝚎 𝚊𝚏𝚝𝚎𝚛 𝚟𝚎𝚛𝚒𝚏𝚒𝚌𝚊𝚝𝚒𝚘𝚗...' , message.chat.id, msgcon2.message_id)
            time.sleep(2)
            bot.delete_message(message.chat.id, msgcon3.message_id)

        else:
            print('')
        #print('brc')
        D = str(message.text)[10:22]
        #print(D)
        D0 = len(str(message.text))
        #print(D0)
        D1 = str(message.text)[22:(D0-6)]
        #print(D1)
        #print(str(D))
        #print(len(str(D)))
        if D == "-":
            msgAU = bot.send_message((message.chat.id), '⚠️ 𝙸𝚗𝚟𝚊𝚕𝚒𝚍 𝚕𝚒𝚗𝚔')
            time.sleep(2)
            bot.delete_message(message.chat.id, msgAU.message_id)
        elif len(str(message.text)) > 28:
            try:
                broadcastlist = "info_files/Broadcasting/Broadcasting_"+str(D)+str(D1)+".txt"
                a = (broadcast(broadcastlist))
                if os.path.exists(broadcastlist):
                    D2 = 'OK'
                    print("Authentic Broadcast Link")
                elif a  == 20:
                    msgCON = bot.send_message((message.chat.id), '⚠️  𝗧𝗵𝗶𝘀 𝗯𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁𝗲𝗿 𝗵𝗮𝘃𝗲 𝗻𝗼 𝗳𝗿𝗲𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗿 𝘀𝗹𝗼𝘁 !!')
                    msgCON = bot.send_message((message.chat.id), '❌ ️  𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗿 𝘀𝗹𝗼𝘁 𝗶𝘀 𝗳𝘂𝗹𝗹 !!')
                else:
                    D2 = 'NOT OK'
                    print("File not found")
            except Exception as e :
                msgAU = bot.send_message((message.chat.id), '⚠️ 𝗟𝗶𝗻𝗸 𝗲𝗿𝗿𝗼𝗿 !!')
                #time.sleep(2)
                #bot.delete_message(message.chat.id, msgAU.message_id)
            #D2 = auth(D,int(D1))
            #print(D2)
            #print (str(D))
            #print (str(D1))
            A1a = finder('ID',int(message.chat.id))
            A1b = get((A1a),'AnonyID')
            #print(A1b)
            if str(D1) == str(message.chat.id):
                msgslflk = bot.send_message((message.chat.id), '❌ 𝗬𝗼𝘂 𝗰𝗮𝗻𝗻𝗼𝘁 𝘂𝘀𝗲 𝘀𝗲𝗹𝗳 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 𝗹𝗶𝗻𝗸 !!')
                time.sleep(2)
                bot.delete_message(message.chat.id, msgslflk.message_id)
            else:
                if D2 == 'OK':
                    msgCON = bot.send_message((message.chat.id), '✅  𝗟𝗶𝗻𝗸 𝗮𝘂𝘁𝗵𝗲𝗻𝘁𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗱𝗼𝗻𝗲 !!')
                    C1a = finder('AnonyID',int(D1))
                    C1b = get((C1a),'ID')
                    #print ('C1a : '+str(C1a))
                    #print ('C1b : '+str(C1b))

                    with open(broadcastlist, "r") as f:
                        for line in f:
                            if str(message.chat.id) in line:
                                print("You have already subscribed")
                                #break
                        else:
                            print("New subscriber!!")
                            with open(broadcastlist, 'a') as f:
                                print(str(message.chat.id), file=f)
                    anych_modify('Peer',str(D)+str(D1),int(str(message.chat.id)))
                    anych_modify('tout',120,int(str(message.chat.id)))
                    anych_modify('Status','subscriber',int(str(message.chat.id)))
                    #anych_modify('OTP',0,int(C1b))
                    #anych_modify('Status','subscriber',int(C1b))
                    msgpvt2 = bot.send_message(str(D1), '✅ 𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝗻𝗲𝘄 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗿 !!\n\nTotal Subscribers:' +(str(a+1)+'/20'))

                    msgpvt1 = bot.edit_message_text('✅ 𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝘁𝗼 𝘁𝗵𝗲 𝗯𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁𝗲𝗿 !!', message.chat.id, msgCON.message_id)

                    time.sleep(5)
                    #bot.delete_message(message.chat.id, msgpvt2.message_id)
                    #bot.delete_message(str(C1b), msgpvt2.message_id)
                    #print('Peer 2 done')

                elif D2 == 'NOT OK':
                    msgAU1 = bot.send_message((message.chat.id), '❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗹𝗶𝗻𝗸 !!')
                    time.sleep(2)
                    bot.delete_message(message.chat.id, msgAU1.message_id)
                else:
                    msgAU = bot.send_message((message.chat.id), '⚠️𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝗮𝘂𝘁𝗵𝗲𝗻𝘁𝗶𝗰𝗮𝘁𝗲.\n\n𝗟𝗶𝗻𝗸 𝗺𝗶𝗴𝗵𝘁 𝗯𝗲 𝗶𝗻𝘃𝗮𝗹𝗶𝗱 𝗼𝗿 𝗲𝘅𝗽𝗶𝗿𝗲𝗱.')
                    time.sleep(2)
                    bot.delete_message(message.chat.id, msgAU.message_id)

        else:
            msgAU = bot.send_message((message.chat.id), '⚠️ 𝗟𝗶𝗻𝗸 𝗲𝗿𝗿𝗼𝗿 !!')
            time.sleep(2)
            bot.delete_message(message.chat.id, msgAU.message_id)

    elif str(message.text)[0:4] == '/prm':
        bot.send_chat_action(str(message.chat.id), 'typing')
        mid = str(message.chat.id)
        a = find(mid)
        #print('finder result : '+str(a))
        if a == 'not found':
            msgcon = bot.send_message(message.chat.id, "𝚈𝚘𝚞𝚛 𝙸𝙳 𝚒𝚜 𝚗𝚘𝚝 𝚛𝚎𝚐𝚒𝚜𝚝𝚎𝚛𝚎𝚍!!\n\n𝙿𝚕𝚎𝚊𝚜𝚎 𝚠𝚊𝚒𝚝 𝚠𝚑𝚒𝚕𝚎 𝚛𝚎𝚐𝚒𝚜𝚝𝚛𝚊𝚝𝚒𝚘𝚗 𝚒𝚗 𝚙𝚛𝚘𝚐𝚛𝚎𝚜𝚜!!")
            a = reg(str(message.chat.id))
            with open('Anonychat_reg_logs.txt', 'a') as f:
                print('USER Registered : cID('+str(message.chat.id)+') : nID('+str(message.from_user.first_name)+') : tIN('+str(timestemp())+')', file=f)
            bot.send_message('584429967', 'USER Registered: '+str(message.from_user.first_name))
            time.sleep(2)
            msgcon2 = bot.edit_message_text(str(a), message.chat.id, msgcon.message_id)
            time.sleep(1)
            msgcon3 = bot.edit_message_text('𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚠𝚒𝚕𝚕 𝚜𝚝𝚊𝚋𝚕𝚒𝚜𝚑𝚎𝚍 𝚒𝚗 𝚊 𝚠𝚑𝚒𝚕𝚎 𝚊𝚏𝚝𝚎𝚛 𝚟𝚎𝚛𝚒𝚏𝚒𝚌𝚊𝚝𝚒𝚘𝚗...' , message.chat.id, msgcon2.message_id)
            time.sleep(2)
            bot.delete_message(message.chat.id, msgcon3.message_id)

        else:
            print('')
        print('prm')
        D = str(message.text)[10:14]
        #print(D)
        D1 = str(message.text)[20:35]
        #print(D1)
        #print(str(D))
        #print(len(str(D)))
        if D == "-":
            msgAU = bot.send_message((message.chat.id), '⚠️ 𝙸𝚗𝚟𝚊𝚕𝚒𝚍 𝚕𝚒𝚗𝚔')
            time.sleep(2)
            bot.delete_message(message.chat.id, msgAU.message_id)
        elif len(str(D)) == 4:
            D2 = auth(D,int(D1))
            #print(D2)
            #print (str(D))
            #print (str(D1))
            A1a = finder('ID',int(message.chat.id))
            A1b = get((A1a),'AnonyID')
            #print(A1b)
            if str(D1) == str(A1b):
                msgslflk = bot.send_message((message.chat.id), '𝚈𝚘𝚞 𝚌𝚊𝚗 𝚗𝚘𝚝 𝚞𝚜𝚎 𝚜𝚎𝚕𝚏 𝚐𝚎𝚗𝚎𝚛𝚊𝚝𝚎𝚍 𝚕𝚒𝚗𝚔!!\n\n𝙿𝚕𝚎𝚊𝚜𝚎 𝚙𝚊𝚜𝚜 𝚒𝚝 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚙𝚊𝚛𝚝𝚗𝚎𝚛 𝚘𝚛 𝚐𝚎𝚝 𝚕𝚒𝚗𝚔 𝚏𝚛𝚘𝚖 𝚢𝚘𝚞𝚛 𝚙𝚊𝚛𝚝𝚗𝚎𝚛!!')
                time.sleep(2)
                bot.delete_message(message.chat.id, msgslflk.message_id)
            else:
                if D2 == 'OK':
                    msgCON = bot.send_message((message.chat.id), '✅  𝙰𝚞𝚝𝚑𝚎𝚗𝚝𝚒𝚌𝚊𝚝𝚒𝚘𝚗 𝚍𝚘𝚗𝚎 !!')
                    time.sleep(1)
                    C1a = finder('AnonyID',int(D1))
                    C1b = get((C1a),'ID')
                    #print ('C1a : '+str(C1a))
                    #print ('C1b : '+str(C1b))
                    anych_modify('Peer',str(C1b),int(message.chat.id))
                    #print('Peer 1 done')
                    anych_modify('tout',120,int(C1b))
                    anych_modify('Peer',str(message.chat.id),int(C1b))
                    anych_modify('tout',120,int(str(message.chat.id)))
                    anych_modify('Status','permanent',int(str(message.chat.id)))
                    anych_modify('OTP',0,int(C1b))
                    anych_modify('Status','permanent',int(C1b))
                    msgpvt1 = bot.edit_message_text('𝚈𝚘𝚞 𝚊𝚛𝚎 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚎𝚍 𝚠𝚒𝚝𝚑 𝚙𝚊𝚛𝚝𝚗𝚎𝚛 𝚗𝚘𝚠!!\n\n𝙵𝚛𝚘𝚖 𝚗𝚘𝚠 𝚊𝚕𝚕 𝚢𝚘𝚞𝚛 𝚖𝚎𝚜𝚜𝚊𝚐𝚎𝚜 𝚠𝚒𝚕𝚕 𝚜𝚎𝚗𝚍 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚙𝚊𝚛𝚝𝚗𝚎𝚛 𝚍𝚒𝚛𝚎𝚌𝚝𝚕𝚢 𝚊𝚗𝚍 𝚙𝚛𝚒𝚟𝚊𝚝𝚎𝚕𝚢 !!', message.chat.id, msgCON.message_id)
                    msgpvt2 = bot.send_message(str(C1b), '𝙿𝚎𝚎𝚛 𝚒𝚜 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚎𝚍 𝚞𝚜𝚒𝚗𝚐 𝚢𝚘𝚞𝚛 𝚕𝚒𝚗𝚔!!\n\n𝙵𝚛𝚘𝚖 𝚗𝚘𝚠 𝚊𝚕𝚕 𝚢𝚘𝚞𝚛 𝚖𝚎𝚜𝚜𝚊𝚐𝚎𝚜 𝚠𝚒𝚕𝚕 𝚜𝚎𝚗𝚍 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚙𝚊𝚛𝚝𝚗𝚎𝚛 𝚍𝚒𝚛𝚎𝚌𝚝𝚕𝚢 𝚊𝚗𝚍 𝚙𝚛𝚒𝚟𝚊𝚝𝚎𝚕𝚢 !!')
                    time.sleep(5)
                    msgpvt2a = bot.edit_message_text('𝚈𝚘𝚞𝚛 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 𝚜𝚝𝚒𝚕𝚕 𝚑𝚊𝚟𝚒𝚗𝚐 𝚕𝚒𝚖𝚒𝚝𝚎𝚍 𝚕𝚎𝚊𝚜𝚎 𝚊𝚗𝚍 𝚠𝚒𝚕𝚕 𝚋𝚎 𝚍𝚒𝚜𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚎𝚍 𝚒𝚏 𝚒𝚗𝚊𝚌𝚝𝚒𝚟𝚎 𝚏𝚘𝚛 𝟺𝚖𝚒𝚗 (𝚏𝚛𝚘𝚖 𝚛𝚎𝚌𝚎𝚒𝚟𝚎𝚛 𝚘𝚛 𝚜𝚎𝚗𝚍𝚎𝚛). 𝚄𝚜𝚎 𝚙𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚕𝚒𝚗𝚔 𝚏𝚘𝚛 𝟷𝚖𝚘𝚗𝚝𝚑 𝚕𝚎𝚊𝚜𝚎𝚍 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗.', message.chat.id, msgpvt1.message_id)
                    msgpvt2b = bot.edit_message_text('𝚈𝚘𝚞𝚛 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗 𝚜𝚝𝚒𝚕𝚕 𝚑𝚊𝚟𝚒𝚗𝚐 𝚕𝚒𝚖𝚒𝚝𝚎𝚍 𝚕𝚎𝚊𝚜𝚎 𝚊𝚗𝚍 𝚠𝚒𝚕𝚕 𝚋𝚎 𝚍𝚒𝚜𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚎𝚍 𝚒𝚏 𝚒𝚗𝚊𝚌𝚝𝚒𝚟𝚎 𝚏𝚘𝚛 𝟺𝚖𝚒𝚗 (𝚏𝚛𝚘𝚖 𝚛𝚎𝚌𝚎𝚒𝚟𝚎𝚛 𝚘𝚛 𝚜𝚎𝚗𝚍𝚎𝚛). 𝚄𝚜𝚎 𝚙𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚕𝚒𝚗𝚔 𝚏𝚘𝚛 𝟷𝚖𝚘𝚗𝚝𝚑 𝚕𝚎𝚊𝚜𝚎𝚍 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗.', str(C1b), msgpvt2.message_id)
                    time.sleep(5)
                    bot.delete_message(message.chat.id, msgpvt2a.message_id)
                    bot.delete_message(str(C1b), msgpvt2b.message_id)
                    #print('Peer 2 done')

                elif D2 == 'NOT OK':
                    msgAU1 = bot.send_message((message.chat.id), '❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗹𝗶𝗻𝗸 !!')
                    time.sleep(2)
                    bot.delete_message(message.chat.id, msgAU1.message_id)
                else:
                    msgAU = bot.send_message((message.chat.id), '⚠️𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝗮𝘂𝘁𝗵𝗲𝗻𝘁𝗶𝗰𝗮𝘁𝗲.\n\n𝗟𝗶𝗻𝗸 𝗺𝗶𝗴𝗵𝘁 𝗯𝗲 𝗶𝗻𝘃𝗮𝗹𝗶𝗱 𝗼𝗿 𝗲𝘅𝗽𝗶𝗿𝗲𝗱.')
                    time.sleep(2)
                    bot.delete_message(message.chat.id, msgAU.message_id)

        else:
            msgAU = bot.send_message((message.chat.id), '⚠️ 𝗟𝗶𝗻𝗸 𝗲𝗿𝗿𝗼𝗿 !!')
            time.sleep(2)
            bot.delete_message(message.chat.id, msgAU.message_id)



    elif str(message.text)[0] == '/':
        bot.send_chat_action(str(message.chat.id), 'typing')
        msgUN1 = bot.send_message((message.chat.id), '❌  𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗰𝗼𝗺𝗺𝗮𝗻𝗱')
        time.sleep(2)
        bot.delete_message(message.chat.id, msgUN1.message_id)

    else:
        D1a = finder('ID',int(message.chat.id))
        #print ('D1a : '+str(D1a))
        D1b = get(D1a,'Peer')
        #print ('D1b : '+str(D1b))
        if D1b == '-invalid-':
            bot.send_chat_action(str(message.chat.id), 'typing')
            msgINV = bot.send_message((message.chat.id), "⚠️ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘂𝘀𝗲𝗿 𝗽𝗹𝗲𝗮𝘀𝗲 𝘁𝘆𝗽𝗲 /𝘀𝘁𝗮𝗿𝘁 𝘁𝗼 𝗲𝘅𝗽𝗹𝗼𝗿𝗲.")
            time.sleep(2)
            bot.delete_message(message.chat.id, msgINV.message_id)
        else:
            D1c = finder('ID',(D1b))
            D1d = get(D1c,'Status')
            D2ai = get(D1a,'Status')
            print('D2ai : '+str(D2ai))
            print('D1c : '+str(D1c))
            print('D1d : '+str(D1d))

        try:
            if str(D1d) == '-':
                msgdash = bot.send_message((message.chat.id), "⚠️ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝘄𝗶𝘁𝗵 𝗮𝗻𝘆 𝗽𝗮𝗿𝘁𝗻𝗲𝗿, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝗼𝗿 𝘁𝘆𝗽𝗲 /𝘀𝘁𝗮𝗿𝘁 𝘁𝗼 𝗲𝘅𝗽𝗹𝗼𝗿𝗲.")
                time.sleep(2)
                bot.delete_message(message.chat.id, msgdash.message_id)
            elif str(D1d) == 'not found':
                try:
                    anych_modify('Peer',0,int(str(message.chat.id)))
                    anych_modify('Status','closed',int(str(message.chat.id)))
                    anych_modify('OTP','-',int(str(message.chat.id)))
                    leasing(int(message.chat.id),1728)
                    mid = str(message.chat.id)
                except:
                    print("")
                msgntav = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗻𝗼𝘁 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 !!")
                time.sleep(2)
                bot.delete_message(message.chat.id, msgntav.message_id)
            elif str(D1d) == 'private':
                D2a = finder('ID',int(D1b))
                D2b = get((D2a),'tout')
                D2c = get((D2a),'Peer')
                E2a = finder('ID',int(D2c))
                E2b = get((E2a),'Peer')
                print ("===>>>"+str(D1b)+"======>>"+str(E2b))
                #print ('D2a : '+str(D2a))
                #print ('D2b : '+str(D2b))
                if int(D2b) <= 0 :
                    msgLE = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝗹𝗲𝗮𝘀𝗲 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝗱 !!")
                    time.sleep(2)
                    bot.delete_message(message.chat.id, msgLE.message_id)
                elif D1b != E2b :
                    msgpdc1a = bot.send_message(str((message.chat.id)),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                else:
                    anych_para_modify('BAL',(lookup('MID','BAL',message.chat.id))-0.5,message.chat.id)
                    anych_para_modify('MSGOUT',int(lookup('MID','MSGOUT',message.chat.id))+1,message.chat.id)
                    anych_para_modify('MSGIN',int(lookup('MID','MSGIN',int(D1b)))+1,int(D1b))
                    time.sleep(0)
                    bot.send_message(str(D1b), str(message.text))
                    leasing(int(message.chat.id),10000)
            elif str(D2ai) == 'broadcaster':
                try:
                    a = (broadcast('info_files/Broadcasting/test.txt'))
                    b = 0
                    while b <= a :
                        b+=1
                        print(b)
                        #print(subscribers_ID(Broadcast_list,b-1))
                        #broadcastIDs('info_files/Broadcasting/test.txt',b-1)
                        if b == a:
                            bot.send_message(str(broadcastIDs('info_files/Broadcasting/test.txt',b)),str(message.text))
                            bot.send_message('584429967','Message sent to '+str(a)+' Subscribers')
                            break
                        else:
                            bot.send_message(str(broadcastIDs('info_files/Broadcasting/test.txt',b)),str(message.text))
                except Exception as e:

                    print('Error to send broadcast message /:')
                    mesgUN = bot.send_message((message.chat.id), "❌ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 !!")
                    time.sleep(2)
                    bot.delete_message(message.chat.id, mesgUN.message_id)

            elif str(D2ai) == 'subscriber':
                    msgLE = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝘀𝘁𝗮𝘁𝘂𝘀 𝗶𝘀 '𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗿', 𝘆𝗼𝘂 𝗼𝗻𝗹𝘆 𝗰𝗮𝗻 𝗿𝗲𝗰𝗲𝗶𝘃𝗲 𝘁𝗵𝗲 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗳𝗿𝗼𝗺 𝘆𝗼𝘂𝗿 𝗯𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁𝗲𝗿!!")
                    #time.sleep(2)
                    #bot.delete_message(message.chat.id, msgLE.message_id)

            elif str(D1d) == 'nosub':
                mesgUN = bot.send_message((message.chat.id), "❌ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 !!")
                time.sleep(2)
                bot.delete_message(message.chat.id, mesgUN.message_id)

            elif str(D1d) == 'nosub':
                mesgUN = bot.send_message((message.chat.id), "❌ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 !!")
                time.sleep(2)
                bot.delete_message(message.chat.id, mesgUN.message_id)

            elif str(D1d) == 'permanent':
                D2a = finder('ID',int(D1b))
                D2b = get((D2a),'tout')
                #print ('D2a : '+str(D2a))
                #print ('D2b : '+str(D2b))
                if int(D2b) <= 0 :
                    msgLE = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝗹𝗲𝗮𝘀𝗲 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝗱 !!")
                    time.sleep(2)
                    bot.delete_message(message.chat.id, msgLE.message_id)
                else:
                    bot.send_chat_action(str(D1b), 'typing')
                    time.sleep(0)
                    anych_para_modify('BAL',(lookup('MID','BAL',message.chat.id))-0.5,message.chat.id)
                    anych_para_modify('MSGOUT',int(lookup('MID','MSGOUT',message.chat.id))+1,message.chat.id)
                    anych_para_modify('MSGIN',int(lookup('MID','MSGIN',int(D1b)))+1,int(D1b))
                    bot.send_message(str(D1b), str(message.text))
                    leasing(int(message.chat.id),120)
            elif str(D2ai) == 'paused':
                msgLE = bot.send_message((message.chat.id), "❌ 𝗦𝘆𝘀𝘁𝗲𝗺 𝗶𝘀 𝗯𝘂𝘀𝘆 !! 𝗣𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁!!")
                #time.sleep(2)
                #bot.delete_message(message.chat.id, msgLE.message_id)
            elif str(D2ai) == 'AI' or str(D2ai) == 'waiting':
                D2a = finder('ID',int(message.chat.id))
                D2b = get((D2a),'tout')
                print ('D2a : '+str(D2a))
                print ('D2b : '+str(D2b))
                if int(D2b) <= 0 :
                    msgLE = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝗔𝗜 𝗰𝗿𝗲𝗱𝗶𝘁 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗳𝗶𝗻𝗶𝘀𝗵𝗲𝗱 !!")
                    time.sleep(2)
                    bot.delete_message(message.chat.id, msgLE.message_id)
                else:
                    chtrecord(str(message.from_user.first_name),str(message.chat.id),str(message.text),str(message.chat.id))
                    anych_modify('Status','paused',int(str(message.chat.id)))
                    #time.slee�p(2)
                    resp = OPnAI(str(message.text))
                    bot.send_chat_action(str(message.chat.id), 'typing')
                    txtsp = (int(len(resp)))/48
                    bot.send_chat_action(str(message.chat.id), 'typing')
                    #bot.send_chat_action(str(message.chat.id), 'typing')
                    txtsp = (int(len(resp)))/48
                    bot.send_chat_action(str(message.chat.id), 'typing')
                    txtsp = (int(len(resp)))/48
                    bot.send_chat_action(str(message.chat.id), 'typing')
                    txtsp = (int(len(resp)))/48
                    #print (str(txtsp))
                    #print(str(resp))
                    bot.send_chat_action(str(message.chat.id), 'typing')
                    time.sleep(txtsp)
                    #print(str(resp))
                    chtrecord("AI","999",str(resp),str(message.chat.id))
                    bot.send_chat_action(str(message.chat.id), 'typing')
                    bot.send_message(str(message.chat.id), str(resp))
                    anych_modify('Status',str(D2ai),int(str(message.chat.id)))
                    #anych_para_modify('MSGOUT',int(lookup('MID','MSGOUT',message.chat.id))+1,message.chat.id)
                    #anych_para_modify('MSGIN',int(lookup('MID','MSGIN',int(A1a)))+1,int(A1a))
                    E1a = finder('ID',int(message.chat.id))
                    E2b = round(int(get((E1a),'tout')))
                    print(str(E2b))
                    if (E2b) == 1:
                        msgLE = bot.send_message((message.chat.id), "⚠️ 𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝗼𝗻𝗹𝘆 𝟭 𝗰𝗿𝗲𝗱𝗶𝘁 𝘁𝗼 𝗴𝗲𝘁 𝗔𝗜 𝗿𝗲𝘀𝗽𝗼𝗻𝘀𝗲 !!")
                        time.sleep(2)
                        bot.delete_message(message.chat.id, msgLE.message_id)
                        if str(message.chat.id) == '584429967':
                            leasing(int(message.chat.id),120)
                        else:
                            leasing(int(message.chat.id),(E2b)-24)
                    else:
                        if str(message.chat.id) == '584429967':
                            leasing(int(message.chat.id),120)
                        else:
                            leasing(int(message.chat.id),(E2b)-24)

            elif str(D1d) != 'linked':
                try:
                    A1a = finder('ID',int(message.chat.id))
                    A1b = get((A1a),'Peer')
                    A1bi = get((A1a),'Nickname')
                    B1a = finder('ID',int(A1b))
                    B1b = get((B1a),'Peer')
                    B1bi = get((B1a),'Nickname')
                    anych_modify('Peer',0,int(str(message.chat.id)))
                    anych_modify('Status','closed',int(str(message.chat.id)))
                    anych_modify('OTP','-',int(str(message.chat.id)))
                    anych_modify('Peer',0,int(A1b))
                    anych_modify('Status','closed',int(A1b))
                    anych_modify('OTP','-',int(A1b))
                    leasing(int(message.chat.id),1728)
                    leasing(int(A1b),1728)
                    #bot.send_message(str(message.chat.id),"Your peer is disconnected !!")
                    msgpdc1a = bot.send_message(str(A1b),"❌ 𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝘀 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 !!")
                    time.sleep(2)
                    bot.delete_message(message.chat.id, msgpdc1a.message_id)
                except Exception as e:
                        print(e)
                        anych_modify('Peer',0,int(str(message.chat.id)))
                        anych_modify('Status','closed',int(str(message.chat.id)))
                        anych_modify('OTP','-',int(str(message.chat.id)))
                        leasing(str(message.chat.id),1728)
                        mid = str(message.chat.id)
                msgpdc1a = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝗻𝗼𝘁 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 !!")
                time.sleep(2)
                bot.delete_message(message.chat.id, msgpdc1a.message_id)
            else:
                A1a = finder('ID',int(message.chat.id))
                A1b = str(get(A1a,'Peer'))
                VDOchk = lookup('MID','MSG',int(A1b))
                if VDOchk == 0:
                    bot.send_message((message.chat.id), "❌  𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗵𝗮𝘀 𝗯𝗹𝗼𝗰𝗸𝗲𝗱 𝘁𝗵𝗲 𝘁𝗲𝘅𝘁 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗿𝗲𝗰𝗲𝗶𝘃𝗶𝗻𝗴 !!")
                    bot.send_message((A1b), "❌  𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗮𝘁𝘁𝗲𝗺𝗽𝘁 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘆𝗼𝘂 𝗮 𝘁𝗲𝘅𝘁 𝗺𝗲𝘀𝘀𝗮𝗴𝗲! 𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝗮𝗯𝗹𝗲 𝘁𝗲𝘅𝘁 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗿𝗲𝗰𝗲𝗶𝘃𝗶𝗻𝗴 𝗳𝗿𝗼𝗺 𝘆𝗼𝘂𝗿 𝘀𝗲𝘁𝘁𝗶𝗻𝗴𝘀!!")
                else:
                    D2a = finder('ID',int(D1b))
                    D2b = get((D2a),'tout')
                    #print ('D2a : '+str(D2a))
                    #print ('D2b : '+str(D2b))
                    if int(D2b) == 'yo =0':
                        msgLE = bot.send_message((message.chat.id), "❌ 𝗬𝗼𝘂𝗿 𝗹𝗲𝗮𝘀𝗲 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝗱 !!")
                        time.sleep(2)
                        bot.delete_message(message.chat.id, msgLE.message_id)
                    else:
                        A1a = finder('ID',int(message.chat.id))
                        A1b = get((A1a),'Peer')
                        A1bi = get((A1a),'Nickname')
                        B1a = finder('ID',int(A1b))
                        B1b = get((B1a),'Peer')
                        B1bi = get((B1a),'Nickname')
                        bot.send_chat_action(int(D1b), 'typing')
                        time.sleep(2)
                        if (lookup('MID','CEN',int(A1b))) == 1  :
                            text = profanity.censor(str(message.text))
                            #bot.send_message((message.chat.id), "❌  𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗵𝗮𝘀 𝗯𝗹𝗼𝗰𝗸𝗲𝗱 𝘁𝗵𝗲 𝗼𝗯𝗷𝗲𝗰𝘁𝗶𝗼𝗻𝗮𝗯𝗹𝗲 𝘁𝗲𝘅𝘁 𝗿𝗲𝗰𝗲𝗶𝘃𝗶𝗻𝗴 !!")
                            #bot.send_message((A1b), "❌  𝗬𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗮𝘁𝘁𝗲𝗺𝗽𝘁 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘆𝗼𝘂 𝗮 𝗼𝗯𝗷𝗲𝗰𝘁𝗶𝗼𝗻𝗮𝗯𝗹𝗲 𝘁𝗲𝘅𝘁! 𝗜𝗳 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝘀𝗲𝗲 𝘂𝗻𝗰𝗲𝗻𝘀𝗼𝗿𝗲𝗱 𝘁𝗲𝘅𝘁 𝗽𝗹𝗲𝗮𝘀𝗲 𝗱𝗶𝘀𝗮𝗯𝗹𝗲 𝗰𝗲𝗻𝘀𝗼𝗿 𝗳𝗲𝗮𝘁𝘂𝗿𝗲 𝗳𝗿𝗼𝗺 𝘀𝗲𝘁𝘁𝗶𝗻𝗴𝘀")
                        elif (lookup('MID','NTI',int(A1b))) == 1 :
                            text = OPnAI('change my words to romatic words:'+str(message.text))
                            if text == '⚠️ 𝗔𝗜 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗼𝘃𝗲𝗿𝗹𝗼𝗮𝗱𝗲𝗱 !! \n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 𝗹𝗮𝘁𝗲𝗿!!':
                                text = "?"
                            else:
                                print('fem text sucessfully done!!')
                        else:
                            text = str(message.text)
                        anych_para_modify('BAL',(lookup('MID','BAL',message.chat.id))-0.5,message.chat.id)
                        anych_para_modify('MSGOUT',int(lookup('MID','MSGOUT',message.chat.id))+1,message.chat.id)
                        anych_para_modify('MSGIN',int(lookup('MID','MSGIN',int(D1b)))+1,int(D1b))
                        bot.send_message(int(D1b), text)
                        leasing(int(message.chat.id),120)
                        with open('info_files/chat_recorder.txt', 'a') as f:
                            print('Message from : ('+str(A1bi)+')-TO-('+str(B1bi)+')\n "'+str(message.text)+'" \n', file=f)
        except Exception as e:
            bot.send_chat_action(str(message.chat.id), 'typing')
            mesgUN = bot.send_message((message.chat.id), "❌ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 !!")
            time.sleep(2)
            bot.delete_message(message.chat.id, mesgUN.message_id)
            print(e)
bot.infinity_polling(interval=2, timeout=0)