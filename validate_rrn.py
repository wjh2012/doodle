from collections import defaultdict

ocr_results = [
        {
            "name": "Annotation1",
            "points": {
                "x1": 435,
                "y1": 296,
                "x2": 535,
                "y2": 328
            },
            "text": "770830",
            "score": [
                0.31693560825221606
            ]
        },
        {
            "name": "Annotation1",
            "points": {
                "x1": 564,
                "y1": 293,
                "x2": 674,
                "y2": 329
            },
            "text": "1640364",
            "score": [
                0.6900641060063657
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 64,
                "y1": 652,
                "x2": 94,
                "y2": 666
            },
            "text": "상품명",
            "score": [
                0.9987234647259652
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 276,
                "y1": 652,
                "x2": 306,
                "y2": 666
            },
            "text": "계약액",
            "score": [
                0.9936177233389905
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 410,
                "y1": 650,
                "x2": 450,
                "y2": 666
            },
            "text": "계약기간",
            "score": [
                0.9983580112457275
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 60,
                "y1": 676,
                "x2": 98,
                "y2": 690
            },
            "text": "이자지급",
            "score": [
                0.9279569983482361
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 118,
                "y1": 676,
                "x2": 154,
                "y2": 690
            },
            "text": "만전지금",
            "score": [
                0.565990149974823
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 166,
                "y1": 676,
                "x2": 202,
                "y2": 688
            },
            "text": "자급",
            "score": [
                0.46302028368547027
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 216,
                "y1": 676,
                "x2": 238,
                "y2": 688
            },
            "text": "",
            "score": [
                0.0
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 272,
                "y1": 676,
                "x2": 310,
                "y2": 690
            },
            "text": "과세선택",
            "score": [
                0.9842479825019836
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 354,
                "y1": 676,
                "x2": 386,
                "y2": 690
            },
            "text": "우",
            "score": [
                0.3942944947639262
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 400,
                "y1": 676,
                "x2": 458,
                "y2": 690
            },
            "text": "한도",
            "score": [
                0.8594250759228752
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 58,
                "y1": 698,
                "x2": 102,
                "y2": 714
            },
            "text": "인금적립기간",
            "score": [
                0.8304001357826579
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 170,
                "y1": 698,
                "x2": 214,
                "y2": 714
            },
            "text": "연금수기간",
            "score": [
                0.39077678193206616
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 268,
                "y1": 696,
                "x2": 310,
                "y2": 716
            },
            "text": "",
            "score": [
                0.0
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 372,
                "y1": 700,
                "x2": 400,
                "y2": 712
            },
            "text": "아니오",
            "score": [
                0.9563378379841084
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 408,
                "y1": 698,
                "x2": 450,
                "y2": 714
            },
            "text": "연금지금주기",
            "score": [
                0.5807793046387151
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 57,
                "y1": 726,
                "x2": 136,
                "y2": 742
            },
            "text": "예금잔액동보제외신청",
            "score": [
                0.7261917524054486
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 142,
                "y1": 726,
                "x2": 448,
                "y2": 742
            },
            "text": "금차신청계좌에 대하여는 사고예방을 위한여금진액동보를 생략하여주시기바랍니다.",
            "score": [
                0.26409043238684526
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 57,
                "y1": 752,
                "x2": 148,
                "y2": 772
            },
            "text": "청",
            "score": [
                0.29719610636880134
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 120,
                "y1": 780,
                "x2": 168,
                "y2": 794
            },
            "text": "현금IIC카트",
            "score": [
                0.49285443490500075
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 188,
                "y1": 780,
                "x2": 222,
                "y2": 794
            },
            "text": "전자동장",
            "score": [
                0.4949202239513397
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 242,
                "y1": 782,
                "x2": 278,
                "y2": 794
            },
            "text": "전자매",
            "score": [
                0.1822784584653736
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 298,
                "y1": 780,
                "x2": 332,
                "y2": 794
            },
            "text": "고통기도",
            "score": [
                0.37887176871299744
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 354,
                "y1": 780,
                "x2": 450,
                "y2": 794
            },
            "text": "자통장",
            "score": [
                0.5928272915780364
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 59,
                "y1": 799,
                "x2": 99,
                "y2": 825
            },
            "text": "",
            "score": [
                0.0
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 106,
                "y1": 804,
                "x2": 202,
                "y2": 820
            },
            "text": "전자통장 별칭(한굴10자)",
            "score": [
                0.13662221519498716
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 110,
                "y1": 826,
                "x2": 200,
                "y2": 840
            },
            "text": "영문명(전자화패 발급시)",
            "score": [
                0.20529579990051172
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 60,
                "y1": 846,
                "x2": 98,
                "y2": 860
            },
            "text": "동장지급",
            "score": [
                0.682295024394989
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 108,
                "y1": 848,
                "x2": 204,
                "y2": 862
            },
            "text": "동장안으로 한금자통입출금기",
            "score": [
                0.34782369748014064
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 212,
                "y1": 848,
                "x2": 276,
                "y2": 862
            },
            "text": "이용하여한금인호",
            "score": [
                0.5452325104323076
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 284,
                "y1": 848,
                "x2": 364,
                "y2": 862
            },
            "text": "계좌이처가 가능하도록",
            "score": [
                0.3682486200687995
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 372,
                "y1": 848,
                "x2": 456,
                "y2": 862
            },
            "text": "주시기바라이이로 인반",
            "score": [
                0.55573518872532
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 60,
                "y1": 858,
                "x2": 88,
                "y2": 872
            },
            "text": "서비",
            "score": [
                0.9943949507576283
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 62,
                "y1": 868,
                "x2": 100,
                "y2": 882
            },
            "text": "(CD/ATM)",
            "score": [
                0.3108528484549698
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 418,
                "y1": 868,
                "x2": 444,
                "y2": 882
            },
            "text": "신성인",
            "score": [
                0.9470501917628557
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 116,
                "y1": 890,
                "x2": 146,
                "y2": 906
            },
            "text": "은행명",
            "score": [
                0.9317167375510871
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 214,
                "y1": 890,
                "x2": 278,
                "y2": 904
            },
            "text": ")번호",
            "score": [
                0.469305002222321
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 356,
                "y1": 890,
                "x2": 384,
                "y2": 904
            },
            "text": "예금주",
            "score": [
                0.9808715809060087
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 430,
                "y1": 890,
                "x2": 464,
                "y2": 904
            },
            "text": "이처금액",
            "score": [
                0.31559935212135315
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 60,
                "y1": 902,
                "x2": 100,
                "y2": 916
            },
            "text": "계좌간",
            "score": [
                0.9882062650946372
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 60,
                "y1": 912,
                "x2": 100,
                "y2": 928
            },
            "text": "(은행간)",
            "score": [
                0.7857175546503977
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 60,
                "y1": 926,
                "x2": 100,
                "y2": 940
            },
            "text": "자동이체",
            "score": [
                0.9842696189880371
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 110,
                "y1": 942,
                "x2": 464,
                "y2": 956
            },
            "text": "제조간은행간 자등이체약관을 수령하고 상기와 같이 신청합니다본인계좌촉입근자동출관승인)",
            "score": [
                0.07593407141193996
            ]
        }
    ]

ocr_results2 = [
        {
            "name": "Annotation2",
            "points": {
                "x1": 436,
                "y1": 296,
                "x2": 536,
                "y2": 328
            },
            "text": "970501",
            "score": [
                0.2968575799523399
            ]
        },
        {
            "name": "Annotation2",
            "points": {
                "x1": 565,
                "y1": 293,
                "x2": 675,
                "y2": 328
            },
            "text": "1017521",
            "score": [
                0.9849818733916358
            ]
        }
    ]

import time

def find_rrn(data):
    # 같은 annotation 끼리 그룹화
    grouped_results = defaultdict(list)
    for item in data:
        grouped_results[item['name']].append(item)

    fields = {}

    for group in grouped_results:
        flag = False
        
        for idx, item in enumerate(grouped_results[group]):
            cur_text = item['text']
            
            if len(cur_text) == 6 and cur_text.isdigit():
                flag = True
            elif idx > 0 and len(cur_text) == 7 and cur_text.isdigit() and flag is True:
                left_text = grouped_results[group][idx-1]['text']
                rrn = left_text+cur_text
                validate_rrn(rrn)
                flag=False
            else:
                flag=False
            
def validate_rrn(str):
    numbers = [int(char) for char in str]
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    n_sum = sum(num * weight for num, weight in zip(numbers[:12], weights))
    result = (11 - (n_sum % 11)) % 10
    print(numbers[12] == result) 

start_time = time.perf_counter() 
find_rrn(ocr_results)
end_time = time.perf_counter()  
execution_time = end_time - start_time 
print(f"execution time: {execution_time:.9f} seconds")

start_time = time.perf_counter() 
find_rrn(ocr_results2)
end_time = time.perf_counter()  
execution_time = end_time - start_time
print(f"execution time: {execution_time:.9f} seconds")

start_time = time.perf_counter() 
validate_rrn("9705011017521")
end_time = time.perf_counter()  
execution_time = end_time - start_time
print(f"valid execution time: {execution_time:.9f} seconds")