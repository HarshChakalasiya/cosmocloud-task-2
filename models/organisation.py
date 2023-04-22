class ChatModel(Model):
    message_id: str = Field(default=None, alias="_id", primary_field=True)
    room_id: str = Field(default=None, alias="roomId", key_name="roomId")
    sender_id: str = Field(default=None, alias="senderId", key_name="senderId")
    receiver_id: str = Field(default=None, alias="receiverId", key_name="receiverId")
    message_type: Optional[MessageType] = Field(default=None, alias="messageType", key_name="messageType")
    message: Optional[str] = Field(default=None)
    status: Optional[ChatMessageStatus] = Field(default=None)
    attachment: Optional[Any] = Field(default=None)
    message_time: str = Field(default=None, alias="msgTime", key_name="msgTime")

class RoomModel(Model):
    room_id: str = Field(default=None,alias="_id", primary_field=True )
    room_name: Any = Field(default=None, alias="roomName", key_name="roomName")
    staff_member: Optional[UUID] = Field(default=None, alias="staffMember", key_name="staffMember")
    staff_member_status: Optional[UserStatus] = Field(default=None, alias="staffMemberStatus", key_name="staffMemberStatus")
    client: Optional[UUID] = Field(default=None, alias="client", key_name="client")
    client_status: Optional[UserStatus] = Field(default=None, alias="clientStatus", key_name="clientStatus")
    # messages: Optional[List[MessageModel]] = []
    last_pinged: str = Field(default=None, alias="lastPinged", key_name="lastPinged")
    active: bool = False
    roomClosed: bool = False
    room_created: str = Field(default=None, alias="roomCreated", key_name="roomCreated")