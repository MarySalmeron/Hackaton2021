import psycopg2
from typing import Union

class Bd():

  #Base de datos
  hostname = 'dbcontracargos.cluster-cr3eijvzbpoy.us-east-2.rds.amazonaws.com'
  username = 'postgres'
  password = 'holamundo'
  database = 'dbcontracargos'

  def __init__(self, database: str, hostname='localhost', username='postgres', password=''):
    self.hostname=hostname
    self.username=username
    self.password=password
    self.database=database

  def __connect(self) -> psycopg2.connect:
    return psycopg2.connect(f"dbname={self.database} user={self.username} password={self.password} host={self.hostname}")

  def do_query(self, myQuery: str, returnAffectedRows=False) -> Union[tuple, dict]:
    myConnection = self.__connect()
    cur = myConnection.cursor()
    affected_rows = 0
    try:
      affected_rows = cur.execute( myQuery )
    except:
      affected_rows = cur.execute( myQuery.replace("''","'") )	
      
    result=cur.fetchall()
    myConnection.commit()
    myConnection.close()
    if returnAffectedRows == True:
      return {'result':result, 'affected_rows':affected_rows}
    return result