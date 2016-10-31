import random
from time import sleep

"""_define__"""
def strike_check(pn_list,cn_list):
	strk_cnt=0
	ball_cnt=0
	pn_cnt=0
	for player_num in pn_list:
		for com_num in cn_list:
			if player_num == com_num:
				if com_num == cn_list[pn_cnt]:
					strk_cnt+=1
				else:
					ball_cnt+=1
		pn_cnt+=1
	print('\n')
	if not(strk_cnt or ball_cnt): print('아웃!') #숫자 하나도 못맞출경우
	elif strk_cnt==3: print('삼진! 축하합니다!'); return 1
	else:
		if strk_cnt: print(strk_cnt,'스트라이크! '), #개행 없는 표준출력을 위해 ','사용
		if ball_cnt: print(ball_cnt,'볼! ')
	return 0

"""__main__"""
loop_cnt=0
pn_list=[0,0,0]
num_data=[1,2,3,4,5,6,7,8,9]

print('\n\n[<숫자 야구 게임>]\n')

print('컴퓨터가 세개의 수를 정하고 있습니다.\n')
cn_list= random.sample(num_data,3) #중복 순열
sleep(1)
	
while True:
	i=0
	loop_cnt+=1
	print("\n~제", loop_cnt,'회 시작~')
	if loop_cnt ==3:
		print('(힌트: 세 수의 합은',sum(cn_list),')\n')
	#print(cn_list,'\n')
	while i!=3:
		print(i+1,'번째 공 위치 선택: ')
		pn_list[i]= int(input('>> '))
		i+=1
		
	if strike_check(pn_list,cn_list):
		break	

