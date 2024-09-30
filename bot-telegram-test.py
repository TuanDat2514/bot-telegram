
import datetime
import math
import random
import os
from telegram import PhotoSize, Update,Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from typing import List, Sequence, Tuple,cast

import requests
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    InvalidCallbackData,
    PicklePersistence,
    MessageHandler,
    filters,
    
)

TOKEN = os.environ.get("TOKEN")
message = "Complete the following tasks and contact @Serve18jl2 customer service to apply for free ₱22.\n"+ "①. Register: https://18jlvip.com\n"+"②. Join the official Telegram channel: \n"+"https://t.me/+gCnLv8l8ZeIxMzFl\n"+"Follow the official Facebook:\n"+ "https://facebook.com/18jlcomOfficial\n"+"③. Get free ₱22: @Serve18jl2"
caption = ''
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    check = False
    read_file = open("list-chat-id.txt", "r")
    list_id = read_file.read().split('\n')
    if(str(update.effective_chat["id"]) in list_id):
        check = True
    if(not check):
        f = open("list-chat-id.txt", "a")
        f.writelines(f'{str(update.effective_chat["id"])}\n')
        f.close()
    photo = PhotoSize(file_id='AgACAgUAAxkBAAMJZvoR3amlFIfAXmpy8S7BhmiDt_kAAizDMRtnG9FX-k_l2vWjrmIBAAMCAAN4AAM2BA', file_size=84657, file_unique_id='AQADLMMxG2cb0Vd9', height=360, width=640)
    await update.message.reply_photo(photo=photo,caption=message)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat["id"]

    """ message = "Đây là bot"
    for i in range(5):
        url = f"https://api.telegram.org/bot{TOKEN}/se
        ndMessage?chat_id={chat_id}&text={f'{message} {i}'}"
        print(requests.get(url).json()) # this sends the message """
    
    await update.message.reply_text(f'Hello {chat_id} {update.effective_user.id}')
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.24h.com.vn")
    ele = driver.find_elements(By.XPATH,"//h3//a[contains(@class,'d-block fw-medium color-main hover-color-24h')]")
    for i in ele:
        print (ele[i]) """
    response = requests.get("https://www.24h.com.vn/")
    soup = BeautifulSoup(response.content,'html.parser')
    contents = soup.find_all('a',attrs={'d-block fw-medium color-main hover-color-24h'})
    for content in contents:
        c = content.get('href')
        await  update.message.reply_text(f'{c}')
def build_keyboard(current_list: List[int]) -> InlineKeyboardMarkup:
    """Helper function to build the next inline keyboard."""
    return InlineKeyboardMarkup.from_column(
        [InlineKeyboardButton("🧙‍♀️ Start", callback_data="/start"),
         InlineKeyboardButton("🧝 Hello", callback_data="/hello",url='https://t.me/+wLbYQNicpKplZWFl'),
         InlineKeyboardButton("🙆 News", callback_data="/news"),
         InlineKeyboardButton("🙆 Crypto", callback_data="/crypto")]
    )

async def list_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.callback_query.data == "/news":
        response = requests.get("https://www.24h.com.vn/")
        soup = BeautifulSoup(response.content,'html.parser')
        contents = soup.find_all('a',attrs={'d-block fw-medium color-main hover-color-24h'})
        chat_id = update.effective_chat["id"]
        message = update.message.text
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}'
        requests.get(url)
    await update.callback_query.answer()
def get_photo(photo_size) -> PhotoSize:
    return photo_size

async def value_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo1 = update.message.photo
    context.user_data[0] = update.message.photo
    context.user_data[1] = update.message.caption_html
    caption = update.message.caption
    await update.message.reply_text(f'Value Input : {update.message.text_html} {caption}') 
async def setCaption(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'setCaption') 
async def send_Ads(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo = context.user_data.get(0)[0]
    caption = context.user_data.get(1)
    file = open('list-chat-id.txt','r')
    list_id = file.read().split('\n')
    for id in list_id:
        if id != '':
            await context.bot.send_photo(chat_id=id,caption=caption,photo=photo,parse_mode='HTML')
        """ url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={id}&caption={caption}&photo=https://yt3.googleusercontent.com/rwlnBmxBIHnAIz261w3REJSt0PQ7I5p7Fe8xmRyAUBBM2rdCHfET_7GX1qG9x4HUzQet3nKc=s160-c-k-c0x00ffffff-no-rj'
        requests.get(url) """
    """ await update.message.reply_photo(photo='https://yt3.googleusercontent.com/rwlnBmxBIHnAIz261w3REJSt0PQ7I5p7Fe8xmRyAUBBM2rdCHfET_7GX1qG9x4HUzQet3nKc=s160-c-k-c0x00ffffff-no-rj',
                                     caption="đây là caption",
                                     parse_mode='HTML',
                    
                                     ) """
    # await context.bot.send_message(chat_id=-4590561078,text="Chính no")

async def handle_invalid_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Informs the user that the button is no longer available."""
    await update.callback_query.answer()
    await update.effective_message.edit_text(
        "Sorry, I could not process this button click 😕 Please send /start to get a new keyboard."
    )

async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = requests.get('https://webgia.com/tien-ao/')
    soup = BeautifulSoup(response.content,'html.parser')
    contents = soup.find_all('a',attrs={'coin-name'})
    tbody= soup.find('tbody',attrs={'coin-main'})
    trs= tbody.find_all('tr')
    print(len(trs))
    arr = []
    for index in range(len(trs)-1):
        # print(arr_td.find_all('td')[2])
        coin_name = contents[index].find('span').text
        coin_price = trs[index].find_all('td')[2].text
        coin = (coin_name,coin_price)
        arr.append(coin)
    abc =''
    for i in range(len(trs)-1):
        a = f'<a style="color:#fc5252">{arr[i][0]} | {arr[i][1]}</a>\n'
        abc = abc + a
        print(f'{arr[i][0]}\t | {arr[i][1]} \n')
    message = f'----------Crypto----------\n'+ abc
    await update.effective_message.reply_text(message,parse_mode='HTML')
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("news", news))
app.add_handler(CommandHandler("setCaption", setCaption))
app.add_handler(CommandHandler("sendAds",send_Ads))
app.add_handler(CommandHandler("crypto", crypto))
app.add_handler(MessageHandler(filters.ALL,value_input))
app.add_handler(CallbackQueryHandler(handle_invalid_button, pattern=InvalidCallbackData))
app.add_handler(CallbackQueryHandler(list_button))


app.run_polling()