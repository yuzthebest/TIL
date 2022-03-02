# django



## 기본 working 방법

![img](readme.assets/basic-django.png)

request와 response의 구조고 MTV(model template view) 아키텍처를 가지고 있음.

URLs : 요청 url기준으로 http요청을 적절한 view로 보내줌.

View : Http 요청을 수신하고 응답을 반환함. 템플릿에게 응답의 서식 설정을 맡김

Template : 파일의 구조나 레이아웃 정의. (ex.html페이지) 실제 내용을 보여주는데 사용되는 플레이스 홀더.


구현 방법

1) 가상환경 생성
   python -m venv <파일 이름>

2) 가상환경 실행

   source <파일이름>/Scripts/activate

3) 가상환경에 장고설치

   pip install django==3.2.12

4) 프로젝트 생성

   django-admin startproject <프로젝트명>

5) 서버 활성화

   python manage.py runserver

6) application 구현

   python manage.py startapp <어플리케이션명>