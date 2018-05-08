if answ[1] == 'когда':
	months = ['сентября','октября','ноября','декабря','января','февраля','марта','апреля','мая','июня','июля','августа']
	randnum = random.randint(0,10)
	if randnum <= 4:
		apisay(random.choice(['Никогда','Когда рак на горе свистнет','Очень скоро','Завтра']),toho,torep)
	else:
		apisay('Я уверена это случится '+str(random.randint(1,31))+' '+random.choice(months)+' '+str(random.randint(2018,2050)),toho,torep)