from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough,RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables=['topic']
)

model = ChatOpenAI()
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template = "explain the followin joke {text}",
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel(
    {
     'joke': RunnablePassthrough(),
     'explaination':RunnableSequence(prompt2,model,parser)
    }
)

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)
print(final_chain.invoke({'topic':'cricket'}))