from public import *
import subprocess
import re
from telethon import events, Button

@bot.on(events.CallbackQuery(data=b'create-vless'))
async def create_vless(event):
    async def create_vless_(event):
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
        cmd = f'printf "%s\n" "{user}" "{exp}" "{ip}" "{Quota}" | addvless-bot'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"Terjadi kesalahan: {e}\nSubproses output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        x = [x.group() for x in re.finditer("vless://(.*)", a)]
        print(x)
        uuid = re.search("vless://(.*?)@", x[0]).group(1)
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
        **◇⟨VLESS ACCOUNT⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Username :** `{user}`
**» Domain :** `{DOMAIN}`
**» Limit Quota :** `{ip} GB`
**» Limit Login :** `{Quota} HP`
**» HTTP   :** `80,8080,2086,8880`
**» TLS    :** `443,8443`
**» UUID    :** `{uuid}`
**» Networks     :** `(WS) or (gRPC)`
**» Path        :** `/vless`
**» ServiceName :** `vless-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» URL TLS    :**
```{x[0]}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL HTTP    :**
```{x[1].𝚛𝚎𝚙𝚕𝚊𝚌𝚎(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL gRPC   :** 
```{x[2].𝚛𝚎𝚙𝚕𝚊𝚌𝚎(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**⟨Link Save Account⟩**
https://{DOMAIN}:81/vless-{user}.txt
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
        await create_vless_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)

@bot.on(events.CallbackQuery(data=b'cek-vless'))
async def cek_vless(event):
    async def cek_vless_(event):
        cmd = 'cek-vless'.strip()
        result = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True, env={"TERM": "xterm"}
        )

        # Hapus karakter escape ANSI
        clean_result = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', result).strip()

        await event.edit(f"""
**◇━━━━━━━━━━━━━━━━━━◇**
 ** ◇⟨Cek Vless User Login⟩◇**
**◇━━━━━━━━━━━━━━━━━━◇**
{clean_result}

**Shows Logged In Users Vless**
""", buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "vless")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await cek_vless_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)
		
@bot.on(events.CallbackQuery(data=b'renew-vless'))
async def ren_vless(event):
    async def ren_vless_(event):
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
        cmd = f'printf "%s\n" "{user}" "{exp}" "{ip}" "{Quota}" | bot-renew-vle'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**Successfully Renew User `{user}`**")
        else:
            msg = f"""
**{user} {exp} Days, limit ip {ip}, limit Quota {Quota} GB**
"""
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await ren_vless_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)


# CEK member VLESS
@bot.on(events.CallbackQuery(data=b'cek-membervl'))
async def cek_vless(event):
    async def cek_vless_(event):
        cmd = 'cek-mvs'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""

{z}

**Shows Users from databases**
""", buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "menu")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await cek_vless_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)



@bot.on(events.CallbackQuery(data=b'delete-vless'))
async def delete_vless(event):
    async def delete_vless_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username :**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{user}" | bot-del-vle'
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
        await delete_vless_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)



@bot.on(events.CallbackQuery(data=b'trial-vless'))
async def trial_vless(event):
    async def trial_vless_(event):
        cmd = f'printf "%s\n" "TrialVL`</dev/urandom tr -dc X-Z0-9 | head -c4`" "1" "1" "1" | bot-trialvless'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Already Exist**")
        else:
            today = DT.date.today()
            later = today + DT.timedelta(days=int(1))
            x = [x.group() for x in re.finditer("vless://(.*)", a)]
            print(x)
            remarks = re.search("#(.*)", x[0]).group(1)
            # domain = re.search("@(.*?):", x[0]).group(1)
            uuid = re.search("vless://(.*?)@", x[0]).group(1)
            # path = re.search("path=(.*)&", x[0]).group(1)
            msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
 **◇⟨TRIAL VLESS ACCOUNT⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Username :** `{remarks}`
**» Host Server :** `{DOMAIN}`
**» HTTP   :** `80,8080,2086,8880`
**» TLS    :** `443,8443`
**» UUID    :** `{uuid}`
**» NetWork     :** `(WS) or (gRPC)`
**» Path        :** `/vless`
**» ServiceName :** `vless-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» URL TLS    :**
```{x[0]}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL HTTP    :**
```{x[1].𝚛𝚎𝚙𝚕𝚊𝚌𝚎(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL gRPC   :** 
```{x[2].𝚛𝚎𝚙𝚕𝚊𝚌𝚎(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**⟨Link Save Account⟩**
https://{DOMAIN}:81/vless-{remarks}.txt
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
        await trial_vless_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)

@bot.on(events.CallbackQuery(data=b'limit-vless'))
async def limit_vless(event):
	async def limit_vless_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username :**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Limit Ip :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
			await event.edit("**Loading......**")
			cmd = f'printf "%s\n" "{user}" "{pw}" | bot-ganti-ip-vless'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"`{user}` **Succesfully Change Limit IP**")
		else:
			await event.respond(f"""
```
{a}
```
**GANTI IP vless**
**» 🤖@amqyu**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await limit_vless_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)

@bot.on(events.CallbackQuery(data=b'quota-vless'))
async def quota_vless(event):
	async def quota_vless_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username :**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Limit Quota :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
			await event.edit("**Loading......**")
			cmd = f'printf "%s\n" "{user}" "{pw}" | bot-quota-vl'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"`{user}` **Succesfully Change Limit Quota**")
		else:
			await event.respond(f"""
```
{a}
```
**GANTI QUOTA vless**
**» 🤖@amqyu**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await quota_vless_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)

@bot.on(events.CallbackQuery(data=b'lock-vless'))
async def lock_vless(event):
	async def lock_vless_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Username:**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		await event.edit("**Loading......**")
		cmd = f'printf "%s\n" "{exp}" | bot-lock-vl'
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
		await lock_vless_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)
#UNLOCK ssh
@bot.on(events.CallbackQuery(data=b'unlock-vless'))
async def unlock_vless(event):
	async def unlock_vless_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Username :**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		await event.edit("**Loading......**")
		cmd = f'printf "%s\n" "{exp}" | bot-unlock-vl'
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
		await unlock_vless_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)
		

@bot.on(events.CallbackQuery(data=b'vless'))
async def vless(event):
    async def vless_(event):
        inline = [
            [Button.inline("𝗧𝗿𝗶𝗮𝗹", "trial-vless"),
             Button.inline("𝗖𝗿𝗲𝗮𝘁𝗲", "create-vless")],
            [Button.inline("𝗖𝗵𝗲𝗰𝗸 𝗨𝘀𝗲𝗿 𝗟𝗼𝗴𝗶𝗻", "cek-vless")],
            [Button.inline("𝗥𝗲𝗻𝗲𝘄", "renew-vless"),
             Button.inline("𝗗𝗲𝗹𝗲𝘁𝗲", "delete-vless")],
            [Button.inline("𝗟𝗶𝘀𝘁 𝗺𝗲𝗺𝗯𝗲𝗿", "cek-membervl")],
            [Button.inline("𝗟𝗼𝗰𝗸", "lock-vless"),
             Button.inline("𝗨𝗻𝗹𝗼𝗰𝗸", "unlock-vless")],
            [Button.inline("𝗖𝗵𝗮𝗻𝗴𝗲 𝗟𝗶𝗺𝗶𝘁 𝗜𝗣", "limit-vless")],
            [Button.inline("𝗖𝗵𝗮𝗻𝗴𝗲 𝗟𝗶𝗺𝗶𝘁 𝗤𝘂𝗼𝘁𝗮", "quota-vless")],
             [Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
       **◇⟨VLESS SERVICE⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**  Service:** `VLESS`
**  Hostname/IP:** `{DOMAIN}`
**  ISP:** `{z["isp"]}`
**  Country:** `{z["country"]}`
**» ** 🤖@amqyu
**◇━━━━━━━━━━━━━━━━━◇**
"""
        await event.edit(msg, buttons=inline)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await vless_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)

