from private import *
import subprocess
from telethon import events, Button
import asyncio
import os

@bot.on(events.NewMessage(pattern='/cancel'))
async def cancel_command(event):
    sender = await event.get_sender()
    user_id = str(sender.id)

    if valid(user_id) != "true":
        await event.reply("Buy Premium Chat: @amqyu")
        return

    await event.reply(
        "**❌ Operasi dibatalkan.**",
        buttons=[[Button.inline("‹ 𝗠𝗲𝗻𝘂 ›", b"menu")]]
    )
    
    
@bot.on(events.CallbackQuery(data=b'reboot'))
async def rebooot(event):
	async def rebooot_(event):
		await event.edit("**Loading......**")
		cmd = f'reboot'
		
		subprocess.check_output(cmd, shell=True)
		await event.edit(f"""
**» REBOOT SERVER**
**» 🤖@amqyu**"""
    ,buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await rebooot_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)


@bot.on(events.CallbackQuery(data=b'resx'))
async def rebooot(event):
	async def rebooot_(event):
		cmd = f'bot-restart'
		await asyncio.sleep(5)
		await event.edit("**✅ Successfully Restart All Service**")
		
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.edit(f"""
**{z}**
**» 🤖@amqyu**"""
    ,buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await rebooot_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)
        

@bot.on(events.CallbackQuery(data=b'speedtest'))
async def speedtest(event):
	async def speedtest_(event):
		await event.edit("**Loading......**")
		cmd = 'speedtest-cli --share'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")

		await event.respond(f"""
**
{z}
**
**» 🤖@amqyu**
""",buttons=[[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await speedtest_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)

@bot.on(events.CallbackQuery(data=b'setup_backup'))
async def set_backupbot(event):
    sender = await event.get_sender()
    user_id = str(sender.id)

    # Validasi user yang boleh set token & id (hanya admin)
    if valid(user_id) != "true":
        await event.answer("❌ Akses ditolak. Hubungi admin: @amqyu", alert=True)
        return

    async with bot.conversation(event.chat_id) as user:
        await event.respond('**Input Bot Token :**')
        token_input = await user.wait_event(events.NewMessage(incoming=True, from_users=event.sender_id))
        token = token_input.raw_text.strip()

        await event.respond('**Input Telegram ID :**')
        id_input = await user.wait_event(events.NewMessage(incoming=True, from_users=event.sender_id))
        admin_id = id_input.raw_text.strip()

        # Pastikan direktori /root ada (biasanya sudah ada, tapi untuk jaga-jaga)
        try:
            os.makedirs("/root", exist_ok=True)

            with open("/root/.bckupbot", "w") as f:
                f.write(f"{token}\n{admin_id}\n")

            await event.respond("**✅ Token dan ID berhasil disimpan.**")
        except Exception as e:
            await event.respond(f"**❌ Gagal menyimpan data:**\n`{e}`")
            
     
@bot.on(events.CallbackQuery(data=b'backup'))
async def run_backupku(event):
    sender = await event.get_sender()
    user_id = str(sender.id)

    if valid(user_id) != "true":
        await event.answer("Buy Premium Chat: @amqyu", alert=True)
        return

    if not os.path.exists("/root/.bckupbot"):
        await event.respond("**❗ Token dan ID belum disetel.**\nSilahkan atur terlebih dahulu di menu *Atur Setup Backup*.")
        return

    try:
        with open("/root/.bckupbot", "r") as f:
            lines = f.readlines()
            if len(lines) < 2 or not lines[0].strip() or not lines[1].strip():
                raise ValueError("Isi file tidak lengkap.")
            token = lines[0].strip()
            admin_id = lines[1].strip()
    except Exception as e:
        await event.respond(f"**❌ Gagal membaca data token/id:**\n`{e}`\nSilakan atur ulang di menu *Atur Setup Backup*.")
        return

    await event.edit("**Please Wait...**")

    # Jalankan skrip dan ambil output (link)
    try:
        output = subprocess.check_output("cadangkan-bot", shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()

        # Debugging: log output
        print(f"Output: {output}")

        # Jika output mengandung "http", anggap itu adalah link
        if "http" in output:
            await event.respond(f"**✅ Backup Successfully**\n\n", link_preview=False)
        else:
            await event.respond(f"**Backup berhasil tapi link tidak ditemukan. Output:\n{output}**")

    except subprocess.CalledProcessError as e:
        error_message = e.output.decode("utf-8")
        await event.respond(f"**❌ Backup gagal:**\n```{error_message}```")
        

@bot.on(events.CallbackQuery(data=b'restore'))
async def restore(event):
    async def restore_(event):
        async with bot.conversation(event.chat_id) as user:
            await event.respond('**Input Link Backup :**')
            user_input = await user.wait_event(events.NewMessage(incoming=True, from_users=event.sender_id))
            backup_link = user_input.raw_text
        await event.edit("**Loading......**")
        cmd = f'printf "%s\n" "{backup_link}" | bot-restore'
        try:
            restore_output = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except subprocess.CalledProcessError:
            await event.respond("**Link Not Exist**")
        else:
            msg = f"""```{restore_output}```
**🤖@amqyu**"""
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()
    
    # Validate user permission
    a = valid(str(sender.id))
    if a == "true":
        await restore_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)
        
		
@bot.on(events.CallbackQuery(data=b'backer'))
async def backers(event):
	async def backers_(event):
		inline = [
[Button.inline("𝗦𝗲𝘁𝘂𝗽 𝗕𝗮𝗰𝗸𝘂𝗽","setup_backup")],
[Button.inline("𝗥𝗲𝘀𝘁𝗼𝗿𝗲","restore"),
Button.inline("𝗕𝗮𝗰𝗸𝘂𝗽","backup")],
[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨MENU BACKUP & RESTORE⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
** » Domain:** `{DOMAIN}`
** » ISP:** `{z["isp"]}`
** » Region:** `{z["country"]}`
**🤖 »**@amqyu
**◇━━━━━━━━━━━━━━━━━◇**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await backers_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)

@bot.on(events.CallbackQuery(data=b'setting'))
async def settings(event):
	async def settings_(event):
		inline = [
[Button.inline("𝗕𝗮𝗰𝗸𝘂𝗽 & 𝗥𝗲𝘀𝘁𝗼𝗿𝗲","backer")],
[Button.inline("𝗦𝗽𝗲𝗲𝗱𝘁𝗲𝘀𝘁","speedtest")],
[Button.inline("𝗥𝗲𝗯𝗼𝗼𝘁 𝘀𝗲𝗿𝘃𝗲𝗿","reboot"),
Button.inline("𝗥𝗲𝘀𝘁𝗮𝗿𝘁 𝗦𝗲𝗿𝘃𝗲𝗿","resx")],
[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
       **◇⟨MENU SETTINGS⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
** » Domain:** `{DOMAIN}`
** » ISP:** `{z["isp"]}`
** » Region:** `{z["country"]}`
**🤖 »**@amqyu
**◇━━━━━━━━━━━━━━━━━◇**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await settings_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)
