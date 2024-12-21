import google.generativeai as genai

#generate the conversation and print it
def generateConversation(person_A, person_B, topic):
    genai.configure(api_key="AIzaSyBSbWQAVWyXYZmM3yJhfVjAxBXsFxu533E")
    model = genai.GenerativeModel("gemini-1.5-flash")

    

    response = model.generate_content((
        "write me a funny conversation between", person_A, "and", person_B,
        "about the topic of", topic,
        "that has a resolution and a plot. the resolution should be 1 side wins if it is an arguement, the morally rightious one should win. Also i dont want any cheesiness, make the conversation how real conversations go. No compromises, and when it starts with violence, it ends with violence. do not add anything else, just the conversation. Do not change the names given in the conversation. Make the conversation alternate talking. the action should never have its own line in before both people have spoken. before line 3, it has to come at the end of the sentence. i want physical stuff! however, do not let action make the conversation seem robotic. There should NOT be action every line, or even every 2 lines. Make the action smooth and not random or robotic. the conversation should be in the format 'speaker: words' and new line every time somebody speaks. The action should not seem wierd, such as if i bite an apple and speak normally next line, that is bad."
    ))

    return response

#GUI
#does not work
