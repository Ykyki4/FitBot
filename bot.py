import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pathlib import PurePath, Path
from environs import Env

env = Env()
env.read_env()
logging.basicConfig(level=logging.INFO)
bot = Bot("5463514865:AAHz5-6ItrUh-nq6XwcJ5X_uA4I7rNv5css")
dp = Dispatcher(bot, storage=MemoryStorage())

class reg_states(StatesGroup):
    menu_state = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    main_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pp_bread = types.KeyboardButton("Безуглеводный ПП хлеб")
    bread_spreads = types.KeyboardButton("Намазки на хлеб")
    eggs_breakfasts = types.KeyboardButton("Завтраки из яиц")
    bakery = types.KeyboardButton("Выпечка")
    salates_and_snacks = types.KeyboardButton("Салаты и закуски")
    soup = types.KeyboardButton("Супы")
    hot_dishes = types.KeyboardButton("Горячие блюда")
    what_and_when = types.KeyboardButton("Что и когда готовить")
    main_menu_markup.row(pp_bread, bread_spreads)\
        .row(eggs_breakfasts, bakery)\
        .row(salates_and_snacks, soup)\
        .row(hot_dishes, what_and_when)
    await bot.send_message(message.chat.id,
                           "Здравствуйте, выберите категорию.",
                           reply_markup=main_menu_markup)
    await reg_states.menu_state.set()

@dp.message_handler(state=reg_states.menu_state)
async def get_main_menu_button(message: types.Message):
    main_meu_button = types.KeyboardButton("Главное меню")
    if message.text == "Главное меню":
        await start(message)
    if message.text == "Безуглеводный ПП хлеб":
        pp_bread_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bran_bread = types.KeyboardButton("Безуглеводный хлеб из отрубей")
        flax_bread = types.KeyboardButton("Безуглеводный льняной хлеб")
        fitnes_bread = types.KeyboardButton("Фитнес хлеб")
        cheese_bread = types.KeyboardButton("Сырный хлеб")
        psyllium_bread = types.KeyboardButton("Безуглеводные булочки из псиллиума")
        pp_bread_markup.row(bran_bread, flax_bread, fitnes_bread)\
            .row(cheese_bread, psyllium_bread).add(main_meu_button)
        await bot.send_message(message.chat.id,
                               "Выберите рецепт.",
                               reply_markup=pp_bread_markup)
    if message.text == "Намазки на хлеб":
        bread_spreads_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        avocado_cream = types.KeyboardButton("Авокадо-крем")
        mexican_guacamole = types.KeyboardButton("Мексиканский гуакамоле")
        home_made_hummus = types.KeyboardButton("Хумус по-домашнему")
        firt_cheese_and_egg_spread = types.KeyboardButton("Яично-сырная намазка №1")
        second_cheese_and_egg_spread = types.KeyboardButton("Яично-сырная намазка №2")
        forshmak = types.KeyboardButton("Форшмак из селёдки")
        riet_with_red_fish = types.KeyboardButton("Риет с красной рыбой")
        tuna_pate = types.KeyboardButton("Паштет из тунца")
        bread_spreads_markup.row(avocado_cream, mexican_guacamole)\
            .row(firt_cheese_and_egg_spread, second_cheese_and_egg_spread)\
            .row(home_made_hummus, forshmak)\
            .row(riet_with_red_fish, tuna_pate).add(main_meu_button)
        await bot.send_message(message.chat.id,
                               "Выберите рецепт.",
                               reply_markup=bread_spreads_markup)
    if message.text == "Завтраки из яиц":
        eggs_breakfasts_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cheese_and_tomate_egg_roll = types.KeyboardButton("Яичный рулет с сыром и томатами")
        rice_egg_pancake = types.KeyboardButton("Рисовый яйцеблин")
        egg_in_tomate = types.KeyboardButton("Яйцо в помидоре")
        fast_omelette = types.KeyboardButton("Быстрый омлет в духовке")
        cheese_and_meat_egg_pancake = types.KeyboardButton("Яицеблин с фаршем и сыром")
        egg_roll = types.KeyboardButton("Яичный рулет")
        chicken_omelette = types.KeyboardButton("Куриное филе в омтеле")
        pp_pizza = types.KeyboardButton("ПП-пицца в сковороде")
        cheese_cakes = types.KeyboardButton("Сырно-кабачковые лепёшки")
        mini_omelettes = types.KeyboardButton("Мини-омлеты")
        eggs_breakfasts_markup.row(cheese_and_tomate_egg_roll, rice_egg_pancake)\
            .row(egg_in_tomate, fast_omelette)\
            .row(cheese_and_meat_egg_pancake, egg_roll)\
            .row(chicken_omelette, pp_pizza)\
            .row(cheese_cakes, mini_omelettes).add(main_meu_button)
        await bot.send_message(message.chat.id,
                               "Выберите рецепт.",
                               reply_markup=eggs_breakfasts_markup)
    if message.text == "Выпечка":
        bakery_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Сырные колечки")
        button2 = types.KeyboardButton("Овсяно-сырные оладушки")
        button3 = types.KeyboardButton("Овсяная ПП запеканка")
        button4 = types.KeyboardButton("Ленивые пирожки с капустой")
        button5 = types.KeyboardButton("Кабачковые пирожки с мясом")
        button6 = types.KeyboardButton("Пышный ПП хачапури на сковородке")
        button7 = types.KeyboardButton("ПП синнабоны")
        button8 = types.KeyboardButton("Кунжутное печенье")
        button9 = types.KeyboardButton("Сырно-чесночные ПП ватрушки")
        button10 = types.KeyboardButton("Торт чернослив-миндаль")
        button11 = types.KeyboardButton("Морковный кекс")
        button12 = types.KeyboardButton("Чизкейк за 10 минут без выпечки")
        button13 = types.KeyboardButton("Яблочный кекс с курагой")
        button14 = types.KeyboardButton("Кексы с бананом")
        button15 = types.KeyboardButton("Тыквенный пирог")
        button16 = types.KeyboardButton("Абрикосовый пирог")

        bakery_markup.row(button1, button2) \
            .row(button3, button4) \
            .row(button5, button6) \
            .row(button7, button8) \
            .row(button9, button10) \
            .row(button11, button12) \
            .row(button13, button14) \
            .row(button15, button16).add(main_meu_button)

        await bot.send_message(message.chat.id,
                               "Выберите рецепт.",
                               reply_markup=bakery_markup)

    if message.text == "Салаты и закуски":
        salate_and_snacks_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Салат овощной с кальмаром гриль")
        button2 = types.KeyboardButton("Салат с запечёным лососем")
        button3 = types.KeyboardButton("Салат из сважих овощей с говядиной")
        button4 = types.KeyboardButton("Салат с тунцом и сельдереем")
        button5 = types.KeyboardButton("Салат с тунцом")
        button6 = types.KeyboardButton("Салат из нута и овощей")
        button7 = types.KeyboardButton("Чечевичный салат с томатами")
        button8 = types.KeyboardButton("Салат с курицей и тыквой")
        button9 = types.KeyboardButton("Салат с брокколи и киноа")
        button10 = types.KeyboardButton("Рулетики из цукини и курицей")
        button11 = types.KeyboardButton("Ролл с тунцом")
        salate_and_snacks_markup.row(button1, button2, button3) \
            .row(button4, button5, button6) \
            .row(button7, button8, button9) \
            .row(button10, button11).add(main_meu_button)

        await bot.send_message(message.chat.id,
                               "Выберите рецепт.",
                               reply_markup=salate_and_snacks_markup)
    if message.text == "Супы":
        soups_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Мисо-суп с тофу и пекинской капустой")
        button2 = types.KeyboardButton("Кукурузный суп с креветками и сыром")
        button3 = types.KeyboardButton("Грибной суп-пюре с сельдереем и курицей")
        button4 = types.KeyboardButton("Суп-пюре из чечевицы с томатный соком")
        button5 = types.KeyboardButton("Суп-пюре из шпината и курицы")
        button6 = types.KeyboardButton("Суп-пюре из сельдерея")
        button7 = types.KeyboardButton("Имбирно-тыквенный суп-пюре")
        button8 = types.KeyboardButton("Белковый суп")

        soups_markup.row(button1, button2) \
            .row(button3, button4) \
            .row(button5, button6) \
            .row(button7, button8).add(main_meu_button)
        await bot.send_message(message.chat.id,
                               "Выберите рецепт.",
                               reply_markup=soups_markup)
    if message.text == "Горячие блюда":
        hot_dishes_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Гречка по-французски")
        button2 = types.KeyboardButton("Котлетки с моцареллой")
        button3 = types.KeyboardButton("Цветная капуста с курицей")
        button4 = types.KeyboardButton("Рис с индейкой в азиатском стиле")
        button5 = types.KeyboardButton("Печеночная запеканка")
        button6 = types.KeyboardButton("Рыбные котлеты")
        button7 = types.KeyboardButton("Говядина в томатно-луковом соусе")
        button8 = types.KeyboardButton("Фаршированные кальмары")
        button9 = types.KeyboardButton("Рататуй с моцареллой")
        button10 = types.KeyboardButton("Касная рыба в сливках")
        button11 = types.KeyboardButton("Баклажаны с индейкой")
        button12 = types.KeyboardButton("Стейк из цветной капусты")

        hot_dishes_markup.row(button1, button2, button3) \
            .row(button4, button5, button6) \
            .row(button7, button8, button9) \
            .row(button10, button11, button12).add(main_meu_button)
        await bot.send_message(message.chat.id,
                               "Выберите рецепт.",
                               reply_markup=hot_dishes_markup)

if __name__ == "__main__":
    executor.start_polling(dp)