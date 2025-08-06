from private import *
import subprocess
import re
from telethon import events, Button

@bot.on(events.CallbackQuery(data=b'create-vmess'))
async def create_vmess(event):
    async def create_vmess_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username :**')
            user = (await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text

        async with bot.conversation(chat) as exp_conv:
            await event.respond('**Expired :**')
            exp = (await exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text

        async with bot.conversation(chat) as ip_conv:
            await event.respond('**Limit Quota :**')
            ip = (await ip_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text

        async with bot.conversation(chat) as Quota_conv:
            await event.respond('**Limit Ip :**')
            Quota = (await Quota_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text
         
        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{user}" "{exp}" "{ip}" "{Quota}" | addws-bot'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"An error occurred: {e}\nSubprocess output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        b = [x.group() for x in re.finditer("vmess://(.*)", a)]

        z = base64.b64decode(b[0].replace("vmess://", "")).decode("ascii")
        z = json.loads(z)

        z1 = base64.b64decode(b[1].replace("vmess://", "")).decode("ascii")
        z1 = json.loads(z1)

        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
     **  ◇⟨VMESS ACCOUNT⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Username :** `{user}`
**» Domain :** `{DOMAIN}`
**» Limit Quota :** `{ip} GB`
**» Limit Login :** `{Quota} HP`
**» HTTP   :** `80,8080,2086,8880`
**» TLS    :** `443,8443`
**» UUID    :** `{z["id"]}`
**» Network     :** `(WS) or (gRPC)`
**» Path        :** `/vmess`
**» ServiceName :** `vmess-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» URL TLS    :**
```{b[0].strip("'").replace(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL HTTP    :**
```{b[1].strip("'").replace(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL gRPC   :** 
```{b[2].strip("'")}```
**◇━━━━━━━━━━━━━━━━━◇**
**⟨Link Save Account⟩**
https://{DOMAIN}:81/vmess-{user}.txt
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ** 🤖@Amiqyu


        """

        await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await create_vmess_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)


@bot.on(events.CallbackQuery(data=b'trial-vmess'))
async def trial_vmess(event):
    async def trial_vmess_(event):
      
        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "TrialVM`</dev/urandom tr -dc X-Z0-9 | head -c4`" "1" "1" "1" | bot-trialvmess'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"An error occurred: {e}\nSubprocess output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=1)  # You may need to adjust this, as "exp" is not defined in the scope
        b = [x.group() for x in re.finditer("vmess://(.*)", a)]

        z = base64.b64decode(b[0].replace("vmess://", "")).decode("ascii")
        z = json.loads(z)

        z1 = base64.b64decode(b[1].replace("vmess://", "")).decode("ascii")
        z1 = json.loads(z1)
        
        remarks = z.get("ps", "N/A")

        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨TRIAL VMESS ACCOUNT⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Username :** `{remarks}`
**» Host Server :** `{DOMAIN}`
**» HTTP   :** `80,8080,2086,8880`
**» TLS    :** `443,8443`
**» UUID    :** `{z["id"]}`
**» NetWork     :** `(WS) or (gRPC)`
**» Path        :** `/vmess`
**» ServiceName :** `vmess-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» URL TLS    :**
```{b[0].strip("'").replace(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL HTTP    :**
```{b[1].strip("'").replace(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL gRPC   :** 
```{b[2].strip("'")}```
**◇━━━━━━━━━━━━━━━━━◇**
**⟨Link Save Account⟩**
https://{DOMAIN}:81/vmess-{remarks}.txt
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** 30 Minutes
**◇━━━━━━━━━━━━━━━━━◇**
**» ** 🤖@Amiqyu
        """
        await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await trial_vmess_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)
        

#CEK VMESS
@bot.on(events.CallbackQuery(data=b'cek-vmess'))
async def cek_vmess(event):
    async def cek_vmess_(event):
        cmd = 'cek-ws'.strip()
        result = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True, env={"TERM": "xterm"}
        )

        # Hapus karakter escape ANSI
        clean_result = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', result).strip()

        await event.edit(f"""
**◇━━━━━━━━━━━━━━━━━━◇**
 ** ◇⟨Cek Vmess User Login⟩◇**
**◇━━━━━━━━━━━━━━━━━━◇**
{clean_result}

**Shows Logged In Users Vmess**
""", buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "vmess")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await cek_vmess_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)



## CEK member VMESS
@bot.on(events.CallbackQuery(data=b'cek-member'))
async def cek_vmess(event):
    async def cek_vmess_(event):
        cmd = 'bash cek-mws'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""

{z}

**Shows Users from databases**
""", buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "vmess")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await cek_vmess_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)





@bot.on(events.CallbackQuery(data=b'delete-vmess'))
async def delete_vmess(event):
    async def delete_vmess_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
            await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{user}" | bot-del-vme'
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
        await delete_vmess_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)
        

@bot.on(events.CallbackQuery(data=b'renew-vmess'))
async def ren_vmess(event):
    async def ren_vmess_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username :**')
            user = await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = user.raw_text

        async with bot.conversation(chat) as exp_conv:
            await event.respond('**Expired :**')
            exp = await exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = exp.raw_text
            
        async with bot.conversation(chat) as ip_conv:
            await event.respond('**Limit Quota:**')
            ip = await ip_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip = ip.raw_text
            
        async with bot.conversation(chat) as Quota_conv:
            await event.respond('**Limit Ip :**')
            Quota = await Quota_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            Quota = Quota.raw_text         
    
        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{user}" "{exp}" "{ip}" "{Quota}" | bot-renew-vme'

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
        await ren_vmess_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)

@bot.on(events.CallbackQuery(data=b'limit-vmess'))
async def limit_vmess(event):
	async def limit_vmess_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username :**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Limit Ip :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
			await event.edit("**Loading......**")
			cmd = f'printf "%s\n" "{user}" "{pw}" | bot-ganti-ip-vmess'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"`{user}` **Succesfully Change Limit IP**")
		else:
			await event.respond(f"""
```
{a}
```
**GANTI IP VMESS**
**» 🤖@Amiqyu**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await limit_vmess_(event)
	else:
		await event.answer("Buy Premium Chat: @Amiqyu",alert=True)

@bot.on(events.CallbackQuery(data=b'quota-vmess'))
async def quota_vmess(event):
	async def quota_vmess_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username :**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Limit Quota :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
			await event.edit("**Loading......**")
			cmd = f'printf "%s\n" "{user}" "{pw}" | bot-quota-vm'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"`{user}` **Succesfully Change Limit Quota**")
		else:
			await event.respond(f"""
```
{a}
```
**GANTI QUOTA VMESS**
**» 🤖@Amiqyu**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await quota_vmess_(event)
	else:
		await event.answer("Buy Premium Chat: @Amiqyu",alert=True)

@bot.on(events.CallbackQuery(data=b'lock-vmess'))
async def lock_vmess(event):
	async def lock_vmess_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Username :**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		await event.edit("**Loading......**")
		cmd = f'printf "%s\n" "{exp}" | bot-lock-vm'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{exp}` **Successfully Locked**")
		else:
			msg = f"""**User** `{exp}` **Successfully Locked**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await lock_vmess_(event)
	else:
		await event.answer("Buy Premium Chat: @Amiqyu",alert=True)
#UNLOCK ssh
@bot.on(events.CallbackQuery(data=b'unlock-vmess'))
async def unlock_vmess(event):
	async def unlock_vmess_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Username :**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		await event.edit("**Loading......**")
		cmd = f'printf "%s\n" "{exp}" | bot-unlock-vm'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{exp}` **Successfully Unlocked**")
		else:
			msg = f"""**User** `{exp}` **Successfully Unlocked**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await unlock_vmess_(event)
	else:
		await event.answer("Buy Premium Chat: @Amiqyu",alert=True)
		
@bot.on(events.CallbackQuery(data=b'vmess'))
async def vmess(event):
    async def vmess_(event):
        inline = [
            [Button.inline("𝗧𝗿𝗶𝗮𝗹", "trial-vmess"),
             Button.inline("𝗖𝗿𝗲𝗮𝘁𝗲", "create-vmess")],
            [Button.inline("𝗖𝗵𝗲𝗰𝗸 𝗨𝘀𝗲𝗿 𝗟𝗼𝗴𝗶𝗻", "cek-vmess")],
            [Button.inline("𝗥𝗲𝗻𝗲𝘄", "renew-vmess"),
            Button.inline("𝗗𝗲𝗹𝗲𝘁𝗲", "delete-vmess")],
            [Button.inline("𝗟𝗶𝘀𝘁 𝗠𝗲𝗺𝗯𝗲𝗿", "cek-member")],
            [Button.inline("𝗟𝗼𝗰𝗸", "lock-vmess"),
            Button.inline("𝗨𝗻𝗹𝗼𝗰𝗸", "unlock-vmess")],
            [Button.inline("𝗖𝗵𝗮𝗻𝗴𝗲 𝗟𝗶𝗺𝗶𝘁 𝗜𝗣", "limit-vmess")],
            [Button.inline("𝗖𝗵𝗮𝗻𝗴𝗲 𝗟𝗶𝗺𝗶𝘁 𝗤𝘂𝗼𝘁𝗮", "quota-vmess")],
            [Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
   **    ◇⟨VMESS SERVICE⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Service:** `VMESS`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
**» ** 🤖@Amiqyu
**◇━━━━━━━━━━━━━━━━━◇**
"""
        await event.edit(msg, buttons=inline)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await vmess_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)



