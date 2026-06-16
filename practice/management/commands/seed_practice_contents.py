from django.core.management.base import BaseCommand
from practice.models import PracticeContent, PracticeProgress


LESSONS = [{'slug': 'function-view-render-basic',
  'order': 1,
  'title': '関数ベースView（1）renderの基本',
  'concept': '関数ベースView',
  'summary': 'requestを受け取り、render()でHTMLを返す最も基本的なViewを練習します。',
  'explanation': 'DjangoのViewは、ブラウザから送られてきたrequestを受け取り、HTMLなどのレスポンスを返す場所です。関数ベースViewは普通のPython関数として書けるため、最初に処理の流れを理解しやすい形です。画面を表示する場合は、django.shortcutsからrenderをimportし、return '
                 'render(request, "テンプレート名") の形で返します。',
  'practice_task': 'home関数を完成させてください。\n'
                   '\n'
                   '必要な条件:\n'
                   '1. render()でrequestと"practice/home.html"を返す。',
  'starter_code': 'from django.shortcuts import render\n\n\ndef home(request):\n    pass\n',
  'sample_solution': 'from django.shortcuts import render\n'
                     '\n'
                     '\n'
                     'def home(request):\n'
                     '    return render(request, "practice/home.html")\n',
  'required_patterns': 'from\\s+django\\.shortcuts\\s+import\\s+render\n'
                       'def\\s+home\\s*\\(\\s*request\\s*\\)\\s*:\n'
                       'return\\s+render\\s*\\(\\s*request\\s*,\\s*["\']practice/home\\.html["\']\\s*\\)'},
 {'slug': 'function-view-context-basic',
  'order': 2,
  'title': '関数ベースView（2）contextを渡す',
  'concept': 'context',
  'summary': 'Viewで作った辞書データをHTMLテンプレートに渡す基本を練習します。',
  'explanation': 'contextは、Viewからテンプレートへ渡す辞書型のデータです。例えば {"title": "Django練習"} を渡すと、HTML側では {{ title }} '
                 'のように表示できます。Viewは画面を返すだけでなく、画面に必要なデータを準備する役割も持ちます。',
  'practice_task': 'home関数にcontextを追加してください。\n'
                   '\n'
                   '必要な条件:\n'
                   '1. contextという辞書にtitleというキーを入れる。\n'
                   '2. titleのデータには、好きなページ名前を書く。\n'
                   '3. render()の第三引数としてcontextを渡す。',
  'starter_code': 'from django.shortcuts import render\n'
                  '\n'
                  '\n'
                  'def home(request):\n'
                  '    context = {}\n'
                  '    return render(request, "practice/home.html")\n',
  'sample_solution': 'from django.shortcuts import render\n'
                     '\n'
                     '\n'
                     'def home(request):\n'
                     '    context = {"title": "Django練習ページ"}\n'
                     '    return render(request, "practice/home.html", context)\n',
  'required_patterns': 'context\\s*=\\s*\\{[^}]*["\']title["\']\\s*:\\s*["\'][^"\']+["\'][^}]*\\}\n'
                       'return\\s+render\\s*\\(\\s*request\\s*,\\s*["\']practice/home\\.html["\']\\s*,\\s*context\\s*\\)'},
 {'slug': 'template-variable-basic',
  'order': 3,
  'title': 'テンプレート構文（1）変数を表示する',
  'concept': 'テンプレート変数',
  'summary': 'HTMLテンプレートでPython側から渡された値を表示する練習です。',
  'explanation': 'Djangoテンプレートでは、contextで渡された値を {{ 変数名 }} '
                 'の形で表示します。これはPythonコードを直接HTMLに書いているのではなく、Djangoテンプレート専用の書き方です。まずはh1やpタグの中で変数を表示する基本を覚えます。',
  'practice_task': 'HTMLテンプレートを完成させてください。\n\n必要な条件:\n1. h1タグの中でtitleを表示する。\n2. pタグの中でmessageを表示する。',
  'starter_code': '<h1></h1>\n<p></p>\n',
  'sample_solution': '<h1>{{ title }}</h1>\n<p>{{ message }}</p>\n',
  'required_patterns': '<h1>\\s*\\{\\{\\s*title\\s*\\}\\}\\s*</h1>\n<p>\\s*\\{\\{\\s*message\\s*\\}\\}\\s*</p>'},
 {'slug': 'template-for-basic',
  'order': 4,
  'title': 'テンプレート構文（2）for文で繰り返す',
  'concept': 'for文',
  'summary': 'テンプレート内でリストを繰り返し表示する基本を練習します。',
  'explanation': 'リストの内容を画面に並べたいときは、テンプレート内で {% for item in items %} を使います。for文の中で {{ item }} を表示し、最後に {% endfor %} '
                 'で閉じます。HTMLのul/liタグと組み合わせると、リスト表示を作りやすくなります。',
  'practice_task': 'itemsをリスト表示してください。\n'
                   '\n'
                   '必要な条件:\n'
                   '1. itemsをfor文で繰り返す。\n'
                   '2. liタグの中でitemを表示する。\n'
                   '3. endforで閉じる。',
  'starter_code': '<ul>\n  <li></li>\n</ul>\n',
  'sample_solution': '<ul>\n{% for item in items %}\n  <li>{{ item }}</li>\n{% endfor %}\n</ul>\n',
  'required_patterns': '<ul>\n'
                       '\\{%\\s*for\\s+item\\s+in\\s+items\\s*%\\}\n'
                       '<li>\\s*\\{\\{\\s*item\\s*\\}\\}\\s*</li>\n'
                       '\\{%\\s*endfor\\s*%\\}\n'
                       '</ul>'},
 {'slug': 'template-if-empty-basic',
  'order': 5,
  'title': 'テンプレート構文（3）if文とemptyを使う',
  'concept': 'if・empty',
  'summary': '条件分岐とデータがない場合の表示を練習します。',
  'explanation': 'テンプレートでは {% if 条件 %} を使って表示を切り替えられます。また、for文には {% empty %} '
                 'という便利な構文があります。リストが空の場合だけ表示したいメッセージを書くときに使います。',
  'practice_task': 'lessonsを表示するテンプレートを書いてください。\n'
                   '\n'
                   '必要な条件:\n'
                   '1. lessonsをfor文で繰り返す。\n'
                   '2. 各lessonについて、is_openがTrueのときだけlesson.nameをliで表示する。(if, endifを利用)\n'
                   '3. lessonsが空の場合(empty)は「データが存在しません。」とliで表示する。\n'
                   '4. endforで閉じる。',
  'starter_code': '<ul>\n</ul>\n',
  'sample_solution': '<ul>\n'
                     '{% for lesson in lessons %}\n'
                     '  {% if lesson.is_open %}\n'
                     '    <li>{{ lesson.name }}</li>\n'
                     '  {% endif %}\n'
                     '{% empty %}\n'
                     '  <li>データが存在しません。</li>\n'
                     '{% endfor %}\n'
                     '</ul>\n',
  'required_patterns': '\\{%\\s*for\\s+lesson\\s+in\\s+lessons\\s*%\\}\n'
                       '\\{%\\s*if\\s+lesson\\.is_open\\s*%\\}\n'
                       '<li>\\s*\\{\\{\\s*lesson\\.name\\s*\\}\\}\\s*</li>\n'
                       '\\{%\\s*endif\\s*%\\}\n'
                       '\\{%\\s*empty\\s*%\\}\n'
                       'データが存在しません。\n'
                       '\\{%\\s*endfor\\s*%\\}'},
 {'slug': 'templateview-basic',
  'order': 6,
  'title': 'TemplateView（1）ページを表示する',
  'concept': 'TemplateView',
  'summary': 'TemplateViewを使って、テンプレート表示中心のページを作る基本を練習します。',
  'explanation': 'TemplateViewは、HTMLテンプレートを表示するための汎用Viewです。単純な説明ページやトップページのように、複雑な処理が少ないページで便利です。TemplateViewを継承したクラスを作り、template_nameに表示したいHTMLのパスを書きます。',
  'practice_task': 'AboutViewを完成させてください。\n'
                   '\n'
                   '必要な条件:\n'
                   '1. AboutViewクラスがTemplateViewを継承させる。\n'
                   '2. template_nameにpractice/about.htmlを指定する。',
  'starter_code': 'from django.views.generic import TemplateView\n\n\nclass AboutView():\n    pass\n',
  'sample_solution': 'from django.views.generic import TemplateView\n'
                     '\n'
                     '\n'
                     'class AboutView(TemplateView):\n'
                     '    template_name = "practice/about.html"\n',
  'required_patterns': 'from\\s+django\\.views\\.generic\\s+import\\s+TemplateView\n'
                       'class\\s+AboutView\\s*\\(\\s*TemplateView\\s*\\)\\s*:\n'
                       'template_name\\s*=\\s*["\']practice/about\\.html["\']'},
 {'slug': 'templateview-context',
  'order': 7,
  'title': 'TemplateView（2）get_context_dataを使う',
  'concept': 'get_context_data',
  'summary': 'TemplateViewからテンプレートへ追加データを渡す方法を練習します。',
  'explanation': 'TemplateViewでテンプレートに値を渡したい場合は、get_context_data()を上書きします。まずsuper().get_context_data(**kwargs)で元のcontextを取得し、その辞書に値を追加してreturnします。',
  'practice_task': 'AboutViewにget_context_dataを追加してください。\n'
                   '\n'
                   '必要な条件:\n'
                   '1. get_context_data(self, **kwargs)メソッドを定義する。\n'
                   '2. super().get_context_data(**kwargs)を呼び出す。\n'
                   '3. contextにpage_titleを追加する。データは好きなページ名を入力する。\n'
                   '4. contextをreturnする。',
  'starter_code': 'from django.views.generic import TemplateView\n'
                  '\n'
                  '\n'
                  'class AboutView(TemplateView):\n'
                  '    template_name = "practice/about.html"\n',
  'sample_solution': 'from django.views.generic import TemplateView\n'
                     '\n'
                     '\n'
                     'class AboutView(TemplateView):\n'
                     '    template_name = "practice/about.html"\n'
                     '\n'
                     '    def get_context_data(self, **kwargs):\n'
                     '        context = super().get_context_data(**kwargs)\n'
                     '        context["page_title"] = "TemplateViewの練習"\n'
                     '        return context\n',
  'required_patterns': 'def\\s+get_context_data\\s*\\(\\s*self\\s*,\\s*\\*\\*kwargs\\s*\\)\\s*:\n'
                       'context\\s*=\\s*super\\s*\\(\\s*\\)\\.get_context_data\\s*\\(\\s*\\*\\*kwargs\\s*\\)\n'
                       'context\\s*\\[\\s*["\']page_title["\']\\s*\\]\\s*=\\s*["\'][^"\']+["\']\n'
                       'return\\s+context'},
 {'slug': 'templateview-url',
  'order': 8,
  'title': 'TemplateView（3）urls.pyに接続する',
  'concept': 'as_view',
  'summary': 'TemplateViewのクラスをURLに接続する基本を練習します。',
  'explanation': 'クラスベースViewは、そのままURLに渡すのではなく、as_view()を呼び出してView関数として使える形にします。urls.pyでは path("about/", '
                 'AboutView.as_view(), name="about") のように書きます。',
  'practice_task': 'AboutViewをURLに接続してください。\n'
                   '\n'
                   '必要な条件:\n'
                   '1. AboutViewをimportする。\n'
                   '2. urlpatternsにpathを追加する。\n'
                   '3. "about/" にAboutView.as_view()を接続する。\n'
                   '4. name="about"を付ける。',
  'starter_code': 'from django.urls import path\nfrom .views import AboutView\n\nurlpatterns = [\n]\n',
  'sample_solution': 'from django.urls import path\n'
                     'from .views import AboutView\n'
                     '\n'
                     'urlpatterns = [\n'
                     '    path("about/", AboutView.as_view(), name="about"),\n'
                     ']\n',
  'required_patterns': 'from\\s+django\\.urls\\s+import\\s+path\n'
                       'from\\s+\\.views\\s+import\\s+AboutView\n'
                       'urlpatterns\\s*=\\s*\\[\n'
                       'path\\s*\\(\\s*["\']about/["\']\\s*,\\s*AboutView\\.as_view\\s*\\(\\s*\\)\\s*,\\s*name\\s*=\\s*["\']about["\']\\s*\\)'},
 {'slug': 'view-class-get-basic',
  'order': 9,
  'title': 'Viewクラス（1）getで表示する',
  'concept': 'Viewクラス',
  'summary': 'Viewクラスを使ってGETアクセス時の表示処理を書く基本を練習します。',
  'explanation': 'django.viewsのViewクラスを継承すると、HTTPメソッドごとに処理を書けます。GETアクセスの処理はget(self, '
                 'request)に書きます。関数ベースViewよりも処理を整理しやすくなります。',
  'practice_task': 'ProfileViewのget処理を書いてください。\n'
                   '\n'
                   '必要な条件:\n'
                   '1. get(self, request)を定義する。\n'
                   '2. requestと"practice/profile.html"をrenderで返す。',
  'starter_code': 'from django.views import View\n'
                  'from django.shortcuts import render\n'
                  '\n'
                  '\n'
                  'class ProfileView(View):\n'
                  '    pass\n',
  'sample_solution': 'from django.views import View\n'
                     'from django.shortcuts import render\n'
                     '\n'
                     '\n'
                     'class ProfileView(View):\n'
                     '    def get(self, request):\n'
                     '        return render(request, "practice/profile.html")\n',
  'required_patterns': 'from\\s+django\\.views\\s+import\\s+View\n'
                       'from\\s+django\\.shortcuts\\s+import\\s+render\n'
                       'class\\s+ProfileView\\s*\\(\\s*View\\s*\\)\\s*:\n'
                       'def\\s+get\\s*\\(\\s*self\\s*,\\s*request\\s*\\)\\s*:\n'
                       'return\\s+render\\s*\\(\\s*request\\s*,\\s*["\']practice/profile\\.html["\']\\s*\\)'},
 {'slug': 'view-class-post-basic',
  'order': 10,
  'title': 'Viewクラス（2）postで送信を受け取る',
  'concept': 'postメソッド',
  'summary': 'GETとPOSTを別々のメソッドで扱う基本を練習します。',
  'explanation': 'フォーム送信などのPOSTリクエストはpost(self, request)に書きます。get()は画面表示、post()は送信処理というように分けると、コードの役割が読みやすくなります。',
  'practice_task': 'ProfileViewにpost処理を追加してください。\n'
                   '\n'
                   '必要な条件:\n'
                   '1. post(self, request)を定義する。\n'
                   '2. context辞書を作成する。\n'
                   '3. キーで"submitted"、データでTrueを入れる。\n'
                   '4. requestと"practice/profile.html"をrenderで返す。'
                   '5. renderの第三引数にcontextを渡す。',
  'starter_code': 'from django.views import View\n'
                  'from django.shortcuts import render\n'
                  '\n'
                  '\n'
                  'class ProfileView(View):\n'
                  '    def get(self, request):\n'
                  '        return render(request, "practice/profile.html")\n',
  'sample_solution': 'from django.views import View\n'
                     'from django.shortcuts import render\n'
                     '\n'
                     '\n'
                     'class ProfileView(View):\n'
                     '    def get(self, request):\n'
                     '        return render(request, "practice/profile.html")\n'
                     '\n'
                     '    def post(self, request):\n'
                     '        context = {"submitted": True}\n'
                     '        return render(request, "practice/profile.html", context)\n',
  'required_patterns': 'def\\s+post\\s*\\(\\s*self\\s*,\\s*request\\s*\\)\\s*:\n'
                       'context\\s*=\\s*\\{[^}]*["\']submitted["\']\\s*:\\s*True[^}]*\\}\n'
                       'return\\s+render\\s*\\(\\s*request\\s*,\\s*["\']practice/profile\\.html["\']\\s*,\\s*context\\s*\\)'},
 {'slug': 'forms-form-class',
  'order': 11,
  'title': 'forms（1）Formクラスを作る',
  'concept': 'forms.Form',
  'summary': 'forms.Formを継承して入力フォームの項目を定義する練習です。',
  'explanation': 'Djangoのformsを使うと、入力項目やバリデーションをPython側で管理できます。forms.Formを継承したクラスを作り、その中にCharFieldなどのフィールドを書きます。',
  'practice_task': 'MessageFormを作ってください。\n'
                   '\n'
                   '必要な条件:\n'
                   '1. MessageFormクラスにforms.Formを継承させる。\n'
                   '2. messageをforms.CharFieldで定義する。\n'
                   '3. labelは"メッセージ"で指定する。\n'
                   '4. max_lengthは100で指定する。',
  'starter_code': 'from django import forms\n\n\nclass MessageForm():\n    pass\n',
  'sample_solution': 'from django import forms\n'
                     '\n'
                     '\n'
                     'class MessageForm(forms.Form):\n'
                     '    message = forms.CharField(label="メッセージ", max_length=100)\n',
  'required_patterns': 'from\\s+django\\s+import\\s+forms\n'
                       'class\\s+MessageForm\\s*\\(\\s*forms\\.Form\\s*\\)\\s*:\n'
                       'message\\s*=\\s*forms\\.CharField\\s*\\([^)]*label\\s*=\\s*["\']メッセージ["\'][^)]*max_length\\s*=\\s*100[^)]*\\)'},
 {'slug': 'forms-view-get',
  'order': 12,
  'title': 'forms（2）GETで空のフォームを表示する',
  'concept': 'フォーム表示',
  'summary': 'Viewのget処理で空のフォームを作り、テンプレートに渡す練習です。',
  'explanation': 'フォームページでは、最初にアクセスしたときに空のフォームを表示します。get()の中で form = MessageForm() を作り、そのフォームをcontext辞書に入れてテンプレートへ渡します。contextを使うことで、テンプレート側では {{ form }} のようにフォームを表示できます。',
  'practice_task': 'MessageViewのget処理を書いてください。\n'
                   '\n'
                   '必要な条件:\n'
                   '1. get(self, request)を定義する。\n'
                   '2. MessageForm()で空のformを作る。\n'
                   '3. contextという辞書を作成する。\n'
                   '4. contextのキーには"form"を、データにはformを入れる。\n'
                   '5. requestと"practice/message.html"をrenderで返す。\n'
                   '6. renderの第三引数にcontextを渡す。',
  'starter_code': 'from django.views import View\n'
                  'from django.shortcuts import render\n'
                  '\n'
                  'from .forms import MessageForm\n'
                  '\n'
                  '\n'
                  'class MessageView(View):\n'
                  '    pass\n',
  'sample_solution': 'from django.views import View\n'
                     'from django.shortcuts import render\n'
                     '\n'
                     'from .forms import MessageForm\n'
                     '\n'
                     '\n'
                     'class MessageView(View):\n'
                     '    def get(self, request):\n'
                     '        form = MessageForm()\n'
                     '        context = {"form": form}\n'
                     '        return render(request, "practice/message.html", context)\n',
  'required_patterns': 'class\\s+MessageView\\s*\\(\\s*View\\s*\\)\\s*:\n'
                       'def\\s+get\\s*\\(\\s*self\\s*,\\s*request\\s*\\)\\s*:\n'
                       'form\\s*=\\s*MessageForm\\s*\\(\\s*\\)\n'
                       'context\\s*=\\s*\\{\\s*["\\\']form["\\\']\\s*:\\s*form\\s*\\}\n'
                       'return\\s+render\\s*\\(\\s*request\\s*,\\s*["\\\']practice/message\\.html["\\\']\\s*,\\s*context\\s*\\)'},
 {'slug': 'forms-view-post',
  'order': 13,
  'title': 'forms（3）POSTで入力を検証して結果を渡す',
  'concept': 'is_valid・cleaned_data',
  'summary': 'POSTされたデータをFormに渡し、検証済みの入力内容をcontextで画面に返す練習です。',
  'explanation': 'POST処理では、request.POSTをフォームクラスに渡して、送信された入力内容を受け取ります。その後、form.is_valid()で入力内容が正しいか確認します。正しい場合だけcleaned_dataから安全に値を取り出せます。取り出したmessageはcontextに追加することで、テンプレート側に表示用データとして渡せます。',
  'practice_task': 'MessageViewにpost処理を追加してください。\n'
                   '\n'
                   '必要な条件:\n'
                   '1. post(self, request)を定義する。\n'
                   '2. MessageForm(request.POST)で送信内容を受け取るformを作る。\n'
                   '3. contextという辞書を作成し、キー"form"にデータformを入れる。\n'
                   '4. if文でform.is_valid()を確認する。\n'
                   '5. 条件がTrueの場合、form.cleaned_data["message"]をmessage変数に入れる。\n'
                   '6. 条件がTrueの場合、contextの"message"にmessageを入れる。\n'
                   '7. requestと"practice/message.html"をrenderで返す。\n'
                   '8. renderの第三引数にcontextを渡す。',
  'starter_code': 'class MessageView(View):\n',
  'sample_solution': 'class MessageView(View):\n'
                     '    def post(self, request):\n'
                     '        form = MessageForm(request.POST)\n'
                     '        context = {"form": form}\n'
                     '        if form.is_valid():\n'
                     '            message = form.cleaned_data["message"]\n'
                     '            context["message"] = message\n'
                     '        return render(request, "practice/message.html", context)\n',
  'required_patterns': 'def\\s+post\\s*\\(\\s*self\\s*,\\s*request\\s*\\)\\s*:\n'
                       'form\\s*=\\s*MessageForm\\s*\\(\\s*request\\.POST\\s*\\)\n'
                       'context\\s*=\\s*\\{\\s*["\\\']form["\\\']\\s*:\\s*form\\s*\\}\n'
                       'if\\s+form\\.is_valid\\s*\\(\\s*\\)\\s*:\n'
                       'message\\s*=\\s*form\\.cleaned_data\\s*\\[\\s*["\\\']message["\\\']\\s*\\]\n'
                       'context\\s*\\[\\s*["\\\']message["\\\']\\s*\\]\\s*=\\s*message\n'
                       'return\\s+render\\s*\\(\\s*request\\s*,\\s*["\\\']practice/message\\.html["\\\']\\s*,\\s*context\\s*\\)'}]


class Command(BaseCommand):
    help = "Create or update practice contents for the Django training app."

    def handle(self, *args, **options):
        for item in LESSONS:
            content, created = PracticeContent.objects.update_or_create(
                slug=item["slug"],
                defaults={
                    "order": item["order"],
                    "title": item["title"],
                    "concept": item["concept"],
                    "summary": item["summary"],
                    "explanation": item["explanation"],
                    "practice_task": item["practice_task"],
                    "starter_code": item["starter_code"],
                    "sample_solution": item["sample_solution"],
                    "required_patterns": item["required_patterns"],
                },
            )
            PracticeProgress.objects.get_or_create(content=content)
            action = "created" if created else "updated"
            self.stdout.write(self.style.SUCCESS(f"{content.order}. {content.title} {action}"))
