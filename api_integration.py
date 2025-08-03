import google.generativeai as genai

def init_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash")

def build_prompt(context,question):
    return f"""
    You are an AI assistant for a technology company called *IdeaNestTech*.

    The company offers full-stack development, AI chatbots, digital marketing, startup incubation, and an online academy with certified training programs.

    Respond clearly, professionally, and helpfully using the context below.

    -----
    Context:
    {context}
    -----

    User Question:
    {question}

    Helpful Answer:
    """

def ask_gemini(model, prompt):
    response = model.generate_content(prompt)
    return response.text.strip()


