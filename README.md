# Trabalho-sobre-plantas.
Atividade final de POO com temática de classificação de plantas. 

Este trabalho se baseia em um sistema simples de classificação de plantas, feito em python e seguindo conceitos básicos de POO.

A classificação é inspirada na linha evolutiva das plantas, resumida em: Briófitas, Pteridófitas, Gimnospermas e Angiospermas. Essas classificações representam os grupos propriamente ditos, cada uma contendo uma lista de plantas já cadastradas. A classe Plantas serve como base para todas as outras, guardando as informações comuns como nome popular e nome científico. A partir dela, as plantas são especializadas em outras classes de acordo com a presença ou ausência de vasos condutores, sementes e frutos.

O arquivo main.py interage com o usuário por meio de um menu no terminal, que permite identificar plantas usando perguntas de sim ou não sobre características como ser vascular, ter sementes e frutos. Com as respostas, o sistema classifica automaticamente essa planta. Outra função do menu principal permite ver características das plantas cadastradas, onde o usuário escolhe uma classificação e uma planta, e o sistema exibe informações como vasos condutores, sementes e frutos, obtidas pela estrutura de herança das classes.

Como executar: Ter o Python 3 instalado, baixar todos os arquivos e rodar o arquivo main.py. Quando carregar, irá aparecer um menu com 3 opções: 

<img width="396" height="132" alt="image" src="https://github.com/user-attachments/assets/58d8224b-a1e9-425b-858a-f50709080377" />

O usuário então digita um input, em que:
1 - Identifica uma planta
2 - Ver características de plantas
0 - Sair

Ao selecionar a primeira opção (1), o usuário é questionado sobre as características da planta que deseja identificar, devendo responder com "s" para sim e "n" para não.

<img width="402" height="277" alt="image" src="https://github.com/user-attachments/assets/f50167fc-6907-48bc-a831-a7093a594318" />

Se o usuário selecionar a segunda opção (2), as classificações evolutivas de uma planta aparecerão: Briófitas, Pteridófitas, Gimnospermas e Angiospermas, cada uma numerada para que o usuário possa escolher.

<img width="324" height="362" alt="image" src="https://github.com/user-attachments/assets/ea4aa6a5-1370-47bc-8d77-60de9f810381" />

Conforme mostrado na imagem acima, o usuário seleciona opções usando dígitos, recebendo uma resposta final dependendo dessas escolhas.

Retornando às opções iniciais do menu, se o usuário escolher a terceira opção (0), o programa simplesmente exibirá uma mensagem "encerrando...", fechando o sistema.

<img width="397" height="133" alt="image" src="https://github.com/user-attachments/assets/ea1f51cf-9f10-4dae-b6bc-eddd582ee3a7" />

 
