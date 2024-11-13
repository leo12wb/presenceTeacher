from database.database import get_db_connection
from models.activitiesPresencesTeacher import ActivitiesPresencesTeacher
Table = ActivitiesPresencesTeacher

def create(table: Table):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO activitiesPresencesTeacher (description, status) VALUES (%s, %s, %s)",
        (table.presencesTeacherId, table.activitiespresencesTeacherId, table.status)
    )

    table_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return Table(id=table_id, **table.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM activitiesPresencesTeacher")
    res = cursor.fetchall()
    cursor.close()
    connection.close()
    return res

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM activitiesPresencesTeacher WHERE id = %s", (id,))
    res = cursor.fetchone()
    cursor.close()
    connection.close()
    return res if res else None

def update(id: int, table: Table):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE activitiesPresencesTeacher SET presencesTeacherId = %s, activitiespresencesTeacherId = %s, status = %s WHERE id = %s",
        (table.presencesTeacherId, table.activitiespresencesTeacherId, table.status, id)
    )

    connection.commit()
    cursor.close()
    connection.close()
    return Table(id=id, **table.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM activitiesPresencesTeacher WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
