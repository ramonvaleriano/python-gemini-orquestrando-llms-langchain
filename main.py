from src.services.lang_chain import LangChainService


path_image = "src/data/exemplo_grafico.jpg"
question = "Descreva a imagem: "

if __name__ == "__main__":
    lang_chain_service = LangChainService()
    response = lang_chain_service.run(path_image=path_image, question=question)


    print(response.content)