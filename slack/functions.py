from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

load_dotenv(find_dotenv())


def openAICall(user_input, used_id):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    "Proceed with the reply.
    
    
    """

    signature = f"Kind regards"
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "{user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, signature=signature, used_id=used_id)

    return response

def draftEmail(user_input, used_id):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    You are a helpful assistant that drafts an email reply based on an a new email.
    
    Your goal is to create the email for cutomer support team.
    
    Keep your reply short and to the point and mimic the style of the email so you reply in a similar manner to match the tone.
    
    Start your reply by saying: "Hi, here's a draft for your reply:". And then proceed with the reply on a new line.
    
    Make sure to sign of with {signature}.
    
    """

    signature = f"Kind regards, \n <@"+used_id+">" 

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "Here's the email to reply to and consider any other comments from the user for reply as well: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, signature=signature, used_id=used_id)

    return response

def makeJiraTask(user_input, used_id):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
        Subject: [Task] Create Jira task for [specific task]
    **Description:**
    [Provide a brief description of the task you want to create in Jira.]
    **Details:**
    - **Title:** [Provide a title for the Jira task]
    - **Priority:** [Specify the priority of the task (e.g., High, Medium, Low)]
    - **Assignee:** [Indicate the person or team responsible for the task]
    - **Due Date:** [Specify the deadline for completing the task]
    - **Components:** [Specify if any specific components or modules are involved]
    - **Description:**
    [Provide a detailed description of the task, including any relevant information, requirements, or dependencies.]
    **Acceptance Criteria:**
    - [List specific criteria that must be met for the task to be considered completed]
    **Attachments:**
    - [Attach any relevant files, documents, or images, if applicable]
        
        """

    signature = f"Kind regards, \n <@"+used_id+">" 

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "Here's the details of the task and add input from the user for reply as well: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, signature=signature, used_id=used_id)

    return response

def birthdayWish(user_input, used_id):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    Your goal is to create a bithday wish to my office colleague
    
    Keep your reply not more that 150 charectors, and in a similar manner to match the tone.
    
    Start your reply by saying: "Hi, here's a draft for your wish:". And then proceed with the reply on a new line.
    
    Make sure to sign of with [Name] in new line.
        
        """

    signature = f"Kind regards, \n <@"+used_id+">" 

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "Here's the birthday and consider any other comments from the user for reply as well: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, signature=signature, used_id=used_id)

    return response
    
