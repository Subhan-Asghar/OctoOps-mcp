import os 
from github import Github, Auth
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

mcp=FastMCP("OctoOps")
load_dotenv()
# Github Authorization 
def git_auth():
    
    access_token = os.getenv("GITHUB_TOKEN")
    if not access_token:
        raise EnvironmentError("Missing GITHUB_TOKEN in environment variables.")
    
    auth = Auth.Token(access_token)
    return Github(auth=auth)