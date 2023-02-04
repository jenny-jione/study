## 2. 데이터베이스 프로그램 부분

import os
import ast
class ourDatabase:
    def __init__(self):
        pass
    
    def command_executor(self, command):
        
        mode = command['mode']
        target = command['target']
        name = command['name']
        task = command['task']
        options = command['options']

        if mode == 'create':
            self.create(**command)
        
        elif mode == 'alter':
            self.alter(**command)    
            
        elif mode == 'insert':
            self.insert(**command)
            
        elif mode == 'update':
            pass
        
        elif mode == 'delete':
            pass
            
        elif mode == 'select':
            print("hihihihihihi")
            self.select(**command)
        
            
        else:
            raise Exception('SYNTAX ERROR')
            

    
    def create(self, **kwargs):
        table_name = kwargs['name']
        if os.path.isfile(table_name):
            raise Exception(f"{table_name} Already exists!")
        
        with open(table_name, 'w') as f:
            print(kwargs['task']['column'])
            print("*")
            f.write(str(kwargs['task']['column']) + '\n')     ## 질문
            
        with open(f"{table_name}.meta", 'w') as mf:
            print(kwargs['task']['type'])
            mf.write(str(kwargs['task']['type']))
            

        print(f'Table {kwargs["name"]} created')
        
        
    def alter(self, **kwargs):
        if not os.path.isfile(kwargs['name']):
            raise Exception('Duplicated Table!')
        
        if kwargs['task']['job'] == 'add':
            with open(kwargs['name'], 'r') as f:
                data = f.readline()
                data = ast.literal_eval(data)
                data.append(kwargs['task']['target_name'])

            with open(f'{kwargs["name"]}.meta', 'r') as mf:
                metadata = mf.readline()
                metadata = ast.literal_eval(metadata)
                metadata.append(kwargs['task']['target_type'])

            with open(kwargs['name'], 'w') as f:
                f.write(str(data))

            with open(f'{kwargs["name"]}.meta', 'w') as mf:
                mf.write(str(metadata))
        
            print(f'Table {kwargs["name"]} altered')
            
            
        elif kwargs['task']['job'] == 'change':
            pass
        
        
        elif kwargs['task']['job'] == 'drop':
            pass
        
        else:
            raise Exception('SYNTAX ERROR')
    
    
    def drop(self, **kwargs):
        pass
    
    
    
    def insert(self, **kwargs):
        print("database.py -- insert")
        table_name = kwargs['name']
        if not os.path.isfile(table_name):
            raise Exception('No such table')
        
        values = kwargs['task']['values']
        
        with open(table_name, 'r') as f:
            data = f.readline()
            keys = ast.literal_eval(data)
        
        with open(table_name, 'a') as f2:
            print(values)
            f2.write(str(values) + '\n')
        
        # 아래 메타데이터 부분은 옵션입니다!
        # 메타데이터 부분에서 우리가 create 시 정의한 자료형을 기입하고,
        # 
        with open(f'{table_name}.meta', 'r') as mf:
            metadata = mf.readline()
            metadata = ast.literal_eval(metadata)
        
        if not len(values) == len(keys):
            raise Exception('Value objects mismatching')
        
        for value, metadatum in zip():
            pass
    
    
    
    def update(self, **kwargs):
        pass
    
    
    def delete(self, **kwargs):
        pass
    
    
    def select(self, **kwargs):
        table_name = kwargs['name']
        print("table name:", table_name)
        
        # if not os.path.isfile(table_name):
        #     raise Exception(f"No Such Database:{table_name}")
        
        # with open(table_name, 'r') as f:
        #     datas = f.readlines()
        
        # print(datas)
        
        # trimmed = []
        # for data in datas:
        #     data = data.replace('\n', '')
        #     data = ast.literal_eval(data)
        #     trimmed.append(data)
        
        # for t in trimmed:
        #     print(t)