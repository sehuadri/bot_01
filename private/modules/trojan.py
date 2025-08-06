from private import *
import subprocess
import re
from telethon import events, Button

@bot.on(events.CallbackQuery(data=b'create-trojan'))
async def create_trojan(event):
    async def create_trojan_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username :**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        
        async with bot.conversation(chat) as exp:
            await event.respond('**Expired :**')
            exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = (await exp).raw_text

        async with bot.conversation(chat) as ip:
            await event.respond('**Limit Quota :**')
            ip = ip.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip = (await ip).raw_text
        
        async with bot.conversation(chat) as Quota:
            await event.respond('**Limit Ip :**')
            Quota = Quota.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            Quota = (await Quota).raw_text


        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{user}" "{exp}" "{ip}" "{Quota}" | addtr-bot'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"Terjadi kesalahan: {e}\nSubproses output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        b = [x.group() for x in re.finditer("trojan://(.*)", a)]
        print(b)
        domain = re.search("@(.*?):", b[0]).group(1)
        uuid = re.search("trojan://(.*?)@", b[0]).group(1)
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
     **◇⟨TROJAN ACCOUNT⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Username :** `{user}`
**» Domain :** `{DOMAIN}`
**» Limit Quota :** `{ip} GB`
**» Limit Login :** `{Quota} HP`
**» HTTP   :** `80,8080,2086,8880`
**» TLS    :** `443,8443`
**» UUID    :** `{uuid}`
**» NetWork     :** `(WS) or (gRPC)`
**» Path        :** `/trojan-ws/multi-path`
**» ServiceName :** `trojan-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» URL TLS    :**
```{𝚋[0]}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL HTTP    :**
```{𝚋[1].𝚛𝚎𝚙𝚕𝚊𝚌𝚎(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL gRPC   :** 
```{𝚋[2].𝚛𝚎𝚙𝚕𝚊𝚌𝚎(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**⟨Link Save Account⟩**
https://{DOMAIN}:81/trojan-{user}.txt
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ** 🤖@amqyu
"""
        await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await create_trojan_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)

@bot.on(events.CallbackQuery(data=b'cek-tr'))
async def cek_trojan(event):
    async def cek_trojan_(event):
        cmd = 'cek-tr'.strip()
        result = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True, env={"TERM": "xterm"}
        )

        # Hapus karakter escape ANSI
        clean_result = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', result).strip()

        await event.edit(f"""
**◇━━━━━━━━━━━━━━━━━━◇**
  **◇⟨Cek Trojan User Login⟩◇**
**◇━━━━━━━━━━━━━━━━━━◇**
{clean_result}

**Shows Logged In Users Trojan**
""", buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "trojan")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await cek_trojan_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)


@bot.on(events.CallbackQuery(data=b'trial-trojan'))
async def trial_trojan(event):
    async def trial_trojan_(event):
        cmd = f'printf "%s\n" "TrialTR-`</dev/urandom tr -dc X-Z0-9 | head -c4`" "1" "1" "1" | bot-trialtrojan'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Already Exist**")
        else:
            today = DT.date.today()
            later = today + DT.timedelta(days=int(1))
            b = [x.group() for x in re.finditer("trojan://(.*)", a)]
            print(b)
            remarks = re.search("#(.*)", b[0]).group(1)
            domain = re.search("@(.*?):", b[0]).group(1)
            uuid = re.search("trojan://(.*?)@", b[0]).group(1)
            msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨TRIAL TROJAN ACCOUNT⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Username :** `{remarks}`
**» Host Server :** `{DOMAIN}`
**» HTTP   :** `80,8080,2086,8880`
**» TLS    :** `443,8443`
**» UUID    :** `{uuid}`
**» NetWork     :** `(WS) or (gRPC)`
**» Path        :** `/trojan-ws`
**» ServiceName :** `trojan-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» URL TLS    :**
```{𝚋[0]}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL HTTP    :**
```{𝚋[1].𝚛𝚎𝚙𝚕𝚊𝚌𝚎(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL gRPC   :** 
```{𝚋[2].𝚛𝚎𝚙𝚕𝚊𝚌𝚎(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**⟨Link Save Account⟩**
https://{DOMAIN}:81/trojan-{remarks}.txt
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** 30 Minutes
**◇━━━━━━━━━━━━━━━━━◇**
**» ** 🤖@amqyu
"""
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await trial_trojan_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)

@bot.on(events.CallbackQuery(data=b'renew-trojan'))
async def ren_trojan(event):
    async def ren_trojan_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username :**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        
        async with bot.conversation(chat) as exp:
            await event.respond('**Expired :**')
            exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = (await exp).raw_text

        async with bot.conversation(chat) as ip:
            await event.respond('**Limit Quota :**')
            ip = ip.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip = (await ip).raw_text

        async with bot.conversation(chat) as Quota:
            await event.respond('**Limit Ip :**')
            Quota = Quota.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            Quota = (await Quota).raw_text


        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{user}" "{exp}" "{ip}" "{Quota}" | bot-renew-tro'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**Successfully Renew User**")
        else:
            msg = f"""
**{user} {exp} Days, limit ip {ip}, limit Quota {Quota} GB**
"""
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await ren_trojan_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)



# CEK member tr
@bot.on(events.CallbackQuery(data=b'cek-membertr'))
async def cek_tr(event):
    try:
        # Menjalankan perintah bash
        cmd = 'cek-mts'.strip()
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

        # Mengirim hasil ke pengguna
        await event.edit(f"""
{result}

**Shows Users from databases**
        """, buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", b"menu")]])

    except subprocess.CalledProcessError as e:
        # Jika terjadi error saat eksekusi perintah bash
        await event.edit(f"Error: {str(e)}", buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", b"menu")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await cek_tr_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)


		
@bot.on(events.CallbackQuery(data=b'delete-trojan'))
async def delete_trojan(event):
    async def delete_trojan_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username :**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{user}" | bot-del-tro'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**Successfully Delete User**")
        else:
            msg = f"""**Successfully Deleted**"""
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await delete_trojan_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)

@bot.on(events.CallbackQuery(data=b'limit-trojan'))
async def limit_trojan(event):
	async def limit_trojan_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username :**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Limit Ip :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
			await event.edit("**Loading......**")
			cmd = f'printf "%s\n" "{user}" "{pw}" | bot-ganti-ip-trojan'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"`{user}` **Succesfully Change Limit IP**")
		else:
			await event.respond(f"""
```
{a}
```
**GANTI IP trojan**
**» 🤖@amqyu**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await limit_trojan_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)

@bot.on(events.CallbackQuery(data=b'quota-trojan'))
async def quota_trojan(event):
	async def quota_trojan_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username :**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Limit Quota :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
			await event.edit("**Loading......**")
			cmd = f'printf "%s\n" "{user}" "{pw}" | bot-quota-trj'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"`{user}` **Succesfully Change Limit Quota**")
		else:
			await event.respond(f"""
```
{a}
```
**GANTI QUOTA trojan**
**» 🤖@amqyu**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await quota_trojan_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)

@bot.on(events.CallbackQuery(data=b'lock-trojan'))
async def lock_trojan(event):
	async def lock_trojan_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Username :**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		await event.edit("**Loading......**")
		cmd = f'printf "%s\n" "{exp}" | bot-lock-trj'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{exp}` **Successfully Locked**")
		else:
			msg = f"""**Successfully Locked**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await lock_trojan_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)
#UNLOCK ssh
@bot.on(events.CallbackQuery(data=b'unlock-trojan'))
async def unlock_trojan(event):
	async def unlock_trojan_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Username :**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		await event.edit("**Loading......**")
		cmd = f'printf "%s\n" "{exp}" | bot-unlock-trj'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{exp}` **Successfully Unlocked**")
		else:
			msg = f"""**Successfully Unlocked**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await unlock_trojan_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)

@bot.on(events.CallbackQuery(data=b'trojan'))
async def trojan(event):
    async def trojan_(event):
        inline = [
            [Button.inline("𝗧𝗿𝗶𝗮𝗹", "trial-trojan"),
             Button.inline("𝗖𝗿𝗲𝗮𝘁𝗲", "create-trojan")],
            [Button.inline("𝗖𝗵𝗲𝗰𝗸 𝗨𝘀𝗲𝗿 𝗟𝗼𝗴𝗶𝗻", "cek-tr")],
            [Button.inline("𝗥𝗲𝗻𝗲𝘄", "renew-trojan"),
             Button.inline("𝗗𝗲𝗹𝗲𝘁𝗲", "delete-trojan")],           
            [Button.inline("𝗟𝗶𝘀𝘁 𝗺𝗲𝗺𝗯𝗲𝗿", "cek-membertr")],
            [Button.inline("𝗟𝗼𝗰𝗸", "lock-trojan"),
             Button.inline("𝗨𝗻𝗹𝗼𝗰𝗸", "unlock-trojan")],
            [Button.inline("𝗖𝗵𝗮𝗻𝗴𝗲 𝗟𝗶𝗺𝗶𝘁 𝗜𝗣", "limit-trojan")],
            [Button.inline("𝗖𝗵𝗮𝗻𝗴𝗲 𝗟𝗶𝗺𝗶𝘁 𝗤𝘂𝗼𝘁𝗮", "quota-trojan")],
             [Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
     **◇⟨TROJAN SERVICE⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Service:** `TROJAN`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
**» ** 🤖@amqyu
**◇━━━━━━━━━━━━━━━━━◇**
        """
        await event.edit(msg, buttons=inline)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await trojan_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)