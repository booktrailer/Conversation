import streamlit as st
from conversation import *
from get_emoji import * 

#heade
st.header('Conversation Builder')
st.text('Create conversations between your favorite characters and celebrities. Fights, arguements discussions, its all possible. Your imagination is the limit!')

#colums
col1, col2, col3 = st.columns(3)

# inputs
person_A = col1.text_input("Person A", "Monkey D. Luffy")
person_B = col2.text_input("Person B", "Roronoa Zoro")
topic = col3.text_input("Topic", "bananas vs apples")

#space
st.text(' ')

# Generate button
generate_button = st.button("Build Conversation", type='primary')

#space
st.text(' ')

# conversation
conversation = st.empty()

if generate_button:
    try:
        #need for creating the chat thing
        storage = (person_A, person_B, topic)

        conver_str = generateConversation(person_A, person_B, topic)

        #do the json fixer
        conversation_text = conver_str.candidates[0].content.parts[0].text

        response_lines = conversation_text.split('\n')
        lines = [line.strip() for line in response_lines if line.strip()]

        #get emojis
        a_emoji = getEmoji(storage[0])
        b_emoji = getEmoji(storage[1])

        a_emoji = a_emoji.candidates[0].content.parts[0].text
        a_emoji = a_emoji.strip()
        if len(a_emoji) > 2:
            a_emoji = "🙂"

        b_emoji = b_emoji.candidates[0].content.parts[0].text
        b_emoji = b_emoji.strip()
        if len(b_emoji) > 2:
            b_emoji = "🥹"
        
        a_name = lines[0].split(':')[0]
        b_name = lines[1].split(':')[0]

        for line in lines:
            if line.startswith(f"{a_name}:"):
                st.chat_message("user", avatar=a_emoji).markdown(f"**{a_name}:** {line[len(a_name) + 1:].strip()}")
            elif line.startswith(f"{b_name}:"):
                st.chat_message("assistant", avatar=b_emoji).markdown(f"**{b_name}:** {line[len(b_name) + 1:].strip()}")
            else:
                # For any unexpected lines show a system message
                st.chat_message("system").markdown(line)

    except Exception as e:
        st.error(f"An error occurred: {e}")
