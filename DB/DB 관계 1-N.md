# DB 관계 1 : N

## Model Relationship

- RDBMS

## Foreign Key

- 외래 키
- 관계형 DB에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블에서 1개의 키에 해당하고, 이는 **참조되는 테이블의 기본 키**를 가리킴
- 참조하는 테이블의 행 1개의 값은 참조되는 테이블의 행 값에 대응
  - 참조되는 테이블에 나타나지 않는  값을 포함할 수 없음
- 참조하는 테이블의 여러 행이, 참조되는 테이블의 동일한 행을 참조할 수 있음(1:N)

## Foreign Key 특징

- 키를 사용하여 부모 테이블의 유일한 값을 참조(참조 무결성)
- 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야함.
- 참조 무결성
  - 관련된 2개의 테이블간의 일관성
  - 외래 키가 선언된 테이블의 외래키  속성 값은 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야함
- 데이터 무결성
  - 데이터의 정확성과 일관성 유지 보증하는 중요한 기능
  - 무결성 제한의 유형
    - 개체 무결성
    - 참조 무결성
    - 범위(도메인) 무결성

## ForiegnKey field

- A many-to-one relationship
- 2개의 위치 인자 필요
  1. 참조하는 model class
  2. on_delete 옵션
     - `on_delete` : 외래 키가 참조하는 객체가 삭제되면 외래 키를 가진 객체를 어떻게 처리할지
     - 데이터 무결성을 위한 매우 중요한 설정
       - CASCADE : 부모 객체 삭제 시 참조하는 객체도 삭제
       - 
- migrate 작업 시 필드 이름에 _id를 추가하여 DB 열 이름을 만듦

- comment 모델 정의하기

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

### 데이터베이스의 ForeignKeyField 표현

- ForeignKey 인스턴스 변수명_id 로 Field가 만들어짐
- 참조하는 클래스 이름의 소문자 단수형으로 작성하는게 바람직



### 1:N 관계 related manager

- 역참조
  - Article(1) -> Comment(N)
  - `article.comment` 형태로 사용 불가. `article.comment_set` manager 생성됨.
  - 게시글에 몇 개의 댓글이 작성되었는지 Django ORM이 보장 불가
    - comment가 없을 수도 있음
    - **애초에 실제 Article 클래스에는 Comment와의 어떤 관계도 작성되지 않음!**
- 참조
  - Comment(N) -> Article(1)
  - 댓글은 반드시 자신이 참조하고 있는 게시글이 있음. 따라서 `comment.article`과 같이 접근 가능
  - 실제 ForeignKeyField 또한 Comment클래스에서 작성됨



### ForeignKey - 'related_name'

- 역참조 시 사용할 이름을 변경할 수 있는 옵션
- `related_name='comments'` 작성 시 `article.comment_set` 가`article.comments`로 대체됨.





## Comment CREATE

### CommentForm 작성

```python
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
```

### detail 페이지에 CommentForm 출력

```python
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

```HTML
<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
</form>
```



### 댓글 작성 로직

```python
def comments_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```

- `save(commit=False)`
  - **DB에 저장하지 않고 인스턴스 객체만 생성**
  - 저장하기 전에 객체에 대한 사용자 지정 처리 수행 시 유용
  - 생략하면 article_id 값이 없어서 저장할 수 없음



## Comment READ

### 댓글 출력

- 특정 article에 있는 모든 댓글 가져온 후 context에 추가

```python
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)
```

```HTML
<h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>{{ comment.content }}</li>
    {% endfor %}
  </ul>
```



## Comment DELETE

```python
urlpatterns = [
    ...,
     path('<int:article_pk>/comments/<int:comment_pk>/delete', views.comments_delete, name='comments_delete'),
]
```

```python
@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

- 명시적인 URL을 위해 article_pk도 가져온다.



## Comment 추가사항

### 댓글 개수 출력

```
{{ comments|length }}
{{ article.comment_set.all|length }}
```