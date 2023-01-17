# 2023.01.16 Mon

import socket

kangsan = '192.168.0.62'
myhome = '172.30.1.39'
def run_client(host=myhome, port=7789):

    print("a")
    with socket.socket() as sock:
        name = input("이름을 입력해주세요: ")
        sock.connect((host, port))

        for _ in range(100):
            data = input(">>> ")
            data = f'{name} 이 말합니다: {data}'
            sock.sendall(data.encode())

            try:
                if 'quit' in data:
                    sock.close()
                    break

            except KeyboardInterrupt:
                sock.close()
                break

if __name__ == "__main__":
    print("hi i am client")
    run_client()


# 파이썬의 멀티스레드
# 소켓 통신할 때 사용한다
# 온라인 게임 --> 유저 하나하나가 모두 스레드.
# 멀티스레드. 멀티프로세스. 비동기
# 멀티스레드, 멀티프로세스는 작업을 정확히 나누어야 함. ㅋ ㅓ ㅁ ㄱ ㅗ ㅇ 


# 숙제. (둘 중 하나)
# 1. 비동기(멀티스레드, 멀티프로세스)를 이용해서 크롤링 코드 짜오기
# 2. 소켓을 사용해서 텍스트 데이터를 주고받았음. ==> 숙제: 소켓프로그래밍을 이용해서 이미지/파일을 전송하는 코드.
# 언제끼지? 2주 뒤. 설 연휴 끝나고.