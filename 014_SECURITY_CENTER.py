import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
===============================================================================
ARQUIVO........: 014_SECURITY_CENTER.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: SECURITY CENTER
VERSÃƒÆ'O.........: 1.0.0

===============================================================================

SECURITY CENTER

MISSÃƒÆ'O

Centralizar o gerenciamento de seguranÃƒÂ§a da Plataforma IOTEC.

Responsabilidades

Ã¢â‚¬Â¢ UsuÃƒÂ¡rios
Ã¢â‚¬Â¢ Perfis
Ã¢â‚¬Â¢ PermissÃƒÂµes
Ã¢â‚¬Â¢ SessÃƒÂµes
Ã¢â‚¬Â¢ Auditoria de Login
Ã¢â‚¬Â¢ Controle de Acesso
Ã¢â‚¬Â¢ PolÃƒÂ­ticas de SeguranÃƒÂ§a

===============================================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import logging
import uuid

LOGGER = logging.getLogger("SECURITY_CENTER")


# =============================================================================
# PERFIS
# =============================================================================

class Role(Enum):

    ADMIN = "ADMIN"

    DIRECTOR = "DIRECTOR"

    MANAGER = "MANAGER"

    ANALYST = "ANALYST"

    OPERATOR = "OPERATOR"

    GUEST = "GUEST"


# =============================================================================
# USUÃƒÂRIO
# =============================================================================

@dataclass
class User:

    id: str

    username: str

    full_name: str

    email: str

    role: Role

    active: bool = True

    created_at: datetime = field(default_factory=datetime.now)

    last_login: datetime | None = None


# =============================================================================
# SECURITY CENTER
# =============================================================================

class SecurityCenter:

    def __init__(self):

        self.users = {}

        self.audit = []

        LOGGER.info("Security Center iniciado.")

    # ----------------------------------------------------------------------

    def add_user(

        self,

        username,

        full_name,

        email,

        role

    ):

        user = User(

            id=str(uuid.uuid4()),

            username=username,

            full_name=full_name,

            email=email,

            role=role

        )

        self.users[username] = user

        self.audit.append(

            f"{datetime.now()} - UsuÃƒÂ¡rio criado: {username}"

        )

        LOGGER.info(f"UsuÃƒÂ¡rio registrado -> {username}")

    # ----------------------------------------------------------------------

    def login(self, username):

        if username not in self.users:

            LOGGER.warning("UsuÃƒÂ¡rio inexistente.")

            return False

        user = self.users[username]

        if not user.active:

            LOGGER.warning("UsuÃƒÂ¡rio desativado.")

            return False

        user.last_login = datetime.now()

        self.audit.append(

            f"{datetime.now()} - Login: {username}"

        )

        LOGGER.info(f"Login efetuado -> {username}")

        return True

    # ----------------------------------------------------------------------

    def disable_user(self, username):

        if username in self.users:

            self.users[username].active = False

            self.audit.append(

                f"{datetime.now()} - UsuÃƒÂ¡rio desativado: {username}"

            )

    # ----------------------------------------------------------------------

    def dashboard(self):

        print()

        print("=" * 80)

        print("SECURITY CENTER")

        print("=" * 80)

        print()

        print("UsuÃƒÂ¡rios:", len(self.users))

        print("Eventos de Auditoria:", len(self.audit))

        print()

        print("-" * 80)

        for user in self.users.values():

            print(f"UsuÃƒÂ¡rio.....: {user.username}")

            print(f"Nome........: {user.full_name}")

            print(f"Perfil......: {user.role.value}")

            print(f"Ativo.......: {user.active}")

            print(f"ÃƒÅ¡ltimo Login: {user.last_login}")

            print("-" * 80)

    # ----------------------------------------------------------------------

    def show_audit(self):

        print()

        print("=" * 80)

        print("AUDITORIA")

        print("=" * 80)

        print()

        for item in self.audit:

            print(item)


# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    security = SecurityCenter()

    security.add_user(

        username="admin",

        full_name="Administrador",

        email="admin@iotec.com",

        role=Role.ADMIN

    )

    security.add_user(

        username="diretor",

        full_name="Diretor Executivo",

        email="diretor@iotec.com",

        role=Role.DIRECTOR

    )

    security.login("admin")

    security.login("diretor")

    security.dashboard()

    security.show_audit()



