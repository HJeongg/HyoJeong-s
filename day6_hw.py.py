import turtle as t
                         #행운의 네잎클로버 그리기

t.color("green")         #네잎클로버가 초록색이므로 전체색을 초록색으로 지정
t.begin_fill()       
t.speed(0)
t.left(45)             

# 첫번째 잎 그리기
t.forward(80)
for x in range(100):     #다각형 그리기를 토대로 각이 많아질수록 원처럼 보이는 점을 이용함 
    t.forward(1.5)       
    t.left(180/100)      #반원은 180도이므로 180도만큼 회전하도록 설정

t.right(90)              #나머지 반쪽 잎을 그리기 위해 각도 조절
for x in range(100):     #전과 동일
    t.forward(1.5)
    t.left(180/100)
    
t.forward(200)           #두번째 잎을 그리기 위해 각도를 조절 

# 두번째 잎 그리기
for x in range(100):     #첫번째 잎 그리기와 동일하게 설정
    t.forward(1.5)
    t.lt(180/100)

t.right(90)              #각도조절
for x in range(100):     #전과 동일
    t.forward(1.5)
    t.lt(180/100)

t.forward(200)           #반대쪽에 세번째 잎을 그리기 위해 이동

# 세번째 잎 그리기
for x in range(100):     #동일 설정
    t.forward(1.5)
    t.lt(180/100)

t.right(90)
for x in range(100):
    t.forward(1.5)
    t.lt(180/100)

# 마지막 잎 그리기    
t.forward(200)           #마지막 잎을 그리기 위해 위치 이동
for x in range(100):     #동일 설정
    t.forward(1.5)
    t.lt(180/100)
    
t.right(90)
for x in range(100):
    t.forward(1.5)
    t.lt(180/100)     #잎그리기 종료

    
t.forward(100)        #줄기를 그리기 위해 거북이를 중앙으로 이동

t.end_fill()          #이때까지의 모든 선안에 초록색이 채워지도록 설정(잎 색 설정)

t.pensize(10)         #줄기를 굵게 표현하기 위함.
t.right(90)           #줄기를 밑으로 내리기 위하여 거북이 방향 조절 
t.forward(250)        #줄기 그리기
t.left(30)            #끝부분이 꺾어진 줄기 표현
t.forward(30)
