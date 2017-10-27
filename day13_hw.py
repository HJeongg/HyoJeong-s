import turtle as t
import random

t.shape("circle")                       # 공튀기기게임처럼 보이기 위해 거북이를 원모양으로 설정
t.color("blue")
t.pensize(5)
t.speed(0)

t.up()                                    # 정사각형을 왼쪽 맨 위에 만들기 위해 좌표 이동
t.goto(-478,404)                     
t.down()

for x in range(4):                    # 가로x세로 길이가 각각 500인 정사각형을 만듦
    t.forward(500)
    t.right(90)


# 정사각형 장애물 2개 만들기 __ 정사각형, 길이는 50부터 100까지 랜덤
length = random.randint(50,100)
def make_barrier():
    t.setheading(0)
    t.pensize(2)
    for x in range(4):
        t.forward(length)
        t.left(90)

# 장애물 1 그리기
t.up()
t.goto(-200,0)
t.down()
make_barrier()

# 장애물 2 그리기
t.up()
t.goto(-350,300)
t.down()
make_barrier()

# 게임시작을 중앙에서 하기 위해 좌표이동
t.up()                                   
t.goto(-232,161)
t.down()

t.color("gray")                       # 사각형과 공의 튀김을 구별하기 위해 굵기와 색 재선정
t.pensize(1)
t.heading != 0                       # 처음에 직선으로 출발하면 계속 일자로 움직이므로 직선출발을 불가능하게 설정함
t.heading != 90
t.heading != 180
t.heading != 270

# 오른쪽 벽에 닿았을 때
def hit_right(i):                        
    if x >= i:                  #  x좌표가 경계선 a(+22)를 넘었을 때 
        if y <= b:                      # 아래로 내려가는 방향일 때 튕김설정
            t.right(2*(ang-270))     # 반사각으로 방향이 바뀌도록 설정
        else:                             # 위로 올라가는 방향일 때 튕김설정
            t.left(2*(90-ang))    

# 왼쪽 벽을 맞았을 때
def hit_left(i):
    if x <= i:   # x좌표가 경계선i를 넘었을 때
        if y <= b:      # 위에서 아래로
            t.left(2*(270-ang))
        else:           # 아래에서 위로
            t.right(2*(ang-90))

#위쪽 벽을 맞았을 때
def hit_top(i):   
    if y >= i:   # y좌표가 경계선 i를 넘었을 때
        if x <= a:      # 오른쪽에서 왼쪽으로 가는 방향이었을 때
            t.left(2*(180-ang))
        else:           # 왼쪽에서 오른쪽으로 가는 방향이었을 때
            t.right(2*ang)

# 아래쪽 벽을 맞았을 때
def hit_bottom(i):
    if y <= i:   # y좌표가 경계선 i를 넘었을 때
        if x <= a:      # 오른쪽에서 왼쪽
            t.right(2*(ang-180))
        else:           # 왼쪽에서 오른쪽
            t.left(2*(360-ang))


t.speed(0)                           # 공이 튀기는 속도 조절                   
m = random.randint(1,360)
w = t.setheading(m)

while True:                           # 공을 무한대로 움직임
    a = t.xcor()
    b = t.ycor()

# <좌표> _ 왼쪽위: (-478,404), 오른쪽위:(22,404), 왼쪽아래:(-478,-96), 오른쪽아래:(22,-96)
    if a <= -478 or a >= 22 or b >= 404 or b <= -96:           # 가장 큰 사각형에서 튕기기
        x = t.xcor()
        y = t.ycor()
        ang = t.heading()
    
        hit_right(22)
        hit_left(-478)
        hit_top(404)
        hit_bottom(-96)

# 장애물1에 부딪혔을 때
# 장애물1의 좌표_ 왼쪽 위:(-200,0+length) 왼쪽 아래:(-200,0), 오른쪽 위:(-200+length,0+length), 오른쪽 아래: (-200+length,0) 
    if t.xcor() <= (-200+length) and t.xcor() >= -200 and t.ycor() <= (0+length) and t.ycor() >= 0 :
        x = t.xcor()
        y = t.ycor()
        ang = t.heading()
        if x <= (-200+length-1) and y <= (0+length-1) and  y>= 0+1:
            if y <= b:
                t.right(2*(ang-270))
            else:
                t.left(2*(90-ang))
        if x >= -200+1 and y <= (0+length-1) and y >= 0+1:
            if y <= b:
                t.left(2*(270-ang))
            else:
                t.right(2*(ang-90))
        if y >= 0+1 and x >= -200+1 and x <= (-200+length-1):
            if x <= a:
                t.right(2*(ang-180))
            else:
                t.left(2*(360-ang))
        if y <= (0+length-1) and x >= -200+1 and x <= (-200+length-1):
            if x <= a:
                t.left(2*(180-ang))
            else:
                t.right(2*ang)
        
    # 장애물2에 부딪혔을 때
    # 장애물2의 좌표_왼쪽위(-350,300+length), 왼쪽아래(-350,300), 오른쪽위(-350+length,300+length), 오른쪽아래(-350+length,300)
    if t.xcor() <= (-350+length) and t.xcor() >= -350 and t.ycor() <= (300+length) and t.ycor() >= 300:
        x = t.xcor()
        y = t.ycor()
        ang = t.heading()
        if x <= (-350+length-1) and y <= (300+length-1) and  y >= 300+1:
            if y <= b:
                t.right(2*(ang-270))
            else:
                t.left(2*(90-ang))
        if x >= -350+1 and y <= (300+length)-1 and y >= 300+1:
            if y <= b:
                t.left(2*(270-ang))
            else:
                t.right(2*(ang-90))
        if y >= 300+1 and x >= -350+1 and x <= (-350+length-1):
            if x <= a:
                t.right(2*(ang-180))
            else:
                t.left(2*(360-ang))
        if y <= (300+length-1) and x >= -350+1 and x <= (-350+length-1):
            if x <=a:
                t.left(2*(180-ang))
            else:
                t.right(2*ang)

# 1씩 나아가는 것으로 속도조절        
    t.forward(1)

