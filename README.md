# Django Blog

## 1. 목표 및 기능

### 1.1 목표
* Django를 이용하여 CRUD 기능 구현

### 1.2 기능
* 회원가입, 로그인, 로그아웃
* 게시글 CRUD
* 게시글 검색
* 게시글 조회수 표시
* 게시글 이미지 업로드
* 댓글 CRD
* 대댓글 CRD

## 2. 개발 환경 및 배포 URL

### 2.1 개발 환경
* python==3.11.3
* Django==3.2
* Pillow==10.0.0

### 2.2 배포 URL
* 미배포

## 3. 프로젝트 구조 및 개발 일정

### 3.1 프로젝트 구조
```
project_django_blog
└─blogapp
     ├─app
     ├─blog
     |  ├─migrations
     |  └─templates
     |        └─blog
     ├─media
     ├─templates
     ├─user
     |  ├─migrations
     |  └─templates
     |        └─user
     └─venv
```

### 3.2 ERD 구조
![DBTable](./readme_files/DB_table.PNG)

### 3.3 개발 일정
* 2023.07.17 ~ 2023.07.20

## 4. 동작 화면
* 메인화면

![메인화면](./readme_files/메인화면.PNG)

* 회원가입

![회원가입](./readme_files/회원가입.PNG)

* 로그인

![로그인](./readme_files/로그인후.PNG)

로그인 시 기존 url로 넘어갑니다.

* 블로그 첫 화면

![블로그첫화면](./readme_files/글없는블로그.PNG)

* 글 작성 화면

![글작성화면](./readme_files/글작성화면.PNG)

* 글 작성된 화면

![글작성된화면](./readme_files/글작성된화면.PNG)

* 카테고리 검색 화면

![글검색화면](./readme_files/글검색화면.PNG)

* 상세보기 화면

![디테일화면](./readme_files/디테일화면.PNG)

* 글 수정 화면

![글수정화면](./readme_files/글수정화면.PNG)

* 글 수정된 화면

![글수정된화면](./readme_files/글수정된화면.PNG)

* 댓글, 대댓글 화면

![댓글대댓글화면](./readme_files/댓글대댓글화면.PNG)

* 로그아웃 유저 화면

![로그아웃화면](./readme_files/로그아웃화면.PNG)
![로그아웃디테일](./readme_files/로그아웃디테일.PNG)