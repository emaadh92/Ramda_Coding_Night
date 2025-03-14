# import streamlit as st
# import random
# import time
# st.title("Quiz App")

# questions = [
#     {
#         "question": "What is the capital of Pakistan?",
#         "options": ["Karachi", "Islamabad", "Lahore", "Quetta"],
#         "answer": "Islamabad"
#     },
#     {
#         "question": "What is the capital of Turkey?",
#         "options": ["Istanbul", "Ankara", "Izmir", "Antalya"],
#         "answer": "Ankara"
#     },
#     {
#         "question": "Who is the founder of Pakistan?",
#         "options": ["Allama Iqbal", "Quaid-e-Azam", "Liaquat Ali Khan", "Sir Syed Ahmed Khan"],
#         "answer": "Quaid-e-Azam"
#     },
#     {
#         "question": "How many provinces are there in Pakistan?",
#         "options": ["3", "4", "5", "6"],
#         "answer": "4"
#     },
#     {
#         "question": "What is the national language of Pakistan?",
#         "options": ["Urdu", "Sindhi", "Punjabi", "Pashto"],
#         "answer": "Urdu"
#     },
#     {
#         "question": "What is the currency of Pakistan?",
#         "options": ["Rupee", "Dollar", "Euro", "Yen"],  
#         "answer": "Rupee"
#     },
#     {
#         "question": "Which city Know as City of Lights?",
#         "options": ["Karachi", "Lahore", "Islamabad", "Quetta"],
#         "answer": "Karachi"
#     }
# ]

# if "current_question" not in st.session_state:
#     st.session_state.current_question = random.choice(questions)

# question = st.session_state.current_question

# st.subheader(question["question"])

# selected_option = st.radio("Choose Cottect answer", question["options"] , key=question["answer"])


# if st.button("Submit Answer"):
#     if selected_option == question["answer"]:
#         st.success("✔️ Correct Answer")
#         st.balloons()
#     else:
#         st.error("❌ Wrong Answer! Correct Answer is: " + question["answer"])
#     time.sleep(3)

#     st.session_state.current_question = random.choice(questions)

#     st.rerun()


testing = bin(194  + 766)
print(testing)