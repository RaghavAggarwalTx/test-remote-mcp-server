from fastmcp import FastMCP
import random 
import json 

#create the fastMcp server instance
mcp=FastMCP("Simpele Calculator Server")

#Tool: Add two numbers 
@mcp.tool
def ad(a:int ,b:int)->int:
    """Add two numbers together.
    Args:
    a:First Number.
    b:Second Number.
    Returns : The sum of a and b
    """
    return a+b


#Tool: Generate a random number 
@mcp.tool
def random_(min_val:int =1 ,max_val:int=100)->int:
    """Generate a random number within a range.
    Args:
    min_value:Minimum value (default: 1).
    max_value:Maximum value (default: 100).
    Returns : 
        A random integer between min_value and max_value
    """
    return random.randint(min_val,max_val)


#Resource : Server Information
@mcp.resource("info://server")
def server_info()->str:
    """Get information about server . """
    info={
        "name":"Simpele Calculator Server",
        "version":"1.0.0",
        "description":"A basic MCP server with math tools ",
        "tools":["add","random_number"],
        "author":"Raghav"
    }
    return json.dumps(info,indent=2)

#Start the server 
if __name__=='main':
    mcp.run(transport="http",host="0.0.0.0",port=8000)


