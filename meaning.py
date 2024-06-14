import requests


def synonym(string):
	url="https://www.merriam-webster.com/dictionary/"+string
	var=requests.get(url)
	meaning=var.content
	word=meaning[1801:2050].strip()
	title=word.split('\n')[0]
	word_=word.split('\n')[1].strip()
	mea=word.split('\n')[1].strip()
	finalmeaning=mea[33:102]
	return finalmeaning.split('-')[1].strip()


print synonym("ghost")



