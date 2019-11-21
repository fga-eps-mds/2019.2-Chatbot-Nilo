# Como subir um ChatBot na Digital Ocean para o Telegram
Neste tutorial vamos subir um ChatBot criado com base no boilerplate ou no próprio Nilo para o telegram através de uma droplet na DigitalOcean.
Para isto vamos criar um domínio, criar uma droplet, acessá-la usando ssh, configurar o nginx para o domínio, gerar um certificado através do Certbot e subir o bot.

## Criando um Domínio
Existem vários sites que vendem e oferecem domínios, para o Nilo, foi usado o site freenom.com que oferece alguns domínios gratuitos.

## Criando uma Droplet

### Criando a chave ssh

Para acessarmos a nossa droplet pelo terminal, primeiro temos que criar uma chave ssh. SSH é um protocolo para acessar máquinas remotas com segurança através do seu terminal.

Para gerá-la digite o seguinte comando no terminal:

    $ ssh-keygen

Ao digitar o comando, o terminal vai perguntar pelo diretório e o arquivo onde será guardada a chave:

```
Generating public/private rsa key pair.
Enter file in which to save the key (/algum/diretório/.ssh/id_rsa):
```

Você pode digitar aonde você deseja que o arquivo seja salvo, ou apertar Enter pra salvar no caminho padrão.

Ele vai pedir então por uma palavra-passe, pode deixar em branco também:

    Enter passphrase (empty for no passphrase): 

Após isso, sua chave ssh foi criada com sucesso.

### Adicionando a chave pública ao DigitalOcean

O processo que acabamos de realizar vai gerar dois arquivos, uma chave privada que vai ficar na sua máquina e a chave pública, que é salva com a extensão `.pub`.

Vamos adicionar o conteúdo dessa chave a nossa conta para podermos adicionar nas nossas droplets.

Ao fazer login na conta, na barra lateral clique em _Security_.

![](https://i.imgur.com/NJ6iXve.png)

Vá na seção _SSH Keys_, e clique em _Add SSH Key_.

Um modal vai aparecer, com um campo para inserir a chave. Insira o conteúdo do arquivo `.pub` aqui.

![](https://i.imgur.com/L6xtD33.png)

Logo abaixo, existe um campo para adicionar o nome da chave, o nome pode ser qualquer coisa.

![](https://i.imgur.com/Vsk2kiv.png)

Clique em _Add SSH Key_ e pronto!


### Criando a Droplet

As droplets são as nossas máquinas virtuais na Digital Ocean. Existem várias configurações de droplet com preços variados, para o Nilo, foi usada uma de 15$, a Digital Ocean normalmente disponibiliza 50$, para novos usuários utilizarem no primeiro mês.

Na barra superior, clique no botão _Create_ e _Droplets_ no menu que abrir.

![](https://i.imgur.com/n4FgAST.png)

Ao criar a droplet, pode-se criar uma máquina apenas com o SO e instalar tudo diretamente, ou podem ser utilizados os _One-click apps_, que são máquinas pré-configuradas com algumas dependências que nosso projeto possa ter. Para o Nilo, foi usada uma droplet com o Docker já instalado.

![](https://i.imgur.com/EmcIHy1.png)

Abaixo da escolha de sistema operacional, há a escolha do tipo de hardware da Droplet, no caso do Nilo, foi usada uma de $15 com 3GB de RAM, mas você pode escolher qualquer uma que seja do seu interesse.

![](https://imgur.com/hh16FOo.png)

As próximas opções podem ser deixadas como padrão.

Para escolher a região, escolha a que estiver mais próxima de você.

![](https://i.imgur.com/y40SBnI.png)


Agora, é adicionada a chave SSH.

![](https://i.imgur.com/ahQnXc3.png)

Agora escolha o nome da droplet e clique em criar!

![](https://imgur.com/T3qYYpu.png)

Com a droplet criada, vamos apontar o domínio para ela.

### Apontando um domínio para a nossa droplet

Supondo que você ja tenha criado um domínio, chegou a hora de configurá-lo na Digital Ocean, para isso, você pode seguir esse tutorial para trocar os NameServers do seu domínio: https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars , repare que para a maioria dos sites de domínios, a configuração é parecida.

Antes de começar a configurar a sua máquina, você deve apontar seu domínio para ela. Na página inicial do projeto, haverá uma lista com os domínios, selecione o que deseja e você vai entrar na tela de _Records_.

![](https://i.imgur.com/sjTTTiT.png)

Em _hostname_ você deverá colocar o seu subdomínio, por exemplo: "qualquercoisa.seudominio.com"

* Para usar o domínio raíz digite '@'
* Para usar um wildcard, e direcionar qualquer subdomínio para um IP específico coloque '\*'


Em _Will Direct To_ você deverá colocar o IP para qual deseja que seja direcionado, nesse caso é o IP da sua droplet.

TTL (Time to Live) é o tempo que o record ficará guardado em cache para o usuário. Carregar dados do cache é rápido, logo, maiores valores de TTL geram uma experiência de usuário mais rápida, mas enquanto o cache local do visitante não expirar ele não verá mudanças realizadas no DNS.

Nosso record ficará assim então (lembrando que o IP da sua droplet será diferente do mostrado aqui):

![](https://imgur.com/ZQExXrw.png)

Crie o record e siga para o próximo passo!

### Configurando a máquina

Para entrar na droplet utilizando a chave SSH que você criou, abra um terminal e entre utilizando o comando

    $ ssh <usuário>@<IP da máquina>

O usuário por padrão é o root.

Na primeira vez que conectar, você será perguntado se tem certeza que deseja se conectar, basta digitar 'yes'.

Após isso, será apresentado uma mensagem de boas-vindas e o input do terminal vai mudar mostrando o usuário e o nome da droplet.

## Configurando o Nginx para o seu Domínio

### Instalando o Nginx

Para instalar o nginx utilize os seguintes comandos
```
$ sudo apt update
$ sudo apt install nginx
```

### Ajustando o FireWall

Antes de configurar o Nginx, é preciso liberá-lo na para o firewall, para ver a lista de serviços disponíveis para o firewall digite 

    $ sudo ufw app list 

Você deve receber uma lista de aplicações para o firewall parecida com esta: 

```
Available applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH
```
Como por enquanto estamos configurando só o trafégo HTTP, para liberar essa aplicação, é necessário utilizar o comando:

    $ sudo ufw allow 'Nginx HTTP' 

Você pode verificar sua mudança usando o comando:

    $ sudo ufw status

E você deve ver o tráfego http na saída, a saída deve-se parecer com isso:

```
Output
Status: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere                  
Nginx HTTP                 ALLOW       Anywhere                  
OpenSSH (v6)               ALLOW       Anywhere (v6)             
Nginx HTTP (v6)            ALLOW       Anywhere (v6)
```

### Checando o Status do seu Servidor

Neste ponto, o seu servidor nginx deve estar rodando, para conferir isso digite: 

     $ sudo systemctl status nginx

Se sua saída for similar a essa:

```
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2018-04-20 16:08:19 UTC; 3 days ago
     Docs: man:nginx(8)
 Main PID: 2369 (nginx)
    Tasks: 2 (limit: 1153)
   CGroup: /system.slice/nginx.service
           ├─2369 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
           └─2380 nginx: worker process
```
Então seu servidor estará rodando corretamente.


### Gerenciando as opções do nginx
Para parar seu servidor web, digite:

    $ sudo systemctl stop nginx

Para iniciar seu servidor web, digite:

    $ sudo systemctl start nginx

Para reinicar seu servidor web,:

    $ sudo systemctl restart nginx

Se você estiver simplesmente mexer nas configurações, você pode fazer reload do seu nginx para que não precise parar ele para atualizar as configurações:

    $ sudo systemctl reload nginx

Por padrão, o Nginx é configurado para iniciar quando o servidor é ligado. Se não é isso que você quer, você pode digitar:

    $ sudo systemctl disable nginx

Para retornar a configuração anterior de iniciar o Nginx quando o servidor for ligado, digite:

    $ sudo systemctl enable nginx

### Configurando o nginx para o domínio

Para configurar o nginx para o seu domínio, você tem que ter alguma página html para o nginx se referir. Para criar uma página html referente ao seu domínio execute os seguintes comandos em ordem:

Obs.: Onde está escrito [DOMINIO] você deverá por o link principal do seu domínio.

1 - Crie uma pasta para seu domínio, usando a flag -p para criar qualquer outra pasta necessária:

    $ sudo mkdir -p /var/www/[DOMINIO]/html

2 - Depois, atribua a propriedade do pasta para o usuário atual:

    $ sudo chown -R $USER:$USER /var/www/[DOMINIO]/html

3  - Depois, crie uma página  `index.html` para referenciar a página inicial do seu domínio:

    $ nano /var/www/[DOMINIO]/html/index.html

4 - Pode escrever qualquer código html para deixar como padrão na sua página inicial, caso não ache necessário, pode deixar em branco e salvar (Ctrl+X depos Y e depois ENTER para salvar no nano).

5 - Agora você deve criar uma configuração para o seu site nas configurações do nginx, para isso digite:

    $ sudo nano /etc/nginx/sites-available/[DOMINIO]

6 - Escreva o seguinte código no arquivo:

```
server {
        listen 80;
        listen [::]:80;

        root /var/www/[DOMINIO]/html;
        index index.html index.htm index.nginx-debian.html;

        server_name [DOMINIO] www.[DOMINIO];

        location / {
                try_files $uri $uri/ =404;
        }
}
```

7 - Crie uma versão espelhada deste arquivo na pasta /etc/nginx/sites-enabled:

    $ sudo ln -s /etc/nginx/sites-available/[DOMINIO] /etc/nginx/sites-enabled/

8 - Para evitar um possível problema de memória abra o arquivo nginx.conf:

    $ sudo nano /etc/nginx/nginx.conf

E descomente a linha escrita `server_names_hash_bucket_size` retirando o #:

```
...
http {
    ...
    server_names_hash_bucket_size 64;
    ...
}
...
```

Você terminou sua configuração agora veja se não há nenhum erro de sintaxe nos arquivos do nginx:

    $ sudo nginx -t

Se estiver tudo certo, pode reiniciar o nginx com as novas configurações:

    $ sudo systemctl restart nginx

Pronto, agora o nginx está configurado para o seu domínio, agora vamos gerar um certificado SSL para ele usando a ferramenta Certbot.

## Gerando um Certificado SSL para o seu domínio

### Instalando o Certbot

Primeiro, adicione o repositório:

    $ sudo add-apt-repository ppa:certbot/certbot

Você vai precisar apertar ENTER para aceitar, Depois, atualize a lista de pacotes:

    $ sudo apt update

E instale o pacote nginx do certbot:

    $ sudo apt install python-certbot-nginx

### Permitindo HTTPS através do firewall

Antes, você tinha permitindo o trafego HTTP do servidor nginx, agora você precisará de ambos então execute:

    $ sudo ufw allow 'Nginx Full'

E, retire a permissão agora redundante do tráfego HTTP:

    $ sudo ufw delete allow 'Nginx HTTP'

### Gerando o Certificado

Para gerar o certificado SSL basta executar o seguinte comando:

    $ sudo certbot --nginx -d [DOMINIO] -d www.[DOMINIO]

Se tudo der certo, o ` certbot ` perguntará como você deseja definir sua configuração:

```
Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
-------------------------------------------------------------------------------
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
-------------------------------------------------------------------------------
Select the appropriate number [1-2] then [enter] (press 'c' to cancel):
```

Escolha a configuração que você desejar e aperte ENTER, após isso o `certbot` vai terminar o processo dizendo se a criptografia foi bem sucedida e mostrando o lugar onde os dados da criptografia foram armazenados:
```
IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/[DOMINIO]/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/[DOMINIO]/privkey.pem
   Your cert will expire on 2018-07-23. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
 - Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le
```

Após isso seus certificados devem estar prontos, para testá-los tente acessar seu domínio por https://[DOMINIO] e veja se o cadeado funciona corretamente.

Nota: Para verificar a auto-renovação do certificado digite o comando:

    $ sudo certbot renew --dry-run

## Subindo o ChatBot para o Telegram

### Criando um WebHook no seu domínio

Antes de mexermos na configuração do ChatBot precisamos criar um WebHook nas configurações do seu domínio no nginx. Para isso abra o arquivo na pasta do nginx referente ao seu domínio:

    $ sudo nano /etc/nginx/sites-available/[DOMINIO]

E depois da configuração `location /` adicione uma configuração `location /webhooks/telegram/webhook` :

```
server {
    ...
    location / {
        try_files $uri $uri/ =404;
    }

    location /webhooks/telegram/webhook {
        proxy_pass http://[IP]:5001/webhooks/telegram/webhook;
    }
    ...
}
```
Nota: Troque o [IP] pelo IP público da sua droplet.

### Configurando o bot

Caso não tenha clonado o repositório do bot que você quer upar na sua droplet digite:

    $ git clone [SEU_REPOSITORIO]

Entre na pasta do seu repositório:

    $ cd [SEU_PROJETO]

Abra o arquivo de ambiente do telegram:

    $ nano docker/bot-telegram.env

Modifique o arquivo de acordo com as informações do seu bot e do seu domínio:

```
TELEGRAM_BOT_USERNAME=[SEU_BOT]
TELEGRAM_TOKEN=[TOKEN_DO_SEU_BOT]
TELEGRAM_WEBHOOK=https://[DOMINIO]/webhooks/telegram/webhook
```

Após isso só resta subir o bot para o telegram!

### Subindo o Bot

Se ainda não tiver treinado o seu ChatBot digite:

    $ sudo make train

Caso a droplet não reconhecer o comando make rode:

    $ sudo apt install make

Após treinar seu bot suba ele para o telegram:

    $ sudo docker-compose up -d --build bot_telegram

Após isso use o comando:
    $ sudo docker-compose logs -f bot_telegram

Para ter verificar se seu bot está rodando, esse comando não deve mostrar nenhum erro e a última linha deve se parecer com:

    INFO    root - Rasa Core server is up and running on http://localhost:5001

Agora, só resta testar ele no telegram, tente iniciar uma conversa com ele, se ele responder normalmente então ele está funcionando corretamente!

## Tutoriais utilizados:

- Subindo uma instância do Rancher na Digital Ocean: https://gist.github.com/guilhesme23/833b24745f79e21b401feec96fea958a (Só a parte de criar e configurar a Droplet)
- How To Install Nginx on Ubuntu 18.04: https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04
- Como Proteger o Nginx com o Let's Encrypt no Ubuntu 18.04: https://www.digitalocean.com/community/tutorials/como-proteger-o-nginx-com-o-let-s-encrypt-no-ubuntu-18-04-pt
- Configuring Nginx to Proxy Webhooks: https://ansonvandoren.com/posts/configuring-nginx-to-proxy-webhooks/

### Observação:

As versões finais dos arquivos de configuração do nginx usados para o deploy do Nilo podem ser encontradas no repositório.
