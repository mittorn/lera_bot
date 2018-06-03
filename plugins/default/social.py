if answ[1] == 'инфо':
	apisay(open('files/txt/info','r').read(),toho,'')
if answ[1] == 'инфа':
	apisay('Вероятность этого равна '+str(random.randint(0,146))+'%',toho,torep)
if (answ[1]=='кого'):	
					if (toho < 2000000000):
						apisay('В личной переписке это не работает. Лишь в конфе',toho,torep)
					else:
						resapi = toho-2000000000;
						text = answ
						param = (('v', '5.68'), ('chat_id',resapi),('access_token',token))
						res = requests.post('https://api.vk.com/method/messages.getChatUsers', data=param)
						res = json.loads(res.text)
						rand = random.randint(0,len(res['response'])-1)
						param = (('v', '5.68'), ('user_ids',res['response'][rand]),('access_token',token))
						name = requests.post('https://api.vk.com/method/users.get', data=param)
						name = json.loads(name.text)
						name = name['response'][0]['first_name']+' '+name['response'][0]['last_name']
						if (random.randint(0,1)==0):
							apisay('Предпологаю, что это - '+name,toho,torep)
						else:
							apisay('Вангую, это '+name,toho,torep)
if answ[1] == 'модули':
	apisay('<br>'.join(dir),toho,torep)
if (answ[1]=='надо'):
	if (random.randint(0,1)==0):
		apisay('Однозначно, нет.',toho,torep)
	else:
		apisay('Да, надо.',toho,torep)
if (answ[0] in kb_name and answ[1] in ['стат','статус','стата']):
	text = '[ Статистика ]<br>Система:<br>&#8195;Процессоры:<br>'
	for idx, cpu in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
		text += '&#8195;&#8195;Ядро №'+str(idx+1)+': '+str(cpu)+'%<br>'
	mem = psutil.virtual_memory()
	MB = 1024 * 1024
	text += '&#8195;ОЗУ:<br>&#8195;&#8195;Всего: '+str(int(mem.total / MB))+'MB<br>&#8195;&#8195;Использовано: '+str(int((mem.total - mem.available) / MB))+'MB<br>&#8195;&#8195;Свободно: '+str(int(mem.available / MB))+'MB'
	param = (('v', '5.68'), ('peer_id',toho), ('access_token', token),('message', text),('forward_messages',torep))
	requests.post('https://api.vk.com/method/messages.send', param)
if answ[1] == 'обнова':
        apisay(open('files/txt/upd','r').read(),toho,torep)
if answ[1] == 'когда':
	months = ['сентября','октября','ноября','декабря','января','февраля','марта','апреля','мая','июня','июля','августа']
	randnum = random.randint(0,10)
	if randnum <= 4:
		apisay(random.choice(['Никогда','Когда рак на горе свистнет','Очень скоро','Завтра']),toho,torep)
	else:
		apisay('Я уверена это случится '+str(random.randint(1,31))+' '+random.choice(months)+' '+str(random.randint(2018,2050)),toho,torep)
if (answ[1]=='кто'):	
					if (toho < 2000000000):
						apisay('В личной переписке это не работает. Лишь в конфе',toho,torep)
					else:
						resapi = toho-2000000000;
						text = answ
						param = (('v', '5.68'), ('chat_id',resapi),('access_token',token))
						res = requests.post('https://api.vk.com/method/messages.getChatUsers', data=param)
						res = json.loads(res.text)
						rand = random.randint(0,len(res['response'])-1)
						param = (('v', '5.68'), ('user_ids',res['response'][rand]),('access_token',token))
						name = requests.post('https://api.vk.com/method/users.get', data=param)
						name = json.loads(name.text)
						name = name['response'][0]['first_name']+' '+name['response'][0]['last_name']
						if (random.randint(0,1)==0):
							apisay('Есть вероятность, что это - '+name,toho,torep)
						else:
							apisay('Я уверена, это у нас '+name,toho,torep)
if (answ[1]=='кофейник'):	
        apisay('http://vkcoffee.operator555.su',toho,'')
if answ[1] == 'помощь':
	apisay(open('files/txt/help','r').read(),toho,'')
if answ[1] == 'id':
	param = (('v','5.68'),('access_token',token),('message_ids',torep))
	ret = requests.post('https://api.vk.com/method/messages.getById',data = param).text
	
	try:
		ret = json.loads(ret)['response']['items'][0]['fwd_messages'][0]['user_id']
		apisay('id пользователя: '+str(ret), toho, torep)
	except:
		apisay('Ваш id: '+str(userid), toho, torep)
if answ[1] == 'дата':
	apisay(time.ctime(),toho,torep)
if (answ[0] in kb_name and answ[1] in ['гусь']):
	apisay(open('system/goose','r').read(),toho,torep)
if answ[1] == 'цит':
	apisay(open('files/txt/quotes/quote'+str(random.randint(1,14)),'r').read(),toho,'')

