#-*-encoding=utf8-*-
import time
import requests
t=time.time()

r=requests.post('http://127.0.0.1:5002/?inputStr="乙肝和冠心病那个严重"')
print(r.text)


#患者精神可，少量进食，睡眠可，诉自造瘘口排气排出软便。查体：一般情况可，心、肺未见明显异常。腹膨隆，腹部可见一长约12cm手术疤痕。左下腹可见造瘘口，造瘘肠管无溃疡及红肿。腹软、可见胃肠型，全腹无压痛反跳痛及肌紧张，未触及异常包块。腹叩呈鼓音，无移动性浊音。肠鸣音活跃，可闻及气过水声。双下肢无水肿，神经系统查体未见异常。

