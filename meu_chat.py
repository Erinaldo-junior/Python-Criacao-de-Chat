# Titulo: Meu chat
# Bolão de iniciar chat
    # Popup (janela na frente da tela)  
    # Titulo: Bem vindo ao meu chat
    # Campo de texto: -> escreva seu nome no chat
    # Entrar no chat
        # Sumir com o titulo 
        # Sumir com botão "Iniciar Chat"
        # Fechar a janela popup     
        # Carregar o chat
            # Carregar as mensagens que já foram enviadas
            # Campo: digite sua mensagem
            # Botão de enviar

# A biblioteca que será usada para construir o site, se chama (flet), essa ferramenta permite criar com o mesmo codigo, sites, aplicativos e programas de computador, ele cria o FrontEnd e o BackEnd juntos.

# importar o flet
import flet as ft

# Criar a função principal do aplicativo
def main(pagina):
    # Criar todas as funcionalidades

    # Cria o elemento
    titulo = ft.Text('Bem vindo ao Chat:') 

    titulo_janela = ft.Text('Bem vindo ao meu chat')
    
    # Aqui estamos criando um campo de texto com um rotulo chamado escreva seu nome no chat, a janela exige que seja passada uma lista de botões.
    campo_nome_usuario = ft.TextField(label='escreva seu nome no chat')
    
    # A janela de popup cahamada chat e uma coluna onde começa vazio, e quando vai adicionando as mensagens, o chat vai adicionando os textos a coluna.
    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem): # Aqui estamos criando o tunel de comunicação, que permite os computadores se comunicarem
        
        texto_chat = ft.Text(mensagem)
        
        #Para adicionar os elementos dentro do chat usamos chat.controls.append()
        chat.controls.append(texto_chat)
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel) # para criar o tunel de comunicação no site usamos a função .pubsub 

    def enviar_mensagem(evento):

        # Para adicionar um elemento a uma coluna criada usamos o .value
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value

        # mensagem vai ser o nome de usuario e a mensagem
        mensagem =  f"{nome_usuario}: {texto_mensagem}"

        pagina.pubsub.send_all(mensagem)

        # para o campo de mensagens limpar automaticamente, depois de ter usado ele, coloca ele como campo vazio.
        campo_mensagem.value = ''

        pagina.update()

    # Com essa função on_submit=, conseguimos enviar a mensagem também apertando enter
    campo_mensagem = ft.TextField(label='digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    
    # para adicionar o botão e o campo de mensagens um do lado do outro usamos a função .Row(), nos usamos ela pra criar uma linha
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])

    def entrar_chat(evento):
        # para remover o titulo e o botão iniciar chat, usamos a função remove()
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f"{campo_nome_usuario.value}: entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    botao_entrar = ft.ElevatedButton('Entrar no Chat', on_click=entrar_chat) 
    janela =  ft.AlertDialog(title= titulo_janela, content=campo_nome_usuario, actions=[botao_entrar]) 

    # Toda interação que um usuario faz com o site e chamado de evento
    def iniciar_chat(evento):

        # O flet chama as janelas de dialog, para abrir a janela usamos a janela.open = True, se quiser fechar (False). Sempre que fizer uma edição na pagina usamos o pagina.update()
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    #Para adicionar uma funcionalidade para o botão, e usado o on_click= 
    botao_iniciar = ft.ElevatedButton('Inciar Chat', on_click= iniciar_chat)
    
    # Adiciona o elemento na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# Rodar o seu aplicativo
# A view= e a forma de visualização do site.

ft.app(main, view= ft.WEB_BROWSER)