# region IMPORTS
from pathlib import Path
from whaaaaat import style_from_dict, Token
# endregion

# region WEBSITES
websites = {'whatsapp': 'https://web.whatsapp.com/'}
# endregion

# region SELECTOR
whatsapp_selectors_dict = {
    'login_area':'#app > div > div > div.landing-header',

    'new_chat_button': '#side > header div[role="button"] span[data-icon="chat"]',
    'search_contact_input_new_chat': '#app > div > div > div > div > span > div > span > div > div > div > label > div > div',
    'contact_list_elements_filtered_new_chat': '#app > div > div span > div > span > div div > div div > div div > span > span[title][dir]',
    'group_list_elements_filtered_new_chat': '#app > div > div span > div > span > div div > div div > div div > span[title][dir]',

    'search_contact_input':'#side > div > div > label > div > div',
    'chat_list_elements_filtered':'#pane-side > div > div > div > div > div > div > div > div > div > span > span[title][dir]',

    'target_focused_title': '#main > header div > div > span[title]',
    'message_area': '#main > footer div.selectable-text[contenteditable]',
    'last_seen':'#main > header > div > div > span[title]',
    'target_chat_header': '#main > header',
    'contact_info_page_elements': '#app > div > div > div:nth-child(2) > div:last-of-type > span > div > span > div > div > div:first-child > div',
    'contact_info_page_group_element_heading': '#app > div > div > div:nth-child(2) > div:last-of-type > '
                                    'span > div > span > div > div > div:first-child > div:nth-child(5)>div>div>div>div:first-child>span',
    'contact_info_page_group_elements': '#app > div > div > div:nth-child(2) > div:last-of-type > '
                                    'span > div > span > div > div > div:first-child > div:nth-child(5)>div:nth-child(2)>div>div',
    'contact_info_page_close_button': '#app > div > div > div:nth-child(2) > div:last-of-type > span > div > span > div > header > div > div > button',
    'chat_or_message_search': '#side > div:nth-child(3) > div > label > div > div:last-child',
    'chats_groups_messages_elements': '#side > div:last-child > div > div > div > div',
    'contact_element': 'span > span > span[class^="matched-text"]',
    'group_element': 'div:last-child > div:first-child > div:first-child > div > span > span[class^="matched-text"]',
    'attach_file' : '#main > header > div > div > div:nth-child(2) > div',
    'choose_file' : '#main > header > div > div > div > span > div > div > ul > li:nth-child(3) > button',
    'send_file' : '#app > div > div > div > div > span > div > span > div > div > div > span > div > div > span',
    'profile_photo_element': '#side > header > div > div > img',
    'about_edit_button_element': '#app > div > div > div > div > span > div > div > div > div:nth-child(4) > div > div > span > div > span',
    'about_text_area': '#app > div > div > div > div > span > div > div > div > div:nth-child(4) > div > div > div > div'
}
# endregion

# region PATHS
data_folder_path = Path.home() / 'wplay'
logs_path = Path.home() / 'wplay' / 'logs'
user_data_folder_path = Path.home() / 'wplay' / '.userData'
# endregion

# region MENU STYLES
menu_style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})
# endregion
