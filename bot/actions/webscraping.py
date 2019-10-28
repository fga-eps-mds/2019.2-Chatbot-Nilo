import requests
from bs4 import BeautifulSoup

class WebScrapingIntegration:
	def __init__(self):
		self.url = 'https://fga.unb.br/coordenacao'
		self.request = requests.get(self.url)
		self.soup = BeautifulSoup(self.request.text, 'html.parser')
		self.coordinators = self.soup.find_all('div', class_='article-body article-body-text-article')

	def software_coordinator(self):
		names = ''
		find_coordinator = True
		for coord_td in self.coordinators:
			list_tds = coord_td.find_all('td')
			span_counter = int(0)
			for coord_list in list_tds:
				html_next_element = coord_list.next_element
				if html_next_element.find('span') != -1:
					span_counter+=1
					continue
				elif html_next_element.find('Eng.') != -1 and html_next_element.find('Software') == -1:
					find_coordinator = False
					continue
				elif html_next_element.find('Eng.') != -1 and html_next_element.find('Software') != -1:
					find_coordinator = True
					continue
				elif coord_list.next_element.next_element.name == 'a' and span_counter > 4 and find_coordinator:
					names = names + 'Prof(a). ' + coord_list.next_element.next_element.next_element + ' ' + coord_list.next_element.next_element.next_element.next_element
					names+='\n'
				elif span_counter > 4 and find_coordinator and coord_list.next_element != '\xa0':
					names+= coord_list.next_element
					names+='\n'
		return names

	def energy_coordinator(self):
		names = ''
		find_coordinator = True
		for coord_td in self.coordinators:
			list_tds = coord_td.find_all('td')
			span_counter = int(0)
			for coord_list in list_tds:
				html_next_element = coord_list.next_element
				if html_next_element.find('span') != -1:
					span_counter += 1
					continue
				elif html_next_element.find('Eng.') != -1 and html_next_element.find('Energia') == -1:
					find_coordinator = False
					continue
				elif html_next_element.find('Eng.') != -1 and html_next_element.find('Energia') != -1:
					find_coordinator = True
					continue
				elif coord_list.next_element.next_element.name == 'a' and span_counter > 4 and find_coordinator:
					names = names + 'Prof(a). ' + coord_list.next_element.next_element.next_element + ' ' + coord_list.next_element.next_element.next_element.next_element
					names += '\n'
				elif span_counter > 4 and find_coordinator and coord_list.next_element != '\xa0':
					names += coord_list.next_element
					names += '\n'
		return names

	def aeroespace_coordinator(self):
		names = ''
		find_coordinator = True
		for coord_td in self.coordinators:
			list_tds = coord_td.find_all('td')
			span_counter = int(0)
			for coord_list in list_tds:
				html_next_element = coord_list.next_element
				if html_next_element.find('span') != -1:
					span_counter += 1
					continue
				elif html_next_element.find('Eng.') != -1 and html_next_element.find('Aeroespacial') == -1:
					find_coordinator = False
					continue
				elif html_next_element.find('Eng.') != -1 and html_next_element.find('Aeroespacial') != -1:
					find_coordinator = True
					continue
				elif coord_list.next_element.next_element.name == 'a' and span_counter > 4 and find_coordinator:
					names = names + 'Prof(a). ' + coord_list.next_element.next_element.next_element + ' ' + coord_list.next_element.next_element.next_element.next_element
					names += '\n'
				elif span_counter > 4 and find_coordinator and coord_list.next_element != '\xa0':
					names += coord_list.next_element
					names += '\n'
		return names

	def automotive_coordinator(self):
		names = ''
		find_coordinator = True
		for coord_td in self.coordinators:
			list_tds = coord_td.find_all('td')
			span_counter = int(0)
			for coord_list in list_tds:
				html_next_element = coord_list.next_element
				if html_next_element.find('span') != -1:
					span_counter += 1
					continue
				elif html_next_element.find('Eng.') != -1 and html_next_element.find('Automotiva') == -1:
					find_coordinator = False
					continue
				elif html_next_element.find('Eng.') != -1 and html_next_element.find('Automotiva') != -1:
					find_coordinator = True
					continue
				elif coord_list.next_element.next_element.name == 'a' and span_counter > 4 and find_coordinator:
					names = names + 'Prof(a). ' + coord_list.next_element.next_element.next_element + ' ' + coord_list.next_element.next_element.next_element.next_element
					names += '\n'
				elif span_counter > 4 and find_coordinator and coord_list.next_element != '\xa0':
					names += coord_list.next_element
					names += '\n'
		return names

	def eletronics_coordinator(self):
		names = ''
		find_coordinator = True
		for coord_td in self.coordinators:
			list_tds = coord_td.find_all('td')
			span_counter = int(0)
			for coord_list in list_tds:
				html_next_element = coord_list.next_element
				if html_next_element.find('span') != -1:
					span_counter += 1
					continue
				elif html_next_element.find('Eng.') != -1 and html_next_element.find('Eletrônica') == -1:
					find_coordinator = False
					continue
				elif html_next_element.find('Eng.') != -1 and html_next_element.find('Eletrônica') != -1:
					find_coordinator = True
					continue
				elif coord_list.next_element.next_element.name == 'a' and span_counter > 4 and find_coordinator:
					names = names + 'Prof(a). ' + coord_list.next_element.next_element.next_element + ' ' + coord_list.next_element.next_element.next_element.next_element
					names += '\n'
				elif span_counter > 4 and find_coordinator and coord_list.next_element != '\xa0':
					names += coord_list.next_element
					names += '\n'
		return names