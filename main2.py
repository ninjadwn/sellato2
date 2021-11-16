import os

from datetime import datetime
from telethon.sync import TelegramClient
from telethon import TelegramClient,events,sync,Button
from telethon import functions,types
import json

bot = "2111909649:AAFjw74qcC4UqqHNdszYxSjyqV6oCtG7uhU"
api_id = 2689527
api_hash = "9836eebbf05d6fbbc948bb055d3cf966"
client = TelegramClient(bot,api_id,api_hash)
client.start()



admin_id = 1771075910   #USER ID ACCOUNT TELEGRAM PER UTILIZZARE I COMANDI ADMIN DEL BOT

if os.path.exists("storage.json"):            
    with open("storage.json", "r+") as f:     
        SAVES = json.load(f)                  
else:
    SAVES = {"Users": [], "Gain": 0.05}     
    with open("storage.json", "w+") as f:    
        json.dump(SAVES, f)                  
    

def save():                                 
    global SAVES                            
    with open("storage.json", "w+") as f:  
        json.dump(SAVES, f)                 

@client.on(events.NewMessage)
async def my_event_handler(e):
    
    client.parse_mode = 'html'

    #----- VARIABILI -----#
    
    try:
        sender_id = int(e.peer_id.user_id)
    except:
        try:
            sender_id = int(e.peer_id.chat_id)
        except:
            sender_id = int(e.peer_id.channel_id)
    
    userpath = "users/" + str(sender_id) + "/"
    text = e.text.split(' ')
    
    #----- VARIABILI -----#


    if(e.text == "/chatid"):
        await e.respond("<pre>" + str(sender_id) + "</pre>")




    if(sender_id == admin_id):
        if(text[0] == "/invia"):
            try:
                messaggio1 = e.text.replace(text[0], "")
                messaggio = messaggio1.replace(text[1], "")
                
                await client.send_message(int(text[1]), "👮 Operatore: " + messaggio.lstrip())
                
                await e.respond("Messaggio inviato")
            
            except:
                await e.respond("Errore")
        
        
        
        elif(text[0] == "/add"):
            try:
                credito = float(text[2])
                
                file = open("users/" + text[1] + "/saldo", "r")
                saldo1 = file.read()
                file.close()
                
                saldo = float(saldo1)
                
                calcolo = saldo + credito
                
                file = open("users/" + text[1] + "/saldo", "w")
                file.truncate(0)
                file.write(str(calcolo))
                
                await client.send_message(int(text[1]), "🎉 <b>CREDITO RICARICATO</b> 🎉\nℹ️ Caro utente, ti informiamo che il tuo credito è stato ricaricato con +" + str(credito) + " EUR",
                    buttons=[[Button.inline("✅ ACCETTA ✅", "home")]])
                
                await e.respond("OPERAZIONE RIUSCITA")
            
            except:
                await e.respond("ERRORE")
        
        
        
        elif(text[0] == "/ban"):
            try:
                utente = text[1]
            
                file = open("users/" + str(utente) + "/ban", "w")
                file.write("")
                file.close()
                
                await e.respond("UTENTE BANNATO")
            
            except:
                await e.respond("ERRORE")
        
        
        
        elif(text[0] == "/unban"):
            try:
                utente = text[1]
            
                os.remove("users/" + str(utente) + "/ban")
                
                await e.respond("UTENTE SBANNATO")
            
            except:
                await e.respond("ERRORE")

                
    
        
        
        elif(e.text == "/help"):
            await e.respond("""/add {USER_ID} {SOLDI}   - RICARICA SALDO AD UN UTENTE
            esempio.   /add 2020410978 1.55
            
            
            
            /invia {USER_ID} {MESSAGGIO}   - INVIA UN MESSAGGIO AD UN UTENTE, USALO PER COMUNICARE TRAMITE CHAT-LIVE O PER SEGNALARGLI QUALCOSA.
            esempio.   /mex 2020410978 Ciao come va?
            
            
            
            /ban {USER_ID}   - BANNA UN UTENTE DAL BOT
            esempio.   /ban 2020410978
            
            
            
            /unban {USER_ID}   - SBANNA UN UTENTE DAL BOT
            esempio.   /unban 2020410978""")
    
    
    
        if(text[0] == "/start"):
                sender = await e.get_sender()
                
                if e.sender_id in SAVES["Users"]:
                    try:
                        file = open(userpath + "check", "r")
                        file.close()
                    except:
                        os.mkdir(userpath)
                        
                        file = open(userpath + "check", "w")
                        file.write("")
                        file.close()
                        
                        file = open(userpath + "saldo", "w")
                        file.write("0.00")
                        file.close()
                        
                        file = open(userpath + "stato", "w")
                        file.write("null")
                        file.close()
                        
                        file = open(userpath + "history", "w")
                        file.write("")
                        file.close()
                    file = open(userpath + "stato", "w")
                    file.truncate(0)
                    file.write("null")
                    file.close()
                    
                    file = open(userpath + "saldo", "r")
                    saldo = file.read()
                    file.close()
                    
                    await e.respond("👋Benvenuto " + str(sender.first_name)  +  " nel bot ufficiale di @appacificarsi!\n\n👀 Se sei in cerca di un UserBot / Bot Personalizzato, clicca il pulsante SHOP dove potrai visionare i prezzi e ciò che presentano!\n\n💶 Saldo attuale: <b>" + saldo.replace(".", ",") + " €\n\n❔Perché scegliermi?\n\n📶 VPS Online 24h/24h (No Blocchi/Slowdown).\n💳 Rapporto qualità/prezzo assurdo.\n⚙️ Supporto 100% Online e disponibile.\n\n👇Inizia ad orientarti usando i pulsanti sottostanti!",
                    buttons=[[Button.inline("💰SALDO💰", "ricarica"), Button.inline("🛍SHOP️🛍️", "shop")], 
                    [Button.url("✅FEEDBACK✅", "https://t.me/joinchat/EqEQfeA5SOZjNjA0"), Button.url("⚠ToS", "https://telegra.ph/TOS-10-12")],
                    [Button.inline("🎛 Pannello Admin", 'admin_panel')],
                    [Button.url("☎ASSISTENZA☎️", "https://t.me/AgonyDevBot")],
                    [Button.url("👨‍💻DEVELOPER👨‍💻", "https://t.me/AgonyDevProject")]])
                else:
                    try:
                        file = open(userpath + "check", "r")
                        file.close()
                    except:
                        os.mkdir(userpath)
                        
                        file = open(userpath + "check", "w")
                        file.write("")
                        file.close()
                        
                        file = open(userpath + "saldo", "w")
                        file.write("0.00")
                        file.close()
                        
                        file = open(userpath + "stato", "w")
                        file.write("null")
                        file.close()
                        
                        file = open(userpath + "history", "w")
                        file.write("")
                        file.close()
                    SAVES["Users"].append(e.sender_id)
                    file = open(userpath + "stato", "w")
                    file.truncate(0)
                    file.write("null")
                    file.close()
                    
                    file = open(userpath + "saldo", "r")
                    saldo = file.read()
                    file.close()
                    
                    await e.respond("👋Benvenuto " + str(sender.first_name)  +  " nel bot ufficiale di @appacificarsi!\n\n👀 Se sei in cerca di un UserBot / Bot Personalizzato, clicca il pulsante SHOP dove potrai visionare i prezzi e ciò che presentano!\n\n💶 Saldo attuale: <b>" + saldo.replace(".", ",") + " €\n\n❔Perché scegliermi?\n\n📶 VPS Online 24h/24h (No Blocchi/Slowdown).\n💳 Rapporto qualità/prezzo assurdo.\n⚙️ Supporto 100% Online e disponibile.\n\n👇Inizia ad orientarti usando i pulsanti sottostanti!",
                    buttons=[[Button.inline("💰SALDO💰", "ricarica"), Button.inline("🛍SHOP️🛍️", "shop")], 
                    [Button.url("✅FEEDBACK✅", "https://t.me/joinchat/EqEQfeA5SOZjNjA0"), Button.url("⚠ToS", "https://telegra.ph/TOS-10-12")],
                    [Button.inline("🎛 Pannello Admin", 'admin_panel')],
                    [Button.url("☎ASSISTENZA☎️", "https://t.me/AgonyDevBot")],
                    [Button.url("👨‍💻DEVELOPER👨‍💻", "https://t.me/AgonyDevProject")]])
    
    
    
    
    else:
        try:
            file = open(userpath + "check", "r")
            file.close()
        except:
            os.mkdir(userpath)
            
            file = open(userpath + "check", "w")
            file.write("")
            file.close()
            
            file = open(userpath + "saldo", "w")
            file.write("0.00")
            file.close()
            
            file = open(userpath + "stato", "w")
            file.write("null")
            file.close()
            
            file = open(userpath + "history", "w")
            file.write("")
            file.close()
            
            try:
                if(text[0] == "/start"):
                    referralid = int(text[1])
                    
                    file = open("users/" + str(referralid) + "/saldo", "r")
                    saldonow1 = file.read()
                    file.close()
                    
                    saldonow = float(saldonow1)
                    
                    calcolo = saldonow + SAVES["Gain"]
                    print(calcolo)
                    
                    file = open("users/" + str(referralid) + "/saldo", "w")
                    file.truncate(0)
                    file.write(str(calcolo))
                    file.close()
                    
                    await client.send_message(int(referralid), f"<b>AVVISO</b> 🎉\nℹ️ Caro utente, ti informiamo che un utente ha avviato il bot tramite il tuo link Referral, il tuo credito attuale è stato aggiornato con +{str(SAVES['Gain'])} EUR.",
                        buttons=[[Button.inline("✅ ACCETTA ✅", "home")]])
            
            except:
                null = ""
        
        
        
        
        
        try:
            file = open(userpath + "ban", "r")
            file.close()
            
            await e.respond("⛔ <b>SEI STATO BANNATO</b> ⛔\nℹ️ Siamo spiacenti, ma sei stato permanentemente bannato. Da ora in poi non potrai più utilizzare le funzioni del BOT.")
        
        except:
            file = open(userpath + "stato", "r")
            stato = file.read()
            file.close()
            
            if(e.text == "/annulla"):
                file = open(userpath + "stato", "w")
                file.truncate(0)
                file.write("null")
                file.close()

                await e.respond("❌ <b>Chat Terminata</b> ❌",
                    buttons=[[Button.inline("⬅️ indietro", "home")]])
            

            if(stato == "chatlive"):
                if(e.text == "/annulla"):
                    null = ""
                
                else:
                    await client.send_message(int(admin_id), "<pre>" + str(sender_id) + "</pre> ha appena avviato la chat e ti ha inviato un messaggio:")
                
                    result = await client(functions.messages.ForwardMessagesRequest(
                    from_peer='me',
                    id=[e.id],
                    to_peer=int(admin_id),
                    with_my_score=True ))
            
            
            if(text[0] == "/start"):
                sender = await e.get_sender()
                
                file = open(userpath + "stato", "w")
                file.truncate(0)
                file.write("null")
                file.close()
                
                file = open(userpath + "saldo", "r")
                saldo = file.read()
                file.close()
                if e.sender_id in SAVES["Users"]:
                    await e.respond("👋Benvenuto " + str(sender.first_name)  +  " nel bot ufficiale di @appacificarsi!\n\n👀 Se sei in cerca di un UserBot / Bot Personalizzato, clicca il pulsante SHOP dove potrai visionare i prezzi e ciò che presentano!\n\n💶 Saldo attuale: <b>" + saldo.replace(".", ",") + " €\n\n❔Perché scegliermi?\n\n📶 VPS Online 24h/24h (No Blocchi/Slowdown).\n💳 Rapporto qualità/prezzo assurdo.\n⚙️ Supporto 100% Online e disponibile.\n\n👇Inizia ad orientarti usando i pulsanti sottostanti!",
                    buttons=[[Button.inline("💰SALDO💰", "ricarica"), Button.inline("🛍SHOP️🛍️", "shop")], 
                    [Button.url("✅FEEDBACK✅", "https://t.me/joinchat/EqEQfeA5SOZjNjA0"), Button.url("⚠ToS", "https://telegra.ph/TOS-10-12")],
                    [Button.url("☎ASSISTENZA☎️", "https://t.me/AgonyDevBot")],
                    [Button.url("👨‍💻DEVELOPER👨‍💻", "https://t.me/AgonyDevProject")]])
                else:
                    SAVES["Users"].append(e.sender_id)
                    await e.respond("👋Benvenuto " + str(sender.first_name)  +  " nel bot ufficiale di @appacificarsi!\n\n👀 Se sei in cerca di un UserBot / Bot Personalizzato, clicca il pulsante SHOP dove potrai visionare i prezzi e ciò che presentano!\n\n💶 Saldo attuale: <b>" + saldo.replace(".", ",") + " €\n\n❔Perché scegliermi?\n\n📶 VPS Online 24h/24h (No Blocchi/Slowdown).\n💳 Rapporto qualità/prezzo assurdo.\n⚙️ Supporto 100% Online e disponibile.\n\n👇Inizia ad orientarti usando i pulsanti sottostanti!",
                    buttons=[[Button.inline("💰SALDO💰", "ricarica"), Button.inline("🛍SHOP️🛍️", "shop")], 
                    [Button.url("✅FEEDBACK✅", "https://t.me/joinchat/EqEQfeA5SOZjNjA0"), Button.url("⚠ToS", "https://telegra.ph/TOS-10-12")],
                    [Button.url("☎ASSISTENZA☎️", "https://t.me/AgonyDevBot")],
                    [Button.url("👨‍💻DEVELOPER👨‍💻", "https://t.me/AgonyDevProject")]])
                



@client.on(events.CallbackQuery())
async def callbackQuery(e):
    client.parse_mode = 'html'

    #----- VARIABILI -----#

    try:
        sender_id = int(e.original_update.peer.user_id)
    except:
        try:
            sender_id = int(e.original_update.peer.chat_id)
        except:
            sender_id = int(e.original_update.peer.channel_id)
    
    userpath = "users/" + str(sender_id) + "/"
    
    #----- VARIABILI -----#
    
    
    if(e.data == b"home"):
        sender = await e.get_sender()
            
        file = open(userpath + "stato", "w")
        file.truncate(0)
        file.write("null")
        file.close()
        
        file = open(userpath + "saldo", "r")
        saldo = file.read()
        file.close()
        
        await e.delete()
        
        await e.respond("👋Benvenuto " + str(sender.first_name)  +  " nel bot ufficiale di @appacificarsi!\n\n👀 Se sei in cerca di un UserBot / Bot Personalizzato, clicca il pulsante SHOP dove potrai visionare i prezzi e ciò che presentano!\n\n💶 Saldo attuale: <b>" + saldo.replace(".", ",") + " €\n\n❔Perché scegliermi?\n\n📶 VPS Online 24h/24h (No Blocchi/Slowdown).\n💳 Rapporto qualità/prezzo assurdo.\n⚙️ Supporto 100% Online e disponibile.\n\n👇Inizia ad orientarti usando i pulsanti sottostanti!",
                buttons=[[Button.inline("💰SALDO💰", "ricarica"), Button.inline("🛍️SHOP🛍️", "shop")], 
                [Button.url("✅FEEDBACK✅", "https://t.me/joinchat/EqEQfeA5SOZjNjA0"), Button.url("⚠ToS", "https://telegra.ph/TOS-10-12")],
                [Button.url("☎ASSISTENZA☎️", "https://t.me/AgonyDevBot")],
                [Button.url("👨‍💻DEVELOPER👨‍💻", "https://t.me/AgonyDevProject")]])
    
    
    
    
    elif(e.data == b"shop"):
        await e.edit("🛍 <b>Menu shop</b> 🛍\nℹ️ Utilizza i pulsanti per selezionare la categoria.",
            buttons=[[Button.inline("🦹USERBOT🦹", "ubot"), Button.inline("🤖BOT🤖", "bot")],
            [Button.inline("⚙️ALTRO⚙️", "account")],           
            [Button.inline("⬅️ indietro", "home")]])
    
    
    
    
    elif(e.data == b"cronologia"):
        file = open(userpath + "history", "r", encoding='utf8')
        history = file.read()
        file.close()
    
        if(history == ""):
            await e.answer("❌ ERRORE ❌\n\nℹ️ Non hai effettuato nessun acquisto.", alert=True)
        
        else:
            await e.edit(history,
                buttons=[[Button.inline("⬅️ INDIETRO", "home")]])
    
    
            

    elif(e.data == b"ubot"):
        await e.edit("🛍 <b>Menu Shop</b> 🛍\nℹ️ Utilizza i pulsanti per selezionare l'articolo e per procedere successivamente all'acquisto.Tutti gli account sono cracked",
            buttons=[[Button.inline("🤖 Personalizzato", "comprapers"), Button.inline("🤖 Spammer", "compraspammer")],
            [Button.inline("🤖 Fake Feeder", "comprafake")],
            [Button.inline("⬅️ indietro", "shop")]])
                    
    elif(e.data == b"bot"):
        await e.edit("🛍 <b>Menu Shop</b> 🛍\nℹ️ Utilizza i pulsanti per selezionare l'articolo e per procedere successivamente all'acquisto.",
            buttons=[[Button.inline("🤖 Adder Bot", "compraraspabot"), Button.inline("🤖 Spammer Bot", "compraspammerbot")],
            [Button.inline("🤖 Logger bot", "compraloggerbot"), Button.inline("🤖 Shop Bot", "comprashopbot")],
            [Button.inline("🤖 Limitati Bot", "compralimitatibot"), Button.inline("🤖 Antiscam bot", "comprablacklistbot")],
            [Button.inline("⬅️ indietro", "shop")]])
    
    elif(e.data == b"account"):
        await e.edit("🛍 <b>Menu Shop</b> 🛍\nℹ️ Utilizza i pulsanti per selezionare l'articolo e per procedere successivamente all'acquisto.",
            buttons=[[Button.inline("⚽Dazn Cracked", "compradazncracked"), Button.inline("⚽Dazn Privato", "compradaznprivato")],
            [Button.inline("🍿Netflix Cracked", "compranetflixcracked"), Button.inline("🧻Porn Hub", "comprapornhub")],
            [Button.inline("✈Nord Vpn", "compranordvpn"), Button.inline("🏰Disney Plus", "compradisneyplus")],
            [Button.inline("🛍️Wish", "comprawish"), Button.inline("🎧Spotify", "compraspotify")],
            [Button.inline("⬅️ indietro", "shop")]])
            
            
    elif e.data.__contains__(b"compra"):
        contenuto = str(e.data)
    
        if(contenuto.__contains__("comprapers")):
            nome = "Personalizzato"
            prezzo = 2.00
            prezzostr = "2,00"
        
        elif(contenuto.__contains__("compraspammer")):
            nome = "Spammer"
            prezzo = 2.00
            prezzostr = "2,00"
        
        elif(contenuto.__contains__("comprafake")):
            nome = "Fake Feeder"
            prezzo = 2.00
            prezzostr = "2,00"
                               
        elif(contenuto.__contains__("compraraspabot")):
            nome = "🤖 Adder bot"
            prezzo = 3.00
            prezzostr = "3,00"
        
        elif(contenuto.__contains__("compraspammerbot")):
            nome = "🤖 Spammer bot"
            prezzo = 3.00
            prezzostr = "3,00"
        
        elif(contenuto.__contains__("compraloggerbot")):
            nome = "🤖 Logger bot"
            prezzo = 5.00
            prezzostr = "5,00"
            
        elif(contenuto.__contains__("comprashopbot")):
            nome = "🤖 Shop bot"
            prezzo = 4.00
            prezzostr = "4,00"

        elif(contenuto.__contains__("compralimitatibot")):
            nome = "🤖 Limitati bot"
            prezzo = 1.00
            prezzostr = "1,00"

        elif(contenuto.__contains__("comprablacklistbot")):
            nome = "🤖 Antiscam bot"
            prezzo = 5.00
            prezzostr = "5,00"
            
        elif(contenuto.__contains__("compradazncracked")):
            nome = "Dazn Cracked"
            prezzo = 00.30
            prezzostr = "00,30"
        
        elif(contenuto.__contains__("compradaznprivato")):
            nome = "Dazn Privato"
            prezzo = 1.00
            prezzostr = "1,00"
         
        elif(contenuto.__contains__("compranetflixcracked")):
            nome = "Netflix Cracked"
            prezzo = 00.30
            prezzostr = "00,30"
              
        elif(contenuto.__contains__("comprapornhub")):
            nome = "Porn Hub"
            prezzo = 00.40
            prezzostr = "00.40"
            
        elif(contenuto.__contains__("compranordvpn")):
            nome = "Nord Vpn"
            prezzo = 00.40
            prezzostr = "00,40"

        elif(contenuto.__contains__("compradisneyplus")):
            nome = "Disney Plus"
            prezzo = 00.40
            prezzostr = "00,40"
            
        elif(contenuto.__contains__("comprawish")):
            nome = "Wish"
            prezzo = 00.30
            prezzostr = "00,30"
            
        elif(contenuto.__contains__("compraspotify")):
            nome = "Spotify"
            prezzo = 00.30
            prezzostr = "00,30"

        
        now = datetime.now()
        dataora = now.strftime("%d/%m/%Y %H:%M:%S")
        
        try:
            ubot = filesend
            
            file = open(userpath + "stato", "w", encoding='utf8')
            file.truncate(0)
            file.write(prezzostr.replace(",", ".") + " " + str(filesend) + " COMPRABOT 🛒 ARTICOLO: " + nome + "\n💰 PREZZO: " + prezzostr + " EUR\n🕔 Data & ora: " + str(dataora))
            file.close()
        
        
        except:
            file = open(userpath + "stato", "w", encoding='utf8')
            file.truncate(0)
            file.write(prezzostr.replace(",", ".") + " 🛒 ARTICOLO: " + nome + "\n💰 PREZZO: " + prezzostr + " EUR\n🕔 Data & ora: " + str(dataora))
            file.close()
        
        
        
        await e.edit("✅ <b>PROCEDI ALL'ACQUISTO</b>\nℹ️ Nome articolo: " + nome + "\n💰 Prezzo: " + str(prezzostr) + " EUR\n\n⚠️ Premendo sul pulsante acquisto il tuo credito residuo verrà scalato e riceverai l'articolo entro e non oltre 24 ore direttamente qui sulla messaggistica del BOT.\n💬 Per qualsiasi domanda o richiesta di aiuto puoi contattarci tramite chat-live. Trovi il pulsante tornando alla Homepage del BOT.",
            buttons=[[Button.inline("🔴 ACQUISTA 🔴", "acquistato")],
                [Button.inline("⬅️ INDIETRO", "shop")]])
    
    
    
    
    
    elif(e.data == b"acquistato"):
        file = open(userpath + "saldo", "r")
        saldo = file.read()
        file.close()
        
        file = open(userpath + "stato", "r", encoding='utf8')
        stato = file.read()
        file.close()
        
        if(stato.__contains__("COMPRABOT")):
            prezzo1 = stato.split(' ')
            prezzo2 = prezzo1[0]
            
            prezzo = float(prezzo2)
            
            saldoattuale = float(saldo)
            
            filetemp = prezzo1[1]
            filesend = "files/" + prezzo1[1]
            
            
            if(saldoattuale < prezzo):
                await e.answer("❌ ERRORE ❌\n\nℹ️ Saldo NON sufficente per completare questa transazione. Ricarica il saldo prima di procedere con l'acquisto.", alert=True)
            
            else:
                calcolo = float(saldoattuale - prezzo)
                
                file = open(userpath + "saldo", "w")
                file.truncate(0)
                file.write(str(calcolo))
                file.close()
                
                
                cron1 = stato.replace(prezzo2, "")
                cron2 = cron1.replace(filetemp, "")
                cron = cron2.replace("COMPRABOT", "")
                
                
                await client.send_message(int(admin_id), "<pre>" + str(sender_id) + "</pre> HA ACQUISTATO:\n" + cron.lstrip() + "\n\nQUESTO ACQUISTO E' AUTOMATICO NON DEVI FARE NULLA TU.")
                
                
                file = open(userpath + "history", "r", encoding='utf8')
                history = file.read()
                file.close()
                
                
                file = open(userpath + "stato", "w")
                file.write("null")
                file.close()
                
                
                file = open(userpath + "history", "w", encoding='utf8')
                file.write(history + "\n\n" + cron.lstrip())
                file.close()
                
                await e.edit("🔄 INVIO IN CORSO. . . 🔄\n<i>Non chiudere questa schermata, sto inviando il file...</i>")
                
                await e.respond(file=filesend)
                
                await e.respond("🎉 <b>ACQUISTO COMPLETATO</b> 🎉\n❤️ Grazie del tuo acquisto!",
                    buttons=[[Button.inline("⬅️ INDIETRO", "home")]])
        
        
        
        else:
            prezzo1 = stato.split(' ')
            prezzo2 = prezzo1[0]
            
            prezzo = float(prezzo2)
            
            saldoattuale = float(saldo)
            
            if(saldoattuale < prezzo):
                await e.answer("❌ ERRORE ❌\n\nℹ️ Saldo NON sufficente per completare questa transazione. Ricarica il saldo prima di procedere con l'acquisto.", alert=True)
            
            else:
                calcolo = float(saldoattuale - prezzo)
                
                file = open(userpath + "saldo", "w")
                file.truncate(0)
                file.write(str(calcolo))
                file.close()
                
                await client.send_message(int(admin_id), "<pre>" + str(sender_id) + "</pre> HA ACQUISTATO:\n" + stato.replace(prezzo2, "").lstrip())
                
                
                file = open(userpath + "history", "r", encoding='utf8')
                history = file.read()
                file.close()
                
                
                file = open(userpath + "stato", "w")
                file.write("null")
                file.close()
                
                
                file = open(userpath + "history", "w", encoding='utf8')
                file.write(history + "\n\n" + stato.replace(prezzo2, "").lstrip())
                file.close()
                
                
                await e.edit("🎉 <b>ACQUISTO COMPLETATO</b> 🎉\nℹ️ Grazie per aver effettuato l'acquisto!\nRiceverai il tuo articolo entro e non oltre le 24 ore, riceverai un messaggio sulla chat del BOT non appena un operatore prenderà in carico la tua richiesta.",
                    buttons=[[Button.inline("⬅️ INDIETRO", "home")]])



    
    elif(e.data == b"ricarica"):
        await e.edit("👀Clicca il pulsante Ricarica e scegli il tipo di pagamento con cui vuoi ricaricare il tuo saldo!",
                buttons=[[Button.inline("💶Ricarica", "ricaricasaldo")],
                [Button.inline("📄Cronologia", "cronologia")],
                [Button.inline("⬅️ indietro", "home")]]),
                                
    elif(e.data == b"ricaricasaldo"):
        await e.edit("Ecco il tuo modo per guadagnare €!!",
                buttons=[[Button.inline("🥵🆕 Referral", 'referral')],
                [Button.inline("⬅️ INDIETRO", "home")]])
                #buttons=[[Button.inline("💰PayPal", "paypal"), Button.inline("💳Bitcoin", "bitcoin")],[Button.inline("🥵🆕 Referral", 'referral')],
                #[Button.inline("⬅️ INDIETRO", "home")]])
    
    elif (e.data == b"referral"):
        await e.edit(f"🆕 Invita i tuoi amici e guadagna soldi!\n🥵 Ogni amico invitato tramite il tuo link verrà aggiunto {str(SAVES['Gain'])}€ di saldo, praticamente invitane 6 e prenditi gratuitamente un netflix!\n\n💴 Usa questo link per iniziare a guadagnare: http://t.me/QUI_METTI_TUO_LINK_BOT/?start={e.sender_id}", buttons=[[Button.inline("INDIETRO", 'home')]])

    elif (e.data == b"admin_panel"):
        await e.edit(f"Scegli.", buttons =[[Button.inline("Messaggio Globale", 'global'),Button.inline("Guadagno Referral", "gain")]])

    elif e.data == b"global":
        await e.delete()
        async with client.conversation(e.chat_id) as conv:
            msg1 = await conv.send_message("✅ Che messaggio devo mandare?")
            msg2 = await conv.get_response()
        for x in SAVES["Users"]:
                await client.send_message(x, f"👮‍♀️: {msg2.message}")

    elif e.data == b"gain":
        await e.delete()
        async with client.conversation(e.chat_id) as conv:
            f = await conv.send_message(f"✅ L\'attuale guadagno impostato è `{SAVES['Gain']}`'")
            f2 = await conv.get_response()
        SAVES["Gain"] = str(f2.message)
        await client.send_message(e.chat_id, f"Ok, attuale guadagno: {SAVES['Gain']}")

    elif(e.data == b"paypal"):
        file = open(userpath + "stato", "w")
        file.truncate(0)
        file.write("paypal")
        file.close()
        
        await e.edit("☑️Perfetto! Ora paga con la cifra che vuoi che ti sia aggiunta al tuo saldo! Per pagare: » https://paypal.me/RiftGive «\n\n\n🖼Dopo aver pagato, manda lo screen della TRANSAZIONE che hai effettuato all'assistenza!",
            buttons=[[Button.inline("⬅️ indietro", "home")]])
    
    
    
    
    elif(e.data == b"bitcoin"):
        await e.delete()
        await e.respond("Tipo di pagamento non attualmente disponibile",
                buttons=[[Button.inline("⬅️ indietro", "home")]])
    
    
    
    
    elif(e.data == b"pagamentopaypal"):
        await client.send_message(int(admin_id), "<pre>" + str(sender_id) + "</pre> DOVREBBE AVER PAGATO CON PAYPAL.\nCONTROLLA IL SALDO E VEDI QUANTO TI HA PAGATO ED AGGIUNGI IL SALDO AL SUO ID ACCOUNT.")
        
        await e.edit("✅ <b>OPERAZIONE COMPLETATA</b> ✅\nℹ️ Un operatore controllerà il tuo pagamento, se risulterà valido riceverai un riscontro qui sulla chat del BOT.",
            buttons=[[Button.inline("⬅️ INDIETRO", "home")]])
    
    
    
    
    
    elif(e.data == b"pagamentobitcoin"):
        await client.send_message(int(admin_id), "<pre>" + str(sender_id) + "</pre> DOVREBBE AVER PAGATO CON BITCOIN (BTC).\nCONTROLLA IL SALDO SUL WALLET E VEDI QUANTO TI HA PAGATO ED AGGIUNGI IL SALDO AL SUO ID ACCOUNT.")
        
        await e.edit("✅ <b>OPERAZIONE COMPLETATA</b> ✅\nℹ️ Un operatore controllerà il tuo pagamento, se risulterà valido riceverai un riscontro qui sulla chat del BOT.",
            buttons=[[Button.inline("⬅️ INDIETRO", "home")]])
    
    
    
    
    
    elif(e.data == b"chatlive"):
        file = open(userpath + "stato", "w")
        file.truncate(0)
        file.write("chatlive")
        file.close()
    
        await e.edit("💬 <b>CHAT-LIVE ATTIVA</b> 💬\nℹ️ Da ora in poi qualsiasi messaggio che invii sarà recapitato ai nostri operatori, tutte le risposte verranno ricevute qui in questa chat. Per terminare la chat live premi il pulsante in basso o utilizza il comando /annulla.",
            buttons=[[Button.inline("❌ CHIUDI CHAT ❌", "chatclose")]])
    
    
    
    
    
    elif(e.data == b"chatclose"):
        file = open(userpath + "stato", "w")
        file.truncate(0)
        file.write("null")
        file.close()
    
        await e.edit("❌ <b>CHAT TERMINATA</b> ❌",
            buttons=[[Button.inline("⬅️ INDIETRO", "home")]])
    


print('.')
client.run_until_disconnected()