from flask import Flask
import json
import graphene
import os 
class information(graphene.ObjectType):
    Title = graphene.String()
    Description = graphene.String()
    Time = graphene.Time()
    Images = graphene.String()


data = [
    {
        "name": "amogh",
        "age": "23"
    },
    {
        "name": "ashish",
        "age": "244"
    }
]

class Query(graphene.ObjectType):

    array = graphene.List(information)
    def resolve_array(root,info):
        return data



schema = graphene.Schema(query=Query)

print(schema)







# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True, use_reloader=True)