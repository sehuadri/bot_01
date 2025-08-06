from public import *
#CEK VMESS
@bot.on(events.CallbackQuery(data=b'info'))
async def info_vps(event):
	async def info_vps_(event):
		cmd = 'bot-vps-info'.strip()
		
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""```{z}```
🤖@amqyu
""",buttons=[[Button.inline(" 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂 ","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await info_vps_(event)
	else:
		await event.answer("Buy Premium Chat: @amqyu",alert=True)