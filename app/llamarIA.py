import ollama

llm_model = ollama.chat(model='llama3:8b', messages=[
                        {"role": "user", "content": ""}])['model']

def get_llm_response(prompt, model=llm_model):
    response = ollama.chat(model=model, messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ])
    return response['message']['content']