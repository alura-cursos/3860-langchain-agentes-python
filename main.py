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
pergunta = "Quais os dados da USP?"
pergunta = "Quais os dados da uNiCAmP?"
pergunta = "Quais os dados da uNi CAmP?"
pergunta = "Quais os dados da uNicomP?"
pergunta = "Dentre USP e UFRJ, qual você recomenda para a acadêmica Ana?"
pergunta = "Dentre uni camp e USP, qual você recomenda para a Ana?"
pergunta = "Quais as faculdades com melhores chances para a Ana entrar?"
pergunta = "Dentre todas as faculdades existentes, quais Ana possui mais chance de entrar?"
pergunta = "Além das faculdades favoritas da Ana existem outras faculdades. Considere elas também. Quais Ana possui mais chance de entrar?"

agente = AgenteOpenAIFunctions()
executor = AgentExecutor(agent=agente.agente,
                        tools=agente.tools,
                        verbose=True)
resposta = executor.invoke({"input" : pergunta})
print(resposta)
