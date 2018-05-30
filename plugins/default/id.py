if answ[1] == 'id':
	param = (('v','5.68'),('access_token',token),('message_ids',torep))
	ret = requests.post('https://api.vk.com/method/messages.getById',data = param).text
	
	try:
		ret = json.loads(ret)['response']['items'][0]['fwd_messages'][0]['user_id']
		apisay('id пользователя: '+str(ret), toho, torep)
	except:
		apisay('Ваш id: '+str(userid), toho, torep)