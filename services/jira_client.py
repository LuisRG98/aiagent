import os
import requests
from dotenv import load_dotenv

load_dotenv()

JIRA_URL = os.getenv("JIRA_BASE_URL")
AUTH = (os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")

def create_jira_task(task: dict):
    issue_data = {
        "fields": {
            "project": {"key": PROJECT_KEY},
            "summary": task["descripcion"],
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": task["descripcion"]
                            }
                        ]
                    }
                ]
            },
            "issuetype": {"name": "Task"}
        }
    }

    response = requests.post(
        f"{JIRA_URL}/rest/api/3/issue",
        json=issue_data,
        auth=AUTH,
        headers={"Accept": "application/json", "Content-Type": "application/json"}
    )
    
    if response.status_code == 201:
        return response.json().get("key")
    else:
        return f"Error: {response.status_code} - {response.text}"
