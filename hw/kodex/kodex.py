REP_JAUM = {
    "ㄲ": "ㄱ", "ㄸ": "ㄷ", "ㅃ": "ㅂ", "ㅆ": "ㅅ", "ㅉ": "ㅈ", "ㅎ": "ㅍ"
}

JAUM_CODE = {
    'ㄱ' : '1', 'ㄱ*' : '1', 'ㄲ' : '1', 'ㅋ' : '1',
    'ㄴ' : '2', 'ㄴ*' : '2', 'ㅇ' : '2', 'ㅇ*' : '2', 
    'ㄷ' : '3', 'ㄸ' : '3', 'ㅌ' : '3', 'ㅅ*' : '3', 'ㅊ' : '3', 
    'ㄹ' : '4', 'ㄹ*' : '4', 
    'ㅁ' : '5', 'ㅁ*' : '5', 
    'ㅂ' : '6', 'ㅂ*' : '6', 'ㅃ' : '6', 'ㅍ' : '6', 'ㅎ' : '6', 
    'ㅅ' : '7', 'ㅆ' : '7', 'ㅈ' : '7', 'ㅉ' : '7'
}


def kodex_convert(result):
    print("== kodex start ==")
    
    # (1) 자소 단위로 풀어 쓰고, 첫글자 초성 ‘ㅇ’(이응)을 제외한 모든 초성 ‘ㅇ’을 제거한다. (초성이응제거)
    print(result)
    print('''\n(1) 자소 단위로 풀어 쓰고, 첫글자 초성 ‘ㅇ’(이응)을 제외한 모든 초성 ‘ㅇ’을 제거한다. (초성이응제거)''')
    
    kodex_1 = []
    kodex_1.append(result[0])
    for kw in result[1:]:
        if kw[0] == 'ㅇ':
            kw = kw[1:]
        if kw:
            kodex_1.append(kw)
    
    print(kodex_1)
    
    
    # (2) 같은 자음이 연속되는 종성-초성에서 종성을 제거한다. (중복종성제거)
    print('''\n(2) 같은 자음이 연속되는 종성-초성에서 종성을 제거한다. (중복종성제거)''')
    kodex_2 = kodex_1[:]
    
    for i, kw in enumerate(kodex_2):
        if i>0:
            pre_kw = kodex_2[i-1]
            if pre_kw[-1] == kw[0]:
                pre_kw = pre_kw[:-1]
                kodex_2[i-1] = pre_kw
   
    print(kodex_2)
    
        
    # (3) 첫 글자 초성을 대표 자음으로 변환한다. (초성대표자음화)
    print('''\n(3) 첫 글자 초성을 대표 자음으로 변환한다. (초성대표자음화)''')
    kodex_3 = kodex_2[:]
    
    first_kw = kodex_3[0]
    first_kw_first = first_kw[0]
    print(first_kw_first)
    
    if first_kw_first in REP_JAUM:
        kodex_3[0][0] = REP_JAUM[first_kw_first]
        first_rep_jaum = REP_JAUM[first_kw_first]
    else:
        first_rep_jaum = first_kw_first
        
    print(kodex_3)
    
    
    
    # (4) 나머지 자음에 대해서 kodex 자음 코드로 치환한다. 이때 모음이 자동적으로 제거된다. (코드치환)
    print('''\n(4) 나머지 자음에 대해서 kodex 자음 코드로 치환한다. 이때 모음이 자동적으로 제거된다. (코드치환)''')
    kodex_4 = []
    for kw in kodex_3[:]:
        for ch in kw:
            if ch in JAUM_CODE:
                kodex_4.append(JAUM_CODE[ch])
                    
    print(kodex_4)
    kodex_4[0] = first_rep_jaum
    print(kodex_4)
    
    
    # (5) 종성-초성 관계에 있는 연속 중복 코드를 제거한다. (연속중복코드제거)
    print('''\n(5) 종성-초성 관계에 있는 연속 중복 코드를 제거한다. (연속중복코드제거)''')
    prev = ''
    kodex_result = ""
    for i, code in enumerate(kodex_4):
        if i>0:
            prev = kodex_4[i-1]
        if prev != code:
            kodex_result += str(code)
    
    print("kodex result :", kodex_result)