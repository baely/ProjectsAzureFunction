import json

import azure.functions as func

def main(projectsList: func.HttpRequest, projects: func.DocumentList) -> func.HttpResponse:
    projects = [
        {
            k: v for k, v in project.items() if not k.startswith("_")
        } for project in projects
    ]

    return func.HttpResponse(json.dumps(projects))
