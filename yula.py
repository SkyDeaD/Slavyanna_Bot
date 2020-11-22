import logging
import time

import pymongo
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot("1490467845:AAHp3p3evm1MQ-LnwFi9Zhhw0Ui38xfRpLs")
db = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)
client = pymongo.MongoClient(
    'mongodb+srv://SkyDeaD:GamerVD76@aliceskybotandother-ik6lu.mongodb.net/sl?retryWrites=true&w=majority')
dbm = client.sl
users = dbm.users


banuser = 0
admuser = 0
userstatus = 0
useradm = 0
unmuteuser = 0; key = 0


@db.message_handler(lambda message: message.chat.type == 'private', commands=['start'])
async def start_handler(message):
    await message.reply(F'Привет, {message.from_user.first_name}!\nНажми 👉/help👈 ')


@db.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    if message.chat.type == 'private':
        q = await bot.get_chat(577096232)
        c = await bot.get_chat(-1001484115605)
        await message.reply(F'''
Я - бот Ювао, разработанный 👉[{q.first_name}](tg://user?id=577096232)👈 

Бот создавался для конфы 👉[{c.title}](https://t.me/YgolokNeko)👈


На данный момент доступны следующие команды:

*👤me* - информация о себе.

*ℹ️info* - полная информация о пользователе и группе.

*🌟admins* - список администраторов.

*📜rules* - правила чата.

*✂setrules* - установить/обновить правила чата.

*🗞delrules* - удалить правла чата.

*🤐Mute* - кидает выбранного пользователя в мут.

*😬Amute* - попытка замутить администратора. Доступна только владельцу группы. Администратор должен быть назначен через бота.

*😀Unmute* - размучевает выбранного пользователя.

*😃Unban* - разбанивает выбранного пользователя.

*🤕Kick* - выгоняет выбранного пользователя.

*😣Akick* - попытка кикнуть администратора. Доступна только владельцу группы. Администратор должен быть назначен через бота.

*📌Pin* - закрепляет выбранное сообщение.

*❌Unpin* - открепляет закреплённое сообщение.

*🚫Delete* - удаляет выбранное сообщение.

*🧹Purge* - чистит чат. Удаляет выбранное сообщение и всё то, что ниже его.

*⏫Promote* - повышает выбранного пользователя до администратора; доступно только владельцу чата.

*⏬Demote* - понижает выбранного администратора; доступно только владельцу чата.

Так же существуют команды, которые отстуствуют в списке.


Для полноценный работы в группе мне требуются следующие разрешения:

〽️Изменения профиля группы
❌Удаление сообщений
📛Блокировка участников
📨Пригласительные ссылки
📌Закрепление сообщений
⭐️Добавление администраторов
''', parse_mode='markdown')
    else:
        await message.reply('''
На данный момент доступны следующие команды:

*👤me* - информация о себе.

*ℹinfo* - полная информация о пользователе и группе.

*🌟admins* - список администраторов.

*📜rules* - правила чата.

*✂setrules* - установить/обновить правила чата.

*🗞delrules* - удалить правла чата.

*🤐Mute* - кидает выбранного пользователя в мут.

*😬Amute* - попытка замутить администратора. Доступна только владельцу группы. Администратор должен быть назначен через бота.

*😀Unmute* - размучевает выбранного пользователя.

*😃Unban* - разбанивает выбранного пользователя.

*🤕Kick* - выгоняет выбранного пользователя.

*😣Akick* - попытка кикнуть администратора. Доступна только владельцу группы. Администратор должен быть назначен через бота.

*📌Pin* - закрепляет выбранное сообщение.

*❌Unpin* - открепляет закреплённое сообщение.

*🚫Delete* - удаляет выбранное сообщение.

*🧹Purge* - чистит чат. Удаляет выбранное сообщение и всё то, что ниже его.

*⏫Promote* - повышает выбранного пользователя до администратора; доступно только владельцу чата.

*⏬Demote* - понижает выбранного администратора; доступно только владельцу чата.

Так же существуют команды, которые отстуствуют в списке.
''', parse_mode='markdown')


@db.message_handler(content_types=['new_chat_members'])
async def handler_new_member(message: types.Message):
    global unmuteuser
    global key
    for user in message.new_chat_members:
        if user.id in [1490467845]:
            await bot.send_message(message.chat.id,
                                   'Привет! Я - бот-администратор Ювао. Для полноценный работы выдай мне следующие разрешения:\n\n〽️Изменения профиля группы\n❌Удаление сообщений\n📛Блокировка участников\n📨Пригласительные ссылки\n📌Закрепление сообщений\n⭐️Добавление администраторов')
        else:
            for user in message.new_chat_members:
                unmuteuser = user.id
                sti = open('welcome.webp', 'rb')
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton(text='Начать общаться', callback_data='3')
                key = keyboard.add(item1)
                await bot.send_sticker(message.chat.id, sti, reply_to_message_id=message.message_id)
                await bot.send_message(message.chat.id,
                                       F'Добро пожаловать в чат [{message.chat.title}](https://t.me/{message.chat.username}), [{user.first_name}](tg://user?id={user.id})!\n\nПредлагаю ознакомиться с правилами:\n👉/rules👈',
                                       reply_to_message_id=message.message_id, reply_markup=keyboard,
                                       parse_mode='markdown')
                await bot.restrict_chat_member(message.chat.id, user.id,
                                               until_date=time.time())


@db.message_handler(lambda message: message.chat.type != 'private', commands=['mute'])
async def handle_mute(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status not in ['administrator', 'creator']:
        await message.reply('У Вас недостаточно прав для выполнения этой комманды.')
        return
    if usera.can_restrict_members is False:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_restrict_members is not True:
        await message.reply(
            'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников.')
        return
    if message.reply_to_message is None:
        await message.reply('Я не понимаю, о ком идёт речь?')
        return
    user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_member is False:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не является участником чата.',
            parse_mode='markdown')
        return
    if user.status in ['administrator', 'creator']:
        await message.reply('Я не буду мутить администратора!')
        return
    if user.can_send_messages is False:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) и так молчит.',
            parse_mode='markdown')
        return
    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=time.time())
    await message.reply(
        F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) потерял голос.',
        parse_mode='markdown')
    sticker_mute = open('mute.webp', 'rb')
    await message.answer_sticker(sticker_mute)


@db.message_handler(lambda message: message.chat.type != 'private', commands=['muteall'])
async def handle_muteall(message: types.Message):
    if message.from_user.id not in [691117028, 1192665194]:
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_restrict_members is False:
        return
    permissions = types.ChatPermissions(can_send_messages=False, can_send_media_messages=False,
                                        can_send_polls=False, can_send_other_messages=False,
                                        can_add_web_page_previews=False, can_invite_users=False)
    await bot.set_chat_permissions(message.chat.id, permissions)
    sticker_allmute = open('allmute.webp', 'rb')
    await message.answer_sticker(sticker_allmute)


@db.message_handler(lambda message: message.chat.type != 'private', commands=['unmuteall'])
async def handle_unmuteall(message: types.Message):
    if message.from_user.id not in [691117028, 1192665194]:
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_restrict_members is False:
        return
    permissions = types.ChatPermissions(can_send_messages=True, can_send_media_messages=True,
                                        can_send_polls=True, can_send_other_messages=True,
                                        can_add_web_page_previews=True, can_invite_users=True)
    await bot.set_chat_permissions(message.chat.id, permissions)
    sticker_unallmute = open('unmuteall.webp', 'rb')
    await message.answer_sticker(sticker_unallmute)


@db.message_handler(lambda message: message.chat.type != 'private', commands=['amute'])
async def handle_amute(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status != 'creator':
        await message.reply('У Вас недостаточно прав для выполнения этой комманды.')
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_restrict_members is False:
        await message.reply(
            'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников.')
        return
    if message.reply_to_message is None:
        await message.reply('Я не понимаю, о ком идёт речь?')
        return
    user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_member is False:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не является участником чата.',
            parse_mode='markdown')
        return
    if user.can_send_messages is False:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) и так молчит.',
            parse_mode='markdown')
        return
    try:
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=time.time())
        await message.reply(
            F'У [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) был снят с должности администратора и потерял голос.',
            parse_mode='markdown')
        sticker_mute = open('mute.webp', 'rb')
        await message.answer_sticker(sticker_mute)
    except:
        await message.reply('Я не могу замутить данного пользователя.')
        sticker_nonmute = open('cant.webp', 'rb')
        await message.answer_sticker(sticker_nonmute)


@db.message_handler(lambda message: message.chat.type != 'private', commands=['unmute'])
async def handle_unmute(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status not in ['administrator', 'creator']:
        return
    if usera.can_restrict_members is False:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_restrict_members is False:
        await message.reply(
            'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников.')
        return
    if message.reply_to_message is None:
        await message.reply('Я не понимаю, о ком идёт речь?')
        return
    user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_member is False:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не является участником чата.',
            parse_mode='markdown')
        return
    if user.status in ['administrator', 'creator']:
        await message.reply('Администратор не может быть в муте.')
        return
    if user.can_send_messages in [True, None]:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не в муте.',
            parse_mode='markdown')
        return
    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=True,
                                   can_send_media_messages=True, can_send_other_messages=True,
                                   can_add_web_page_previews=True)
    await message.reply(
        F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) снова может говорить.',
        parse_mode='markdown')
    sticker_unmute = open('unmute.webp', 'rb')
    await message.answer_sticker(sticker_unmute)


@db.message_handler(lambda message: message.chat.type != 'private', commands=['promote'])
async def handle_promote(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status != 'creator':
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_promote_members is not True:
        await message.reply(
            'Для выполнения данной команды требуются следующие права администратора:\n\n⭐️Добавление администраторов.')
        return
    if message.reply_to_message is None:
        await message.reply('Я не понимаю, о ком идёт речь?')
        return
    user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_member is False:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не является участником чата.',
            parse_mode='markdown')
        return
    if user.status in ['administrator', 'creator']:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) уже является администратором!',
            parse_mode='markdown')
        return
    await message.reply(
        F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) повышен(а)!',
        parse_mode='markdown')
    await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_change_info=True,
                                  can_delete_messages=True, can_invite_users=True, can_restrict_members=True,
                                  can_pin_messages=True, can_promote_members=True)


@db.message_handler(lambda message: message.chat.type != 'private', commands=['demote'])
async def handle_demote(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status != 'creator':
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_promote_members is not True:
        await message.reply(
            'Для выполнения данной команды требуются следующие права администратора:\n\n⭐️Добавление администраторов.')
        return
    if message.reply_to_message is None:
        await message.reply('Я не понимаю, о ком идёт речь?')
        return
    user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_member is False:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не является участником чата.',
            parse_mode='markdown')
        return
    if user.status not in ['administrator', 'creator']:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не является администратором.',
            parse_mode='markdown')
        return
    await message.reply(
        F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) понижен(а)!',
        parse_mode='markdown')
    await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_change_info=False,
                                  can_delete_messages=False, can_invite_users=False, can_restrict_members=False,
                                  can_pin_messages=False, can_promote_members=False)


@db.message_handler(lambda message: message.chat.type != 'private', commands=['kick'])
async def handle_kick(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status not in ['administrator', 'creator']:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    if usera.can_restrict_members is False:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_restrict_members is not True:
        await message.reply(
            'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников.')
        return
    if message.reply_to_message is None:
        await message.reply('Я не понимаю, о ком идёт речь?')
        return
    user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_member is False:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не является участником чата.',
            parse_mode='markdown')
        return
    if user.status in ['administrator', 'creator']:
        await message.reply('Я не могу кикнуть администратора.')
        return
    await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply(
        F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) решил(а) отойти 😄',
        parse_mode='markdown')
    sticker_kick = open('kick.webp', 'rb')
    await message.answer_sticker(sticker_kick)


@db.message_handler(lambda message: message.chat.type != 'private', commands=['akick'])
async def handle_akick(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status != 'creator':
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_restrict_members is False:
        await message.reply(
            'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников.')
        return
    if message.reply_to_message is None:
        await message.reply('Я не понимаю, о ком идёт речь?')
        return
    user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_member is False:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не является участником чата.',
            parse_mode='markdown')
        return
    try:
        await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) решил(а) отойти 😄',
            parse_mode='markdown')
        sticker_kick = open('kick.webp', 'rb')
        await message.reply_sticker(sticker_kick)
    except:
        await message.reply('Я не могу кикнуть данного пользователя.')
        sticker_nonkick = open('cant.webp', 'rb')
        await message.answer_sticker(sticker_nonkick)


@db.message_handler(lambda message: message.chat.type != 'private', commands=['unban'])
async def handle_unban(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status not in ['administrator', 'creator']:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    if usera.can_restrict_members is False:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_restrict_members is False:
        await message.reply(
            'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников.')
        return
    if message.reply_to_message is None:
        await message.reply('Я не понимаю, о ком идёт речь?')
        return
    user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_member is False:
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не является участником чата.',
            parse_mode='markdown')
        return
    if user.status != 'restricted':
        await message.reply(
            F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не забанен.',
            parse_mode='markdown')
        return
    await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply(
        F'Ладно, [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) может вернуться.',
        parse_mode='markdown')
    sticker_unban = open('unban.webp', 'rb')
    await message.answer_sticker(sticker_unban)


@db.message_handler(lambda message: message.chat.type != 'private', commands=['pin'])
async def handle_pin(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status not in ['administrator', 'creator']:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    if usera.can_pin_messages is False:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_pin_messages is False:
        await message.reply(
            'Для выполнения данной команды требуются следующие права администратора:\n\n📌Закрепление сообщений.')
        return
    if message.reply_to_message is None:
        await message.reply('Выберите сообщение, которое нужно закрепить.')
        return
    await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    await message.delete()


@db.message_handler(lambda message: message.chat.type != 'private', commands=['unpin'])
async def handle_unpin(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status not in ['administrator', 'creator']:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    if usera.can_pin_messages is False:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_pin_messages is False:
        await message.reply(
            'Для выполнения данной команды требуются следующие права администратора:\n\n📌Закрепление сообщений.')
        return
    await bot.unpin_chat_message(message.chat.id)
    await message.delete()


@db.message_handler(lambda message: message.chat.type != 'private', commands=['del'])
async def handle_del(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status not in ['administrator', 'creator']:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    if usera.can_delete_messages is False:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_delete_messages is False:
        await message.reply(
            'Для выполнения данной команды требуются следующие права администратора:\n\n❌Удаление сообщений.')
        return
    if message.reply_to_message is None:
        await message.reply('Выберите сообщение, которое нужно удалить.')
        return
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(message.chat.id, message.reply_to_message.message_id)


@db.message_handler(lambda message: message.chat.type != 'private', commands=['purge'])
async def handle_purge(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status not in ['administrator', 'creator']:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    prom = await bot.get_chat_member(message.chat.id, 1490467845)
    if prom.can_delete_messages is False:
        await message.reply(
            'Для выполнения данной команды требуются следующие права администратора:\n\n❌Удаление сообщений.')
        return
    if usera.can_delete_messages is False:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    if message.reply_to_message is None:
        await message.reply('Выберите сообщение, ниже которого будет очищен чат.')
        return
    i = message.reply_to_message.message_id
    q = message.message_id
    for d in range(i, q):
        try:
            await bot.delete_message(message.chat.id, d)
        except:
            pass
    await message.delete()
    await message.answer('Чистка завершена.')


@db.message_handler(lambda message: message.chat.type != 'private', commands=['setrules'])
async def handle_rules(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status != 'creator':
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    if message.from_user.id not in [1192665194]:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    x = users.find_one({'rules': {'$exists': True}, 'chatid': message.chat.id})
    if x is None:
        rules = message.reply_to_message.text
        users.insert_one({'rules': rules, 'chatid': message.chat.id})
        await message.reply(F'Правила чата [{message.chat.title}](https://t.me/{message.chat.username}) установлены.',
                            parse_mode='markdown')
    elif x is not None:
        rules = message.reply_to_message.text
        users.delete_one({'rules': {'$exists': True}, 'chatid': message.chat.id})
        users.insert_one({'rules': rules, 'chatid': message.chat.id})
        await message.reply(F'Правила чата [{message.chat.title}](https://t.me/{message.chat.username}) обновлены.',
                            parse_mode='markdown')


@db.message_handler(lambda message: message.chat.type != 'private', commands=['delrules'])
async def handle_rules(message: types.Message):
    usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if usera.status != 'creator':
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    if message.from_user.id not in [1192665194]:
        await message.reply('У Вас недостаточно прав для выполнения этой команды.')
        return
    users.delete_one({'rules': {'$exists': True}, 'chatid': message.chat.id})
    await message.reply(F'Правила чата [{message.chat.title}](https://t.me/{message.chat.username}) удалены.',
                        parse_mode='markdown')


@db.message_handler(lambda message: message.chat.type != 'private', commands=['rules'])
async def handle_rules(message: types.Message):
    x = users.find_one({'rules': {'$exists': True}, 'chatid': message.chat.id})
    if x is None:
        await bot.send_message(message.chat.id, F'В данном чате пока что нет правил.',
                               reply_to_message_id=message.message_id, parse_mode='markdown')
    else:
        for rul in users.find({'chatid': message.chat.id}):
            await bot.send_message(message.chat.id, rul['rules'], reply_to_message_id=message.message_id,
                                   parse_mode='markdown')


@db.message_handler(lambda message: message.chat.type != 'private', commands=["report"])
async def handle_report(message: types.Message):
    if message.reply_to_message is None:
        await message.reply('Выберите сообщение, на которое хотите пожаловаться.')
        return
    adm = await bot.get_chat_administrators(message.chat.id)
    text = 'На данное сообщение поступила жалоба.\n\n'
    for i in adm:
        if i.user.is_bot is False:
            if i.can_restrict_members is not False:
                text += f"\n@{i.user.username}"
    await message.reply(text)


@db.message_handler(commands=['me'])
async def handle_message(message: types.Message):
    await bot.send_message(message.chat.id, F''' 
*Ваше имя*: `{message.from_user.first_name}`
*Ваш юзернейм*: `@{message.from_user.username}`
*Ваш ID*: `{message.from_user.id} `
''', reply_to_message_id=message.message_id, parse_mode='markdown')


@db.message_handler(lambda message: message.chat.type != 'private', commands=['info'])
async def handle_info(message: types.Message):
    if message.reply_to_message is not None:
        adm = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        group_id = await bot.get_chat(message.chat.id)
        await message.reply(F'''
*🚻Имя пользователя*: `{message.reply_to_message.from_user.first_name}`
*🖋Юзернейм пользователя*: `@{message.reply_to_message.from_user.username}`
*ℹ️ID пользователя*: `{message.reply_to_message.from_user.id}`
*📫Статус пользователя*: `{adm.status}`
*📕Название группы*: `{group_id.title}`
*🆔ID группы*: `{group_id.id}`
*🔠Тип группы*: `{group_id.type}`
''', parse_mode='markdown')
        return
    adm = await bot.get_chat_member(message.chat.id, message.from_user.id)
    group_id = await bot.get_chat(message.chat.id)
    await message.reply(F'''
*🚻Имя пользователя*: `{message.from_user.first_name}`
*🖋Юзернейм пользователя*: `@{message.from_user.username}`
*ℹ️ID пользователя*: `{message.from_user.id}`
*📫Статус пользователя*: `{adm.status}`
*📕Название группы*: `{group_id.title}`
*🆔ID группы*: `{group_id.id}`
*🔠Тип группы*: `{group_id.type}`
''', parse_mode='markdown')


@db.message_handler(lambda message: message.chat.type != 'private', commands=['admins'])
async def handle_admins(message: types.Message):
    adm = await bot.get_chat_administrators(message.chat.id)
    text = 'Администраторы чата:\n'
    for i in adm:
        if i.user.is_bot is False:
            if i.can_restrict_members is not False:
                text += f'\nИмя - {i.user.first_name}\nЮзернейм - {i.user.username}\n'
    await message.reply(text)




@db.callback_query_handler(text='1')
async def button_reaction(call: types.CallbackQuery):
    global banuser
    global admuser
    global useradm
    global userstatus
    if call.message:
        if call.from_user.id == admuser and userstatus.status in ['creator']:
            try:
                await bot.kick_chat_member(chat_id=call.message.chat.id, user_id=banuser)
                await call.message.edit_caption(F'*——Админы казнили* [неверного](tg://user?id={banuser})!——',
                                                parse_mode='markdown')
                await bot.send_animation(chat_id=call.message.chat.id,
                                         animation='CgACAgIAAxkBAAMSX7VxHT5zaq-vpOtx5R13mzVPZccAAuoJAAKJuelKbiiXGjLSwoweBA',
                                         reply_to_message_id=call.message.message_id)
            except:
                await call.message.edit_caption('*———Ошибка!———*', parse_mode='markdown')
        elif call.from_user.id == admuser and userstatus.status in ['administrator']:
            if useradm.status == 'creator':
                await call.message.edit_caption('*+++++Батю убить невозможно, сосите сосну+++++*',
                                                parse_mode='markdown')
            elif useradm.status != 'administrator':
                await bot.kick_chat_member(chat_id=call.message.chat.id, user_id=banuser)
                await call.message.edit_caption(F'*——Админы казнили* [неверного](tg://user?id={banuser})!——',
                                                parse_mode='markdown')
                await bot.send_animation(chat_id=call.message.chat.id,
                                         animation='CgACAgIAAxkBAAMSX7VxHT5zaq-vpOtx5R13mzVPZccAAuoJAAKJuelKbiiXGjLSwoweBA',
                                         reply_to_message_id=call.message.message_id)
            else:
                await call.message.edit_caption('*———Ошибка!———*', parse_mode='markdown')


@db.callback_query_handler(text='2')
async def button_reaction(call: types.CallbackQuery):
    global banuser
    global admuser
    if call.message:
        if call.from_user.id == admuser:
            await call.message.edit_caption(
                '\*\*\*' + '*Админы милосердно простили*' + ' ' + F'[Анонима](tg://user?id={banuser})' + '*; ступай с миром.*' + '\*\*\*',
                parse_mode='markdown')
            await bot.send_animation(chat_id=call.message.chat.id,
                                     animation='CgACAgIAAxkBAAMTX7Vx9Zx0TPmhcVTWbCFXk3zmbOsAAucJAAJLC6hJDVEIyeQ9E7UeBA',
                                     reply_to_message_id=call.message.message_id)


@db.callback_query_handler(text='3')
async def button_reaction(call: types.CallbackQuery):
    global unmuteuser
    if call.message:
        if call.from_user.id == unmuteuser:
            await bot.restrict_chat_member(chat_id=call.message.chat.id, user_id=unmuteuser,
                                           can_send_messages=True,
                                           can_send_media_messages=True, can_send_other_messages=True,
                                           can_add_web_page_previews=True)
            await call.message.delete_reply_markup()


@db.message_handler(content_types=['text'])
async def handle_text(message: types.Message):
    if message.text.lower() == 'мяукусь':
        if message.chat.type == 'private':
            return
        if message.reply_to_message is None:
            return
        if message.from_user.id != message.reply_to_message.from_user.id:
            user1 = await bot.get_chat_member(message.chat.id, message.from_user.id)
            user2 = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            if user1.status not in ['administrator', 'creator']:
                await bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time.time())
            if user2.status not in ['administrator', 'creator']:
                await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                               until_date=time.time())
            await bot.send_message(message.chat.id,
                                   F'*{message.from_user.first_name}* и *{message.reply_to_message.from_user.first_name}* разозлили Юля-тян и получили рыбкой по голове.',
                                   reply_to_message_id=message.message_id, parse_mode='markdown')

    elif message.text.lower() == 'юваобанус':
        prom = await bot.get_chat_member(message.chat.id, 1490467845)
        if prom.can_restrict_members is False:
            await message.reply(
                'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников.')
            return
        if message.reply_to_message is None:
            return
        if message.chat.type == 'private':
            return
        usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if usera.status not in ['administrator', 'creator']:
            return
        if usera.can_restrict_members is False:
            await message.reply('У Вас недостаточно прав для выполнения этой команды.')
            return
        global banuser
        banuser = message.reply_to_message.from_user.id
        global admuser
        admuser = message.from_user.id
        global userstatus
        userstatus = await bot.get_chat_member(message.chat.id, message.from_user.id)
        global useradm
        useradm = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton(text='Выгнать плохиша', callback_data='1')
        item2 = types.InlineKeyboardButton(text='Простить и понять', callback_data='2')
        keyboard.add(item1, item2)
        await bot.send_photo(message.chat.id,
                             'AgACAgIAAxkBAAMQX7Vub4z8vRMhFX5WnPETNii1-5IAAi6xMRuwg6lJQzUCj1aT6NdLC-SXLgADAQADAgADeAADrDMDAAEeBA',
                             F'Решается судьба [Анонима](tg://user?id={message.reply_to_message.from_user.id}), Админы, готовьтесь!',
                             reply_to_message_id=message.message_id, reply_markup=keyboard, parse_mode='markdown')

if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)
