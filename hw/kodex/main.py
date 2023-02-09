import sys
from split_jamo import *
from kodex import *

# Kodex 알고리즘
# (1) 자소 단위로 풀어 쓰고, 첫글자 초성 ‘ㅇ’(이응)을 제외한 모든 초성 ‘ㅇ’을 제거한다. (초성이응제거)
# (2) 같은 자음이 연속되는 종성-초성에서 종성을 제거한다. (중복종성제거)
# (3) 첫 글자 초성을 대표 자음으로 변환한다. (초성대표자음화)
# (4) 나머지 자음에 대해서 kodex 자음 코드로 치환한다. 이때 모음이 자동적으로 제거된다. (코드치환)
# (5) 종성-초성 관계에 있는 연속 중복 코드를 제거한다. (연속중복코드제거)

if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        input_keyword = sys.argv[1]
        print(input_keyword)
        result = convert(input_keyword)
        print(result)
        kodex_convert(result)
    else:
        # test_keyword = input("input your text:")
        # test_keywords = ["윈도우즈", "윈도우스", "윈도즈", "프롤로그", "사운드", "싸운드", "패킷", "패키트", "팩킷", "휠터"]
        # test_keywords = ["너까래", "넛까래", "디지털", "디지틀"]
        test_keywords = ["카냑", "카약", "카츄샤", "카튜샤", "플라스마", "플라즈마", "리본", "리봉", "스카웃", "스카우트", "디지틀", "디지탈"]
        
        results = []
        for tkw in test_keywords:
            print(f"====== {tkw} ======")
            res = convert(tkw)
            kodex_convert(res)
            print()
    