# pyrefly: ignore [missing-import]
from openrouter import OpenRouter
from fastapi import APIRouter

router = APIRouter()

client = OpenRouter(
    api_key="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"
)


@router.get("/chat")
def chat():
    response = client.chat.send(
            model="openai/gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."}
            ],
            stream=False, 
            temperature=0.7,
            max_tokens=650

        )
    print(response)
    return {"chat": response}