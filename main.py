import random
def simulate_single_game(prob_a):
    """模拟一局比赛，prob_a是A选手得分的概率"""
    score_a = 0
    score_b = 0
    while True:
        # 模拟一分的争夺
        if random.random() < prob_a:
            score_a += 1
        else:
            score_b += 1        
        # 判断是否分出胜负
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return 1 if score_a > score_b else 0
# 测试：A选手得分概率0.6，模拟一局
result = simulate_single_game(0.6)
print("A胜" if result == 1 else "B胜")
