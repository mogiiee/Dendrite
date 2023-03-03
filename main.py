from flask import Flask
from flask_graphql import GraphQLView
import graphene
from pymongo import MongoClient

# Connect to MongoDB Atlas using the connection string
client="mongodb://amogh:amogh@ac-ztxn30c-shard-00-00.esico7b.mongodb.net:27017,ac-ztxn30c-shard-00-01.esico7b.mongodb.net:27017,ac-ztxn30c-shard-00-02.esico7b.mongodb.net:27017/?ssl=true&replicaSet=atlas-i1fgx7-shard-0&authSource=admin&retryWrites=true&w=majority"

db = client['dendrite']
collection = db['to-do']



app = Flask(__name__)

class Task(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()

class Query(graphene.ObjectType):
    tasks = graphene.List(Task)

    def resolve_tasks(self, info):
        # Fetch tasks from the "tasks" collection in the MongoDB database
        tasks = []
        for task in client.db.tasks.find():
            tasks.append(Task(id=str(task["_id"]), title=task["title"], description=task.get("description")))
        return tasks

class CreateTask(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()

    task = graphene.Field(lambda: Task)

    # def mutate(self, info, title, description=None):
    #     # Create a new task in the "tasks" collection in the MongoDB database
    #     result = client.db.tasks.insert_one({"title": title, "description": description})
    #     task = Task(id=str(result.inserted_id), title=title, description=description)
    #     return CreateTask(task=task)

class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
app.run()
