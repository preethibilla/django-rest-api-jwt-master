from rest_framework.response import Response
from rest_framework.views import status


# def validate_request_data(fn):
#     def decorated(*args, **kwargs):
#         # args[0] == GenericView Object
#         title = args[0].request.data.get("title", "")
#         artist = args[0].request.data.get("artist", "")
#         if not title and not artist:
#             return Response(
#                 data={
#                     "message": "Both title and artist are required to add a song"
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         return fn(*args, **kwargs)

#     return decorated

def validate_request_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        name = args[0].request.data.get("name", "")
        description = args[0].request.data.get("description", "")
        quantity = args[0].request.data.get("quantity", "")
        price = args[0].request.data.get("price", "")
        if not name or not description or not quantity or not price:
            return Response(
                data={
                    "message": "Name, description, quantity, and price are required to add an inventory item"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)

    return decorated
