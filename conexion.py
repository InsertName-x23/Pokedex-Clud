import mysql.connector
from mysql.connector import error

class DAO():
    
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='pupe',
                password='123456',
               db='Pokedex_Crud'
            )
        except Error as ex:
            print("Error al hacer la conexión: {0}".format(ex))
    
    def listarPokemons(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM Pokemon ORDER BY Numero ASC")
                resultado = cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error al hacer la conexión: {0}".format(ex))


        