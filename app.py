import autogen

## 1-set up confguration json for autogen
config_list = [
    {
        'model': "gpt-4",
        'api_key': "openai-key"
    }
]

## 2- set up LLM config object
llm_config={
    # 'request_timeout': 600, # kills the request after certain amount of time if opneain is not responding
    'seed':42,  ## its for cashing, it cashes the respons, so when you run the same task again it's going to
                    # use the cashed version and it will save you money and time
    'config_list':config_list,
    'temperature': 0 # fof coding we don't wnat creativer resposne so keep it at zero

}

# 3- create our first assistant
''' 
 here we created only a single agent
 if you want to create more than one agent you need to define a SYSTEM MESSAGE" to each of them so that
 you'r definning the role that you wants them to take on
 '''
assistant = autogen.AssistantAgent(
    name='assistant',        # name it assistant and pas and then pass in the llm config
    llm_config=llm_config,
    # system_message="chief technincal office of the x company"

)

# 4- create the user proxy
'''
it is an agent that acts on behalf of the user or yourself, it can do things automatically on your behalf
like executing code and responding to the assistant agent or it can ask you at each step for approval to
do those things.

you can have multiple user proxy just like you can have multiple user assistant
defing human input mode: it is wher you defing how much manual input you wnanna to give. check documentation for auto gen
which show we have 3 options, Always, Terminate or never

max_consecutive_auto_reply: set upt the maximum of time that the agent can go back and forth with each other.
if you set it too high, there is a risk that hte agent get into an infinite Loop and continue to go back and forth with
each other which it will be quite costly

termination message: it is looking for a certain keyword that ends the taks. so when it sees terminate, it knows the
task is over and we have human_input_mode='TERMINATE' that's when it's going to ask for input.

code_execution_config: let us to set a couple of setting for when we want executer code.

system design: It is the instruction to tell the user proxy how to determine if the task is being completed, we yuse
the one that autogen came up with.
'''

user_proxy = autogen.UserProxyAgent(
    name='user_proxy',
    # human_input_mode='TERMINATE', # defing human input mode
    human_input_mode='NEVER', # to execute all of this code when I have more than one task
    max_consecutive_auto_reply=10,
    code_execution_config={'work_dir':'web'},
    llm_config=llm_config,
    system_message='Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet'
)

# 5- create a variable to store the task that we want the agent to complete.
# task = '''
# Give me a summary of this article:https://medium.com/data-science-in-your-pocket/react-chain-of-thoughts-and-trees-of-thoughts-explained-with-example-b9ac88621f2c
# '''
task = """
Write python code to output numbers 1 to 100, and then store the code in a file
"""

# 6- we actually need to initiate the chat (user proxy always initiate the chat)

user_proxy.initiate_chat(
    assistant,
    message=task
)
## you can add another task.
task2 = """
Change the code in the file you just created and instead of it make a file to output numbers 1 to 200
"""

## you need to initiate user_porxy again for the second task.
user_proxy.initiate_chat(
    assistant,
    message=task2
)
