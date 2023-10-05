import openai
import gradio

open.api_key = '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'

messages = [{"role": "system", "content": "You are a financial expert that specialize in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")
