# Django Form

## Django Form Class

- 사용자로부터 데이터를 입력받는 방법에는 HTML form, input이 있었다.
- 사용자의 데이터를 받아서 **데이터의 유효성 검증**, 필요시 입력된 데이터를 검증 결과와 함께 다시 표시 등 유효한 데이터에 대해 요구되는 동작을 **올바르게** 수행하는 작업은 꽤 까다로움.
- Django Form을 이용하면 이 작업을 쉽게 할 수 있음.



### Django forms

- Form은 Django 프로젝트의 **주요 유효성 검사** 도구들 중 하나.
- 공격 및 우연한 데이터 손상에 대한 중요한 방어수단
- Django에서는 form 기능의 방대한 부분을 단순화, 자동화 하여 프로그래머가 직접 작성한 코드에서 수행할 수 있는 것 보다 더 안전하게 수행.
- Form에 관련된 작업
  - 렌더링을 위한 데이터 준비 및 재구성
  - 데이터에 대한 HTML forms 생성
  - 클라이언트로부터 받은 데이터 수신 및 처리



### Form Class

- form 내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않은 field에 관련된 에러 메시지 결정
- 사용자의 데이터를 받을 때 해야하는 과중한 작업과 반복 코드를 줄여줌



### Form 선언하기

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

- Modle 선언과 유사, 같은 필드타입 사용
- `forms.Form`클래스를 상속 받음



### Form rendering options

- `.as_p` : label 과 input 쌍을 p태그로 감싸줌
- `.as_ul` : li 태그로 감싸짐, ul은 직접 작성
- `.as_table` : tr 태그로 감싸짐, table은 직접 작성





## Widgets

- Django HTML input 요소 표현 방법 중 하나
- GET/POST 딕셔너리에서 데이터 추출
- 하지만 widgets은 반드시 form field에 할당됨.
- textarea 요소는 form클래스에 없음. widget을 이용해야함.

- HTML 렌더링 처리

- **Form Field**는 input **유효성 검사**를 처리하지만, Widgets는 **단순 raw한 렌더링 처리**

  ```python
  # articles/forms.py
  
  class ArticleForm(forms.Form):
      title = forms.CharField(max_length=10)
      content = forms.CharField(widget=forms.Textarea())
  ```

  





## ModelForm

- 이미 모델에서 필드를 정의한 경우, form에서 필드를 재정의 하는 중복된 행위가 발생할 수 있음.
- ModelForm을 이용해 Modle을 통해 Form Class를 만들 수 있음

### ModelForm Class

- Modle을 통해 Form Class를 만들 수 있는 Helper

- 일반 Form Class와 완전히 같은 방식으로 view에서 사용 가능

- ModelForm 선언하기

  - `forms.ModelForm` 클래스를 상속받음
  - 정의한 클래스 안에 Meta 클래스를 선언.
  - 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta클래스에 작성

  ```python
  class ArticleForm(forms.ModelForm):
      
      class Meta:
          model = Article
          fields = '__all__'
          # exclude = ('title', )
  ```

- `is_valid()`
  - 유효성 검사 실행.
  - django에서는 많은 테스트에 대해 `is_valid()` 제공
- `save()`
  - form에 바인딩된 데이터에서 DB객체를 만들고 저장
  - ModelForm 하위 클래스는 기존 모델 인스턴스를 키워드 인자 instance로 받아들일 수 있음
    - 키워드 인자로 instance가 들어오는 경우 -> UPDATE
    - instance 인자가 없는 경우 -> CREATE



### Widgets 적용

- Form 안에 widget 정의
  - Meta가 아니라 그냥 클래스에 쓸 것을 django에서 권장함

```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
    	label='제목',
    	widget=forms.TextInput(
        	attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        ),
    )
    
    class Meta:
        model = Article
        fields = '__all__'
```





### Form & ModelForm

- Form
  - 어떤 model에 저장해야하는지 알 수 없으므로 유효성 검사 이후 cleaned_data 딕셔너리를 생성
  - cleaned_data 딕셔너리에서 데이터를 가져온 후 save() 호출해야함
  - **model에 연관되지 않은 데이터**를 받을 때 사용
- **ModelForm**
  - django가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의함.
  - 어떤 레코드를 만들어야하는지 알고 있으믈 바로 save() 호출 가능