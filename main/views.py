import random
import urllib.parse
from datetime import date, datetime

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .models import Book


def index(request):
    return HttpResponse('こんにちは、世界！')


def temp(request):
    context = {'msg': 'こんにちは、世界！'}
    return render(request, 'main/temp.html', context)


def list(request):
    books = Book.objects.all()
    return render(request, 'main/list.html', {
        'books': books
    })


def iftag(request):
    return render(request, 'main/iftag.html', {
        'random': random.randint(0, 100)
    })


def yesno(request):
    return render(request, 'main/yesno.html', {
        'flag': None
    })


def firstof(request):
    return render(request, 'main/firstof.html', {
        # 'a': 'おはよう',
        # 'b': 'こんにちは',
        'c': 'こんばんは',
    })


def forloop(request):
    return render(request, 'main/forloop.html', {
        'weeks': ['月', '火', '水', '木', '金', '土', '日']
    })


def forempty(request):
    return render(request, 'main/forempty.html', {
        # 'members': ['鈴木', '佐藤', '山田']
    })


def escape(request):
    return render(request, 'main/escape.html', {
        'msg': '''<img src="https://wings.msn.to/image/wings.jpg" title="logo" />
        <p>WINGSへようこそ</p>'''
    })


def master(request):
    return render(request, 'main/master.html', {
        'msg': 'こんにちは、世界！',
    })


def include(request):
    return render(request, 'main/include.html', {
        'name': '鈴木',
        'current': datetime.datetime.now(),
    })


def date_time(request):
    return render(request, 'main/date_time.html', {
        'today': datetime.now()
    })


def filter(request):
    books = Book.objects.filter(publisher='翔泳社', price=3300)

    # price__gt より大きい
    # price__gte 以上
    # price__lt 未満
    # price__lte 以下
    books = Book.objects.filter(price__lt=3000)

    # LIKE
    # contains 部分一致
    # startswith 前方一致
    # endswith 後方一致
    books = Book.objects.filter(title__contains='独習')

    # 大文字小文字を区別しない完全一致
    books = Book.objects.filter(title__iexact='aaa')

    # 正規表現比較
    books = Book.objects.filter(title__regex=r'[0-9]+')

    # NULL比較
    books = Book.objects.filter(title__isnull=True)

    # 範囲比較
    books = Book.objects.filter(published__range=(date(2018, 1, 1), date(2020, 12, 31)))

    # 候補比較(IN)
    books = Book.objects.filter(publisher__in=['翔泳社', '技術評論社', '日経BP'])

    # データの並び替え(order by)
    books = Book.objects.order_by('publisher', '-published')

    # 取得フィールドの制約
    books = Book.objects.values('title', 'price')

    # 他にも色々ある...

    return render(request, 'main/book_list.html', {
        'books': books
    })


def exclude(request):
    books = Book.objects.exclude(publisher='翔泳社')
    return render(request, 'main/book_list.html', {
        'books': books
    })


def get(request):
    book = Book.objects.get(pk=1)
    return render(request, 'main/book_detail.html', {
        'book': book
    })


def groupby(request):
    # その他主な集計関数
    # Avg
    # Max
    # Min
    # Sum

    return render(request, 'main/groupby.html', {
        'groups': Book.objects.values('publisher').annotate(pub_count=Count('publisher')).order_by('-pub_count')
    })


def union(request):
    # 複数の結果セットを結合する
    # union 和集合
    # intersection 積集合
    # difference 差集合

    b1 = Book.objects.filter(publisher='翔泳社')
    b2 = Book.objects.filter(publisher='技術評論社')
    return render(request, 'main/list.html', {
        'books': b1.union(b2)
    })


def raw(request):
    # 生のSQLを発行する

    books = Book.objects.raw(
        'SELECT * FROM main_book WHERE publisher = %s', ['翔泳社']
    )
    return render(request, 'main/book_list.html', {
        'books': books
    })


def rel(request):
    return render(request, 'main/rel.html', {
        'book': Book.objects.get(pk=1)
    })


def rel2(request):
    return render(request, 'main/rel2.html', {
        'books': Book.objects.all()
    })


def route_param(request, id=1):
    return HttpResponse(f'id値: {id}')


def req_query(request):
    return HttpResponse(f'id値: {request.GET["id"]}')


def req_header(request):
    return HttpResponse(f'Use-Agent: {request.headers["User-Agent"]}')


def req_redirect(request):
    return redirect('list')


def setcookie(request):
    response = HttpResponse(render(request, 'main/setcookie.html'))
    response.set_cookie('app_title',
                        urllib.parse.quote('速習Django'), 60 * 60 * 24 * 30)
    return response


def getcookie(request):
    app_title = urllib.parse.unquote(request.COOKIES['app_title']) if 'app_title' in request.COOKIES else '-'
    return render(request, 'main/getcookie.html', {
        'app_title': app_title
    })


def setsession(request):
    request.session['app_title'] = '速習Django'
    return HttpResponse('セッションを保存しました。')


def getsession(request):
    # title = request.session['app_title'] if 'app_title' in request.session else '-'
    title = request.get('app_title', '-')
    return HttpResponse(title)


class MyTemplateView(TemplateView):
    template_name = 'main/temp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = 'Hello, World!'
        return context
