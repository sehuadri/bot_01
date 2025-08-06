from public import *
import subprocess
import json
import re
import base64
import datetime as DT
import requests
import time
import random
import asyncio
import tempfile
################

@bot.on(events.CallbackQuery(data=b'create-noobz'))
async def create_noobz(event):
    async def create_noobz_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username :**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        
        async with bot.conversation(chat) as pw:
            await event.respond('**Password :**')
            pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            pw = (await pw).raw_text
            
        async with bot.conversation(chat) as exp:
            await event.respond('**Expired :**')
            exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = (await exp).raw_text

        async with bot.conversation(chat) as ip:
            await event.respond('**Limit Quota:**')
            ip = ip.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip = (await ip).raw_text

        async with bot.conversation(chat) as Quota:
            await event.respond('**Limit Ip:**')
            Quota = Quota.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            Quota = (await Quota).raw_text

        
        

        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{user}" "{pw}" "{exp}" "{ip}" "{Quota}" | addnoobz'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"An error occurred: {e}\nSubprocess output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        

        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
   ** ◇⟨Noobzvpn Account⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Host:** `{DOMAIN}`
**» Username:** `{user}`
**» Password:** `{pw}`
**» Limit Login:** `{ip} HP`
**» Limit Quota:** `{Quota} GB`
**◇━━━━━━━━━━━━━━━━━◇**
**» PORT:** `2082`
**» PORT:** `2083`
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨ Payload WS  ⟩◇**
```GET / HTTP/1.1[crlf]Host: [s_host][crlf]Upgrade: websocket[crlf]Connection: Upgrade[crlf]User-Agent: [ua][crlf][crlf]```
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Akun User:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
        """

        await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await create_noobz_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)


@bot.on(events.CallbackQuery(data=b'trial-noobz'))
async def create_noobz(event):
    async def create_noobz_(event):
        async with bot.conversation(chat) as user:
            user = "trialX" + str(random.randint(100, 1000))
            pw = "freenetlite"
            exp = "1"
            ip = "1"
            Quota = "1"        

        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{user}" "{pw}" "{exp}" "{ip}" "{Quota}" | addnoobz'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"An error occurred: {e}\nSubprocess output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        

        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
** ◇⟨Trial Noobzvpn Account⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Host:** `{DOMAIN}`
**» Username:** `{user}`
**» Password:** `{pw}`
**» Limit Login:** `{ip} HP`
**» Limit Quota:** `{Quota} GB`
**◇━━━━━━━━━━━━━━━━━◇**
**» PORT:** `2082`
**» PORT:** `2083`
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨ Payload WS  ⟩◇**
```GET / HTTP/1.1[crlf]Host: [s_host][crlf]Upgrade: websocket[crlf]Connection: Upgrade[crlf]User-Agent: [ua][crlf][crlf]```
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Akun User:** `{today}`
**◇━━━━━━━━━━━━━━━━━◇**
        """

        await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await create_noobz_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)


@bot.on(events.CallbackQuery(data=b'cek-noobz'))
async def cek_vmess(event):
    async def cek_noobz_(event):
        cmd = 'cek-noobz'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""
**◇━━━━━━━━━━━━━━━━━━◇**
   ** ◇⟨Cek Noobz Account⟩◇**
**◇━━━━━━━━━━━━━━━━━━◇**
{z}

**Shows Users noobzvpns in databases**
""", buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "noobzvpns")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await cek_noobz_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)



##########



@bot.on(events.CallbackQuery(data=b'delete-noobz'))
async def delete_noobz(event):
    async def delete_noobz_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username :**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        await event.edit("**Loading......**")
        cmd = f'noobzvpns --remove-user {user}'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Deleted {user} **"""
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await delete_noobz_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)
        

###################


@bot.on(events.CallbackQuery(data=b'block-noobz'))
async def block_noobz(event):
    async def block_noobz_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username :**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        await event.edit("**Loading......**")
        cmd = f'noobzvpns --block-user {user}'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully blocked {user} **"""
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await block_noobz_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)




###################



@bot.on(events.CallbackQuery(data=b'unblock-noobz'))
async def unblock_noobz(event):
    async def unblock_noobz_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username :**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        await event.edit("**Loading......**")
        cmd = f'noobzvpns --unblock-user {user}'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully blocked {user} **"""
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await unblock_noobz_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)




####################


@bot.on(events.CallbackQuery(data=b'renew-noobz'))
async def ren_vmess(event):
    async def ren_noobz_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username :**')
            user = await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = user.raw_text

        async with bot.conversation(chat) as exp_conv:
            await event.respond('**Expired :**')
            exp = await exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = exp.raw_text
            

        await event.edit("**Loading......**") 
        cmd = f'noobzvpns --renew-user {user} --expired-user {user} {exp}'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Renewed  {user} {exp} Days**"""
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Memanggil fungsi valid

    if a == "true":
        await ren_noobz_(event)
    else:
        await event.answer("Buy Premium Chat: @Amiqyu", alert=True)



@bot.on(events.CallbackQuery(data=b'noobzvpns'))
async def vmess(event):
    async def vmess_(event):
        inline = [
            [Button.inline("𝗧𝗿𝗶𝗮𝗹", "trial-noobz"), Button.inline("𝗖𝗿𝗲𝗮𝘁𝗲", "create-noobz")],
            [Button.inline("𝗥𝗲𝗻𝗲𝘄", "renew-noobz"), Button.inline("𝗗𝗲𝗹𝗲𝘁𝗲", "delete-noobz")],
            [Button.inline("𝗖𝗵𝗲𝗰𝗸 𝗨𝘀𝗲𝗿 𝗟𝗼𝗴𝗶𝗻", "cek-noobz")],
            [Button.inline("𝗟𝗼𝗰𝗸", "block-noobz"), Button.inline("𝗨𝗻𝗹𝗼𝗰𝗸", "unblock-noobz")],
            [Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
   **◇⟨NOOBZVPNS SERVICE⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Service:** `NOOBZVPNS`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
**» **🤖@Amiqyu
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


