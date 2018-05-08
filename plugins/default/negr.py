import random
from PIL import Image, ImageDraw
if answ[1] == 'негатив':
	param = (('v','5.68'),('access_token',token),('message_ids',torep))
	ret = requests.post('https://api.vk.com/method/messages.getById',data = param).text
	ret = json.loads(ret)
	try:
		ret = ret['response']['items'][0]['attachments'][0]['photo']
		retkeys = list(ret.keys())
		numlist = 0
		for i in range(len(retkeys)):
			if retkeys[i].find('photo') != -1:
				if int(retkeys[i].split('_')[1]) > numlist:    
					numlist = int(retkeys[i].split('_')[1])
		ret = ret['photo_'+str(numlist)]
		ret = requests.get(ret).content
		open('tmp/attach_neg.jpg','wb').write(ret)
		image = Image.open('tmp/attach_neg.jpg')
		draw = ImageDraw.Draw(image)
		width = image.size[0]
		height = image.size[1]
		pix = image.load()
		for i in range(width):
			for j in range(height):
				a = pix[i, j][0]
				b = pix[i, j][1]
				c = pix[i, j][2]
				draw.point((i, j), (255 - a, 255 - b, 255 - c)) 
		image.save("tmp/negr.jpg", "JPEG")
		del draw
		ret = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer?access_token={access_token}&v=5.68'.format(access_token=token)).json()
		with open('tmp/negr.jpg', 'rb') as f:
			ret = requests.post(ret['response']['upload_url'], files={'file1': f}).text
		ret = json.loads(ret)
		ret = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?v=5.68&album_id=-3&server='+str(ret['server'])+'&photo='+ret['photo']+'&hash='+str(ret['hash'])+'&access_token='+token).text
		ret = json.loads(ret)
		ret = requests.get('https://api.vk.com/method/messages.send?attachment=photo'+str(ret['response'][0]['owner_id'])+'_'+str(ret['response'][0]['id'])+'&v=5.68&peer_id='+str(toho)+'&access_token='+str(token))
	except KeyError:
		apisay('Пикчу-то вставь',toho,torep)
