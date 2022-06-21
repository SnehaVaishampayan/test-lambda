import json

def lambda_handler(event, context):
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from local Lambda! test22 update')
    }
def validate_project_details(project_details):
    print("In validate_project_details trigger changes", project_details)
    if len(project_details) != 3:
        raise Exception("Project details are missing.")
    for each_data in project_details:
        if each_data.lower() == 'name':
            if len(project_details.get('name')) > 15:
                raise Exception("Project details validation failed. Too long Project Name.")

        if each_data.lower() == 'description':
            if len(project_details.get('description')) > 150:
                raise Exception("Project details validation failed. Too long description.")
    return True
