from src.config.database import DatabaseSession


class ItemOperations:
    def __init__(self):
        self.db = DatabaseSession

    pass

"""
    def crear_usuario(self, nombre: str, email: str):
        with self.db.get_session() as session:
            nuevo_usuario = Usuario(nombre=nombre, email=email)
            session.add(nuevo_usuario)
            return nuevo_usuario

    def obtener_usuarios(self):
        with self.db.get_session() as session:
            return session.query(Usuario).all()

    def buscar_por_email(self, email: str):
        with self.db.get_session() as session:
            return session.query(Usuario).filter(Usuario.email == email).first()

    def actualizar_usuario(self, usuario_id: int, **datos):
        with self.db.get_session() as session:
            usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()
            if usuario:
                for key, value in datos.items():
                    setattr(usuario, key, value)
            return usuario
"""