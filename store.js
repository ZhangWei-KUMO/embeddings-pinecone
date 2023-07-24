import * as dotenv from 'dotenv';
dotenv.config();

import { OpenAIEmbeddings } from 'langchain/embeddings/openai';
import { RecursiveCharacterTextSplitter } from 'langchain/text_splitter';
import { PineconeStore } from 'langchain/vectorstores/pinecone';
import * as fs from 'fs';
const textSplitter = new RecursiveCharacterTextSplitter({ chunkSize: 1500, chunkOverlap: 100});
const embedder = new OpenAIEmbeddings();
import {index} from './settings.js';

(async () => {
    //read article
    const article = await fs.readFileSync('files.txt', { encoding: 'utf-8' });
    const splittedText = await textSplitter.createDocuments([article]);
    PineconeStore.fromDocuments(splittedText, embedder,
        { pineconeIndex: index, 
            namespace: 'namespace1' 
        });
})()