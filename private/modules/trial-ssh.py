from private import *

@bot.on(events.CallbackQuery(data=b'trial-ssh'))
async def trial_ssh(event):
    async def trial_ssh_(event):
        user = "TrialSSH-" + str(random.randint(100, 1000))
        pw = "free"
        Quota = "1"
        ip = "1"
        exp = "1"       

        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{user}" "{pw}" "{Quota}" "{ip}" "{exp}" | bot-trialssh'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"Terjadi kesalahan: {e}\nSubproses output: {a}")
            return  # Stop execution if there's an error
        
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
  **◇⟨Trial Ssh & Account⟩◇**
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
**» Port OpenSsh :** 22
**» Port Dropbear :** 22, 109
**» Port Ssh Ws :** 80,2086,8080,8880
**» Port Ssh Ws/Tls :**443,8443
**» Port Ssh Ssl/Tls :**443
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
**» Expired Until:** 30 Minutes
◇━━━━━━━━━━━━━━━━━◇
"""
        await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await trial_ssh_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)
        
