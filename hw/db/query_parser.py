## 1. 쿼리 파서 부분


# dql : select
# dml : insert, update, delete
# ddl : create, alter, rebane, trabcate, drop

class queryParser:
    
    def __init__(self, query):
        # 입력 받을 커맨드 정의
        self.dql = ['select']
        self.dml = ['insert', 'update', 'delete']
        self.ddl = ['create', 'alter', 'drop']
        
        self.command_set = {}
        
        # 입력 쿼리 정규화
        self.origin_query = query
        # self.q = query.replace(',', '').lower().strip().split()

        self.q = query.lower().strip().split()

        print("-- self.q --")
        print(self.q)
        print(type(self.q), len(self.q))
        print("------------")
        
        self.command_set['mode'] = self.q[0]
        # self.command_set['target'] = self.q[1]
        # self.command_set['name'] = self.q[2]
        self.command_set['task'] = {}
        self.command_set['options'] = {}
        
        print(self.command_set)
        print("-command set-")    
    
    
    # 쿼리 기본 문법 확인: 어떤 질의인지 확인
    def generate_job_command(self):
        # DQL 질의 요청시 : SELECT
        if self.q[0] in self.dql:
            self.parse_dql()
            return self.command_set

        # DML 질의 요청시 : INSERT, UPDATE, DELETE
        elif self.q[0] in self.dml:
            self.parse_dml()
            return self.command_set
        
        # DDL 질의 요청시 : CREATE, ALTER, RENAME, TRUNCATE, DROP
        elif self.q[0] in self.ddl:
            self.parse_ddl()
            return self.command_set
        
        else:
            raise Exception('SYNTAX ERROR')
    
    
    def parse_dql(self):
        print("parse_dql :: select")
        
        select_idx = self.q.index('select')
        print(select_idx)
        
        target_start = self.q.index('select')+1
        target_end = self.q.index('from')
        
        target = self.q[target_start:target_end]
        # print(target)
        
        if len(target) == 1:
            self.command_set['target'] = target[0]
        else:
            self.command_set['target'] = target
            
        print(self.command_set['target'])
        
        self.command_set['name'] = self.q[target_end+1]
        
        print('table name: ', self.command_set['name'])
        
        
        print(self.q)
        print(len(self.q))
        print("-----")
        
        # target : select a, b, c from 에서 a, b, c를 구하기
        # target = query.split('from')[0].split('select')[-1].replace(' ', '').split(',')
        
        # if len(target) == 1:
        #     self.command_set['target'] = target[0]
        # else:
        #     self.command_set['target'] = target
        
        # self.command_set['name'] = self.q[3]
        
        # option_set = query.split('from')[-1].split()[1:]
        
        # condition = option_set[0]
        # sub = option_set[1]
        # operand = option_set[2]
        # obj = option_set[3]
        
        # self.command_set['options']['condition'] = condition
        # self.command_set['options']['subject'] = sub 
        # self.command_set['options']['operand'] = operand
        # self.command_set['options']['object'] = obj
    
    
    def parse_dml(self):
        print("== parse_dml == insert, update, delete")
        # 메타데이터 파싱
        if self.command_set['mode'] == 'insert':
            
            col = self.q[2]
            print("-- col --")
            print(col)
            
            if '(' in col and ')' in col:
                insert_keys= col.split('(')[1].split(')')[0].split(',')
                
                # 테이블 이름 재지정
                self.command_set['name'] = col.split('(')[0]
                for insert_key in insert_keys:
                    self.command_set['task'].setdefault('column', []).append(insert_key)
                    
                    
            values = self.q[-1].split('(')[1].split(')')[0].split(',')
            for value in values:
                self.command_set['task'].setdefault('values',[]).append(value)
            
                
        # 선택한 컬럼값들을 변경할때 -> 모든 컬럼값이 아니라 하나이므로
        elif self.command_set['mode'] == 'update':
            pass
        
        elif self.command_set['mode'] == 'delete':
            pass
        
        else:
            raise Exception('SYNTAX ERROR')

        
    def parse_ddl(self):
        # DLL 질의에서 create 요청시
        if self.command_set['mode'] == 'create':

            # create 문에서 작성한 메타데이터 파싱
            commands = ' '.join(self.q[4:-1]).split(',')
            for command in commands:
                command = command.lstrip().split()

                self.command_set['task'].setdefault('column', []).append(command[0])
                self.command_set['task'].setdefault('type', []).append(command[1])
        
        
        # DDL 질의에서 change(alter) 요청시
        elif self.command_set['mode'] == 'alter':
            
            # alter 문에서 작성한 메타데이터 파싱
            command = ' '.join(self.q[3:]).split(' ')            
            self.command_set['task']['job'] = command[0]
            
            # alter 는 add, modify, change, drop이 있다!
            # 편의상 change만 작성하자.
            if self.command_set['task']['job'] == 'add':
                self.command_set['task']['meta_target'] = command[1]
                self.command_set['task']['target_name'] = command[2]
                self.command_set['task']['target_type'] = command[3]

            elif self.command_set['task']['job'] == 'change':
                self.command_set['task']['meta_target'] = command[1]
                self.command_set['task']['target_name'] = command[2]
                self.command_set['task']['target_new_name'] = command[3]
                if len(command) == 7:
                    self.command_set['task']['target_new_type'] = command[4]
                else:
                    self.command_set['task']['target_new_type'] = None
                    

            elif self.command_set['task']['job'] == 'drop':
                self.command_set['task']['meta_target'] = command[1]
                self.command_set['task']['target_name'] = command[2]

            else:
                raise Exception('SYNTAX ERROR')
        
        
        # 직접 만들어 보세요!
        elif self.command_set['mode'] == 'drop':
            print('this is dropping query')             
        
        
        else:
            raise Exception('SYNTAX ERROR')