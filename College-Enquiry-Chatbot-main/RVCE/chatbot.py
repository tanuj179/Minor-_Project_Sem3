from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
nlp = spacy.load('en_core_web_sm')

# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('<b>RVCE BOT</b>')

# nlp = spacy.load("en_core_web_sm")

chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to RVCE! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'   
) 
trainer = ListTrainer(chatbot)

# python app.py
# Training with Personal Ques & Ans 
conversation = [

"Hi",
"Helloo!",
"Hey",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br></br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>.</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",
"course",
"Course",
"Aerospace Engineering", 

"List out pg course",
"List of pg Course.</br><br>Master Of Computer Applications 👉 <a href='https://rvce.edu.in/mca'>Click Here</a> <br>Digital Communication <br>Machine Design <br>Powwer Electronics<br>Computer Network Engineering<br>To know More About PG Course 👉 <a href='https://rvce.edu.in/rvce-pg-programs-offered'> Click Here</a></br>",


"List out ug course",
"List of ug Course.</br><br>Aerospace Engineering 👉 <a href='https://rvce.edu.in//as-mainpage'>Click Here</a> <br>Artificial Intelligence & Machine Learning 👉 <a href='https://rvce.edu.in//aiml-mainpage'>Click Here</a><br>Biotechnology 👉 <a href='https://rvce.edu.in//bt-menu'> Click Here</a></br>",

"Placement",
"Placemnets Details.</br><br>Visit here for Placement Stats👉 <a href='https://rvce.edu.in/placement-statistics'> Click Here</a> </br>",

"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information about RVCE college.",

"What else can you do?",
"I can help you know more about RVCE",
    
   "1",
    "<b >STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below :<pre>1.1 Cultural <br>1.2  Infrastucure<br>1.3  Adminssion<br>1.4 Examination <br>1.5 Placements </b>",
    
    "1.1",
    "<b> CURRICULAR <br> These are the top results: <br> <br> 1.1.1 Extra & Co Curricular </b>",
    "1.1.1",
    "<b> 1.1.1 Extra & Co Curricular<br>The link to  Extra & Co Curricular👉 <a href='https://www.rvce.edu.in/extra-curricular'>Click Here</a> </b>",

    
    "1.2",
    "<b>Infrastucure<br>These are the top results: <br>  1.2.1 Campus IT Infrastucure<br> 1.2.2 Infrastucure Library ,IT,Sports,etc <br> 1.2.3 Caampus Safety Records</b>",
    "1.2.1",
    "<b > 1.2.1 Campus IT Infrastucure<br>The link to 👉 Campus IT Infrastucure <a href='http://rvce.edu.in/Campus-IT-Infrastructure'> Click Here</a></b>",
    "1.2.2",
    "<b > 1.2.2  Infrastucure Library ,IT,Sports,etc<br>The link  Infrastucure Library ,IT,Sports,etc👉<a href='http://rvce.edu.in/rvce-Infrastructures-Library-IT-Sports-etc'> Click Here</a> </b>",
    "1.2.3",
    "<b > 1.2.3 Caampus Safety Records <br>The link to Caampus Safety Records👉 <a href='http://rvce.edu.in/campus-safety-records'> Click Here</a> </b>",

]

trainer.train(conversation)
