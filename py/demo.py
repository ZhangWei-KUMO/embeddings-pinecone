from langchain.document_loaders import TextLoader
from langchain.chat_models import ChatOpenAI

loader = TextLoader("./allText.txt")
data = loader.load()
from dotenv import load_dotenv
load_dotenv()

# 分割
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 2500, chunk_overlap = 200)
all_splits = text_splitter.split_documents(data)
# 存储进本地Chroma向量数据库
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
vectorstore = Chroma.from_documents(documents=all_splits,
                                    embedding=OpenAIEmbeddings())
# 向量相似性搜索
# docs = vectorstore.similarity_search(question)
# len(docs)
llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k-0613", temperature=0.1)
from langchain.chains import RetrievalQA
# 检索回答
qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())
# print(qa_chain({"query": "该公司核心业务、市场定位和竞争优势是什么。处于什么地位，商业模式是什么？"}))
#print(qa_chain({"query": "该公司是否有稳定的盈利能力和良好的财务状况？"}))
#print(qa_chain({"query": "该公司是否有稳定的盈利能力和良好的财务状况？"}))
# print(qa_chain({"query": "该公司的市场风险、竞争风险、法律风险是什么？"}))
# print(qa_chain({"query": "介绍下该公司的管理层成员的背景，以及他们是否具备推动公司发展的能力？"}))
#print(qa_chain({"query": "介绍下该公司所在行业的市场前景和增长趋势"}))
#print(qa_chain({"query": "该公司的大股东分别是谁？各自占比是多少"}))
#print(qa_chain({"query": "该公司历年的营收是多少？"}))
# print(qa_chain({"query": "该公司历年的净利润是多少？"}))
# print(qa_chain({"query": "该公司的研发内容有哪些？"}))
#print(qa_chain({"query": "该公司2021年有哪些主要客户，销售金额和占比是多少？"}))
#print(qa_chain({"query": "该公司2021年有哪些供应商，采购标的、采购金额和占比是多少？"}))
# print(qa_chain({"query": "该公司2021年房屋租赁情况如何？"}))
print(qa_chain({"query": "该公司有哪些经营资质？"}))
#print(qa_chain({"query": "那么该公司是否值得投资？"}))


