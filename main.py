from langchain.agents import AgentExecutor
from agente import AgenteOpenAIFunctions
from dotenv import load_dotenv

load_dotenv()

pergunta = "Quais os dados de Ana?"
pergunta = "Quais os dados de Bianca?"
pergunta = "Quais os dados de Ana e da Bianca?"
pergunta = "Crie um perfil acadêmico para a Ana!"
pergunta = "Compare o perfil acadêmico da Ana com o da Bianca!"
pergunta = "Tenho sentido Ana desanimada com cursos de matemática. Seria uma boa parear ela com a Bianca?"
pergunta = "Tenho sentido Ana desanimada com cursos de matemática. Seria uma boa parear ela com o Marcos?"

agente = AgenteOpenAIFunctions()
executor = AgentExecutor(agent=agente.agente,
                        tools=agente.tools,
                        verbose=True)
resposta = executor.invoke({"input" : pergunta})
print(resposta)
