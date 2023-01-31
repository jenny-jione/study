## 1. 쿼리 파서 부분

class queryParser:
    
    def __init__(self, query):
        self.dql = ['select']
        self.dml = ['insert', 'update', 'delete']
        self.ddl = ['create', 'alter', 'drop']
        
        self.command_set = {}
        
        # 우리 DBMS의 한계!
        self.q = query.lower().strip().split()
        
        self.command_set['mode'] = self.q[0]
        self.command_set['target'] = self.q[1]
        self.command_set['name'] = self.q[2]
        self.command_set['task'] = {}
        self.command_set['options'] = {}
    
    
    def generate_job_command(self):
        if self.q[0] in self.dql:
            print("dql")
            self.parse_dql()
            return self.command_set

        # DML 질의 요청시
        elif self.q[0] in self.dml:
            print("dml")
            self.parse_dml()
            return self.command_set
        
        # DDL 질의 요청시
        elif self.q[0] in self.ddl:
            print("ddl")
            self.parse_ddl()
            return self.command_set
        
        else:
            raise Exception('SYNTAX ERROR')
    
    
    def parse_dql(self):
        target = query.split('from')[0].split('select')[-1].replace(' ', '').split(',')
        
        if len(target) == 1:
            self.command_set['target'] = target[0]
        else:
            self.command_set['target'] = target
        
        self.command_set['name'] = self.q[3]
        
        option_set = query.split('from')[-1].split()[1:]
        
        condition = option_set[0]
        sub = option_set[1]
        operand = option_set[2]
        obj = option_set[3]
        
        self.command_set['options']['condition'] = condition
        self.command_set['options']['subject'] = sub 
        self.command_set['options']['operand'] = operand
        self.command_set['options']['object'] = obj
    
    
    
    
    def parse_dml(self):
        
        # 메타데이터 파싱
        if self.command_set['mode'] == 'insert':
            
            # 선택한 컬럼값들을 변경할때 -> 모든 컬럼값이 아니라 하나이므로
            col = self.q[2]
            if '(' in col and ')' in col:
                insert_keys= col.split('(')[1].split(')')[0].split(',')
                
                # 테이블 이름 재지정
                self.command_set['name'] = col.split('(')[0]
                for insert_key in insert_keys:
                    self.command_set['task'].setdefault('column', []).append(insert_key)
                    
                    
            values = self.q[-1].split('(')[1].split(')')[0].split(',')
            for value in values:
                self.command_set['task'].setdefault('values',[]).append(value)
            
                
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
        
        
        # DDL 질의에서 change 요청시
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