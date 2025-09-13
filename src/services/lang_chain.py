from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.callbacks import Callbacks
from langchain_core.caches import BaseCache

from core.settings import MODEL_1_3_FLASH, GEMINI_API_KEY
from src.helpers.my_helper import encode_image

ChatGoogleGenerativeAI.model_rebuild()

def run():
    llm = ChatGoogleGenerativeAI(
        api_key=GEMINI_API_KEY,
        model=MODEL_1_3_FLASH
    )

    path_image = "src/data/exemplo_grafico.jpg"

    image = encode_image(path_image)

    question = "Descreva a imagem: "

    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": question
            },
            {
                "type": "image_url",
                "image_url": f"data:image/jpeg;base64,{image}"
            }
        ]
    )

    response = llm.invoke([message])

    print(response.content)