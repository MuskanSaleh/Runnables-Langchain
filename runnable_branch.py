
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch,RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda

from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = "Write a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Summarize the foloowing text \n{text}',
    input_variables=['text']
)

model = ChatOpenAI()
parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1,model,parser)
#takes tuple
branch_chain = RunnableBranch(
    (lambda x : len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain,branch_chain)
print(final_chain.invoke({'topic':'Russia vs Ukraine'}))









