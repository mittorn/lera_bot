# -*- coding: utf-8 -*-
if answ[1] == 'хуй':
	a=list(map(str,answ_text.split()))
	m=["а", "о", "е", "ё", "э", "у", "ю", "я", "и"]
	s={
	    'я':"хуя",
	    'а':"хуя",
	    'о':"хуё",
	    'ё':"хуё",
	    'е':"хуе",
	    'э':"хуе",
	    'у':"хую",
	    'ю':"хую",
	    'и':"хуи"
	}
	r=""
	try:
		for n in a:
			if len(n)<4:
				r+=n+" "
			elif n[0] in m and n[2] == n[0]:
				r+=s[n[0]]+n[3::]+" "
			elif n[0] in m:
				r+=s[n[0]]+n[1::]+" "
			elif n[1] in m and n[3] == n[1]:
				r+=s[n[1]]+n[4::]+" "
			elif n[1] in m:
				r+=s[n[1]]+n[2::]+" "
			elif n[2] in m:
				r+=s[n[2]]+n[3::]+" "
			elif n[3] in m:
				r+=s[n[3]]+n[4::]+" "
			elif n[-1] in m:
				r+=s[n[-1]]+n[5::]+" "
		print(r)
		apisay(r,toho,torep)
	except:
		print("Видать накосячил")