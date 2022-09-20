from flask import Response
from flask_restx import Namespace, Resource, fields

namespace = "User"
user_namespace = Namespace(namespace)

user_namespace.model("user_model", {"name": fields.String(readOnly=True, description="User name")})


@user_namespace.route("/user/<int:id>")
class UserById(Resource):
    @user_namespace.doc(response={})
    # @user_namespace.expect(reqeust={})
    def get(self, id: int):
        return [{"name": "ss", "user_id": id}]


@user_namespace.route("/user/<string:name>")
class UserByName(Resource):
    def get(self, name: str):
        return {"GetUserResponse": [{"name": name, "user_id": id}]}

    def post(self, name: str):
        return Response({"result": "new user created", "user": {"name": name}})
