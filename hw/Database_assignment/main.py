from query_parser import *

# 우리 parser의 한계로 create 명령문은 이런식으로만 들어갑니다!
# 컴파일러 개발이 어려운 프로그래밍중 하나인 이유가 이런 이유도 있죠...

query = '''create table members (
                id int,
                name varchar(10),
                age int
            )'''

qp = queryParser(query)
result = qp.generate_job_command()

print(result)


# {'mode': 'create',
#  'target': 'table',
#  'name': 'members',
#  'task': {'column': ['id', 'name', 'age'],
#   'type': ['int', 'varchar(10)', 'int']},
#  'options': {}}