import os
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from settings import index
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

vectorstore = Pinecone(
    index, embed.embed_query, "秦刚是谁", "events"
)
llm = ChatOpenAI(
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    model_name='gpt-3.5-turbo',
    temperature=0.1
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)
# xq = openai.Embedding.create(input="秦刚是谁", 
#                              engine="text-embedding-ada-002")['data'][0]['embedding']
# print(xq)
# res = index.query(vector=xq, top_k=1, include_metadata=True,namespace="events")
# for match in res['matches']:
#     print(f"{match['score']:.2f}: {match['metadata']['text']}")