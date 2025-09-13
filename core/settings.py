import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", None)
MODEL_GEMMA_3N_E2B_IT = os.getenv("MODEL_GEMMA_3N_E2B_IT", None)
MODEL_LEARNLM_2_0_FLASH_EXPERIMENTAL = os.getenv(
    "MODEL_LEARNLM_2_0_FLASH_EXPERIMENTAL", None
)
MODEL_1_3_FLASH = os.getenv("MODEL_1_3_FLASH", None)

MARITACA_SABIA = os.getenv("MARITACA_SABIA", None)
MARITACA_API_KEY = os.getenv("MARITACA_API_KEY", None)
