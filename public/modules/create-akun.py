from public import *

@bot.on(events.CallbackQuery(data=b'create-akun'))
async def create_akun(event):
    async def create_akun_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        
        async with bot.conversation(chat) as pw:
            await event.respond('**Password:**')
            pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            pw = (await pw).raw_text
            
        async with bot.conversation(chat) as exp_conv:
            await event.respond('**Expired :**')
            exp = (await exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text

        async with bot.conversation(chat) as ip_conv:
            await event.respond('**Limit Quota :**')
            ip = (await ip_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text

        async with bot.conversation(chat) as Quota_conv:
            await event.respond('**Limit Ip :**')
            Quota = (await Quota_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text

     await event.edit("**Wait.. Setting up an Account**")
        cmd = f'printf "%s\n" "{user}" "{pw}" "{exp}" "{ip}" "{Quota}" | addssh-bot'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"Terjadi kesalahan: {e}\nSubproses output: {a}")
            return  
            
        try:
            with open('/etc/xray/dns', 'r') as file:
              NS = file.read().strip()
        except FileNotFoundError:
              NS = "Not found"

        try:
            with open('/etc/slowdns/server.pub', 'r') as file:
              PUB = file.read().strip()
        except FileNotFoundError:
              PUB = "Not found"

            

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        z = requests.get("http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
◇━━━━━━━━━━━━━━━━━◇
     **◇⟨Ssh Account⟩◇**
◇━━━━━━━━━━━━━━━━━◇
**» ISP:** `{z["isp"]}`
**» Location:** `{z["country"]}`
**» Host:** `{DOMAIN}`
**» Host SlowDNS:** `{NS}`
**» Username:** `{user}`
**» Password:** `{pw}`
**» Limit Quota :** `{Quota} GB`
**» Limit Login :** `{ip} HP`
◇━━━━━━━━━━━━━━━━━◇
**» Pub Key:** `{PUB}`
**» Port OpenSsh :** 80, 22
**» Port Dropbear :** 443, 80, 109
**» Port Ssh Ws :** 80,2086,8080,8880
**» Port Ssh Ws/Tls :**443,8443
**» Port Ssh Ssl/Tls :**443
**» Port Ssh UDP :** 1-65535 
**» BadVPN UDP :** 7100, 7300, 7300
◇━━━━━━━━━━━━━━━━━◇
**⟨FORMAT HTTP CUSTOM⟩**
`{DOMAIN}:1-65535@{user}:{pw}`
◇━━━━━━━━━━━━━━━━━◇
**⟨Save Account⟩**
https://{DOMAIN}:81/ssh-{user}.txt
◇━━━━━━━━━━━━━━━━━◇
**⟨Payload Websocket⟩**
```GET /cdn-cgi/trace HTTP/1.1[crlf]Host: Bug_Kalian[crlf][crlf]GET-RAY / HTTP/1.1[crlf]Host: [host][crlf]Connection: Upgrade[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]```
◇━━━━━━━━━━━━━━━━━◇
**» Expired Until:** {later}
◇━━━━━━━━━━━━━━━━━◇
"""
        await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await create_akun_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)
