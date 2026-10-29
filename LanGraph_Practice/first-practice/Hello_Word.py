from typing import Dict, TypedDict
from langgraph.graph import StateGraph

#Create AgentState class - shared data structure to keep tracking the information as the application runs
class AgentState(TypedDict): #the state schema 
    message: str

#First node - fundemental element in langgraph
def greeting_node(state: AgentState)-> AgentState: #input and output are the state as the state keep changing 
    # docstrings is what will tell the AI agent that what is this function perform - like comment 
    """Simple node adding greeting message to the state """
    state['message'] = "Hi " + state["message"] + ", how is your day is going?"  #updating the state part 

    return state

#build the graph - stategraph
graph = StateGraph(AgentState) #parsing the state schema inside 

#add node to the graph
graph.add_node("greeter", greeting_node)  #parsing the name of the node and the action perform 

#START
graph.set_entry_point("greeter") # the parameter here is the first node to connect to it 
#END
graph.set_finish_point("greeter") # the parameter here is the last node connected to the end point 

#compiling the graph
app = graph.compile()

#visualizing part
#Generate mermaid diagram
mermaid = app.get_graph().draw_mermaid()
print(mermaid)

#save it to a file
with open("workflow.mmd", "w", encoding="utf-8") as f:
    f.write(mermaid)

#run and print the message result 
result = app.invoke({"message": "Bob"})
print(result["message"])
