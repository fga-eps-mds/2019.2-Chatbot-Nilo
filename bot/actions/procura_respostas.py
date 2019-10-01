def procura_resposta_por_topico(topico):
	with open('actions/FAQ_Estagio.txt','r') as file:
		resposta = []
		topico_atual = 0
		for line in file:
			if line[1] == '.':
				topico_atual = int(line[0])
				continue
			elif line[2] == '.':
				topico_atual = int(line[1])*10 + int(line[0])
				continue
			if topico_atual == topico:
				resposta.append(line)
			elif topico_atual > topico:
				break
	return resposta
