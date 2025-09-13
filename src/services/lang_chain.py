from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.callbacks import Callbacks
from langchain_core.caches import BaseCache

from core.settings import MODEL_1_3_FLASH, GEMINI_API_KEY
from src.helpers.my_helper import encode_image

ChatGoogleGenerativeAI.model_rebuild()

print(f"Model: {MODEL_1_3_FLASH}, Chave: {GEMINI_API_KEY}")

class LangChainService:
    def __init__(self):
        self.__model = MODEL_1_3_FLASH
        self.__gemini_apy_key = GEMINI_API_KEY
        self.llm = ChatGoogleGenerativeAI(
            api_key=self.__gemini_apy_key, model=self.__model
        )

    def run(self, path_image=None, question=None):
        image = encode_image(path_image)
        message = HumanMessage(
            content=[
                {"type": "text", "text": question},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image}"},
            ]
        )

        response = self.llm.invoke([message])

        return response