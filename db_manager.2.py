try:
    import schedule
    import time
    import pandas as pd
    import array as arr
    import numpy as np
    import telebot
    import os
    import sys
    import csv
    import sqlite3
    import random
            


    bot = telebot.TeleBot("5768243722:AAGuPYWlGCH9x7I-N5bJ3u6royTuEfQ5ZFw")
    bot.send_message('584429967', '🌀Anonymous Chats DB Started!!')
    print('🌀Anonymous Chats DB Started!!')
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #                       Integer converter
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    def intconvert():
        try:
            # Connect to the database
            conn = sqlite3.connect('Anonychatdb_5.0v.db')
            c = conn.cursor()
            # Get the table and column names
            columns_to_convert = ('ID', 'tout', 'AnonyID', 'Peer', 'OTP', 'Timer')
            # Convert the specified columns to integers
            for col_name in columns_to_convert:
                c.execute(f"UPDATE my_table SET {col_name} = CAST({col_name} AS INTEGER)")
            # Commit the changes and close the connection
            conn.commit()
            conn.close()
            print ("🟢 Int conversion executed!!")
        except Exception as e:
            print ("🔴 Int conversion failed!! :/"+str(e))
    
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #                       Peering Task
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    
    def peering_task():
        print('=========================================')
        print('Peering task run at : '+str(timestemp()))
        print('=========================================')
        waiting()
        intconvert()
        #flush()
        try:
            u = (readytoconnect('waiting','Status'))
            o = (len(u))
            #print('o ='+str(o))
            mod = o % 2
            loc = True
            i = -1
            #print(mod)
            if o == 1 :
              print('🟠 no peer available')  
            else:
                if mod > 0:
                    #This is an odd number
                    while loc:
                        i += 1
                        peering(u[i],int(findpeer((u[o-2]))))
                        o -= 1
                        if o == 1 :
                            loc = False
                        else:
                            loc = True
                else:
                    while loc:
                        i += 1
                        peering(u[i],int(findpeer((u[o-1]))))
                        o -= 1
                        if o == 0 :
                            print('🟢 peering task completed')
                            loc = False
                        else:
                            loc = True
        except Exception as e:
            #print('error in peering() :\ '+str(e))
            if str(e) == 'list index out of range':
                print('🟠 No enrty available :\ '+str(e))
            else:
                print('Exception [24-52] /:'+str(e))
    def readytoconnect(S,refc):
        try:
            conn = sqlite3.connect('Anonychatdb_5.0v.db')
            c = conn.cursor()
            c.execute("SELECT Status FROM my_table")
            rows = c.fetchall()
            conn.close()
        
            indexes = [i for i, row in enumerate(rows) if row[0] == S]
            return indexes
        except Exception as e:
            return '[error]/:'+str(e)
    
    def findpeer(Q):
        try:
            conn = sqlite3.connect('Anonychatdb_5.0v.db')
            cursor = conn.cursor()
            cursor.execute(f"SELECT ID FROM my_table LIMIT 1 OFFSET ?", (Q,))
            row = cursor.fetchone()
            conn.close()
            if row is not None:
                return row[0]
            else:
                return None
        except Exception as e:
            print('error to find peer findpeer() \:'+str(e))
        
    def peering(R,PID):
        import telebot
        bot = telebot.TeleBot("5768243722:AAGuPYWlGCH9x7I-N5bJ3u6royTuEfQ5ZFw")
        #df = pd.read_csv('/code/Python_Lab/Anonychat/Anonychatdb01.2.csv')
        H = get(R,'ID')
        D1a = finder('ID',int(PID))
        D1b = get(D1a,'ID')
        D1c = get(D1a,'Status')
        E1a = finder('ID',D1b)
        E1b = get(E1a,'Status')
        E1c = get(H,'Nickname')
        print('PID : '+str(PID))
        print ('D1b : '+str(D1b))
        print ('D1c : '+str(D1c))
        print ('E1b : '+str(E1b))
        print ('E1c : '+str(E1c))
        print('H : '+str(H))
        
        try:
            #love_emojis = ['❤️', '💕', '💘', '💗', '💞', '💓', '💖', '💝', '👋', '😃', '😍', '🤠', '🤟', '🙌', '👏', '👁', '🔥', '😈', '😻', '🌹', '⚡️']
            love_emojis = ['✅']
            random_love_emoji = random.choice(love_emojis)
            bot.send_message(str(D1b), ' 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝘄𝗶𝘁𝗵 𝗻𝗲𝘄 𝗿𝗮𝗻𝗱𝗼𝗺 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 !! \n\n𝗙𝗿𝗼𝗺 𝗻𝗼𝘄 𝗮𝗹𝗹 𝘆𝗼𝘂𝗿 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝘄𝗶𝗹𝗹 𝗿𝗲𝗰𝗲𝗶𝘃𝗲𝗱 𝗯𝘆 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗱𝗶𝗿𝗲𝗰𝘁𝗹𝘆 !!')
            bot.send_message(str(D1b),random_love_emoji)
            bot.send_message(str(D1b), '𝗡𝗢𝗧𝗘 ‼️ : 𝗬𝗼𝘂 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝗳𝗿𝗼𝗺 𝘆𝗼𝘂𝗿 𝗰𝘂𝗿𝗿𝗲𝗻𝘁 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗶𝗳 𝘆𝗼𝘂 𝗼𝗿 𝘆𝗼𝘂𝗿 𝗽𝗮𝗿𝘁𝗻𝗲𝗿 𝗱𝗼 𝗻𝗼𝘁 𝗿𝗲𝘀𝗽𝗼𝗻𝗱 𝘄𝗶𝘁𝗵 𝗶𝗻 𝟭𝟬 𝗺𝗶𝗻𝘂𝘁𝗲𝘀!!!!')
            
        except Exception as e :
            print('peering function error :/ '+str(e))
            print(str(D1b)+' ID is unreachable Anony Manager will flush this ID')
            flushID(str(D1b))
            print(str(D1b)+' ID has been flushed!!')
        
        anych_modify('Peer',PID,H)
        anych_modify('Status','linked',H)
        

        
        
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #                       timestemp
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||     
    def timestemp():
        import time
        from datetime import datetime
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string
    
    
    
    def anych_modify(C,V,mid):
        try:
            conn = sqlite3.connect('Anonychatdb_5.0v.db')
            cursor = conn.cursor()
            cursor.execute(f"UPDATE my_table SET {C}=? WHERE ID=?", (V, mid))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
    
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #                       Find module
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def finder(C,Q):
        try:
            conn = sqlite3.connect('Anonychatdb_5.0v.db')
            cursor = conn.cursor()
            cursor1 = conn.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM my_table WHERE {C} < ?", (Q,))
            cursor1.execute(f"SELECT rowid FROM my_table WHERE {C} = ?", (Q,))
            row = cursor.fetchone()
            row1 = cursor1.fetchone()
            conn.close()
            if row1 is not None:
                return row[0]
            else:
                return "not found"
        except Exception as e:
            print(e)
    
    #print(finder('ID',int('2346439310')))
    
    
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #                       Get module
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    
    def get(index,C):
        try:
            conn = sqlite3.connect('Anonychatdb_5.0v.db')
            cursor = conn.cursor()
            cursor.execute(f"SELECT {C} FROM my_table LIMIT 1 OFFSET ?", (index,))
            row = cursor.fetchone()
            conn.close()
            if row is not None:
                return row[0]
            else:
                return None
        except Exception as e:
            print('failed to get() value \: '+str(e))
            
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #                       inspector
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    def inspector():
        global state
        cmd = 'ps -fA | grep python'
        x = os.popen(cmd)
        o = x.read()
        #print(o)
        x2 = str(o.find('Anonychat_bot.5.2.py'))
        #print('find :'+str(x2))
        try:
            global state
            import telebot
            bot = telebot.TeleBot('5768243722:AAGuPYWlGCH9x7I-N5bJ3u6royTuEfQ5ZFw')
            x3 = x2.isnumeric()
            if x2 == '-1':
                if state == 'down':
                    state = 'down'
                else:
                    state = 'down'
                    bot.send_message('584429967', '𝙳𝙱 𝙼𝙰𝙽𝙰𝙶𝙴𝚁 : 𝙰𝚗𝚘𝚗𝚢𝙲𝚑𝚊𝚝 𝚋𝚘𝚝 𝚒𝚜 𝙳𝚘𝚠𝚗 🔴')
                return 'down'
            elif x3 == True:
                if state == 'up':
                    state = 'up'
                else:
                    state = 'up'
                    bot.send_message('584429967', '𝙳𝙱 𝙼𝙰𝙽𝙰𝙶𝙴𝚁 : 𝙰𝚗𝚘𝚗𝚢𝙲𝚑𝚊𝚝 𝚋𝚘𝚝 𝚒𝚜 𝚄𝚙 🟢')
                #print('up')
                return 'up'
            else :
                if state == 'down':
                    state = 'down'
                else:
                    state = 'down'
                    bot.send_message('584429967', '𝙳𝙱 𝙼𝙰𝙽𝙰𝙶𝙴𝚁 : 𝙰𝚗𝚘𝚗𝚢𝙲𝚑𝚊𝚝 𝚋𝚘𝚝 𝚒𝚜 𝙳𝚘𝚠𝚗 🔴')
                #print('error')
                return 'error'
        except Exception as e:
            try:
                if state == 'error':
                    state = 'error'
                else:
                    state = 'error'
                    #bot.send_message('584429967', '𝙳𝙱 𝙼𝙰𝙽𝙰𝙶𝙴𝚁 : 𝙷𝚊𝚟𝚒𝚗𝚐 𝚎𝚛𝚛𝚘𝚛 𝚝𝚘 𝚌𝚑𝚎𝚌𝚔 𝙰𝚗𝚘𝚗𝚢𝙲𝚑𝚊𝚝 𝚋𝚘𝚝 𝚑𝚎𝚊𝚛𝚝𝚋𝚎𝚊𝚝 ‼️.')
                #print('error /: '+str(e))
                return 'may be down'
            except:
                print('error')
    
    #print (get(10,'ID'))
    
    
    def waiting():
        try:
            conn = sqlite3.connect('Anonychatdb_5.0v.db')
            cursor = conn.cursor()
            
            # Check if there are rows where tout is less than 0
            query = "SELECT COUNT(*) FROM my_table WHERE tout <= 0"
            cursor.execute(query)
            result = cursor.fetchone()
            
            if result[0] == 0:
                print("⚠️No min tout threshold crossed!!")
            else:
                # Update the rows where tout is less than 0
                update_query = "UPDATE my_table SET Status = 'waiting', tout = 1200 WHERE tout <= 0"
                cursor.execute(update_query)
                # Commit the changes
                conn.commit()
                print ("🔄 Status changed!!")
            
            # Close the connection
            conn.close()
            
        except Exception as e:
            print ("🔴 Status changed failed!! :/"+str(e))
            
        
    def flush():
        try:
            conn = sqlite3.connect('Anonychatdb_5.0v.db')
            c = conn.cursor()
            c.execute('DELETE FROM my_table WHERE tout < 0')
            conn.commit()
            conn.close()
            print ("🟢 Flushing executed!!")
            #print(df)
            return 'User ID Flushed'
        except Exception as e:
            print ("🔴 Flushing failed!! :/"+str(e))
            
    def flushID(mid):
        conn = sqlite3.connect('Anonychatdb_5.0v.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM my_table WHERE ID = ?", (mid,))
        row = cursor.fetchone()
        if row is not None:
            cursor.execute(f"DELETE FROM my_table WHERE ID = ?", (mid,))
            conn.commit()
            conn.close()
        print('User ID Flushed')
    
    def tout():
        try:
            import datetime
            current_time = datetime.datetime.now()
            
            # Extract the seconds component from the current time
            seconds = current_time.second
            
            # Check if seconds is a single digit
            if seconds < 10 :
                # Append a trailing zero to make it two digits
                seconds_str = int(seconds) + '0'
            else:
                # No change required
                seconds_str = int(seconds)

            # Establish connection to the database
            conn = sqlite3.connect('Anonychatdb_5.0v.db')
            c = conn.cursor()
            
            # Update the 'tout' column by subtracting 1 from its current value
            #c.execute("UPDATE my_table SET tout = tout - 60")
            c.execute("UPDATE my_table SET tout = tout - ?", (seconds_str,))
            
            # Commit the changes and close the connection
            conn.commit()
            conn.close()
            print ("🟢 tout decremented successful!!")
        except Exception as e:
            print ("🔴 tout decremented failed!! :/"+str(e))
            
    def tout2():
        try:
            conn = sqlite3.connect('Anonychatdb_5.0v.db')
            cursor = conn.cursor()
            
            # Retrieve the rows from the table
            cursor.execute("SELECT * FROM my_table")
            rows = cursor.fetchall()
            
            # Iterate through the rows and update the 'tout' column
            for row in rows:
                # Generate a random number in the range of 58 to 60
                decrement = random.randint(10, 60)
                
                # Decrement the 'tout' column by the random number
                updated_tout = row[2] - decrement
                
                # Ensure the updated value is not negative
                if updated_tout < 0:
                    updated_tout = 0
                
                # Update the row with the new 'tout' value
                cursor.execute("UPDATE my_table SET tout = ? WHERE ID = ?", (updated_tout, row[0]))
            
            # Commit the changes and close the connection
            conn.commit()
            conn.close()
            print ("🟢 tout decremented successful!!")
        except Exception as e:
            print ("🔴 tout decremented failed!! :/"+str(e))
        
    def test():
        print ('Test')
        
    def topup():
        # Set the path to the database file
        database_file = 'parameter1.0v.db'
        
        # Connect to the database
        conn = sqlite3.connect(database_file)
        
        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()
        
        # Execute the SQL command to update the BAL column
        cursor.execute('UPDATE my_table SET BAL = 50')
        
        # Commit the changes to the database
        conn.commit()
        
        # Close the cursor and database connections
        cursor.close()
        conn.close()
        
        # Print a success message
        print('Balance topup successfully.')
    tout2()
    print(readytoconnect('closed','Status'))
    state = '0'
    schedule.every(0.10).minutes.do(peering_task)
    schedule.every(1).minutes.do(tout2)
    schedule.every().day.at("00:00").do(topup)
    #schedule.every(0.02).minutes.do(flush)
    #schedule.every(0.01).minutes.do(inspector)
    state = str(inspector())
    #flush()
    #peering_task()
    #print(findpeer(5))
    #df = pd.read_csv('/code/Python_Lab/Anonychat/Anonychatdb01.2.csv')
    #print (df)
    
    while True:
     
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)
        
    
    
except Exception as e:
    time.sleep(5)
    print('🔴 Main process error /: '+str(e))
    exec(open('db_manager.py').read())
    exit()


