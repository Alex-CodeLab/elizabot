import json


def registernode(update, context):
    # content = json.loads(update)
    # print(content["message"]["from"]["id"])
    # print(type(update), dir(update))
    print(update.to_dict())
    print(update.effective_user)
    print(update.message)
