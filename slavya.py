import logging
import time
import random
import pymongo
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from pymongo import MongoClient

bot = Bot('1303468919:AAGa9vt8IXsEf1M9SOAUjeN1qwrjv6FEYE0')
db = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)
client = pymongo.MongoClient('mongodb+srv://SkyDeaD:GamerVD76@aliceskybotandother-ik6lu.mongodb.net/sl?retryWrites=true&w=majority')
dbm = client.sl
users=dbm.users

banuser = 0
admuser = 0
userstatus = 0
useradm = 0

@db.message_handler(commands=['start'])
async def start_handler(message):
	if message.chat.type=='private':
		await message.reply(F'Привет, {message.from_user.first_name}!\nНажми 👉/help👈 ')

@db.message_handler(commands=['help'])
async def help_handler(message):
	if message.chat.type=='private':
		q = await bot.get_chat(577096232)
		c = await bot.get_chat(-1001183567504)
		await message.reply(F'''
Я - бот Славя, разработанный 👉[{q.first_name}](tg://user?id=577096232)👈 

Бот создавался для конфы 👉[{c.title}](https://t.me/YgoloMasteraSlavi)👈


На данный момент доступны следующие команды:

*👤me* - информация о себе.

*ℹ️info* - полная информация о пользователе и группе.

*🌟admins* - список администраторов.

*📜* - правила чата.

*✂️* - установить/обновить правила чата.

*🗞* - удалить правла чата.

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
''', parse_mode = 'markdown')
	else:
		help_msg = await message.reply('''
На данный момент доступны следующие команды:

*👤me* - информация о себе.

*ℹ️info* - полная информация о пользователе и группе.

*🌟admins* - список администраторов.

*📜* - правила чата.

*✂️* - установить/обновить правила чата.

*🗞* - удалить правла чата.

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
''', parse_mode = 'markdown')
		time.sleep(60)
		await bot.delete_message(message.chat.id, help_msg.message_id)
		await bot.delete_message(message.chat.id, message.message_id)

@db.message_handler(content_types=['new_chat_members'])
async def handler_new_member(message):
	for user in message.new_chat_members:
		if user.id in [1303468919]:
			await bot.send_message(message.chat.id, 'Привет! Я - бот-администратор Славя. Для полноценный работы выдай мне следующие разрешения:\n\n〽️Изменения профиля группы\n❌Удаление сообщений\n📛Блокировка участников\n📨Пригласительные ссылки\n📌Закрепление сообщений\n⭐️Добавление администраторов')
		else:
			for user in message.new_chat_members:
				sti = open('welcome.webp', 'rb')
				await bot.send_sticker(message.chat.id, sti, reply_to_message_id=message.message_id)
				await bot.send_message(message.chat.id, F'Добро пожаловать в чат [{message.chat.title}](https://t.me/{message.chat.username}), [{user.first_name}](tg://user?id={user.id})!\n\nПредлагаю ознакомиться с правилами:\n👉/rules👈', reply_to_message_id=message.message_id, parse_mode='markdown')

@db.message_handler(commands=['mute'])
async def handle_mute(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['administrator', 'creator']:
			prom = await bot.get_chat_member(message.chat.id, 1303468919)
			if prom.can_restrict_members==True:
				if message.reply_to_message!=None:
					user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
					if user.status not in ['administrator', 'creator']:
						u_mute = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
						if u_mute.can_send_messages==True or u_mute.can_send_messages==None:
							await bot.send_message(message.chat.id, F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) потерял голос.', reply_to_message_id =message.reply_to_message.message_id, parse_mode='markdown')
							await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date = time.time())
							sti = open('mute.webp', 'rb')
							await bot.send_sticker(message.chat.id, sti, reply_to_message_id=message.message_id)
						else:
							await bot.send_message(message.chat.id, F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) и так молчит.', reply_to_message_id=message.message_id, parse_mode='markdown')
					else:
						await bot.send_message(message.chat.id, 'Я не буду мутить администратора!', reply_to_message_id = message.message_id)
				else:
					await bot.send_message(message.chat.id,' Я не понимаю, о ком идёт речь? ', reply_to_message_id = message.message_id)
			else:
				await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников', reply_to_message_id = message.message_id)
		else:
			await bot.delete_message(message.chat.id, message.message_id)

@db.message_handler(commands=['amute'])
async def handle_amute(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['creator']:
			prom = await bot.get_chat_member(message.chat.id, 1303468919)
			if prom.can_restrict_members==True:
				if message.reply_to_message!=None:
					try:
						await bot.send_message(message.chat.id, F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) потерял голос.', reply_to_message_id =message.reply_to_message.message_id, parse_mode='markdown')
						await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=time.time())
						sti = open('mute.webp', 'rb')
						await bot.send_sticker(message.chat.id, sti, reply_to_message_id=message.message_id)
					except:
						await bot.send_message(message.chat.id, 'Я не могу замутить данного пользователя', reply_to_message_id=message.message_id)
				else:
					await bot.send_message(message.chat.id,' Я не понимаю, о ком идёт речь? ', reply_to_message_id=message.message_id)
			else:
				await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников', reply_to_message_id = message.message_id)
		else:
			await bot.send_message(message.chat.id, 'У вас нет прав на выполнение данной комманды!', reply_to_message_id=message.message_id)

@db.message_handler(commands=['unmute'])
async def handle_unmute(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['administrator', 'creator']:
			prom = await bot.get_chat_member(message.chat.id, 1303468919)
			if prom.can_restrict_members==True:
				if message.reply_to_message!=None:
					user = await bot.get_chat_member( message.chat.id, message.reply_to_message.from_user.id)
					if user.status not in ['administrator', 'creator']:
						u_mute = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
						if u_mute.can_send_messages==False:
							await bot.send_message(message.chat.id, F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) снова может говорить.', reply_to_message_id = message.message_id, parse_mode = 'markdown')
							await bot.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
							sti = open('unmute.webp', 'rb')
							await bot.send_sticker(message.chat.id, sti, reply_to_message_id=message.message_id)
						else:
							await bot.send_message(message.chat.id, F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) и так может говорить.', reply_to_message_id=message.message_id, parse_mode='markdown')
					else:
						await bot.send_message(message.chat.id, ' Администратор не может быть в муте. ', reply_to_message_id = message.message_id)
				else:
					await bot.send_message(message.chat.id,' Я не понимаю, о ком идёт речь? ', reply_to_message_id = message.message_id)
			else:
				await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников', reply_to_message_id = message.message_id)
		else:
			await bot.delete_message(message.chat.id, message.message_id)

@db.message_handler(commands=['promote'])
async def handle_promote(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['creator']:
			prom = await bot.get_chat_member(message.chat.id, 1303468919)
			if prom.can_promote_members==True:
				if message.reply_to_message!= None:
					user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
					if user.status not in ['administrator', 'creator']:
						await bot.send_message(message.chat.id, F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) повышен(а)!', reply_to_message_id = message.message_id, parse_mode = 'markdown')
						await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_change_info=True, can_delete_messages=True, can_invite_users=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True)
					else:
						await bot.send_message(message.chat.id, ' Пользователь уже является администратором! ', reply_to_message_id = message.message_id)
				else:
					await bot.send_message(message.chat.id,' Я не понимаю, о ком идёт речь? ', reply_to_message_id = message.message_id)			
			else:
				await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n⭐️Добавление администраторов', reply_to_message_id = message.message_id)
		else:
			await bot.delete_message(message.chat.id, message.message_id)

@db.message_handler(commands=['demote'])
async def handle_demote(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['creator']:
			prom = await bot.get_chat_member(message.chat.id, 1303468919)
			if prom.can_promote_members==True:
				if message.reply_to_message!=None:
					user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
					if user.status in ['administrator', 'creator']:
						try:
							await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_change_info=False, can_delete_messages=False, can_invite_users=False, can_restrict_members=False, can_pin_messages=False, can_promote_members=False)
							await bot.send_message(message.chat.id, F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) понижен(а)!', reply_to_message_id = message.message_id, parse_mode='markdown')
						except:
							await bot.send_message(message.chat.id, ' Я не могу понизить данного пользвателя. ', reply_to_message_id = message.message_id)
					else:
						await bot.send_message(message.chat.id, ' Я не могу понизить пользователя, который не является администратором! ', reply_to_message_id = message.message_id)
				else:
					await bot.send_message(message.chat.id,' Я не понимаю, о ком идёт речь? ', reply_to_message_id = message.message_id)			
			else:
				await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n⭐️Добавление администраторов', reply_to_message_id = message.message_id)
		else:
			await bot.delete_message(message.chat.id, message.message_id)

@db.message_handler(commands=['kick'])
async def handle_kick(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['administrator', 'creator']:
			prom = await bot.get_chat_member(message.chat.id, 1303468919)
			if prom.can_restrict_members==True:
				if message.reply_to_message!=None:
					user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
					if user.status not in ['administrator', 'creator']:
						users = await bot.get_chat(message.chat.id)
						if user.status=='member':
							sti = open('kick.webp', 'rb')
							await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
							await bot.send_message(message.chat.id, F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) решил(а) отойти 😄', reply_to_message_id=message.message_id, parse_mode='markdown')
							await bot.send_sticker(message.chat.id, sti)
							await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
						else:
							await bot.send_message(message.chat.id, F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не является участником чата.', reply_to_message_id=message.message_id, parse_mode='markdown')
					else:
						await bot.send_message(message.chat.id, ' Я не могу кикнуть администратора... ', reply_to_message_id=message.message_id)
				else:
					await bot.send_message(message.chat.id,' Я не понимаю, о ком идёт речь? ', reply_to_message_id=message.message_id)			
			else:
				await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников', reply_to_message_id=message.message_id)

@db.message_handler(commands=['akick'])
async def handle_akick(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['creator']:
			prom = await bot.get_chat_member(message.chat.id, 1303468919)
			if prom.can_restrict_members==True:
				if message.reply_to_message!=None:
					try:
						sti = open('kick.webp', 'rb')
						await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
						await bot.send_message(message.chat.id, F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) решил(а) отойти 😄', reply_to_message_id=message.message_id, parse_mode='markdown')
						await bot.send_sticker(message.chat.id, sti)
						await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
					except:
						await bot.send_message(message.chat.id, 'Я не могу кикнуть данного пользователя', reply_to_message_id=message.message_id)
				else:
					await bot.send_message(message.chat.id,' Я не понимаю, о ком идёт речь? ', reply_to_message_id=message.message_id)
			else:
				await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников', reply_to_message_id = message.message_id)
		else:
			await bot.send_message(message.chat.id, 'У вас нет прав на выполнение данной комманды!', reply_to_message_id=message.message_id)

@db.message_handler(commands=['unban'])
async def handle_unban(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['administrator', 'creator']:
			prom = await bot.get_chat_member(message.chat.id, 1303468919)
			if prom.can_restrict_members==True:
				if message.reply_to_message!=None:
					user = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
					if user.status not in ['administrator', 'creator']:	
						if user.status=='restricted':
							sti = open('unban.webp', 'rb')
							await bot.send_message(message.chat.id, F'Ладно, [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) может вернуться.', reply_to_message_id = message.message_id, parse_mode = 'markdown')
							await bot.send_sticker(message.chat.id, sti)
							await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
						else:
							await bot.send_message(message.chat.id, F'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) не забанен.', reply_to_message_id=message.message_id, parse_mode='markdown')
					else:
						await bot.send_message(message.chat.id, 'Администратор не может быть забанен.', reply_to_message_id = message.message_id)
				else:
					await bot.send_message(message.chat.id, 'Я не понимаю, о ком идёт речь?', reply_to_message_id = message.message_id)			
			else:
				await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n📛Блокировка участников', reply_to_message_id=message.message_id)
		else:
			await bot.delete_message(message.chat.id, message.message_id)

@db.message_handler(commands=['pin'])
async def handle_pin(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['administrator', 'creator']:
			prom = await bot.get_chat_member(message.chat.id, 1303468919)
			if prom.can_pin_messages==True:
				if message.reply_to_message!=None:
					await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
					await bot.delete_message(message.chat.id, message.message_id)
				else:
					await bot.send_message(message.chat.id,' Выберите сообщение, которое нужно закрепить ', reply_to_message_id = message.message_id)			
			else:
				await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n📌Закрепление сообщений', reply_to_message_id=message.message_id)
		else:
			await bot.delete_message(message.chat.id, message.message_id)

@db.message_handler(commands=['unpin'])
async def handle_unpin(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['administrator', 'creator']:
			prom = await bot.get_chat_member(message.chat.id, 1303468919 )
			if prom.can_pin_messages == True:
				await bot.unpin_chat_message(message.chat.id)
				await bot.delete_message(message.chat.id, message.message_id)
			else:
				await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n📌Закрепление сообщений\n❌Удаление сообщений', reply_to_message_id=message.message_id)
		else:
			await bot.delete_message(message.chat.id, message.message_id)

@db.message_handler(commands=['del'])
async def handle_del(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['administrator', 'creator']:
			prom = await bot.get_chat_member(message.chat.id, 1303468919)
			if prom.can_delete_messages==True:
				if message.reply_to_message!=None:
					await bot.delete_message(message.chat.id, message.reply_to_message.message_id)
					await bot.delete_message(message.chat.id, message.message_id)
				else:
					await bot.send_message(message.chat.id,' Выберите сообщение, которое нужно удалить ', reply_to_message_id=message.message_id)
			else:
				await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n❌Удаление сообщений', reply_to_message_id=message.message_id)
		else:
			await bot.delete_message(message.chat.id, message.message_id)

@db.message_handler(commands=['purge'])
async def handle_purge(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['administrator', 'creator']:
			prom = await bot.get_chat_member(message.chat.id, 1303468919)
			if prom.can_delete_messages==True:
				if message.reply_to_message!=None:
					i = message.reply_to_message.message_id
					q = message.message_id
					for d in range(i, q):
						try:
							await bot.delete_message(message.chat.id, d)
						except:
							pass
					await bot.delete_message(message.chat.id, message.message_id)
					await bot.send_message(message.chat.id, ' Чистка завершена. ')
				else:
					await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n❌Удаление сообщений.', reply_to_message_id=message.message_id)
		else:
			await bot.delete_message(message.chat.id, message.message_id)

@db.message_handler(commands=['setrules'])
async def handle_rulses(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['administrator', 'creator']:
			x = users.find_one({'rules':{'$exists':True}, 'chatid':message.chat.id})
			if x == None:
				rules = message.reply_to_message.text
				users.insert_one({'rules':rules, 'chatid':message.chat.id})
				await bot.send_message(message.chat.id, F'Правила чата [{message.chat.title}](https://t.me/{message.chat.username}) установлены.', reply_to_message_id=message.message_id, parse_mode='markdown')
			elif x != None:
				rules = message.reply_to_message.text
				users.delete_one({'rules':{'$exists':True}, 'chatid':message.chat.id})
				users.insert_one({'rules':rules, 'chatid':message.chat.id})
				await bot.send_message(message.chat.id, F'Правила чата [{message.chat.title}](https://t.me/{message.chat.username}) обновлены.', reply_to_message_id=message.message_id, parse_mode='markdown')

@db.message_handler(commands=['delrules'])
async def handle_rulses(message):
	if message.chat.type!='private':
		usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
		if usera.status in ['administrator', 'creator']:
			users.delete_one({'rules':{'$exists':True}, 'chatid':message.chat.id})
			await bot.send_message(message.chat.id, F'Правила чата [{message.chat.title}](https://t.me/{message.chat.username}) удалены.', reply_to_message_id=message.message_id, parse_mode='markdown')

@db.message_handler(commands=['rules'])
async def handle_rulses(message):
	if message.chat.type!='private':
		x = users.find_one({'rules':{'$exists':True}, 'chatid':message.chat.id})
		if x == None:
			await bot.send_message(message.chat.id, F'В данном чате пока что нет правил.', reply_to_message_id=message.message_id, parse_mode='markdown')
		else:
			for rul in users.find({'chatid':message.chat.id}):
				await bot.send_message(message.chat.id, rul['rules'], reply_to_message_id=message.message_id, parse_mode='markdown')

@db.message_handler(commands=["report"])
async def mandle_report(message):
	if message.chat.type!='private':
		if message.reply_to_message!= None:
			adm = await bot.get_chat_administrators(message.chat.id)
			text = 'На данное сообщение поступила жалоба.\n\n'
			for i in adm:
				if i.user.is_bot==False:
					text += f"\n@{i.user.username}"
			await bot.send_message(message.chat.id, text, reply_to_message_id=message.reply_to_message.message_id)
		else:
			await bot.send_message(message.chat.id, " Выберите сообщение, на которое хотите пожаловаться. ", reply_to_message_id = message.message_id)

@db.message_handler(commands=['me'])
async def handle_message(message):
	await bot.send_message( message.chat.id, F''' 
*Ваше имя*: `{message.from_user.first_name}`
*Ваш юзернейм*: `@{message.from_user.username}`
*Ваш ID*: `{message.from_user.id} `
''', reply_to_message_id = message.message_id, parse_mode='markdown')

@db.message_handler(commands=['info'])
async def handle_info(message):
	if message.chat.type!='private':
		if message.reply_to_message!= None:
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
		else:
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

@db.message_handler(commands=['admins'])
async def handle_admins(message):
	if message.chat.type!='private':
		adm = await bot.get_chat_administrators(message.chat.id)
		text = 'Администраторы чата:\n'
		for i in adm:
			if i.user.is_bot==False:
				text += f'\nИмя - {i.user.first_name}\nЮзернейм - {i.user.username}\n'
		await bot.send_message(message.chat.id, text)

@db.message_handler(commands=['save'])
async def handle_save(message):
	if message.from_user.id in [577096232, 609565291]:
		if not message.reply_to_message:
			return
		if message.reply_to_message.content_type == "photo":
			x = users.find_one({'type_cer':'photo', 'doc_id':message.reply_to_message.photo[-1].file_id})
			if x == None:
				users.insert_one({'type_cer':'photo', 'doc_id':message.reply_to_message.photo[-1].file_id})
				await bot.send_message(message.chat.id, 'Файл сохранён!', reply_to_message_id=message.message_id)
			else:
				await bot.send_message(message.chat.id, 'Данный файл уже сохранён!', reply_to_message_id=message.message_id)
		elif message.reply_to_message.content_type == "animation":
			x = users.find_one({'type_cer':'anim', 'doc_id':message.reply_to_message.animation.file_id})
			if x == None:
				users.insert_one({'type_cer':'anim', 'doc_id':message.reply_to_message.animation.file_id})
				await bot.send_message(message.chat.id, 'Файл сохранён!', reply_to_message_id=message.message_id)
			else:
				await bot.send_message(message.chat.id, 'Данный файл уже сохранён!', reply_to_message_id=message.message_id)
		else:
			await bot.send_message(message.chat.id, 'Нужно выбрать фотографию или gif-анимацию.', reply_to_message_id=message.message_id)

@db.message_handler(regexp='фулл')
async def full_ban(message):
	if message.chat.type!='private':
		await bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAPmXyGM-GqjlGEabzESpkikWfQRIcIAAgiuMRtGQhBJHQZufSPeAo_6avuULgADAQADAgADeQADq5wCAAEaBA')

@db.message_handler(regexp='цербера хочу')
async def ceph(message):
	if message.chat.id in [-1001216079799, -1001183567504] and message.from_user.id==609565291:
		n = message.from_user.first_name
		n = n.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
		z = message.from_user.last_name
		if z !=None:
			z = z.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':609565291, 'times':0})
			else:
				users.update_one({'id':609565291}, {'$inc':{'times':1}})
				for time in users.find({'id':609565291}):
					await bot.send_message(message.chat.id, F'*{n} {z}* заебал, хочет Цербера уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')
		else:
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':609565291, 'times':0})
			else:
				users.update_one({'id':609565291}, {'$inc':{'times':1}})
				for time in users.find({'id':609565291}):
					await bot.send_message(message.chat.id, F'*{n}* заебал, хочет Цербера уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')

@db.message_handler(regexp='похуй')
async def pox(message):
	if message.chat.id in [-1001216079799, -1001183567504] and message.from_user.id==577096232:
		n = message.from_user.first_name
		n = n.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
		z = message.from_user.last_name
		if z !=None:
			z = z.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':577096232, 'times':0})
			else:
				users.update_one({'id':577096232}, {'$inc':{'times':1}})
				for time in users.find({'id':577096232}):
					await bot.send_message(message.chat.id, F'*{n} {z}* похуй уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')
		else:
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':577096232, 'times':0})
			else:
				users.update_one({'id':577096232}, {'$inc':{'times':1}})
				for time in users.find({'id':577096232}):
					await bot.send_message(message.chat.id, F'*{n}* похуй уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')

@db.message_handler(regexp='хочу 02')
async def pox(message):
	if message.chat.id in [-1001216079799, -1001183567504] and message.from_user.id==839954020:
		n = message.from_user.first_name
		n = n.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
		z = message.from_user.last_name
		if z !=None:
			z = z.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':839954020, 'times':0})
			else:
				users.update_one({'id':839954020}, {'$inc':{'times':1}})
				for time in users.find({'id':839954020}):
					await bot.send_message(message.chat.id, F'*{n} {z}* хочет 02 уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')
		else:
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':839954020, 'times':0})
			else:
				users.update_one({'id':839954020}, {'$inc':{'times':1}})
				for time in users.find({'id':839954020}):
					await bot.send_message(message.chat.id, F'*{n}* хочет 02 уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')

@db.message_handler(regexp='хочу виолу')
async def pox(message):
	if message.chat.id in [-1001216079799, -1001183567504] and message.from_user.id==593146532:
		n = message.from_user.first_name
		n = n.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
		z = message.from_user.last_name
		if z !=None:
			z = z.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':593146532, 'times':0})
			else:
				users.update_one({'id':593146532}, {'$inc':{'times':1}})
				for time in users.find({'id':593146532}):
					await bot.send_message(message.chat.id, F'*{n} {z}* хочет Виолу уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')
		else:
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':593146532, 'times':0})
			else:
				users.update_one({'id':593146532}, {'$inc':{'times':1}})
				for time in users.find({'id':593146532}):
					await bot.send_message(message.chat.id, F'*{n}* хочет Виолу уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')

@db.message_handler(regexp='слава виоле')
async def pox(message):
	if message.chat.id in [-1001216079799, -1001183567504] and message.from_user.id==593146532:
		n = message.from_user.first_name
		n = n.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
		z = message.from_user.last_name
		if z !=None:
			z = z.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':593146532, 'times':0})
			else:
				users.update_one({'id':593146532}, {'$inc':{'times':1}})
				for time in users.find({'id':593146532}):
					await bot.send_message(message.chat.id, F'*{n} {z}* восхваляет Виолу уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')
		else:
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':593146532, 'times':0})
			else:
				users.update_one({'id':593146532}, {'$inc':{'times':1}})
				for time in users.find({'id':593146532}):
					await bot.send_message(message.chat.id, F'*{n}* восхваляет Виолу уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')

@db.message_handler(regexp='хочу пиццу')
async def pox(message):
	if message.chat.id in [-1001216079799, -1001183567504] and message.from_user.id==541023518:
		n = message.from_user.first_name
		n = n.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
		z = message.from_user.last_name
		if z != None:
			z = z.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':541023518, 'times':0})
			else:
				users.update_one({'id':541023518}, {'$inc':{'times':1}})
				for time in users.find({'id':541023518}):
					await bot.send_message(message.chat.id, F'*{n} {z}* хочет пиццу уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')
		else:
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':541023518, 'times':0})
			else:
				users.update_one({'id':541023518}, {'$inc':{'times':1}})
				for time in users.find({'id':541023518}):
					await bot.send_message(message.chat.id, F'*{n}* хочет пиццу уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')

@db.message_handler(regexp='слава ситису')
async def pox(message):
	if message.chat.id in [-1001216079799, -1001183567504] and message.from_user.id==717015019:
		n = message.from_user.first_name
		n = n.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
		z = message.from_user.last_name
		if z != None:
			z = z.replace('*', '').replace('_', '').replace('`', '').replace('~', '')
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':717015019, 'times':0})
			else:
				users.update_one({'id':717015019}, {'$inc':{'times':1}})
				for time in users.find({'id':717015019}):
					await bot.send_message(message.chat.id, F'*{n} {z}* восхваляет Ситиса уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')
		else:
			x = users.find_one({'id':message.from_user.id})
			if x == None:
				users.insert_one({'id':717015019, 'times':0})
			else:
				users.update_one({'id':717015019}, {'$inc':{'times':1}})
				for time in users.find({'id':717015019}):
					await bot.send_message(message.chat.id, F'*{n}* восхваляет Ситиса уже в*' + ' ' +str(time['times']) + ' ' + '*раз.', reply_to_message_id=message.message_id, parse_mode='markdown')

@db.message_handler(regexp='цербер')
async def handle_cerber(message):
	a=[]
	ran = random.randint(1,2)
	if ran == 1:
		for i in users.find({'type_cer':'photo'}):
			a.append(i['doc_id'])
		print(a)
		p_id = random.choice(a)
		await bot.send_photo(message.chat.id, p_id)
	else:
		for i in users.find({'type_cer':'anim'}):
			a.append(i['doc_id'])
		print(a)
		p_id = random.choice(a)
		await bot.send_photo(message.chat.id, p_id)

@db.callback_query_handler(text='1')
async def button_reaction(call: types.CallbackQuery):
	global banuser
	global admuser
	global useradm
	global userstatus
	if call.message:
		if call.data=='1':
			if call.from_user.id == admuser and userstatus.status in ['creator']:
				try:
					await bot.kick_chat_member(chat_id=call.message.chat.id, user_id=banuser) 
					await call.message.edit_caption(F'*——Суд Властелинов казнил* [неверного](tg://user?id={banuser})!——', parse_mode='markdown')
					await bot.send_animation(chat_id=call.message.chat.id, animation='CgACAgQAAxkBAAIBel8pztumhQxhwkZ8QQ29C_3ltR2-AAJ8AgAC2MRNUZCDixLVkQwVGgQ', reply_to_message_id=call.message.message_id)
				except:
					await call.message.edit_caption('*———Ошибка!———*', parse_mode='markdown')
			elif call.from_user.id == admuser and userstatus.status in ['administrator']:
				if useradm.status not in ['administrator', 'creator']:
					await bot.kick_chat_member(chat_id=call.message.chat.id, user_id=banuser) 
					await call.message.edit_caption(F'*——Суд Властелинов казнил* [неверного](tg://user?id={banuser})!——', parse_mode='markdown')
					await bot.send_animation(chat_id=call.message.chat.id, animation='CgACAgQAAxkBAAIBel8pztumhQxhwkZ8QQ29C_3ltR2-AAJ8AgAC2MRNUZCDixLVkQwVGgQ', reply_to_message_id=call.message.message_id)
				else:
					await call.message.edit_caption('*———Ошибка!———*', parse_mode='markdown')

@db.callback_query_handler(text='2')
async def button_reaction(call: types.CallbackQuery):
	global banuser
	global admuser
	if call.message:
		if call.data=='2':
			if call.from_user.id == admuser:
				await call.message.edit_caption('\*\*\*'+'*Властелины милосердно простили*'+' '+F'[Анонима](tg://user?id={banuser})'+'*; ступай с миром.*'+'\*\*\*', parse_mode='markdown')
				await bot.send_animation(chat_id=call.message.chat.id, animation='CgACAgIAAxkBAAIBe18p1NYZODgJhLLQq28aHskjKP9cAALpAwACgyVYS3rEbZUfdbcKGgQ', reply_to_message_id=call.message.message_id)

@db.message_handler(content_types=['text'])
async def handle_text(message):
	if message.text.lower()=='властилинус пенитратус':
		if message.chat.type!='private':
			if message.reply_to_message!=None:
				if message.from_user.id!=message.reply_to_message.from_user.id:
					user_1 = await bot.get_chat_member(message.chat.id, message.from_user.id)
					user_2 = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
					if user_1.status not in ['administrator', 'creator']:
						await bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date = time.time())
					if user_2.status not in ['administrator', 'creator']:
						await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date = time.time())
					await bot.send_message(message.chat.id, F'*{message.from_user.first_name}* и *{message.reply_to_message.from_user.first_name}* не поделили Ульянин пирожок и были замучены.', reply_to_message_id=message.message_id, parse_mode='markdown' )
	
	elif message.text.lower()=='властилинатус':
		prom = await bot.get_chat_member(message.chat.id, 1303468919)
		if prom.can_restrict_members==True:
			if message.reply_to_message!=None:
				if message.chat.type!='private':
					usera = await bot.get_chat_member(message.chat.id, message.from_user.id)
					if usera.status in ['administrator', 'creator']:
						global banuser
						banuser = message.reply_to_message.from_user.id
						global admuser
						admuser = message.from_user.id
						global userstatus
						userstatus = await bot.get_chat_member(message.chat.id, message.from_user.id)
						global useradm
						useradm = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
						keyboard = types.InlineKeyboardMarkup(row_width = 1)
						item1 = types.InlineKeyboardButton(text='БанХаммером в лицо', callback_data='1')
						item2 = types.InlineKeyboardButton(text='Пощадить Анона', callback_data='2')
						keyboard.add(item1, item2)
						await bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIBeV8puKv2I-flODKea1u-40ECk89sAAL4rjEbsFRRSVEBLpMMCS_oGuc-li4AAwEAAwIAA3kAAwQ8AAIaBA', F'Решается судьба [Анонима](tg://user?id={message.reply_to_message.from_user.id}), Властелины, готовьтесь!', reply_to_message_id=message.message_id, reply_markup=keyboard, parse_mode='markdown')
		else:
			await bot.send_message(message.chat.id, 'Для выполнения данной команды требуются следующие права администратора:\n\n⭐️Добавление администраторов', reply_to_message_id = message.message_id)

if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)