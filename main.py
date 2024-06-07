from langchain.tools import BaseTool
import json
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain import hub
from langchain.agents import Tool
import os
import pandas as pd
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def busca_dados_de_estudante(estudante):
    dados = pd.read_csv("documentos/estudantes.csv")
    dados_com_esse_estudante = dados[dados["USUARIO"] == estudante]
    if dados_com_esse_estudante.empty:
        return {}
    return dados_com_esse_estudante.iloc[:1].to_dict()

class ExtratorDeEstudante(BaseModel):
    estudante:str = Field("Nome do estudante informado, sempre em letras minúsculas. Exemplo: joão, carlos, joana, carla.")

class DadosDeEstudante(BaseTool):
    name = "DadosDeEstudante"
    description = """Esta ferramenta extrai o histórico e preferências de um estudante de acordo com seu histórico."""

    def _run(self, input: str) -> str:
        llm = ChatOpenAI(model="gpt-4o",
                         api_key=os.getenv("OPENAI_API_KEY"))
        parser = JsonOutputParser(pydantic_object=ExtratorDeEstudante)
        template = PromptTemplate(template="""Você deve analisar a {input} e extrair o nome de usuário informado.
                        Formato de saída:
                        {formato_saida}""",
                        input_variables=["input"],
                        partial_variables={"formato_saida" : parser.get_format_instructions()})
        cadeia = template | llm | parser
        resposta = cadeia.invoke({"input" : input})
        estudante = resposta['estudante']
        dados = busca_dados_de_estudante(estudante)
        return json.dumps(dados)
        
        
        

pergunta = "Quais os dados de Bianca?"

llm = ChatOpenAI(model="gpt-4o",
                         api_key=os.getenv("OPENAI_API_KEY"))

dados_de_estudante = DadosDeEstudante()
tools = [
    Tool(name = dados_de_estudante.name,
         func = dados_de_estudante.run,
         description = dados_de_estudante.description)
]

prompt = hub.pull("hwchase17/openai-functions-agent")
agente = create_openai_tools_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agente,
                        tools=tools,
                        verbose=True)
resposta = executor.invoke({"input" : pergunta})
print(resposta)


#resposta = DadosDeEstudante().run(pergunta)
#print(resposta)