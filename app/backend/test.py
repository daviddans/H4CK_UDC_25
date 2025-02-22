
from main import on_chat_question
from llm import ask_deepseek


def main():
        chatquestion = "Holaaaa"
        print(on_chat_question(chatquestion)["choices"][0]["message"]["content"])

if __name__=="__main__":
        main()
