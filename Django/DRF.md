# DRF

## Single Model

### ModelSerializer

- 핵심 기능
  1. 모델 정보에 맞춰 자동으로 필드 생성
  2. serializer에 대한 validation 검사 
  3. `.create()`, `.update()` 의 간단한 기본 구현

```python
# articles/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', )
```

```python
# articles/views.py

from rest_framework.decorator import api_view
from .serializers import ArticleListSerializer

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
```

- 단일 인스턴스 대신 QuerySet 등 직렬화 시, `many=True` 키워드 인자

- `api_view` 데코레이터
  - View 함수가 응답해야할 메서드 목록
  - 필수적으로 작성.



## 1 : N Relation

- Article과 1:N 관계를 갖는 Comment 모델

```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    article = models.ForiegnField(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
```



```python
# articles/serializers.py
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('articles', )
```

```python
# articles/views.py

def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

- `.save()` 메서드에 추가적으로 데이터를 인자로 입력할 수 있음.

- 유효성 검사 시에 댓글이 어떤 게시글에 작성하는 지에 대한 정보(article 필드)를 넘겨주어야함.

  article 필드가 비어있다면 유효성 검사를 통과하지 못함. article필드는 save() 과정에서 인자로 넘겨줄 것임.

  read_only_fields 설정을 통해 해당 필드를 직렬화하지 않고 반환할 때만 필드가 포함되도록 함.

  

### PrimaryKeyRelatedField

- pk를 사용해 관계된 대상을 나타냄

```python
class ArticleListSerializer(serializers.ModelSerializer):
    # 필드가 N 관계를 나타내므로 many=True
    # comment_set 필드값을 직접 입력받지 않으므로 read_only=True
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
```



### Nested relationship

- 참조된 대상은 참조하는 대상의 표현에 포함되거나 중첩될 수 있음
- 이런 중첩 관계를 serializers를 필드로 사용하여 표현

```python
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('articles', )
        

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = serializers.CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
```



### 추가적인 필드

- 특정 게시글의 작성된 댓글을 필드로 추가

```python
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = serializers.CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
```

- `source` 속성으로 필드의 속성값 확인
  - `.count()`는 built-in Queryset API 중 하나
- 이 때 위와 같이 특정 필드를 override 했거나, 추가한 경우 read_only_fields로 사용할 수 없음.  read_only=True를 사용해야함.



## M:N Relation

- Article 모델과 M:N 관계를 갖는 Author 모델
  - 특정 article의 작성자가 여러 명.
  - 하나의 작성자가 여러 article을 작성.

```python
class Author(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    authors  = models.ManyToManyField(Author, related_name='articles')
    title = models.CharField(max_length=100)
```



- 특정 Article의 author를 포함한 세부 정보 직렬화

```python
class ArticleSerializer(serializers.ModelSerializer):
    
    class AuthorSerializer(serialzers.ModelSerializer):
        class Meta:
            model = Author
            fields = ('pk', 'name', )
            
    authors = AuthorSerializer(many=True, read_only=True)
    author_pks = serializers.ListField(write_only=True)
    
    def create(self, validated_data):
        author_pks = validated_data.pop('author_pks')
        article = Article.objects.create(**validated_data)
        
        for author_pk in author_pks:
            article.authors.add(author_pk)
            
        return article
    
    def update(self, instance, validated_data):
        author_pks = validated_data.pop('author_pks')
        
        for attr, value in validated_data.items():
            setattr(article, attr, value)
            article.save()
            
        article.authors.clear()
        
        for author_pk in author_pks:
            article.authors.add(author_pk)
            
        return article
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'authors', 'author_pks')
```

- 특정 article을 조회할 때, 그 세부 정보에 해당 article의 작성자들을 담아야한다. 이를 위한 필드가 `authors` 이다. 
- 작성자들의 pk뿐만 아니라, name까지 담고 싶기 때문에 새로운 Serializer를 내부에서 정의해 직렬화 해준다. 이 필드는 GET요청에 대해서 정보를 반환할 때만 사용할 것이므로 `read_only=True` 인자를 넣어준다.
- 새로운 article을 생성할 때, 해당 article의 author들을 입력해주어야 하는데, 입력받을 필드가 `article_pks`이다. 이 필드는 POST요청에 대해서 정보를 입력할 때만 사용할 것이므로 `write_only=True` 인자를 넣어준다.
- 새로운 필드 `article_pks`를 만들었지만, 실제 Model에는 `article_pks`라는 필드가 없다. 따라서 `author_pks`는 그냥 `save()`메서드로는 저장할 수가 없다. 따라서 `create()`, `update()` 메서드를 따로 override해서 사용한다.
  - save() 메서드는 사실 DB에 새로운 레코드를 저장하는 create 와 기존 값을 Update하는 update로 나누어져 구현되어있다.
- `create()`
  - 유효성 검사가 끝난 후 넘어오는 `validated_data` 에는 `article_pks`가 포함되어있다. 이 값을 제거한 후에 인스턴스를 만든다. 해당 인스턴스에 `article_pks` 에 들어있는 `article_pk`를 넣어준다.
  - 마지막으로 생성한 인스턴스를 반환한다.
- `update()`
  - `create()` 와 달리 한번에 갱신할 방법이 없다.
  - `validated_data` 에서 속성과 값을 순회하면서 하나씩 instance의 속성을 갱신한다.
  - author의 경우 기존 author 정보를 clear 해준 후, 새롭게 add 해준다.
  - 마지막으로 생성한 인스턴스를 반환한다.

