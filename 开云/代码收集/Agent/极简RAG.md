# 1 安装Ollama
# 2 创建虚拟环境
# 3 安装包
安装`llama_index`。  
# 4 代码
```
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
```
主要用上的是`SimpleDirectoryReader`和`VectorStoreIndex`，用他们来做文档切片向量化建立索引等操作，构建模型的内部知识库。  
  
`Ollama`和`OllamaEmbedding`根据使用的模型不同，可以修改成不同的Provider。使用本地ollama，就换成前者。`OllamaEmbedding`用作向量化文档时的模型，`Ollama`负责推理的模型。

```
import logging
import os
from llama_index.core import Settings

Settings.chunk_size = 300
Settings.chunk_overlap = 30
```
按chunk_size个toekn来切分内部文档，切分后的片段之间有chunk_overlap个token的重叠。
> 在 LlamaIndex 里，为了方便存储和查找， 一整篇长文本会被拆成很多小段文本。每一小段，就叫一个 chunk（文本块）。这两行代码，只决定“文本以后会被怎么切碎”，不做任何别的事。
  
```
logging.basicConfig(level=logging.ERROR)

print("正在解析文件...")
documents = SimpleDirectoryReader("./docs").load_data()

print("正在创建索引...")
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=OllamaEmbedding(
        model_name="bge-m3:latest",  # 本地 embedding 模型
        base_url="http://localhost:11434"
    )
)

print("正在创建提问引擎...")
query_engine = index.as_query_engine(
    similarity_top_k=3,
    streaming=True,
    llm=Ollama(
        model="gpt-oss:120b-cloud",               # 本地生成模型
        base_url="http://localhost:11434",
        request_timeout=120
    )
)

print("正在生成回复...")
streaming_response = query_engine.query('张伟是谁？')
print("回答是：")
# 采用流式输出
streaming_response.print_response_stream()
```
上述代码可以看作一个模版，修改模型只需要更换`embed_model`和`llm`参数，从LlamaIndex导入新的Provider。
  
为了不重复创建索引，可以保存索引，下次再读取：
```
# 将索引保存为本地文件
index.storage_context.persist("knowledge_base/test")
print("索引文件保存到了knowledge_base/test")
```
该`index`是之前用`VectorStoreIndex.from_documents()`创建的对象。
  
读取的代码：
```
# 将本地索引文件加载为索引
from llama_index.core import StorageContext,load_index_from_storage
storage_context = StorageContext.from_defaults(persist_dir="knowledge_base/test")
index = load_index_from_storage(storage_context,embed_model=OllamaEmbedding(
        model_name="bge-m3:latest",  # 本地 embedding 模型
        base_url="http://localhost:11434"
    ))
print("成功从knowledge_base/test路径加载索引")
```
推理：
```
print("正在创建提问引擎...")
query_engine = index.as_query_engine(
    # 设置为流式输出
    streaming=True,
    llm=Ollama(
    model="deepseek-v3.1:671b-cloud",               # 本地生成模型
    base_url="http://localhost:11434",
    request_timeout=120
    )
)
print("正在生成回复...")
streaming_response = query_engine.query('小明喜欢什么？')
print("回答是：")
streaming_response.print_response_stream()
```
大功告成!
# 5 补充
至于作为例子的文档，可以随便编写一些文本内容，然后再问模型文档相关的问题。
例如：
```
小明.md
---
小明喜欢吃火锅。
小明最喜欢吃雪糕
---
```
问题：小明喜欢什么？  
输出：
```
正在创建提问引擎...
正在生成回复...
回答是：
小明喜欢吃火锅和雪糕。
```
问题：小明讨厌雪糕，最喜欢火锅？  
输出：
```
正在创建提问引擎...
正在生成回复...
回答是：
不对。根据信息，小明喜欢吃火锅，而且他最喜欢吃的是雪糕。
```  
以上用的模型是`deepseek-v3.1:671b-cloud`

# 问题
在做的时候遇到一些易错的地方，要进行推理，首先要有一个`index`，不管是读取保存好的，还是重新创建，首先要有个它，然后`index.as_query_engine()`创建一个`query_engine`，然后就可以用`query_engine`来问问题，'streaming_response = query_engine.query(xxxx)'，然后再`streaming_response.print_response_stream()`  

容易出问题的地方是，得到了`query_engine`，然后更新内置的提示词模版后，写下列代码:
```
print("正在创建提问引擎...")
new_query_engine = index.as_query_engine(
    # 设置为流式输出
    streaming=True,
    # 此处使用qwen-plus模型，你也可以使用阿里云提供的其它qwen的文本生成模型：https://help.aliyun.com/zh/model-studio/getting-started/models#9f8890ce29g5u
    llm=Ollama(
    model="deepseek-v3.1:671b-cloud",               # 本地生成模型
    base_url="http://localhost:11434",
    request_timeout=120
    )
)
```
错在这个地方，`index`是最初的`index`,我已经更新了`query_engine`了，得到了`new_query_engine`，但是后面习惯性的重新`as_query_engine`一下，又变成原来的`engine`，一直出错。其实只需要`query`,再`print_response_stream()`

它是对`query_engine`进行模版更新，这个时候已经存在`query_engine`了，之后就直接`query`。