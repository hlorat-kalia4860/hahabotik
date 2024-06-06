import asyncio 
from aiogram import Bot, Dispatcher, types 
from aiogram.filters.command import Command 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
 
bot = Bot(token='7399973427:AAEUmsvhIbOrRpDI2_VdBdz1EfSNvRqRUU4') 
dp = Dispatcher() 
# to database: 
 
messageId = '' 
user = [] 
 
 
reg_block = ["Указать имя", "Выбрать часовой пояс", "Выбрать удобное время для уведомлений"] 
main_kb = InlineKeyboardMarkup(inline_keyboard=[ 
[InlineKeyboardButton(text = reg_block[0], callback_data="name")], 
[InlineKeyboardButton(text = reg_block[1], callback_data="tma")], 
[InlineKeyboardButton(text = reg_block[2], callback_data="tmb")], 
[InlineKeyboardButton(text = "Принять", callback_data="confirm")] 
]) 
start = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = "Регистрация", callback_data="reg")]]) 
 
 
@dp.message(Command("start")) 
async def cmd_start(message: types.Message): 
   global messageId, user 
   if message.from_user.id not in user: 
      messageId = await message.answer("Добро пожаловать в нашего бота для хакатона, предлагаем вам пройти регистрацию:", reply_markup=start) 
   else: 
      messageId = await message.answer("Балда ты уже зарегистрирован куда руки тянешь") 
 
@dp.callback_query(lambda query: query.data == 'reg') 
async def ccmd_registration(callback_query: types.CallbackQuery): 
   global messageId 
   await bot.answer_callback_query(callback_query.id) 
   messageId = await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=messageId.message_id, text="Заполните поля ниже", reply_markup=main_kb) 
 
@dp.callback_query(lambda query: query.data == 'name') 
async def editing_name_inlinecallback(callback_query: types.CallbackQuery): 
   global messageId 
   await bot.answer_callback_query(callback_query.id) 
   messageId = await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=messageId.message_id, text="Укажите своё имя") 
   @dp.message() 
   async def name(message: types.Message): 
      global messageId, reg_block, main_kb, user 
      reg_block[0] = message.text 
      main_kb = InlineKeyboardMarkup(inline_keyboard=[ 
[InlineKeyboardButton(text = reg_block[0], callback_data="name")], 
[InlineKeyboardButton(text = reg_block[1], callback_data="tma")], 
[InlineKeyboardButton(text = reg_block[2], callback_data="tmb")], 
[InlineKeyboardButton(text = "Принять", callback_data="confirm")] 
]) 
      messageId = await bot.send_message(chat_id=callback_query.from_user.id, text="Заполните поля ниже", reply_markup=main_kb) 
      user.append(message.from_user.id) 
 
# Запуск процесса поллинга новых апдейтов 
async def main(): 
    await dp.start_polling(bot) 
 
if __name__ == "__main__": 
    asyncio.run(main())
