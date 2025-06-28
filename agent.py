from agents import Agent, OpenAIChatCompletionsModel,set_tracing_disabled,Runner
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
set_tracing_disabled(True)
 

#Reference: https://ai.google.dev/gemini-api/docs/openai
provider = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,)



  # math agent 
math_agent = Agent(
    name="math_assistant",
    instructions="You are a math assisstant. to solve math proplems.",
    model=model,
    handoff_description="handoff to math_assistant if the question related to math or calculation."
)

#english agent
english_agent = Agent(
    name ="english_assistant",
    instructions ="""you are a english assistant. to solve english related proplem like grammer ,write a paragraph ,translation,
     application,email etc related to english query.""",
     model=model,
     handoff_description="hand_off all english related quries to english_assistant.")

computer_agent =Agent(
    name="computer_assistant",
    instructions ="you are a computer assistant you can solve all computer related query like programming, coding, debugging etc",
    model= model,
    handoff_description ="handoff all the proplem related to computer or programming to computer assistant"
)

async def myAgent(user_input):
    manager_agent =Agent(
        name = "manager_agent",
        instructions = """You are a manager agent. You can manage all the agents and route the query to the appropriate agent.
        If the query is related to math, route it to math_assistant.
        If the query is related to english, route it to english_assistant.
        if the query is related to computer or programming, route it to computer_assistant.
        If the query is not related to any of these, respond with 'I am not sure how to help with that.'""",
        model=model,
        handoffs=[math_agent, english_agent, computer_agent],)
    

    response = await Runner.run(
        manager_agent,
        input= user_input,

    )    
    return response.final_output