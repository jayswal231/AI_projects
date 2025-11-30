from openai import OpenAI


client = OpenAI(api_key="key")

def chat():
    print("Chatbot: Namaste! malai sodhnuhos.\n")

    messages = []

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit"]:
            print("Chatbot: feri vetaula!")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        bot_reply = response.choices[0].message.content

        print("Chatbot:", bot_reply)

        messages.append({"role": "assistant", "content": bot_reply})

if __name__ == "__main__":
    chat()
