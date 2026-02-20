from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv()

def main():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7
    )

    system_msg = SystemMessage("You are a helpful assistant.")
    human_msg = HumanMessage("Hello, how are you?")

    prompt = [system_msg, human_msg]

    response = llm.invoke(prompt)

    print("Prompt:")
    print(prompt)
    print("\nResponse:")
    print(response.content)

if __name__ == "__main__":
    main()
