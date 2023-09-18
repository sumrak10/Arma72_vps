class ChatWidgetException(Exception):
    pass

class UserNowInOtherRoom(ChatWidgetException):
    pass

class RoomNotFound(ChatWidgetException):
    pass

class OtherManagerConnectedRoom(ChatWidgetException):
    pass