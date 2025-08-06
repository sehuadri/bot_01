from public import *
import requests
import time
import subprocess
import re
from telethon import events, Button

@bot.on(events.CallbackQuery(data=b'create-shadowsocks'))
async def create_shadowsocks(event):
    user_id = str(event.sender_id)

    async def create_shadowsocks_(event):
        try:
            async with bot.conversation(chat) as user_conv:
                await event.respond('**Username :**')
                user_msg = user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                user = (await user_msg).raw_text

            async with bot.conversation(chat) as exp_conv:
                await event.respond('**Expired :**')
                exp_msg = exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                exp = (await exp_msg).raw_text
   
            
            async with bot.conversation(chat) as ip_limit_conv:
                await event.respond('**Limit Quota :**')
                ip_limit_msg = ip_limit_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                ip_limit = (await ip_limit_msg).raw_text
                      
                      
            async with bot.conversation(chat) as Quota_conv:
                await event.respond('**Limit Ip :**')
                Quota_msg = Quota_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                Quota = (await Quota_msg).raw_text
                 
            await event.edit("**Loading......**")    
            cmd = f'printf "%s\n" "{user}" "{exp}" "{ip_limit}" "{Quota}" | addss-bot'

            a = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode("utf-8")

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            print(f"Exit code: {e.returncode}")
            print(f"Output: {e.output.decode('utf-8')}")
            await event.respond(f"Error executing command: {e}")
            return  # Stop execution to prevent further processing on error

        except Exception as ex:
            print(f"Unexpected error: {ex}")
            await event.respond("An unexpected error occurred.")
            return  # Stop execution to prevent further processing on error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        x = [x.group() for x in re.finditer("ss://(.*)", a)]
        uuid = re.search("ss://(.*?)@", x[0]).group(1)

        msg = f"""
        
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨SHDOWSOCKS ACCOUNT⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Username :** `{user}`
**» Domain :** `{DOMAIN}`
**» Limit Quota :** `{ip_limit} GB`
**» Limit Login :** `{Quota} HP`
**» HTTP   :** `80,8080,2086,8880`
**» TLS    :** `443,8443`
**» UUID    :** `{uuid}`
**» NetWork     :** `(WS) or (gRPC)`
**» Path        :** `/ss-ws`
**» ServiceName :** `ss-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» URL TLS    :**
```{x[0]}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL HTTP   :** 
```{x[1].replace(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL gRPC   :** 
```{x[2].replace(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨Link Save Account⟩◇**
https://{DOMAIN}:81/ss-{user}.txt
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
»  🤖@amqyu

        """

        await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await create_shadowsocks_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)





@bot.on(events.CallbackQuery(data=b'cek-shadowsocks'))
async def cek_shadowsocks(event):
    user_id = str(event.sender_id)
    async def cek_shadowsocks_(event):
        cmd = 'cek-mss'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""
        
        {z}

**Shows Users Shadowsocks in database**
        """, buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "menu")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await cek_shadowsocks_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)




@bot.on(events.CallbackQuery(data=b'cek-shadowsocks-online'))
async def cek_shadowsocks(event):
    async def cek_shadowsocks_(event):
        cmd = 'cek-ss'.strip()
        result = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True, env={"TERM": "xterm"}
        )

        # Hapus karakter escape ANSI
        clean_result = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', result).strip()

        await event.edit(f"""
**◇━━━━━━━━━━━━━━━━━━◇**
** ◇⟨Cek Shdwsk User Login⟩◇**
**◇━━━━━━━━━━━━━━━━━━◇**
{clean_result}

**Shows Logged In Users shadowsocks**
""", buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "shadowsocks")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await cek_shadowsocks_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)



@bot.on(events.CallbackQuery(data=b'delete-shadowsocks'))
async def delete_shadowsocks(event):
    async def delete_shadowsocks_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username :**')
            user_event = user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user_text = (await user_event).raw_text
        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{user_text}" | bot-del-ss'
        try:
            output = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except subprocess.CalledProcessError:
            await event.respond("**Successfully Deleted**")
        else:
            msg = "**Successfully Deleted**"
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await delete_shadowsocks_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)







@bot.on(events.CallbackQuery(data=b'trial-shadowsocks'))
async def trial_shadowsocks(event):
    user_id = str(event.sender_id)
    async def trial_shadowsocks_(event):
        

        try:
            await event.edit("**Loading......**")
            cmd = f'printf "%s\n" "TrialSS`</dev/urandom tr -dc X-Z0-9 | head -c4`" "1" "1" "1" | bot-trialshd'
            a = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode("utf-8")

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            print(f"Exit code: {e.returncode}")
            print(f"Output: {e.output.decode('utf-8')}")
            await event.respond(f"Error executing command: {e}")
            return  # Stop execution to prevent further processing on error

        except Exception as ex:
            print(f"Unexpected error: {ex}")
            await event.respond("An unexpected error occurred.")
            return  # Stop execution to prevent further processing on error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(1))
        x = [x.group() for x in re.finditer("ss://(.*)", a)]
        uuid = re.search("ss://(.*?)@", x[0]).group(1)
        remarks = re.search("#(.*)", x[0]).group(1)

        msg = f"""
        
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨TRIAL SHDWSK ACCOUNT⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Username :** `{remarks}`
**» Host Server :** `{DOMAIN}`
**» HTTP   :** `80,8080,2086,8880`
**» TLS    :** `443,8443`
**» UUID    :** `{uuid}`
**» NetWork     :** `(WS) or (gRPC)`
**» Path        :** `/ss-ws`
**» ServiceName :** `ss-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» URL TLS    :**
```{x[0]}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL HTTP   :** 
```{x[1].replace(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL gRPC   :** 
```{x[2].replace(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨Link Save Account⟩◇**
https://{DOMAIN}:81/ss-{remarks}.txt
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
        await trial_shadowsocks_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)

@bot.on(events.CallbackQuery(data=b'renew-ss-ws'))
async def ren_ss(event):
    async def ren_ss_(event):
        chat = event.chat_id
        sender = await event.get_sender()

        # Check if the user is valid before continuing
        a = valid(str(sender.id))
        if a != "true":
            await event.answer("Buy Premium Chat: @amqyu", alert=True)
            return

        # Get user input for Username, Expiry, IP limit, and Quota
        async with bot.conversation(chat) as conv:
            await event.respond('**Username :**')
            user_msg = await conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = user_msg.raw_text

            await event.respond('**Expired :**')
            exp_msg = await conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = exp_msg.raw_text

            await event.respond('**Limit Quota :**')
            ip_msg = await conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip = ip_msg.raw_text

            await event.respond('**Limit Ip :**')
            quota_msg = await conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            quota = quota_msg.raw_text

        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{user}" "{exp}" "{ip}" "{quota}" | bot-renew-ss'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except subprocess.CalledProcessError:
            await event.respond("**Succesfully Renew User**")
        else:
            msg = f"""
**{user} {exp} Days, limit IP {ip}, limit Quota {quota} GB**
"""
            await event.respond(msg)

    # Call the renew function
    await ren_ss_(event)

@bot.on(events.CallbackQuery(data=b'limit-shadowsocks'))
async def limit_shadowsocks(event):
	async def limit_shadowsocks_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username :**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Limit IP :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
			await event.edit("**Loading......**")
			cmd = f'printf "%s\n" "{user}" "{pw}" | bot-ganti-ip-ss'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"`{user}` **Succesfully Change Limit IP**")
		else:
			await event.respond(f"""
```
{a}
```
**GANTI IP shadowsocks**
**» 🤖@amqyu**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await limit_shadowsocks_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)

@bot.on(events.CallbackQuery(data=b'quota-shadowsocks'))
async def quota_shadowsocks(event):
	async def quota_shadowsocks_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username :**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Limit Quota :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
			await event.edit("**Loading......**")
			cmd = f'printf "%s\n" "{user}" "{pw}" | bot-quota-shd'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"`{user}` **Succesfully Change Limit Quota**")
		else:
			await event.respond(f"""
```
{a}
```
**GANTI QUOTA shadowsocks**
**» 🤖@amqyu**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await quota_shadowsocks_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)

@bot.on(events.CallbackQuery(data=b'lock-shadowsocks'))
async def lock_shadowsocks(event):
	async def lock_shadowsocks_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Username :**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		await event.edit("**Loading......**")
		cmd = f'printf "%s\n" "{exp}" | bot-lock-shd'
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
		await lock_shadowsocks_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)
#UNLOCK ssh
@bot.on(events.CallbackQuery(data=b'unlock-shadowsocks'))
async def unlock_shadowsocks(event):
	async def unlock_shadowsocks_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Username :**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		await event.edit("**Loading......**")
		cmd = f'printf "%s\n" "{exp}" | bot-unlock-shd'
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
		await unlock_shadowsocks_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)




@bot.on(events.CallbackQuery(data=b'shadowsocks'))
async def shadowsocks(event):
    user_id = str(event.sender_id)

    async def shadowsocks_(event):
        inline = [
            [Button.inline("𝗧𝗿𝗶𝗮𝗹", "trial-shadowsocks"),
             Button.inline("𝗖𝗿𝗲𝗮𝘁𝗲", "create-shadowsocks")],
            [Button.inline("𝗖𝗵𝗲𝗰𝗸 𝗨𝘀𝗲𝗿 𝗟𝗼𝗴𝗶𝗻", "cek-shadowsocks-online")],
            [Button.inline("𝗥𝗲𝗻𝗲𝘄", "renew-ss-ws"),
            Button.inline("𝗗𝗲𝗹𝗲𝘁𝗲", "delete-shadowsocks")],
            [Button.inline("𝗟𝗶𝘀𝘁 𝗠𝗲𝗺𝗯𝗲𝗿", "cek-shadowsocks")],
            [Button.inline("𝗟𝗼𝗰𝗸", "lock-shadowsocks"),
            Button.inline("𝗨𝗻𝗹𝗼𝗰𝗸", "unlock-shadowsocks")],
            [Button.inline("𝗖𝗵𝗮𝗻𝗴𝗲 𝗟𝗶𝗺𝗶𝘁 𝗜𝗣", "limit-shadowsocks")],
            [Button.inline("𝗖𝗵𝗮𝗻𝗴𝗲 𝗟𝗶𝗺𝗶𝘁 𝗤𝘂𝗼𝘁𝗮", "quota-shadowsocks")],
            [Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "menu")]]
        
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨SHADOWSOCKS SERVICE⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
» Service: `SHADOWSOCKS`
» Hostname/IP: `{DOMAIN}`
» ISP: `{z["isp"]}`
» Country: `{z["country"]}`
**» ** 🤖@amqyu
**◇━━━━━━━━━━━━━━━━━◇**
"""

        await event.edit(msg, buttons=inline)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await shadowsocks_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)


