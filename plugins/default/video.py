if answ[1] == 'видео':
		param = (('v', '5.68'), ('q',answ_text),('count','10'),('access_token',token),('adult','0'),('forward_messages',torep))
		res = requests.post('https://api.vk.com/method/video.search', data=param)
		res = json.loads(res.text)
		info = ''
		if (res['response']['count'] != 0):
			for item in res['response']['items']:
				if item['id'] == 170754590:
					continue
				if item['title'].lower().find('theync') != -1:
					continue
				info = info+'video'+str(item['owner_id'])+'_'+str(item['id'])+','
			param = (('v', '5.68'), ('peer_id',toho),('access_token',token),('forward_messages',torep),('message','Видео по вашему запросу'),('attachment',info))
			requests.post('https://api.vk.com/method/messages.send', data=param)
		else:
			apisay('Видео по запросу не найдены.',toho,torep)
