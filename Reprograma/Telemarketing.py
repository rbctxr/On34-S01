#Você já deve ter ligado em uma empresa e ouvido uma lista de opções com números que deviam ser digitados com a opção escolhida para ser 
#direcionada a um certo departamento. Seu trabalho agora é criar um minissistema de telemarketing.
#O programa vai mostrar na tela as opções e, dependendo do número digitado, a pessoa vai ser direcionada a um outro atendimento. Ao final, 
#ficará assim:
#Olá! Obrigada por ligar para nós Para falar com Financeiro, digite 1. Para falar com Administrativo, digite 2. Para falar com Recursos Humanos,
#digite 3. Para falar com Assistência Técnica, digite 4.
#Dependendo da resposta, o programa vai mostrar na tela uma frase diferente. Por exemplo: Ao responder 1, vai aparecer a frase: Você será 
#direcionada para o Financeiro.
#Após ser direcionada para o departamento, pergunte: se a pessoa quer deixar um recado para o (nome do departamento) ou falar com atendente. 
#caso a pessoa escolha deixar recado, imprima: "Você pode deixar seu recado agora". Caso ela escolha falar com atendente, imprima: "Por favor, 
#aguarde seu atendimento".

opcao = input('Olá! obrigada por ligar para nós. Para falar com o financeiro, digite 1. Para falar com o administrativo, digite 2. Para falar com os recursos humanos, digite 3. Por fim, para falar com a assistência têcnica, digite 4.')

if opcao == 1:
    pergunta = input("Para deixar recado para o departamento, digite 12. Para falar com o atendente, digite 13.")
    if   pergunta == 12:
    print ("Você pode deixar seu recado agoraa :)")
    elif pergunta == 13:
    print ("Por favor, aguarde seu atendimento :)")