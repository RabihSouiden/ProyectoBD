import psycopg2


def conectar_db():
    conn = psycopg2.connect("dbname=CD4P user=postgres password=123456")
    return conn 

def consultar(usuario):
    connection = conectar_db()
    cursor = connection.cursor()
    postgreSQL_select_Query = """select * from public."MASCOTA" WHERE usuario_dueño ='"""+usuario+"""'"""

    cursor.execute(postgreSQL_select_Query)
    print(postgreSQL_select_Query)
    
    records = cursor.fetchall()
    return records

def consultar_mascotas():
    connection = conectar_db()
    cursor = connection.cursor()
    postgreSQL_select_Query = """select * from public."MASCOTA" """

    cursor.execute(postgreSQL_select_Query)
    print(postgreSQL_select_Query)
    
    records = cursor.fetchall()
    return records

def insertar_mascota(nombre, especie, potencialmenre_peligroso, microchip, edad, tamano, sexo, usuario):
    connection = conectar_db()
    cursor = connection.cursor()
    if potencialmenre_peligroso[0] == 'No':
        potencialmenre_peligroso = False
    else:
        potencialmenre_peligroso = True
    postgreSQL_select_Query = """INSERT INTO public."MASCOTA"(
	 nombre, especie, potencialmente_peligroso, fotografia_medica, microchip, edad, tamano, sexo, usuario_dueño)
	VALUES ('"""+str(nombre)+ """', '"""+str(especie)+ """', """+str(potencialmenre_peligroso)+ """, ' ', '"""+str(microchip[0])+ """ ', '"""+str(edad)+ """', '"""+str(tamano)+ """', '"""+str(sexo[0])+ """', '"""+str(usuario)+ """') """
    print(postgreSQL_select_Query)
    cursor.execute(postgreSQL_select_Query)
    connection.commit()

    cursor.close()
    connection.close()

def consultar_publicaciones():
    connection = conectar_db()
    cursor = connection.cursor()
    postgreSQL_select_Query = """select * from public."PUBLICACION" """

    cursor.execute(postgreSQL_select_Query)
    print(postgreSQL_select_Query)
    
    records = cursor.fetchall()
    return records

def nueva_publicacion(usuario, id_mascota, descripcion, titulo, img):
    connection = conectar_db()
    cursor = connection.cursor()
    img = str(img)
    img = img.replace("'", '"')
    postgreSQL_select_Query = """ INSERT INTO public."PUBLICACION"(
	usuario, mascota, descripcion, likes, titulo, imagen)
	VALUES ( '"""+str(usuario)+"""', '"""+str(id_mascota)+ """', '"""+str(descripcion)+ """',0 , '"""+str(titulo)+"""', ' """+str(img)+""" '); """
    cursor.execute(postgreSQL_select_Query)
    connection.commit()

    cursor.close()
    connection.close()

def consultar_eventos():
    connection = conectar_db()
    cursor = connection.cursor()
    postgreSQL_select_Query = """select * from public."EVENTO" """

    cursor.execute(postgreSQL_select_Query)
    print(postgreSQL_select_Query)
    
    records = cursor.fetchall()
    return records

def insertar_evento(tipo_evento, descripcion, mascotas):
    connection = conectar_db()
    cursor = connection.cursor()
    postgreSQL_select_Query = """ INSERT INTO public."EVENTO"(
	id_tipo_evento, desc_evento, fecha, archivo, mascota)
	VALUES ( """+tipo_evento+""", '"""+descripcion+"""', current_date, ' ' , '"""+mascotas+ """'); """
    print(postgreSQL_select_Query)
    cursor.execute(postgreSQL_select_Query)
    connection.commit()

    cursor.close()
    connection.close()