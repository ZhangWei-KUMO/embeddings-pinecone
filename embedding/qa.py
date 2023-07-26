from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from settings import llm

embeddings = OpenAIEmbeddings()
index_name = "gpt-test-pdf"
vectorstore = Pinecone.from_existing_index(index_name, embeddings,namespace='qingang')

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

res = qa("秦刚为什么不当部长")
print(res)
