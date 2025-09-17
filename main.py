from src.services.lang_chain import LangChainService


path_image = "src/data/exemplo_grafico.jpg"
question = "Quais canais de Youtube você recomenda para que eu possa saber mais a respeito de smarpthones?"

if __name__ == "__main__":
    lang_chain_service = LangChainService()
    #response = lang_chain_service.run(path_image=path_image, question=question)

    response = lang_chain_service.run_maitaca(question=question)


    print(response.content)