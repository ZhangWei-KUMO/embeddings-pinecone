import os
import pinecone
from dotenv import load_dotenv
import openai
from langchain.chat_models import ChatOpenAI

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

pinecone.init(
    environment=os.environ.get("PINECONE_ENVIRONMENT"),
    api_key=os.environ.get("PINECONE_API_KEY")
)

index = pinecone.Index('gpt-test-pdf')

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

llm = ChatOpenAI(
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    model_name='gpt-3.5-turbo',
    temperature=0.0
)