from graphene import (
    Schema,
    String,
    ObjectType
)


class Query(ObjectType):
    greet = String(name=String(default_value='Anonymous'))
    goodbye = String()

    @staticmethod
    def resolve_greet(root, info, name):
        return f"Hey, {name}!"

    @staticmethod
    def resolve_goodbye(root, info):
        return 'See ya!'


schema = Schema(query=Query)

plain_query = """
  {
      greet
  }
"""

result = schema.execute(plain_query)
print('Simple query: ', result.data['greet'])

argument_query = """
  {
    greet (name: "sherlock")
  }
"""

result = schema.execute(argument_query)
print('Query with an argument: ', result.data.get('greet'))
