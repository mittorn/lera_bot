if answ_text == 'exit':
	exitgame()
	apisay('Чат с Лерой окончен',toho,torep)
else:
	param = (('q',answ_text),('adminname','RomkaZVO'))
	ret = requests.post('https://isinkin-bot-api.herokuapp.com/1/talk',data=param).json()
	apisay(ret['text'],toho,'')