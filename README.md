# Operador de emergência

Atividade realizada no processo trainee da computer society IEEE UnB do grupo de estudos de inteligência artificial

## Domínio
O domínio utilizado é o de um operador de serviços de emergência, o qual deve despachar corretamente o serviço de emergência necessário (bombeiro, polícia e/ou ambulância), desligar caso não seja uma emergência e encaminhar para um humano caso seja uma emergência médica.

## Como rodar
1. Coloque a sua chave de API do Gemini no .env (o modelo utilizado é o gemini-3.5-flash (gratuito))

2. Instale as dependências necessárias usando:

```pip install -r requirements.txt```

3. Rode o arquivo agent.py no terminal

Ao receber: <br> " ----- LIGAÇÃO NÃO ERA EMERGÊNCIA ----- " <br> " ------ TRANSFERIDO PARA HUMANO ------ " <br> " ----- LIGAÇÃO CONCLUIDA COM SUCESSO ----- " <br>ou quando estiver com "User: " no terminal aperte ENTER para encerrar a execução


### Reflexão
Leia o arquivo [Reflexao.md](Reflexao.md) para ler o processo de contrução e as decisões tomadas na escrita do [system_prompt](system_prompt.txt)

### feito por João Pedro Lopes da Cruz