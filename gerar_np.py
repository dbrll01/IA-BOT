# Criando novas perguntas e respostas padronizadas com os links corrigidos

novas_perguntas_respostas_corrigidas = {
    "Pergunta": [],
    "Resposta": []
}

# Padrões de perguntas e respostas corrigidos
padroes_corrigidos = [
    {
        "pergunta": "Devo fazer o curso de NR {nr}?",
        "resposta": "Verifique no portal interno de treinamentos se o curso de NR {nr} é necessário para sua função: https://enk.webtraining.com.br/siga/siga_app/templates/padrao/aluno/desktop/desktop.asp"
    },
    {
        "pergunta": "Onde encontro o curso de NR {nr}?",
        "resposta": "O curso de NR {nr} está disponível no portal interno de treinamentos: https://enk.webtraining.com.br/siga/siga_app/templates/padrao/aluno/desktop/desktop.asp"
    },
    {
        "pergunta": "Qual o link para o curso de NR {nr}?",
        "resposta": "Consulte o portal interno de treinamentos para acessar o curso de NR {nr}: https://enk.webtraining.com.br/siga/siga_app/templates/padrao/aluno/desktop/desktop.asp"
    },
    {
        "pergunta": "O curso de NR {nr} é obrigatório?",
        "resposta": "A obrigatoriedade do curso de NR {nr} depende do seu cargo. Verifique se o seu nome se encontra na lista de treinamentos e verifique com o setor de segurança do trabalho."
    },
    {
        "pergunta": "O curso de NR {nr} tem reciclagem?",
        "resposta": "Caso o curso de NR {nr} exija reciclagem, essa informação estará disponível no portal interno de treinamentos: https://enk.webtraining.com.br/siga/siga_app/templates/padrao/aluno/desktop/desktop.asp"
    },
]

# Gerando perguntas e respostas para NR 01 a NR 36
for nr in range(1, 37):
    for padrao in padroes_corrigidos:
        novas_perguntas_respostas_corrigidas["Pergunta"].append(padrao["pergunta"].format(nr=nr))
        novas_perguntas_respostas_corrigidas["Resposta"].append(padrao["resposta"].format(nr=nr))

# Criando DataFrame
df_novas_perguntas_corrigidas = pd.DataFrame(novas_perguntas_respostas_corrigidas)

# Salvando o arquivo CSV corrigido
csv_filename_novas_perguntas_corrigidas = "/mnt/data/novas_perguntas_respostas_nrs_corrigidas.csv"
df_novas_perguntas_corrigidas.to_csv(csv_filename_novas_perguntas_corrigidas, index=False, encoding="utf-8")

# Exibindo o link para download
csv_filename_novas_perguntas_corrigidas
