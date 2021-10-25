# Django Response

## 1. JsonResponse

- `JsonResponse`객체에 데이터를 인자로 담는다.
- 데이터가 딕셔너리가 아니면 `safe=False` 인자를 추가로 넣어야한다.

## Serialization

- **직렬화**
- 데이터 구조나 객체 상태를 동일하거나 다른컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- Serializers in Django
  - Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어줌.

## 2. Django Serializer

- Django 내장 HttpResponse 활용한 JSON 응답 객체

- ```python
  # articles/views.py
  
  from django.http.response import JsonResponse, HttpResponse
  from django.core import serializers
  
  def articles_json2(request):
      articles = Article.objects.all()
      data = serializers.serialize('json', articles)
      return HttpResponse(data, content_type='application/json')
  ```

- 



## 3. Django REST framework 라이브러리(DRF)

- `$ pip install djangorestframework`

- `ModelSerializer` : 모델에 맞춰 자동으로 필드 생성해 serialize해줌

- ```python
  # articles/serializers.py
  
  from rest_framework import serializers
  from .models import Article
  
  class ArticleSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Article
          fields = '__all__'
  
  ```
  
- ```python
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  from .serializers import ArticleSerializer 
  
  # @api_view(['GET'])
  @api_view()
  def article_json_3(request):
      articles = Article.objects.all()
      serializer = ArticleSerializer(articles, many=True)
      return Response(serializer.data)
  ```

- `many=True` : QuerySet 등은 직렬화할 때 필요한 키워드 인자

- DRF의 Response()로 JSON 객체 응답

  - `status` : Response 시 status code를 반환해야함. `status` 모듈에 status code 집합이 포함되어있음

- `raise_exception=True` : serializer 유효성 검사 시 `is_valid()`에 인자로 넣어 유효성 검사 오류 시 예외 발생. 기본적으로 400 반환

## DRF

- Web API 구축을 위한 강력한 Toolkit 제공 라이브러리
- DRF Serializer는 Django의 Form, Model Form클래스와 유사하게 구성 및 작동
- DJango vs DRF
  - Response : HTML vs JSON
  - Model : ModelForm vs serializer

