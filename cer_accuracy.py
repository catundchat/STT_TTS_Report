import numpy as np
import re

# 定义编辑距离函数
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = np.zeros((m+1, n+1), dtype=int)
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    return dp[m][n]

# 定义计算字符错误率CER的函数
def cer(ground_truth, transcription):
    distance = edit_distance(ground_truth, transcription)
    return distance / len(ground_truth)

# 定义计算准确率的函数
def accuracy(ground_truth, transcription):
    correct_chars = sum(1 for gt_char, tr_char in zip(ground_truth, transcription) if gt_char == tr_char)
    return correct_chars / len(ground_truth)

# 去除中文字段里的标点符号
def remove_punctuation(text):
    pattern = re.compile(r"[\u3000-\u303f\uff00-\uffef]|[.,!?;]")
    return re.sub(pattern, "", text)

# 示例
ground_truth = "信息技术部门中机器学习的主要应用之一是向潜在用户或客户推荐项目。这可以分为两种主要的应用：在线广告和项目建议（通常这些建议的目的仍是为了销售产品）。两者都依赖于预测用户和项目的关联，一旦向该用户展示了广告或推荐了该产品，推荐系统要么预测一些行为的概率。"
transcription = "信息技术部门中机器学习的主要运用之一是向潜在用户或客户推荐项目这可以分为两种主要的应用在线广告和项目建议通常这些建议的目的仍然是为了销售产品两者都依赖于预测用户和项目之间的观联一旦向该用户展示的广告和推荐的该产品推荐系统要么预测一些行为的概率"
ground_truth_punc = remove_punctuation(ground_truth)
# print(f"groundtruth without punctuation: {ground_truth_punc}")

# 计算准确率
acc = accuracy(ground_truth, transcription)
acc_punc = accuracy(ground_truth_punc, transcription)
print(f"Accuracy: {acc:.4f}")
print(f"Accuracy without punctuation: {acc_punc:.4f}")

# 计算CER
CER = cer(ground_truth, transcription)
CER_punc = cer(ground_truth_punc, transcription)
print(f"CER: {CER:.4f}")
print(f"CER without punctuation: {CER_punc:.4f}")
