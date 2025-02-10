import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy import create_engine
from fastapi import FastAPI

# Conexão com o banco de dados SQL Server no test01
engine = create_engine("mssql+pyodbc://localhost/test01?driver=ODBC+Driver+17+for+SQL+Server")

# Carregar dados da tabela TEST02
df = pd.read_sql("SELECT column1 AS pergunta, column2 AS resposta FROM TEST02", con=engine)

# Criar a matriz TF-IDF com base nas perguntas
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['pergunta'])

# Função para buscar a resposta mais similar
def buscar_resposta(pergunta_usuario):
    pergunta_tfidf = vectorizer.transform([pergunta_usuario])
    similaridades = cosine_similarity(pergunta_tfidf, tfidf_matrix)
    indice_mais_similar = similaridades.argmax()
    return df.iloc[indice_mais_similar]['resposta']

# Teste local da função
pergunta = "Onde eu entro na empresa?"
resposta = buscar_resposta(pergunta)
print(resposta)

# Criar API com FastAPI
app = FastAPI()

@app.get("/responder/")
def responder(pergunta: str):
    resposta = buscar_resposta(pergunta)
    return {"pergunta": pergunta, "resposta": resposta}
