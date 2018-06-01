from PIL import Image
if answ[1] == 'чеч':
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
		open('tmp/attachment.jpg','wb').write(ret)
		pic1 = Image.open('files/img/chech.png')
		pic2 = Image.open('tmp/attachment.jpg')
		pic1 = pic1.resize(pic2.size)
		pic2 = pic2.convert('RGBA')
		pic3 = Image.alpha_composite(pic2,pic1)
		pic3.save('tmp/chech.jpg')
		ret = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer?access_token={access_token}&v=5.68'.format(access_token=token)).json()
		with open('tmp/chech.jpg', 'rb') as f:
			ret = requests.post(ret['response']['upload_url'], files={'file1': f}).text
		ret = json.loads(ret)
		ret = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?v=5.68&album_id=-3&server='+str(ret['server'])+'&photo='+ret['photo']+'&hash='+str(ret['hash'])+'&access_token='+token).text
		ret = json.loads(ret)
		ret = requests.get('https://api.vk.com/method/messages.send?attachment=photo'+str(ret['response'][0]['owner_id'])+'_'+str(ret['response'][0]['id'])+'&v=5.68&peer_id='+str(toho)+'&access_token='+str(token))
	except KeyError:
		apisay('А что я обрабатывать то должна?',toho,torep)
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
from PIL import Image
if answ[1] == 'тлен':
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
		open('tmp/attachment.jpg','wb').write(ret)
		pic1 = Image.open('files/img/tlen.png')
		pic2 = Image.open('tmp/attachment.jpg')
		pic1 = pic1.resize(pic2.size)
		pic2 = pic2.convert('RGBA')
		pic3 = Image.alpha_composite(pic2,pic1)
		pic3.save('tmp/tlen.jpg')
		ret = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer?access_token={access_token}&v=5.68'.format(access_token=token)).json()
		with open('tmp/tlen.jpg', 'rb') as f:
			ret = requests.post(ret['response']['upload_url'], files={'file1': f}).text
		ret = json.loads(ret)
		ret = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?v=5.68&album_id=-3&server='+str(ret['server'])+'&photo='+ret['photo']+'&hash='+str(ret['hash'])+'&access_token='+token).text
		ret = json.loads(ret)
		ret = requests.get('https://api.vk.com/method/messages.send?attachment=photo'+str(ret['response'][0]['owner_id'])+'_'+str(ret['response'][0]['id'])+'&v=5.68&peer_id='+str(toho)+'&access_token='+str(token))
	except KeyError:
		apisay('А что я обрабатывать то должна?',toho,torep)
from PIL import Image
if answ[1] == 'вм':
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
		open('tmp/attachment.jpg','wb').write(ret)
		pic1 = Image.open('files/img/vietnam.png')
		pic2 = Image.open('tmp/attachment.jpg')
		pic1 = pic1.resize(pic2.size)
		pic2 = pic2.convert('RGBA')
		pic3 = Image.alpha_composite(pic2,pic1)
		pic3.save('tmp/vietnam.jpg')
		ret = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer?access_token={access_token}&v=5.68'.format(access_token=token)).json()
		with open('tmp/vietnam.jpg', 'rb') as f:
			ret = requests.post(ret['response']['upload_url'], files={'file1': f}).text
		ret = json.loads(ret)
		ret = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?v=5.68&album_id=-3&server='+str(ret['server'])+'&photo='+ret['photo']+'&hash='+str(ret['hash'])+'&access_token='+token).text
		ret = json.loads(ret)
		ret = requests.get('https://api.vk.com/method/messages.send?attachment=photo'+str(ret['response'][0]['owner_id'])+'_'+str(ret['response'][0]['id'])+'&v=5.68&peer_id='+str(toho)+'&access_token='+str(token))
	except KeyError:
		apisay('Пикчу то вставь',toho,torep)
from PIL import Image
if answ[1] == 'кек':
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
		open('tmp/attachment.jpg','wb').write(ret)
		image_obj = Image.open('tmp/attachment.jpg')
		try:
			if answ[2] == 'лол':
				image2 = image_obj.crop([0,0,int(image_obj.size[0]/2),int(image_obj.size[1])])
				image2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
				image_obj.paste(image2,(int(image_obj.size[0]/2),0))
				image_obj.save('tmp/kek.jpg')
				sendpic('kek.jpg','',toho,'')
		except IndexError:
			image2 = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
			image2 = image2.crop([0,0,int(image_obj.size[0]/2),int(image_obj.size[1])])
			image2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
			image_obj = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
			image_obj.paste(image2,(int(image_obj.size[0]/2),0))
			image_obj.save('tmp/kek.jpg')
			sendpic('kek.jpg','',toho,'')
	except KeyError:
		apisay('Пикчу то вставь',toho,torep)