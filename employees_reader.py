import ydb

def blocking_query(session, query):
  return session.transaction().execute(
    query,
    commit_tx = True,
    settings = ydb.BaseRequestSettings().with_timeout(3).with_operation_timeout(2)
  )

class Employees_reader:

    def employees_with_clients(self, session):
      query = '''SELECT empl.id as EMPLid, empl.NAME as name, coalesce(client.NAME, 'Unknown') as client,     
FROM employee2 empl LEFT JOIN client2 client ON empl.id = client.ID_EMPLOYEE;'''
      return blocking_query(session, query)
        
reader = Employees_reader()
