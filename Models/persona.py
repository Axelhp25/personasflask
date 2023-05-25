class modelPersona():
    @classmethod
    def create(self, db,nombre,apellido):
        try:
            cursor = db.cursor()
            query = "INSERT INTO personas(nombres,apellidos) VALUES('{}','{}')".format(nombre,apellido)
            cursor.execute(query)
            db.commit()
            return 'registro insertado!'
        except Exception as ex:
            raise Exception(ex)
        
    def personas(db):
        try:
                cursor = db.cursor()
                cursor.execute("select id,nombres,apellidos from personas")
                return cursor
        except Exception as ex:
            raise Exception(ex)