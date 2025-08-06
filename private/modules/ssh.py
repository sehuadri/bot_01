from private import *

#LOCK ssh
@bot.on(events.CallbackQuery(data=b'lock-ssh'))
async def lock_ssh(event):
	async def lock_ssh_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Username:**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		
		cmd = f'printf "%s\n" "{exp}" | bot-lock'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{exp}` **Successfully Locked**")
		else:
			msg = f"**User** `{exp}` **Successfully Locked**"
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await lock_ssh_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)
#UNLOCK ssh
@bot.on(events.CallbackQuery(data=b'unlock-ssh'))
async def unlock_ssh(event):
	async def unlock_ssh_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Username:**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		
		cmd = f'printf "%s\n" "{exp}" | bot-unlock'
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
		await unlock_ssh_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)
#DELETESSH
@bot.on(events.CallbackQuery(data=b'delete-ssh'))
async def delete_ssh(event):
	async def delete_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username :**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
			cmd = f'printf "%s\n" "{user}" | bot-del-ssh'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{user}` **Successfully Deleted**")
		else:
			await event.respond(f"**Successfully Deleted** `{user}`")
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_ssh_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)
#RENEWSSH
@bot.on(events.CallbackQuery(data=b'recov-ssh'))
async def recov_ssh(event):
	async def recov_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username :**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Days :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as iplimit:
			await event.respond("**Ip Limit :**")
			iplimit = iplimit.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			iplimit = (await iplimit).raw_text
		async with bot.conversation(chat) as Quota:
			await event.respond("**Quota :**")
			Quota = Quota.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			Quota = (await Quota).raw_text
			cmd = f'printf "%s\n" "{user}" "{pw}" "{iplimit}" "{Quota}" | bot-renew-ssh'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"`{user}` **Succesfully Renewed**")
		else:
			await event.respond(f"""
```
{a}
```
**RENEW SSH**
**» 🤖@amqyu**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await recov_ssh_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)
        
#LIMITSSH
@bot.on(events.CallbackQuery(data=b'limit-ssh'))
async def limit_ssh(event):
	async def limit_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username :**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Limit-IP :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
			cmd = f'printf "%s\n" "{user}" "{pw}" | bot-ganti-ip-ssh'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"`{user}` **Succesfully Change Limit IP**")
		else:
			await event.respond(f"""
```
{a}
```
**CHANGE IP SSH**
**» 🤖@amqyu**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await limit_ssh_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)

@bot.on(events.CallbackQuery(data=b'quota-ssh'))
async def quota_ssh(event):
	async def quota_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username :**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Limit Quota :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
			cmd = f'printf "%s\n" "{user}" "{pw}" | bot-quota-ssh'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"`{user}` **Succesfully Change Limit Quota**")
		else:
			await event.respond(f"""
```
{a}
```
**CHANGE QUOTA SSH**
**» 🤖@amqyu**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await quota_ssh_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)


@bot.on(events.CallbackQuery(data=b'show-ssh'))
async def show_ssh(event):
    # Fungsi untuk menampilkan semua user SSH
    async def show_ssh_(event):
        try:
            # Perintah untuk mengambil semua user SSH dengan ID >= 1000
            cmd = "awk -F: '($3>=1000)&&($1!=\"nobody\"){print $1}' /etc/passwd"
            x = subprocess.check_output(cmd, shell=True).decode("ascii").split("\n")
            
            # Filter hasil yang tidak kosong
            users = [f"`{user}`" for user in x if user.strip()]
            users_list = "\n".join(users)
            
            # Jumlah total akun SSH
            total_users = len(users)

            # Kirim respon ke user
            await event.edit(f"""
**Showing All SSH Users**

{users_list}

**Total SSH Accounts:** `{total_users}`
""", buttons=[[Button.inline("‹ Main Menu ›", b"menu")]])

        except subprocess.CalledProcessError as e:
            await event.respond(f"Error while fetching SSH users:\n`{e}`", buttons=[[Button.inline("‹ Main Menu ›", b"menu")]])

    # Validasi apakah pengirim memiliki akses
    sender = await event.get_sender()
    a = valid(str(sender.id))  # Fungsi `valid()` harus tersedia
    if a == "true":
        await show_ssh_(event)
    else:
        await event.answer("Buy Premium Chat: @amqyu", alert=True)

		
@bot.on(events.CallbackQuery(data=b'login-ssh'))
async def login_ssh(event):
	async def login_ssh_(event):
		cmd = 'cek-ssh'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

**shows logged in users SSH Ovpn**
**» 🤖@amqyu**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await login_ssh_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)


@bot.on(events.CallbackQuery(data=b'ssh'))
async def ssh(event):
	async def ssh_(event):
		inline = [
[Button.inline("𝗧𝗿𝗶𝗮𝗹","trial-ssh"),
Button.inline("𝗖𝗿𝗲𝗮𝘁𝗲","create-akun")],
[Button.inline("𝗖𝗵𝗲𝗰𝗸 𝗨𝘀𝗲𝗿 𝗟𝗼𝗴𝗶𝗻","login-ssh")],
[Button.inline("𝗥𝗲𝗻𝗲𝘄","recov-ssh"),
Button.inline("𝗗𝗲𝗹𝗲𝘁𝗲","delete-ssh")],
[Button.inline("𝗟𝗶𝘀𝘁 𝗠𝗲𝗺𝗯𝗲𝗿","show-ssh")],
[Button.inline("𝗟𝗼𝗰𝗸","lock-ssh"),
Button.inline("𝗨𝗻𝗹𝗼𝗰𝗸","unlock-ssh")],
[Button.inline("𝗖𝗵𝗮𝗻𝗴𝗲 𝗟𝗶𝗺𝗶𝘁 𝗜𝗣","limit-ssh")],
[Button.inline("𝗖𝗵𝗮𝗻𝗴𝗲 𝗟𝗶𝗺𝗶𝘁 𝗤𝘂𝗼𝘁𝗮","quota-ssh")],
[Button.inline("‹ 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
  **       ◇⟨SSH SERVICE⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Service:** `SSH OVPN`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
**» 🤖@amqyu**
**◇━━━━━━━━━━━━━━━━━◇**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await ssh_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)
