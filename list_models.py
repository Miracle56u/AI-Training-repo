from dotenv import load_dotenv
import os

load_dotenv()
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

models = client.models.list()

for m in models.data:
    print(m.id)