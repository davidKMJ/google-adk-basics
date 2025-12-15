import vertexai
from vertexai import agent_engines

PROJECT_ID = "alpine-dogfish-481015-d3"
LOCATION = "us-central1"

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
)

deployments = agent_engines.list()

for deployment in deployments:
    print(deployment)

# DEPLOYMENT_ID = "projects/339091625388/locations/us-central1/reasoningEngines/8759644211747225600"

# SESSION_ID = "7694728442461290496"

# remote_app = agent_engines.get(DEPLOYMENT_ID)

# remote_app.delete(force=True)

# remote_session = remote_app.create_session(user_id="user")

# print(remote_session["id"])

# for event in remote_app.stream_query(
#     user_id="user",
#     session_id=SESSION_ID,
#     message="I'm going to Laos, any tips?",
# ):
#     print(event, "\n", "=" * 50)