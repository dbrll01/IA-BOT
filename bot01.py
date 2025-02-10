import os
import pandas as pd
import unicodedata
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Definir o caminho do arquivo CSV
csv_path = r'C:\Users\dbras\Downloads\perguntas_respostas_merged_utf8_no_bom.csv'

# Verificar se o arquivo existe
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"O arquivo CSV não foi encontrado no caminho: {csv_path}")

# Carregar o arquivo CSV
df = pd.read_csv(csv_path, encoding='utf-8')
df.columns = df.columns.str.strip().str.lower()

# Verificar se os nomes das colunas estão corretos
if 'pergunta' not in df.columns or 'resposta' not in df.columns:
    raise KeyError("O arquivo CSV deve conter as colunas 'Pergunta' e 'Resposta'")

# Função para normalizar texto
def normalizar_texto(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    return texto

# Normalização das perguntas
df['pergunta'] = df['pergunta'].apply(normalizar_texto)
df['resposta'] = df['resposta'].str.strip()

# Vetorização do texto
vectorizer = TfidfVectorizer(stop_words=list(ENGLISH_STOP_WORDS), ngram_range=(1, 2))
tfidf_matrix = vectorizer.fit_transform(df['pergunta'])

def buscar_resposta(pergunta_usuario, limiar=0.3):
    """Busca a resposta mais relevante com base na similaridade do cosseno."""
    pergunta_usuario = normalizar_texto(pergunta_usuario)
    pergunta_tfidf = vectorizer.transform([pergunta_usuario])
    similaridades = cosine_similarity(pergunta_tfidf, tfidf_matrix)
    indice_mais_similar = similaridades.argmax()
    
    if similaridades[0, indice_mais_similar] < limiar:
        return "Desculpe, não encontrei uma resposta relevante para sua pergunta."
    
    return df.iloc[indice_mais_similar]['resposta']

# Loop de interação com o usuário
print("Olá, como posso lhe ajudar?")
while True:
    pergunta = input("Você: ")
    if normalizar_texto(pergunta) in ['sair', 'exit', 'quit']:
        print("Até logo!")
        break
    resposta = buscar_resposta(pergunta)
    print("Bot:", resposta)
