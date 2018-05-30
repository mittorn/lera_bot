if answ[1] == 'бан':
	param = (('v','5.68'),('access_token',token),('message_ids',torep))
	ret = requests.post('https://api.vk.com/method/messages.getById',data = param).text
	ret = json.loads(ret)['response']['items'][0]['fwd_messages'][0]['user_id']
	
	blacklist = json.load(open('system/blacklist'))
	
	if str(ret) not in blacklist:
		blacklist.append(str(ret))
	
	with open('system/blacklist','w') as file:
		json.dump(blacklist, file)
				
	apisay('Пользователь '+str(ret)+' был добавлен в ЧС!', toho, torep)
	requests.get('https://api.vk.com/method/account.ban?access_token='+str(token)+'&owner_id='+str(ret)+'&v=5.68&lp_version=2')

if answ[1] == 'разбан':
	id = ''
	blacklist = json.load(open('system/blacklist'))
	isFound = True
	
	param = (('v','5.68'),('access_token',token),('message_ids',torep))
	ret = requests.post('https://api.vk.com/method/messages.getById',data = param).text
	
	try:
		ret = json.loads(ret)['response']['items'][0]['fwd_messages'][0]['user_id']
		id = str(ret)
	except:
		try:
			id = answ[2]
		except:
			pass
			
	try:
		blacklist.remove(id)
	except:
		apisay('Пользователь не найден!', toho, torep)
		isFound = False
		
	with open('system/blacklist','w') as file:
		json.dump(blacklist, file)
	
	if isFound == True:
		apisay('Пользователь '+id+' был удален из ЧС!', toho, torep)
		requests.get('https://api.vk.com/method/account.unban?access_token='+str(token)+'&owner_id='+id+'&v=5.68&lp_version=2')