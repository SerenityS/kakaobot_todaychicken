# -*- coding: utf-8 -*-

import datetime
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)


# GET ~/keyboard/ 요청에 반응
def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘의 치킨']
    })


# csrf 토큰 에러 방지, POST 요청에 message response
@csrf_exempt
def message(request):
    today_date = datetime.date.today().strftime("%m월 %d일 ")

    return JsonResponse({
        'message': {
            'text': today_date + '오늘의 추천 치킨 메뉴입니다. \n\n' + chicken(request)
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['오늘의 치킨']
        }
    })


# message 요청 받을시 메뉴 결정
def chicken(request):
    import random

    number = random.randint(0, 97)
    menu = ''

    if number == 0:
        menu = "교촌 오리지날"
    if number == 1:
        menu = "교촌 콤보"
    if number == 2:
        menu = "교촌 윙"
    if number == 3:
        menu = "교촌 스틱"
    if number == 4:
        menu = "교촌 허니 오리지날"
    if number == 5:
        menu = "교촌 허니 콤보"
    if number == 6:
        menu = "교촌 레드 오리지날"
    if number == 7:
        menu = "교촌 레드 콤보"
    if number == 8:
        menu = "교촌 반반 오리지날"
    if number == 9:
        menu = "교촌 반반 콤보"
    if number == 10:
        menu = "교촌 후라이드"
    if number == 11:
        menu = "교촌 살살치킨"
    if number == 12:
        menu = "교촌 소이살살"
    if number == 13:
        menu = "굽네 갈비천왕"
    if number == 14:
        menu = "굽네 오리지널"
    if number == 15:
        menu = "굽네 익스트림 볼케이노"
    if number == 16:
        menu = "굽네 볼케이노"
    if number == 17:
        menu = "굽네 반반"
    if number == 18:
        menu = "굽네 고추바사삭"
    if number == 19:
        menu = "굽네 후르츠 소이갈릭"
    if number == 20:
        menu = "굽네 양념 치킨"
    if number == 21:
        menu = "굽네 딥치즈"
    if number == 22:
        menu = "굽네 오리지널"
    if number == 23:
        menu = "굽네 폭립"
    if number == 24:
        menu = "BHC 붐바스틱"
    if number == 25:
        menu = "BHC 스윗텐더"
    if number == 26:
        menu = "BHC 치레카"
    if number == 27:
        menu = "BHC 뿌링클"
    if number == 28:
        menu = "BHC 맛초킹"
    if number == 29:
        menu = "BHC 양념치킨"
    if number == 30:
        menu = "BHC 후라이드치킨"
    if number == 31:
        menu = "BHC 반반치킨"
    if number == 32:
        menu = "BHC 간장치킨"
    if number == 33:
        menu = "페리카나 후라이드"
    if number == 34:
        menu = "페리카나 양념치킨"
    if number == 35:
        menu = "페리카나 매운 양념치킨"
    if number == 36:
        menu = "페리카나 매운 후라이드치킨"
    if number == 37:
        menu = "페리카나 마늘치킨"
    if number == 38:
        menu = "페리카나 파닭치킨"
    if number == 39:
        menu = "페리카나 간장치킨"
    if number == 40:
        menu = "페리카나 핫칠리치킨"
    if number == 41:
        menu = "페리카나 조청치킨"
    if number == 42:
        menu = "페리카나 핫데블치킨"
    if number == 43:
        menu = "본스치킨 본빵사수"
    if number == 44:
        menu = "본스치킨 레드번"
    if number == 45:
        menu = "본스치킨 슈퍼레드번"
    if number == 46:
        menu = "본스치킨 칠리"
    if number == 47:
        menu = "본스치킨 소이갈릭"
    if number == 48:
        menu = "본스치킨 오리지널"
    if number == 49:
        menu = "본스치킨 바베큐"
    if number == 50:
        menu = "본스치킨 크리스피 후라이드"
    if number == 51:
        menu = "본스치킨 크리스피 양념"
    if number == 52:
        menu = "에디슨치킨 양념"
    if number == 53:
        menu = "에디슨치킨 간장"
    if number == 54:
        menu = "에디슨치킨 후라이드"
    if number == 55:
        menu = "에디슨치킨 반반"
    if number == 56:
        menu = "호식이 간장"
    if number == 57:
        menu = "호식이 후라이드"
    if number == 58:
        menu = "호식이 양념"
    if number == 59:
        menu = "호식이 반반"
    if number == 60:
        menu = "땅땅치킨 매콤찹스"
    if number == 61:
        menu = "땅땅치킨 로얄양념치킨"
    if number == 62:
        menu = "땅땅치킨 건강한 허브봉"
    if number == 63:
        menu = "땅땅치킨 후왕"
    if number == 64:
        menu = "땅땅치킨 땅땅불갈비"
    if number == 65:
        menu = "땅땅치킨 T 후라이드"
    if number == 66:
        menu = "땅땅치킨 서울치킨"
    if number == 67:
        menu = "땅땅치킨 핫홀릭치킨"
    if number == 68:
        menu = "땅땅치킨 허브순살치킨"
    if number == 69:
        menu = "땅땅치킨 독도애치킨"
    if number == 70:
        menu = "땅땅치킨 불골드윙"
    if number == 71:
        menu = "땅땅치킨 미운오리바비큐"
    if number == 72:
        menu = "네네치킨 양념치킨"
    if number == 73:
        menu = "네네치킨 후라이드치킨"
    if number == 74:
        menu = "네네치킨 스노윙치킨"
    if number == 75:
        menu = "네네치킨 크리미언치킨"
    if number == 76:
        menu = "네네치킨 핫블링치킨"
    if number == 77:
        menu = "네네치킨 오리엔탈 파닭"
    if number == 78:
        menu = "네네치킨 반반치킨"
    if number == 79:
        menu = "네네치킨 쇼킹핫치킨"
    if number == 80:
        menu = "네네치킨 후닭"
    if number == 81:
        menu = "네네치킨 소이갈릭치킨"
    if number == 82:
        menu = "네네치킨 마늘치킨"
    if number == 83:
        menu = "또래오래 엔젤치킨"
    if number == 84:
        menu = "또래오래 핫 양념치킨"
    if number == 85:
        menu = "또래오래 리얼핫 양념치킨"
    if number == 86:
        menu = "또래오래 양념치킨"
    if number == 87:
        menu = "또래오래 마왕치킨"
    if number == 88:
        menu = "또래오래 갈릭반핫양념반 치킨"
    if number == 89:
        menu = "또래오래 순살치킨"
    if number == 90:
        menu = "또래오래 어메이찡"
    if number == 91:
        menu = "또래오래 메이플치킨"
    if number == 92:
        menu = "또래오래 반반치킨"
    if number == 93:
        menu = "또래오래 후라이드치킨"
    if number == 94:
        menu = "또래오래 양념치킨"
    if number == 95:
        menu = "또래오래 순살파닭"
    if number == 96:
        menu = "또래오래 바베큐치킨"
    if number == 97:
        menu = "또래오래 목우촌 그릴윙"

    return menu
