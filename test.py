from retriever import load_assets, retrieve
from api_integration import init_gemini, build_prompt, ask_gemini

def main():
    api_key = "enter_your_api_key_here"

    model = init_gemini(api_key)
    embed_model, index, chunks = load_assets()

    print("\n💬 IdeaNestTech Chatbot is ready. Type your questions below.")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("🧑 You: ")
        if question.lower() in ["exit", "quit"]:
            print("👋 Chatbot closed.")
            break

        context_chunks = retrieve(question, embed_model, index, chunks)
        context = "\n\n".join(context_chunks)
        prompt = build_prompt(context, question)

        print("🤖 Thinking...")
        try:
            answer = ask_gemini(model, prompt)
            print(f"🤖 IdeaNestTech: {answer}\n")
        except Exception as e:
            print("❌ Error from Gemini:", e)

if __name__ == "__main__":
    main()
