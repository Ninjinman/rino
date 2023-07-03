from django.shortcuts import render
from django.http import JsonResponse
from .consts import TOMATO_RATE

#設定レベルを定義(0～5)
SETTING_RANK = 0

def slot_game(request):
    return render(request, 'rino/slot_game.html')

def game(request):
    # トマト遷移確率を出力
    tomatoRate = TOMATO_RATE[SETTING_RANK]

    # 1プレイヤー情報取得(今はどの状態？)from DB

    # 2プレイヤー情報が取得できなかったら(初期状態にする)

    # 3次の状態の計算
        # 現在の状態によってロジック変わる switch文
        # 現在が基本B(0)なら　1/tomatoRateでトマト化 みたいな

    # 4状態に応じた出目の計算
        # 中身はようわからん
    
    # 5 3で計算した状態と、4で計算した出目をテーブルに保存

    return JsonResponse({"result": "Success."})

    