import COVID19Py
import telebot
covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('5245972981:AAH-487AyE0XdpUv4nXQnT4g-hDChBuNeh8')


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Hello {message.from_user.first_name}!</b>\n Enter country"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")

    else:
        location = covid19.getLatest()
        final_message = f"<u>Сам такой</u>\n<b>Infected: </b>{location['confirmed']}\n"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                        f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
                        f"{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)



