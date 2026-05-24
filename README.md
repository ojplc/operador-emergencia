# Operador de emergência

O domínio utilizado é o de um operador de serviços de emergência, o qual deve despachar corretamente o serviço de emergência necessário (bombeiro, polícia e/ou ambulância), desligar caso não seja uma emergência e encaminhar para um humano caso seja uma emergência médica.

## Como rodar
1. Coloque a sua chave de API do Gemini no .env (o modelo utilizado é o gemini-3.5-flash (gratuito))

2. Instale as dependências necessárias usando:

```pip install -r requirements.txt```

3. Rode o arquivo agent.py no terminal

Ao receber " ----- LIGAÇÃO NÃO ERA EMERGÊNCIA ----- " ou " ------ TRANSFERIDO PARA HUMANO ------ " ou " ----- LIGAÇÃO CONCLUIDA COM SUCESSO ----- " ou quando estiver com "User: " no terminal aperte ENTER para encerrar a execução


### feito por João Pedro Lopes da Cruz