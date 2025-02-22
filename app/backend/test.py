
from main import on_chat_question
from llm import ask_deepseek


def main():
        chatquestion = " Hola chatbot! "
        answer = on_chat_question(chatquestion)["choices"][0]["message"]["content"]

        print("GEPETO DICE: ")
        print(answer)

if __name__=="__main__":
        main()
