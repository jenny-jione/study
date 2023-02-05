# -*- coding: utf-8 -*-
import re
import sys
"""
    초성 중성 종성 분리 하기
	유니코드 한글은 0xAC00 으로부터
	초성 19개, 중성21개, 종성28개로 이루어지고
	이들을 조합한 11,172개의 문자를 갖는다.
	한글코드의 값 = ((초성 * 21) + 중성) * 28 + 종성 + 0xAC00
	(0xAC00은 'ㄱ'의 코드값)
	따라서 다음과 같은 계산 식이 구해진다.
	유니코드 한글 문자 코드 값이 X일 때,
	초성 = ((X - 0xAC00) / 28) / 21
	중성 = ((X - 0xAC00) / 28) % 21
	종성 = (X - 0xAC00) % 28
	이 때 초성, 중성, 종성의 값은 각 소리 글자의 코드값이 아니라
	이들이 각각 몇 번째 문자인가를 나타내기 때문에 다음과 같이 다시 처리한다.
	초성문자코드 = 초성 + 0x1100 //('ㄱ')
	중성문자코드 = 중성 + 0x1161 // ('ㅏ')
	종성문자코드 = 종성 + 0x11A8 - 1 // (종성이 없는 경우가 있으므로 1을 뺌)
"""
# 유니코드 한글 시작 : 44032, 끝 : 55199
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

REP_JAUM = {
    "ㄲ": "ㄱ",
    "ㄸ": "ㄷ",
    "ㅃ": "ㅂ",
    "ㅆ": "ㅅ",
    "ㅉ": "ㅈ",
    "ㅎ": "ㅍ",
}


def convert(test_keyword):
    kodex_12 = []

    split_keyword_list = list(test_keyword)
    #print(split_keyword_list)

    result = list()
    for keyword in split_keyword_list:
        print(keyword)
        kw = []
        print("kw:", kw)
        # 한글 여부 check 후 분리
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
            char_code = ord(keyword) - BASE_CODE

            char1 = int(char_code / CHOSUNG)
            first = CHOSUNG_LIST[char1] # 초성 한글

            kw.append(first)

            result.append(CHOSUNG_LIST[char1])
            print('초성 : {}'.format(CHOSUNG_LIST[char1]))
            
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            result.append(JUNGSUNG_LIST[char2])
            print('중성 : {}'.format(JUNGSUNG_LIST[char2]))

            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            last = JONGSUNG_LIST[char3] # 종성 한글
            if char3==0:
                result.append('#')
            else:
                result.append(JONGSUNG_LIST[char3])
                kw.append(last)
            print('종성 : {}'.format(JONGSUNG_LIST[char3]))

            print(kw)
            kodex_12.append(kw)
            print(kodex_12)

        else:
            result.append(keyword)
    # result
    print("".join(result))

    return kodex_12

if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        inputfile = open(sys.argv[1], 'r')
        for line in inputfile.readlines():
            convert(line)
    else:
        test_keyword = input("input your text:")
        kodex_1_2 = convert(test_keyword)

    
    print(kodex_1_2)

    print("kodex")

    
    for i, kw in enumerate(kodex_1_2):
        print(i, kw)
        # (1) 자소 단위로 풀어 쓰고, 첫글자 초성 ‘ㅇ’(이응)을 제외한 모든 초성 ‘ㅇ’을 제거한다. (초성이응제거)
        if i>0 and kw[0] == 'ㅇ':
            kw = kw[1:]
        # print(i, kw)

        if i>0:
            pre_kw = kodex_1_2[i-1]
            print("ㅔpre_kw:" , pre_kw)
            if pre_kw[-1] == kw[0]:
                # (2) 같은 자음이 연속되는 종성-초성에서 종성을 제거한다. (중복종성제거)
                print("2!!", kw[0], pre_kw[-1])
                print("pre_kw:", pre_kw)
                pre_kw = pre_kw[:-1]
                print("pre_kw[:-1]",pre_kw)
                print("kodex12", kodex_1_2)

                kodex_1_2[i-1] = pre_kw

                print("-- kodex12", kodex_1_2)


    # (1) 자소 단위로 풀어 쓰고, 첫글자 초성 ‘ㅇ’(이응)을 제외한 모든 초성 ‘ㅇ’을 제거한다. (초성이응제거)
    # (2) 같은 자음이 연속되는 종성-초성에서 종성을 제거한다. (중복종성제거)
    # (3) 첫 글자 초성을 대표 자음으로 변환한다. (초성대표자음화)
    # (4) 나머지 자음에 대해서 kodex 자음 코드로 치환한다. 이때 모음이 자동적으로 제거된다. (코드치환)
    # (5) 종성-초성 관계에 있는 연속 중복 코드를 제거한다. (연속중복코드제거)
