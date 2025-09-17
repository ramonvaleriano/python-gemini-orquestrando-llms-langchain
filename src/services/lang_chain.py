from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_models import ChatMaritalk
from langchain_core.messages import HumanMessage
from langchain_core.callbacks import Callbacks
from langchain_core.caches import BaseCache

from core.settings import (
    MODEL_1_3_FLASH,
    GEMINI_API_KEY,
    MARITACA_API_KEY,
    MARITACA_SABIA,
)
from src.helpers.my_helper import encode_image

ChatGoogleGenerativeAI.model_rebuild()
ChatMaritalk.model_rebuild()

class LangChainService:
    def __init__(self):
        self.__model_defaut = MODEL_1_3_FLASH
        self.__gemini_apy_key = GEMINI_API_KEY
        self.__model_maritaca = MARITACA_SABIA
        self.__maritaca_api_key = MARITACA_API_KEY
        self.llm = ChatGoogleGenerativeAI(
            api_key=self.__gemini_apy_key, model=self.__model_defaut
        )

    def run(self, path_image=None, question=None):
        content_values = [
                {"type": "text", "text": question},
            ]

        if path_image:
            image = encode_image(path_image)
            content_values.append({"type": "image_url", "image_url": f"data:image/jpeg;base64,{image}"})

        message = HumanMessage(
            content=content_values
        )

        response = self.llm.invoke([message])

        return response

    def run_maitaca(self, question=None):
        self.llm = ChatMaritalk(
            api_key=self.__maritaca_api_key, model=self.__model_maritaca
        )

        response = self.llm.invoke(question)

        return response


        



        