from icrawler.builtin import GoogleImageCrawler
import os


@bot.message_handler(commands=['photo'])
def photos(message):

    def asking(message):
        mesg = bot.send_message(
            message.chat.id, 'Напишите кодовое слово и количество фото (не больше 10) тире. Например, "конфетка-3", мау')
        bot.register_next_step_handler(mesg, answer)

    def answer(message):
        l_i = list(message.text)
        l = len(l_i)
        ind = l_i.index('-')
        object = []
        amount = []
        for i in l_i[0:ind]:
            object.append(i)

        for i in l_i[ind+1:l]:
            amount.append(i)

        string_object = ''.join(object)
        string_amount = ''.join(amount)
        int_amout = int(string_amount)

        google_crawler_bot = GoogleImageCrawler(
            storage={'root_dir': 'C:/Users/79384/Desktop/telegram_bot'})
        dirname = 'C:/Users/79384/Desktop/telegram_bot'
        files_original = os.listdir(dirname)
        google_crawler_bot.crawl(keyword=string_object, max_num=int_amout)
        files_after_pars = os.listdir('C:/Users/79384/Desktop/telegram_bot')
        difference_1 = set(files_original).difference(set(files_after_pars))
        difference_2 = set(files_after_pars).difference(set(files_original))
        names_of_photos = list(difference_1.union(difference_2))
        i = 0
        l = len(names_of_photos)
        while i < l:
            bot.send_photo(message.chat.id, photo=open(
                f'{names_of_photos[i]}', 'rb'))
            i += 1
        q = 0
        while q < l:
            os.remove(f'{names_of_photos[q]}')
            q += 1
    asking(message)
