from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from langchain.tools import BaseTool
import json
import os
from typing import List
import pandas as pd


def busca_dados_de_estudante(estudante):
    dados = pd.read_csv("documentos/estudantes.csv")
    dados_com_esse_estudante = dados[dados["USUARIO"] == estudante]
    if dados_com_esse_estudante.empty:
        return {}
    return dados_com_esse_estudante.iloc[:1].to_dict()

class ExtratorDeEstudante(BaseModel):
    estudante:str = Field("Nome do estudante informado, sempre em letras minúsculas.")

class DadosDeEstudante(BaseTool):
    name = "DadosDeEstudante"
    description = """Esta ferramenta extrai o histórico e preferências de um estudante de acordo com seu histórico.
Passe para essa ferramenta como argumento o nome do estudante."""

    def _run(self, input: str) -> str:
        llm = ChatOpenAI(model="gpt-4o",
                         api_key=os.getenv("OPENAI_API_KEY"))
        parser = JsonOutputParser(pydantic_object=ExtratorDeEstudante)
        template = PromptTemplate(template="""Você deve analisar a entrada a seguir e extrair o nome informado em minúsculo.
Entrada:
-----------------
{input}
-----------------
                        Formato de saída:
                        {formato_saida}""",
                        input_variables=["input"],
                        partial_variables={"formato_saida" : parser.get_format_instructions()})
        cadeia = template | llm | parser
        resposta = cadeia.invoke({"input" : input})
        estudante = resposta['estudante']
        # estudante = input
        estudante = estudante.lower().strip()
        dados = busca_dados_de_estudante(estudante)
        return json.dumps(dados)


class Nota(BaseModel):
    area:str = Field("Nome da área de conhecimento")
    nota:float = Field("Nota na área de conhecimento")
    
class PerfilAcademicoDeEstudante(BaseModel):
    nome:str = Field("nome do estudante")
    ano_de_conclusao:int = Field("ano de conclusão")
    notas:List[Nota] = Field("Lista de notas das disciplinas e áreas de conhecimento")
    resumo:str = Field("Resumo das principais características desse estudante de forma a torná-lo único e um ótimo potencial estudante para faculdades. Exemplo: só este estudante tem bla bla bla")
        
class PerfilAcademico(BaseTool):
    name = "PerfilAcademico"
    description = """Cria um perfil acadêmico de um estudante.
Esta ferramenta requer como entrada todos os dados do estudante.
Eu sou incapaz de buscar os dados do estudante.
Você tem que buscar os dados do estudante antes de me invocar."""

    def _run(self, input:str) -> str:
        llm = ChatOpenAI(model="gpt-4o",
                         api_key=os.getenv("OPENAI_API_KEY"))
        parser = JsonOutputParser(pydantic_object=PerfilAcademicoDeEstudante)
        template = PromptTemplate(template = """- Formate o estudante para seu perfil acadêmico.
- Com os dados, identifique as opções de universidades sugeridas e cursos compatíveis com o interesse do aluno
- Destaque o perfil do aluno dando enfase principalmente naquilo que faz sentido para as instituições de interesse do aluno

Persona: você é uma consultora de carreira e precisa indicar com detalhes, riqueza, mas direta ao ponto para o estudante as opções e consequências possíveis.
Informações atuais:

{dados_do_estudante}
{formato_de_saida}
""",
            input_variables=["dados_do_estudante"],
            partial_variables={"formato_de_saida" : parser.get_format_instructions()})
        cadeia = template | llm | parser
        resposta = cadeia.invoke({"dados_do_estudante" : input})
        return resposta
        