from enum import Enum

class UserRole(str, Enum):
    ADMIN = "ADMIN"
    PORTEIRO = "PORTEIRO"
    SINDICO = "SINDICO"