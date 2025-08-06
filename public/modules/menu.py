from public import *
import subprocess
import requests

@bot.on(events.NewMessage(pattern=r"(?:.menu|/menu)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def menu(event):
    # Inline button
    inline = [
        [Button.inline(" 𝗦𝗦𝗛 ", "ssh"), Button.inline(" 𝗩𝗺𝗲𝘀𝘀 ", "vmess")],
        [Button.inline(" 𝗩𝗹𝗲𝘀𝘀 ", "vless"), Button.inline(" 𝗧𝗿𝗼𝗷𝗮𝗻 ", "trojan")], 
        [Button.inline(" 𝗦𝗵𝗮𝗱𝗼𝘄𝘀𝗼𝗰𝗸𝘀 ", "shadowsocks"), Button.inline(" 𝗡𝗼𝗼𝗯𝘇𝘃𝗽𝗻𝘀 ", "noobzvpns")],
        [Button.inline(" 𝗜𝗻𝗳𝗼 ", "info")],
        [Button.inline(" ‹ 𝗕𝗮𝗰𝗸 𝗧𝗼 𝗦𝘁𝗮𝗿𝘁 › ", "start")]
    ]

    sender = await event.get_sender()
    val = valid(str(sender.id))

    if val == "false":
        try:
            await event.answer("Buy Premium Chat: @Amiqyu", alert=True)
        except:
            await event.reply("Buy Premium Chat: @Amiqyu")
        return

    elif val == "true":
        try:
            # Collecting data
            ssh = subprocess.check_output('cat /etc/passwd | grep "home" | grep "false" | wc -l', shell=True).decode("ascii").strip()
            vms = subprocess.check_output('cat /etc/xray/config.json | grep "###" | wc -l', shell=True).decode("ascii").strip()
            vls = subprocess.check_output('cat /etc/xray/config.json | grep "#&" | wc -l', shell=True).decode("ascii").strip()
            trj = subprocess.check_output('cat /etc/xray/config.json | grep "#!" | wc -l', shell=True).decode("ascii").strip()
            shadowsocks = subprocess.check_output('cat /etc/xray/config.json | grep "#@&" | wc -l', shell=True).decode("ascii").strip()
            namaos = subprocess.check_output("cat /etc/os-release | grep -w PRETTY_NAME | head -n1 | sed 's/\"//g' | sed 's/PRETTY_NAME=//g'", shell=True).decode("ascii").strip()
            ipsaya = subprocess.check_output("curl -s ipv4.icanhazip.com", shell=True).decode("ascii").strip()
            z = requests.get("http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()

        except subprocess.CalledProcessError as e:
            await event.reply(f"Error collecting data: {e.output.decode()}")
            return

        # Membagi hasil dengan 2
        vms_half = int(vms) // 2
        vls_half = int(vls) // 2
        trj_half = int(trj) // 2
        shadowsocks_half = int(shadowsocks) // 1
        ssh_half = int(ssh) // 2

        # Building the message
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨ROBOT PUBLIC MENU⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» 𝙾𝚜**     : `{namaos}`
**» 𝙸𝚂𝙿**: `{z["isp"]}`
**» 𝙻𝚘𝚌𝚊𝚝𝚒𝚘𝚗**: `{z["country"]}`
**» 𝙳𝚘𝚖𝚊𝚒𝚗**: `{DOMAIN}`
**» 𝙸𝙿 𝙰𝚍𝚍𝚛𝚎𝚜**: `{ipsaya.strip()}`
**» 𝚃𝚘𝚝𝚊𝚕 𝙰𝚌𝚌𝚘𝚞𝚗𝚝**: 

**» 𝚂𝚜𝚑**: `{ssh}` __account__
**» 𝚅𝚖𝚎𝚜𝚜**: `{vms_half}` __account__
**» 𝚅𝚕𝚎𝚜𝚜**: `{vls_half}` __account__
**» 𝚃𝚛𝚘𝚓𝚊𝚗**: `{trj_half}` __account__
**» 𝚂𝚑𝚊𝚍𝚘𝚠𝚜𝚘𝚌𝚔𝚜**: `{shadowsocks_half}` __account__
**◇━━━━━━━━━━━━━━━━━◇**
"""
        # Sending the message with inline buttons
        x = await event.edit(msg, buttons=inline)
        if not x:
            await event.reply(msg, buttons=inline)
