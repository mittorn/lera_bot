if answ[1] == 'доки':
	param = (('v', '5.68'), ('q',answ_text),('count','100'),('access_token',token),('forward_messages',torep))
	res = requests.post('https://api.vk.com/method/docs.search', data=param)
	res = json.loads(res.text)
	if (res['response']['count'] != 0):
		fcount=0
		info = ''
		for item in res['response']['items']:
			if fcount == 10:
				break
			if item['id'] in (474084484,444393573,337586976,467187768):
				continue
			if item['title'].lower().find('theync') != -1:
				continue
			if item['title'].lower().find('1man1jar') != -1:
				continue
			info = info+'doc'+str(item['owner_id'])+'_'+str(item['id'])+','
			fcount = fcount+1
		param = (('v', '5.68'), ('peer_id',toho),('access_token',token),('forward_messages',torep),('message','Документы по вашему запросу'),('attachment',info))
		requests.post('https://api.vk.com/method/messages.send', data=param)
	else:
		apisay('Документы по запросу не найдены',toho,torep)
if answ[1] == 'гиф':
	param = (('v', '5.68'), ('q',answ_text),('count','100'),('access_token',token),('forward_messages',torep))
	res = requests.post('https://api.vk.com/method/docs.search', data=param)
	res = json.loads(res.text)
	if (res['response']['count'] != 0):
		fcount=0
		info = ''
		for item in res['response']['items']:
			if fcount == 10:
				break
			if item['id'] in (474084484,444393573,337586976,467187768):
				continue
			if item['title'].lower().find('theync') != -1:
				continue
			if item['title'].lower().find('1man1jar') != -1:
				continue
			if item['ext']=='gif':
				info = info+'doc'+str(item['owner_id'])+'_'+str(item['id'])+','
				fcount = fcount+1
		param = (('v', '5.68'), ('peer_id',toho),('access_token',token),('forward_messages',torep),('message','Гифки по вашему запросу'),('attachment',info))
		requests.post('https://api.vk.com/method/messages.send', data=param)
	else:
		apisay('Гифки по запросу не найдены',toho,torep)
if answ[1] == 'фото':
	param = (('v', '5.68'), ('q',answ_text),('count','100'),('access_token',token),('forward_messages',torep))
	res = requests.post('https://api.vk.com/method/photos.search', data=param)
	res = json.loads(res.text)
	if (res['response']['count'] != 0):
		fcount=0
		info = ''
		for item in res['response']['items']:
			if fcount == 10:
				break
			info = info+'photo'+str(item['owner_id'])+'_'+str(item['id'])+','
			fcount = fcount+1
		param = (('v', '5.68'), ('peer_id',toho),('access_token',token),('forward_messages',torep),('message','Фотографии по вашему запросу'),('attachment',info))
		requests.post('https://api.vk.com/method/messages.send', data=param)
	else:
		apisay('Фотографии по запросу не найдены',toho,torep)
