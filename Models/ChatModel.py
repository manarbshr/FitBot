from langchain_google_genai import ChatGoogleGenerativeAI


class ChatModel:
    def __init__(self, retreriver, prompt, model="gemini-1.5-flash"):
        self.chat_model = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )

        self.chain = self._get_chain(retreriver, prompt)

    def _get_chain(self, retreriver, prompt):
        
        chain = {"context": retreriver} | prompt | self.chat_model

        return chain