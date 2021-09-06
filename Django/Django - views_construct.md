# Django - views_create

## 코드

```python
# articles/views/py

from django.shortcuts import render, redirect
from .forms import ArticleForm


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```



## 질문

> create() 함수 첫번째 라인, 왜 `request.method == 'POST'`를 먼저해야할까
>
> update() 도 마찬가지.



## 답변

- GET을 먼저 분기했을 때, GET이 아닌 다른 모든 요청에 대해 POST와 같은 작업을 수행하게 됨. 즉, PUT, PATCH 등의 요청이 와도 DB를 수정하는 작업을 하게 됨.
- 처음과 같이 POST를 먼저 분기하는 이유는 DB를 수정하게 되는 작업은 POST 요청이 왔을 때만 수행하기 위해서임.

