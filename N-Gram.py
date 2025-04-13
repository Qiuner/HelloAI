from collections import defaultdict, Counter
import random
# 第一步：创建语料库
corpus = [
    "我早上去了图书馆",
    "我早上听了一节英语课",
    "我中午看了一部电影",
    "我中午睡了一会儿",
    "我晚上写了一篇作文",
    "我晚上复习了功课",
]

# 第二部：分词函数（按字分词）
def split_words(text):
    return [char for char in text]


# 第三步：统计Bigram词频
bigram_freq = defaultdict(Counter)
for sentence in corpus:
    words = split_words(sentence)
    for i in range(len(words) - 1):
        first, second = words[i], words[i+1]
        bigram_freq[first][second] += 1
# 打印词频率
print("打印词频率")
for first, counter in bigram_freq.items():
    freq_list = [f"{second}：{freq}" for second, freq in counter.items()]
    print(f"{first}: [{', '.join(freq_list)}]")


# 第四步：计算Bigram概率（转为概率分布）
bigram_prob = {}
for first, counter in bigram_freq.items():
    total = sum(counter.values())
    bigram_prob[first] = {second: count / total for second, count in counter.items()}
print("词频概率为：", bigram_prob)


# 第五步：根据前缀生成下一个字
def predict_next_char(prev_char):
    if prev_char not in bigram_prob:
        return None
    candidates = list(bigram_prob[prev_char].items())
    chars, probs = zip(*candidates)
    return random.choices(chars, probs)[0]


# 第六步：输入前缀，生成文本
def generate_text(start_char, length=10):
    result = [start_char]
    current = start_char
    for _ in range(length - 1):
        next_char = predict_next_char(current)
        if not next_char:
            break
        result.append(next_char)
        current = next_char
    return ''.join(result)

# 输入我时
for i in range(10):
    print(generate_text("我"))
