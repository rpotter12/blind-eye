# region IMPORTS
from pathlib import Path

from wplay.utils import browser_config
from wplay.utils import target_search
from wplay.utils import target_select
from wplay.utils import io
from wplay import text_to_speech
from wplay.utils.Logger import Logger
from wplay.utils.helpers import logs_path
from colorama import Fore, Style
from wplay import chatbot
# endregion


# region LOGGER
__logger = Logger(Path(__file__).name)
# endregion


async def chat(target):
    initial_minimize = True
    __logger.info("Chatting with target")
    page, _ = await browser_config.configure_browser_and_load_whatsapp()

    if target is not None:
        try:
            await target_search.search_and_select_target(page, target)
        except Exception as e:
            print(e)
            await page.reload()
            await target_search.search_and_select_target_without_new_chat_button(page, target)
    else:
        target = await target_select.manual_select_target(page)

    print("\033[91m {}\033[00m".format("\nType '...' in a new line or alone in the message to change target person.\nType '#_FILE' to send Image/Video/Documentd etc.\nType '#_TTS' to convert text to speech and send audio file.\n"))

    while True:
        if (initial_minimize):
            browser_config.minimize()
            initial_minimize = False

        await getMessages(page, target)
        message: list[str] = io.ask_user_for_message_breakline_mode()

        if '...' in message:
            message.remove('...')
            await io.send_message(page, message)
            target = input("\n\nNew Target Name: ")
            if target is not None:
                await target_search.search_and_select_target(page, target)
            else:
                await target_select.manual_select_target(page)
            message = io.ask_user_for_message_breakline_mode()

        #Text to speech
        if '#_TTS' in message:
            await text_to_speech.text_to_speech(target)
            await io.send_file(page)

        # File Share:
        if '#_FILE' in message:
            message.remove('#_FILE')
            await io.send_file(page)
        await getMessages(page, target)
        await io.send_message(page, message)

async def getMessages(pg, tg):
    selector = "#main > div > div > div > div > div > div > div > div"
    selector_sender = "#main > div > div > div > div > div > div > div > div > div.copyable-text"
    try:
        # Getting all the messages of the chat
        await pg.waitForSelector(selector)
        values = await pg.evaluate(f'''() => [...document.querySelectorAll('{selector}')]
                                                    .map(element => element.textContent)''')
        sender = await pg.evaluate(f'''() => [...document.querySelectorAll('{selector_sender}')]
                                                    .map(element => element.getAttribute("data-pre-plain-text"))''')
        lastMessage = values[-1]
        last_message_sender = sender[-1]
        last_message_time = sender[-1].split(',')
        last_message_time = last_message_time[0].replace('[', '')
        lastMessage = lastMessage.replace(last_message_time, '')
    except Exception as e:
        print(e)
        lastMessage = ""
    lastOutgoingMessage = ''
    if tg.lower() in last_message_sender.lower() and lastOutgoingMessage != lastMessage:
        print(Fore.GREEN + f"{tg}-", end="")
        print(lastMessage, end="")
        if '/image' in lastMessage:
            bot_msg = await chatbot.Bot(last_Message = lastMessage)
            await io.send_message(pg, bot_msg)
            await io.send_file(pg)
        elif lastMessage[0] == '/':
            bot_msg = await chatbot.Bot(last_Message = lastMessage)
            await io.send_message(pg, bot_msg)
        print(Style.RESET_ALL)
    lastOutgoingMessage = lastMessage
