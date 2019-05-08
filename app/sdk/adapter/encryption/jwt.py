import jwt

from sdk.adapter.encryption import EncryptBase


class JwtEncrypt(EncryptBase):

    def __init__(self) -> None:
        self.password = 'e0ae4cMgUJeht0MSFtyllllo'

    def encode(self, data):
        encode = jwt.encode({'data': data}, self.password, algorithm='HS256')
        if isinstance(encode, bytes):
            encode = encode.decode("utf-8")
        if not isinstance(encode, str):
            raise Exception("Error de servidor, jwt no se puede encriptar")
        return encode

    def decode(self, jwt_txt: str):

        return jwt.decode(jwt_txt.encode("utf-8"), self.password, algorithms=['HS256'])
