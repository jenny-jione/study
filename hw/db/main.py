from query_parser import *
from database import *

# 우리 parser의 한계로 create 명령문은 이런식으로만 들어갑니다!
# 컴파일러 개발이 어려운 프로그래밍중 하나인 이유가 이런 이유도 있죠...

query = '''create table members (
                id int,
                name varchar(10),
                age int
            )'''
            
            
query_select_all = '''select * from members'''

query_select_sth = '''
                        select name, age
                        from members
'''
# where 절도 ...
query_select_where = '''
                        select name, age
                        from members
                        where name = 'jenny'
'''

query3 = '''
            insert into members
            values(1,"jenny",29)
            '''

query_insert = '''
                    insert into members
                    values(2,"jimin",29)
'''


db = ourDatabase()
# qp = queryParser(query_insert)
# qp = queryParser(query_select_all)
# qp = queryParser(query_select_sth)
qp = queryParser(query_select_where)
db.command_executor(qp.generate_job_command())


# for k,v in result.items():
#     print(k, v)


# {'mode': 'create',
#  'target': 'table',
#  'name': 'members',
#  'task': {'column': ['id', 'name', 'age'],
#   'type': ['int', 'varchar(10)', 'int']},
#  'options': {}}