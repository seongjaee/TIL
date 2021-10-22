# Queryset 최적화

DOCUMENT: [https://docs.djangoproject.com/en/3.2/ref/models/querysets/](DOCUMENT: https://docs.djangoproject.com/en/3.2/ref/models/querysets/)

- 게시글이 있으면, 그 게시글에 달린 댓글의 개수와 게시글의 작성자를 인덱스 페이지에 렌더하고 싶다.

  ```python
  # reviews/views.py
  
  def review_index(request):
      reviews = Review.objects.all()
      return render(request, 'articles/index.html', {'reviews': reviews})
  ```

  ```html
  # reviews/index.html
  
  {% for review in reviews %}
  {{ review.author }} - {{ review.comment_set.all|length }}
  ```

- 위와 같은 식으로 만들 수 있다. 게시글-작성자는 N:1관계이므로 정참조를, 게시글-댓글은 1:N관계 이므로 역참조를 하게 된다.

- 하지만 이 과정에서 중복이 일어난다. 모든 article에 대해 정참조와 역참조를 계속 해야한다. 이럴 때 queryset을 이용해 최적화 할 수 있다.

- ```python
  # reviews/views.py
  from django.db.models import Count
  
  def review_index(request):
      reviews = Review.objects\
      			.annotate(comment_count=Count('comment'))\
          		.select_related('author')
      return render(request, 'reviews/index.html', {'reviews': reviews})
  ```

- `annotate` : 추가로 기록

  - Review 테이블을 가져오되, 댓글 개수를 Count 해서 comment_count라는 필드로 추가로 기록하여 가져온다.

- `select_related`: 정참조 때 사용

  - Review 테이블을 가져오되,  Review테이블의 FK를 참조해서 User 테이블의 정보를 합쳐서 가져온다.

- 게시글에 달린 댓글의 작성자를 가져오고 싶을 때는 어떻게 해야할까

  - 게시글에서 댓글을 가져오는 건 역참조, 댓글에서 작성자를 가져오는 건 정참조이다.

  ```python
  Review.objects\
      .prefetch_related(
      	Prefatch(
          	'comment_set',
          	query_set=Comment.objects.select_related('author')
          )
      )
  ```

  - `prefetch_related`: 역참조 때 사용
    - 인자로 lookup을 넣어준다.
    - Prefatch 객체를 사용할 수 있다.
    - Review를 역참조해 Comment를 가져오고 싶으니 Prefatch 객체 lookup 인자에 'comment_set'을 넣는다.
    - Prefatch 객체 query_set인자에는 'comment_set'에서 적용하고 싶은 query를 입력한다. 지금은 Comment에서 작성자를 정참조하고 싶으니 Comment.objects.select_related('author')를 입력한다.