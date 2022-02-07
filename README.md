# discord-bot
python3  discord bot com sqlite inicie facil com:
```
git clone https://github.com/peccato/discord-bot.git
cd discord-bot
virtualenv discordbot
source discordbot/bin/activate
pip install -r requeriments.txt
```
configure o prefixo e o token do bot no arquivo database.db na tabela config
<br />
e seu bot esta pronto para rodar com o comando:
```
python main.py
```

o bot ja vem com os seguintes comandos:<br/>
. `say`  faz o bot falar oque foi escrito apos o comando.
<br/>
. `ship` comando para diversao , mencionando duas pessoas junto com o comando aparece uma porcentagem aleatoria de afinidade.
<br/>
. `editplay` edita a atividade atual do bot na lista de usuarios.
<br/>
. `lolstat` mostra informacoes de uma conta do lol pelo nome de usuario , raramente funciona pois a api riotwatcher dificilmente encontra o username.
<br/>
. `ping` comando para testar se o bot esta respondendo.
