from get_bot import get_bot
from wakeonlan import send_magic_packet

bot = get_bot()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Usage: send mac+ip (yes, with plus)")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Example: 0a:00:aa:00:00:aa+8.8.8.8")


@bot.message_handler(regexp="^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})\+(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
def send_welcome(message):
    message_arr = message.text.split('+')
    mac = message_arr[0]
    ip = message_arr[1]
    send_magic_packet(mac, ip_address=ip)
    bot.reply_to(message, "magic packet was sent")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "it's not a valid 'mac+ip' combination")


if __name__ == '__main__':
    bot.polling()
