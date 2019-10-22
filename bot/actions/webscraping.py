import requests
from bs4 import BeautifulSoup

class WebScrapingIntegration:
	def __init__(self):
		self.url = 'https://fga.unb.br/coordenacao'
		self.r = requests.get(self.url)
		self.soup = BeautifulSoup(self.r.text, 'html.parser')
		self.coordinators = self.soup.find_all('div', class_='article-body article-body-text-article')

	def software_coordinator(self):
		names = ''
		flag = True
		for coord_td in self.coordinators:
			lista = coord_td.find_all('td')
			cont = int(0)
			for coord_list in lista:
				x = coord_list.next_element
				if x.find('span') != -1:
					cont+=1
					continue
				elif x.find('Eng.') != -1 and x.find('Software') == -1:
					flag = False
					continue
				elif x.find('Eng.') != -1 and x.find('Software') != -1:
					flag = True
					continue
				elif coord_list.next_element.next_element.name == 'a' and cont > 4 and flag:
					names = names + 'Prof(a). ' + coord_list.next_element.next_element.next_element + ' ' + coord_list.next_element.next_element.next_element.next_element
					names+='\n'
				elif cont > 4 and flag and coord_list.next_element != '\xa0':
					names+= coord_list.next_element
					names+='\n'
		return names

	def energy_coordinator(self):
		names = ''
		flag = True
		for coord_td in self.coordinators:
			lista = coord_td.find_all('td')
			cont = int(0)
			for coord_list in lista:
				x = coord_list.next_element
				if x.find('span') != -1:
					cont += 1
					continue
				elif x.find('Eng.') != -1 and x.find('Energia') == -1:
					flag = False
					continue
				elif x.find('Eng.') != -1 and x.find('Energia') != -1:
					flag = True
					continue
				elif coord_list.next_element.next_element.name == 'a' and cont > 4 and flag:
					names = names + 'Prof(a). ' + coord_list.next_element.next_element.next_element + ' ' + coord_list.next_element.next_element.next_element.next_element
					names += '\n'
				elif cont > 4 and flag and coord_list.next_element != '\xa0':
					names += coord_list.next_element
					names += '\n'
		return names

	def aeroespace_coordinator(self):
		names = ''
		flag = True
		for coord_td in self.coordinators:
			lista = coord_td.find_all('td')
			cont = int(0)
			for coord_list in lista:
				x = coord_list.next_element
				if x.find('span') != -1:
					cont += 1
					continue
				elif x.find('Eng.') != -1 and x.find('Aeroespacial') == -1:
					flag = False
					continue
				elif x.find('Eng.') != -1 and x.find('Aeroespacial') != -1:
					flag = True
					continue
				elif coord_list.next_element.next_element.name == 'a' and cont > 4 and flag:
					names = names + 'Prof(a). ' + coord_list.next_element.next_element.next_element + ' ' + coord_list.next_element.next_element.next_element.next_element
					names += '\n'
				elif cont > 4 and flag and coord_list.next_element != '\xa0':
					names += coord_list.next_element
					names += '\n'
		return names

	def automotive_coordinator(self):
		names = ''
		flag = True
		for coord_td in self.coordinators:
			lista = coord_td.find_all('td')
			cont = int(0)
			for coord_list in lista:
				x = coord_list.next_element
				if x.find('span') != -1:
					cont += 1
					continue
				elif x.find('Eng.') != -1 and x.find('Automotiva') == -1:
					flag = False
					continue
				elif x.find('Eng.') != -1 and x.find('Automotiva') != -1:
					flag = True
					continue
				elif coord_list.next_element.next_element.name == 'a' and cont > 4 and flag:
					names = names + 'Prof(a). ' + coord_list.next_element.next_element.next_element + ' ' + coord_list.next_element.next_element.next_element.next_element
					names += '\n'
				elif cont > 4 and flag and coord_list.next_element != '\xa0':
					names += coord_list.next_element
					names += '\n'
		return names

	def eletronics_coordinator(self):
		names = ''
		flag = True
		for coord_td in self.coordinators:
			lista = coord_td.find_all('td')
			cont = int(0)
			for coord_list in lista:
				x = coord_list.next_element
				if x.find('span') != -1:
					cont += 1
					continue
				elif x.find('Eng.') != -1 and x.find('Eletrônica') == -1:
					flag = False
					continue
				elif x.find('Eng.') != -1 and x.find('Eletrônica') != -1:
					flag = True
					continue
				elif coord_list.next_element.next_element.name == 'a' and cont > 4 and flag:
					names = names + 'Prof(a). ' + coord_list.next_element.next_element.next_element + ' ' + coord_list.next_element.next_element.next_element.next_element
					names += '\n'
				elif cont > 4 and flag and coord_list.next_element != '\xa0':
					names += coord_list.next_element
					names += '\n'
		return names