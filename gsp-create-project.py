import json
import uuid
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)


def lambda_handler(event, context):
    # LUCAS COMMENT HERE
    print(event)
    logging.info("event ", event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from local Lambda! test22 update')
    }


# This function is responsible for validation of the request payload while creating Project.
def validate_project_details(project_details):
    print("In validate_project_details")
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


# This function is responsible for creating the Project.
def create_project(project_details, login_username):
    print("In create_project ")
    try:
        if not validate_project_details(project_details):
            raise Exception("Project Validation failed.")
        project_details['id'] = str(uuid.uuid4())
        project_details['created'] = datetime.now()
        project_details['updated'] = datetime.now()
        project_details['creator'] = login_username
        return project_details
    except Exception as e:
        print("Exception while creating ProjectModule." + str(e))
    return project_details
