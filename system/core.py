if 'source_act' in result[6]:
	if result[6]['source_act'] == 'chat_invite_user':
		param = (('v', '5.68'), ('user_ids',result[6]['source_mid']),('access_token',token))
		name = requests.post('https://api.vk.com/method/users.get', data=param)
		name = json.loads(name.text)
		name = name['response'][0]['first_name']+' '+name['response'][0]['last_name']
		apisay('Привет, '+name+'<br>В беседе есть бот - Лера<br>Напиши "Лера помощь", чтоб увидеть список команд или "инфо" для того, что бы узнать больше информации о боте.<br>Хочешь в друзья? Заявка обрабатывается автоматически',toho,'')
if result[5].lower().find('гусь') != -1:
    apisay(open('system/gusi/goose'+str(random.randint(1,6)),'r').read(),toho,torep)
