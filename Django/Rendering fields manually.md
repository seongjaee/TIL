# Rendering fields manually

- Form을 직접 작성하기

- [django-docs #rendering-fields-manually](https://docs.djangoproject.com/en/3.2/topics/forms/#rendering-fields-manually)

- `{{ form.name_of_field }}` 식으로 필드의 속성을 꺼내서 쓸 수 있음. 

- ```html
  {% for field in form %}
    {{ field.errors }}
    {{ field.label_tags }}
    {{ field }}
  {% endfor %}
  ```

  식으로 loop를 이용할 수 도 있음

- `{{ field }}` 의 속성에는

  - `.label`
  - `.label_tag`
  - `id_for_label`
  - `value`
  - `html_name`
  - `help_text`
  - `errors`
  - `is_hidden`
  - `field` 들이 있음.



## Bootstrap과 함께 사용

- django-bootstrap v5 : form class에 bootstrap 적용시켜주는 라이브러리
- `$ pip install django-bootstrap-v5`
- `settings.py` , `INSTALLED_APPS` 에 `'bootstrap5'` 추가
- 사용
  - `base.html` 최상단 `{% load bootstrap5 %}`
  - css cdn 붙이는 곳에 `{% bootstrap_css %}`
  - javascript cdn 붙이는 곳에 `{% bootstrap_javascript %}`
  - 각 템플릿 html 에 extends 밑에 `{% load bootstrap5 %}`
  - `{% bootstrap_form form %}` 으로 form

