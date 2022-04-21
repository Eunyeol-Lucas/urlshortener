# URL Shortner Project

> 긴 URL을 짧고 간결하게 단축해주는 서비스를 만들어본다.

⏰ **시행 날짜:** 2022.04.21 목

🍀 **개발환경:** Visual Studio Code

👄 **개발언어:** html, css, python

📚 **라이브러리:** **TailwindCSS, Django 3.2,  DRF(Django REST Framework)**

**🛠 개발 도구** 

- Visual Studio Code
- Google Chrome Browser
- TailwindCSS
- Django
- DRF(Django REST Framework)
- SQLite3

---

## 👆🏻 요구사항

- [ ] 단축된 URL의 기본 형식은 영문과 숫자의 조합으로 구성된 7자리로 코드로 구성 합니다.
  - (예시) `www.naver.com/news/some-long-thingy` ⇒ `localhost:8000/a8bxL0`
  - (조건) 단축 전 URL의 길이와 상관없이 7자리로 고정합니다.
  - (조건) 문자 변환에 사용되는 알고리즘은 직접 선정합니다.
  - (조건) 기존에 단축된 URL들과 중복되어서는 안됩니다.

---

## Database Modeling

| Field      | Type     |
| ---------- | -------- |
| origin_url | URLField |
| short_url  | URLField |

## API Endpoints

| Description        | URL         | Method | Payload                                                 |
| ------------------ | ----------- | ------ | ------------------------------------------------------- |
| 단축 URL 접근      | /:short_url | GET    |                                                         |
| 전체 단축 URL 조회 | /urls/      | GET    |                                                         |
| 단축 URL 생성      | /urls/      | POST   | {<br />"origin_url":text,<br />"short_url": text<br />} |

---

## 기능 구현

1. Base 62을 사용하여 ascii letter와 digits의 조합을 통해 url의 무작위 암호화

   ```python
   from ctypes.wintypes import SIZE
   from django.conf import settings
   from random import choice
   from string import ascii_letters, digits
   
   SIZE = getattr(settings, 'MAXIMUN_URL_CHARS', 7)
   AVAILABLE_CHARS = ascii_letters + digits
   
   def create_random_code(chars=AVAILABLE_CHARS):
       return ''.join([choice(chars) for _ in range(SIZE)])
   
   
   def create_shortend_url(models_instance):
       random_code = create_random_code()
   
       models_class = models_instance.__class__
       if models_class.objects.filter(short_url=random_code).exists():
           return create_shortend_url(models_instance)
       
       return random_code
   ```



---

## 🌏 실제 페이지 

### 🖥 웹 페이지

<div align="center">
  <img src="README.assets/Apr-22-2022 02-43-15.gif" width=500 />
</div>

### 📱 반응형 모바일 페이지
<div align="center">
  <img src="README.assets/Apr-22-2022 02-58-47-0563968.gif" width=300 />
</div>
