## 프로젝트 소개

- 주간 페어 프로그래밍 4 - 영화 리뷰 커뮤니티 CRUD & AUTH & 1:N
- 프로젝트 기간
  - 2022.10.21
- 사용 기술
  - 언어: HTML, CSS, JavaScript, Python
  - 라이브러리: django-bootstrap5, django-extensions, django-imagekit, django-widget-tweaks
  - 프레임워크: Django



## 스크린샷

![pair04](Assets/README.assets/pair04.gif)



## 프로젝트 목적

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야 합니다.

- **CRUD** 구현
- **Staticfiles** 활용 정적 파일(이미지, CSS, JS) 다루기
- Django **Auth** 활용 회원 관리 구현
- Media 활용 동적 파일 다루기
- 모델 간 1 : N 관계 매핑 코드 작성 및 활용
  - 유저 - 리뷰
  - 리뷰 - 댓글
  - 유저 - 댓글



## 프로젝트 설명

- 회원 관리
  - `signup`
    - 회원가입을 진행한다.
    - 회원가입이 끝나면, 메인 페이지(articles:index)로 돌아간다.
  - `login`
    - 로그인을 진행한다.
    - 로그인이 끝나면, 메인 페이지로 돌아간다.
  - `logout`
    - 로그아웃을 진행한다.
    - 로그아웃이 끝나면, 메인 페이지로 돌아간다.
  - `detail`
    - 회원 정보를 보여준다.
    - 회원 정보를 수정하는 기능, 비밀번호를 변경하는 기능, 회원 탈퇴 기능을 제공한다.
      - 회원 정보 페이지의 유저와, 현재 로그인 한 유저가 같을 시에만 해당 기능을 이용할 수 있다.
    - 해당 회원이 작성한 글 목록과 댓글 목록을 볼 수 있다.
  - `update`
    - 회원 정보를 수정한다.
    - 회원 정보 페이지의 유저와, 현재 로그인 한 유저가 같을 시에만 수정할 수 있다.
  - `password`
    - 비밀 번호를 변경한다.
    - 회원 정보 페이지의 유저와, 현재 로그인 한 유저가 같을 시에만 변경할 수 있다.
  - `delete`
    - 회원 탈퇴를 진행한다.
    - 회원 정보 페이지의 유저와, 현재 로그인 한 유저가 같을 시에만 탈퇴할 수 있다.



- 영화 리뷰 관리
  - `index`
    - 사람들이 작성한 리뷰 목록을 보여준다.
    - 한 페이지에 글이 8개씩 보이도록 한다.
  - `create`
    - 영화 리뷰를 작성한다. 이때, 선택적으로 사진을 함께 올릴 수 있다.
    - 로그인 한 유저의 정보를 자동으로 DB에 함께 저장한다.
    - 로그인 한 유저만 글을 작성할 수 있다.
  - `detail`
    - 영화 리뷰의 제목 + 내용 + 영화 제목 + 별점 + 작성자 이름 + 마지막 수정 시간을 보여준다.
    - 사진이 있으면 사진도 보여준다.
    - 해당 글을 작성한 유저만 글을 수정 및 삭제할 수 있다.
    - 댓글을 입력하는 창과, 댓글 목록도 함께 보여준다.
  - `update`
    - 영화 리뷰 정보 페이지에서 수정을 진행할 수 있다.
    - 해당 글을 작성한 유저만 글을 수정할 수 있다.
  - `delete`
    - 영화 리뷰 정보 페이지에서 삭제를 진행할 수 있다.
    - 해당 글을 작성한 유저만 글을 삭제할 수 있다.
  - `search`
    - 게시글을 검색한다.
    - 게시글의 제목, 또는 영화 제목으로 검색할 수 있다.
    - 한 페이지에 글이 8개씩 보이도록 한다.



- 댓글 관리
  - `create_comment`
    - 댓글을 작성한다.
    - 로그인 한 유저의 정보와, 댓글이 작성된 게시글의 정보를 자동으로 DB에 함께 저장한다.
    - 로그인 한 유저만 댓글을 작성할 수 있다.
  - `delete_comment`
    - 댓글을 삭제한다.
    - 로그인 한 유저만 댓글을 삭제할 수 있다.



## 역할 (개발 내용)

- 이준엽: 비밀번호 변경, 회원 탈퇴, 게시글 작성, 게시글 검색, 페이지네이션
- 이주현: 회원가입, 게시글 조회, 게시글 수정, 게시글 삭제
- 최보영: 로그인, 로그아웃, 회원 정보 조회, 회원 정보 수정, 댓글 생성, 댓글 삭제, 페이지네이션, 페이지 디자인



## 배운 점

- 페이지네이션 기능을 구현하는 방법
- select 태그의 option value에 따라, 검색 옵션을 다르게 만드는 방법
- 검색 기능과 페이지네이션을 합칠 때 주의해야 할 점
  - url의 쿼리를 잘 확인하자!



## 문제 해결

### 문제 상황

- 검색 기능에 페이지네이션을 결합하려 하니, 검색 후 페이지를 이동하면 자꾸 에러가 발생하였다.

- 문제 코드

  ```html
  <!-- 이전 페이지 -->
  <a class="page-link" href="?page={{ question_list.previous_page_number }}">이전</a>
  ```

### 해결

- 검색하면 쿼리가 url에 붙는데, 그 형식을 지켜 주어야 했다.

- (Search_option은 검색 옵션(제목, 영화제목)이고, search는 사용자가 검색창에 입력한 내용을 의미한다.)

- 예를 들면 이런 식으로 해결할 수 있다.

  ```html
  <!-- 이전 페이지 -->
  <a class="page-link" href="?Search_option={{ search_options }}&#38;search={{ search }}&#38;page={{ question_list.previous_page_number }}">이전</a>
  ```

  
