import google.generativeai as genai

#generate the conversation and print it
def getEmoji(name):
    genai.configure(api_key="API KEY")
    model = genai.GenerativeModel("gemini-1.5-flash")

    

    response = model.generate_content((
        'I want a whimsical emoji to symbolize the person', name, 'please give me the emoji and no other text around it. do not say stuff like "here is the emoji [emoji]" i just want the emoji. just give me "[emoji]"'
    ))

    return response
