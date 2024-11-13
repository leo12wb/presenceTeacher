from database.database import get_db_connection
from typing import Union
from models.presencesTeacher import PresencesTeacher
from models.auxPresencesTeacher import AuxPresencesTeacher
Table = Union[PresencesTeacher, AuxPresencesTeacher]

def create(table: Table):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO presencesTeacher (_date, _status, start_hour, end_hour, status) VALUES (%s, %s, %s)",
        (table._date, table._status, table.start_hour, table.end_hour, table.status)
    )

    table_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO auxPresencesTeacher (teacherId, presencesTeacherId, status) VALUES (%s, %s, %s)",
        (table.teacherId, table_id, 1)
    )

    connection.commit()
    cursor.close()
    connection.close()
    return Table(id=table_id, **table.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM presencesTeacher")
    res = cursor.fetchall()
    cursor.close()
    connection.close()
    return res

def readAllTeacherActivities(start: str, end: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT 
            pt.id AS id,
            apt2.presencesTeacherId AS presencesTeacherId,
            apt2.activitiespresencesTeacherId AS activitiespresencesTeacherId,
            apt.teacherId AS teacherId,
            pt._date AS _date,
            pt._status AS _status,
            at.abreviation AS abreviation,
            at._description AS _description
        FROM 
            presencesTeacher pt
        JOIN 
            auxPresencesTeacher apt ON apt.presencesTeacherId = pt.id
        JOIN 
            activitiesPresencesTeacher apt2 ON apt2.presencesTeacherId = pt.id
        JOIN 
            activitiesTeacher at ON apt2.activitiespresencesTeacherId = at.id
        WHERE 
            pt._date BETWEEN '%s' AND '%s'  -- Filtro de intervalo de datas
        ORDER BY 
            pt._date;
    
    """
    cursor.execute(query,(start,end))
    res = cursor.fetchall()
    cursor.close()
    connection.close()
    return res

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM presencesTeacher WHERE id = %s", (id,))
    res = cursor.fetchone()
    cursor.close()
    connection.close()
    return res if res else None

def update(id: int, table: Table):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE presencesTeacher SET _date = %s, _status = %s, start_hour = %s, end_hour = %s, status = %s WHERE id = %s",
        (table._date, table._status, table.start_hour, table.end_hour, table.status, id)
    )

    cursor.execute(
        "UPDATE auxPresencesTeacher SET teacherId = %s WHERE presencesTeacherId = %s",
        (table.teacherId, id)
    )

    connection.commit()
    cursor.close()
    connection.close()
    return Table(id=id, **table.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM presencesTeacher WHERE id = %s", (id,))
    cursor.execute("DELETE FROM auxPresencesTeacher WHERE presencesTeacherId = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
