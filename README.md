# PDF 페이지 삽입 도구

PDF 파일의 특정 페이지를 다른 PDF 파일의 특정 위치에 삽입하는 Python 스크립트입니다.

## 기능

- Source PDF에서 특정 페이지를 추출
- Target PDF의 지정된 위치에 해당 페이지 삽입
- 새로운 PDF 파일 생성

## 요구사항

- Python 3.x
- PyPDF2 라이브러리

## 설치

```bash
pip install PyPDF2
```

## 사용 방법

### 1. 필요한 파일 준비

작업 폴더에 다음 파일들을 준비합니다:
- `추출할 페이지가 있는 PDF.pdf` - 페이지를 추출할 소스 PDF
- `삽입할 PDF.pdf` - 페이지를 삽입할 대상 PDF

### 2. 설정 수정

`insert_pdf_page.py` 파일의 `main()` 함수에서 다음 값을 수정합니다:

```python
source_pdf = r"추출할 페이지가 있는 PDF.pdf"  # 소스 PDF 파일 경로
target_pdf = r"삽입할 PDF.pdf"                  # 대상 PDF 파일 경로
n = 28                                          # 추출할 페이지 번호 (1부터 시작)
m = 28                                          # 삽입할 위치 (페이지 번호)
output_pdf = r"./merged_pdf.pdf"                # 출력 파일 경로
```

**매개변수 설명:**
- `n`: Source PDF에서 추출할 페이지 번호 (1부터 시작)
- `m`: Target PDF에서 삽입할 위치 (m번째 페이지 뒤에 삽입됨)
- `output_pdf`: 결과를 저장할 파일 경로

### 3. 실행

```bash
python insert_pdf_page.py
```

### 4. 결과 확인

설정한 출력 경로에 새 PDF 파일이 생성됩니다.

## 예시

```
Source PDF: 5페이지
Target PDF: 10페이지

n = 3, m = 5로 설정하면:

결과 PDF:
- Target PDF의 1~4 페이지
- Source PDF의 3번째 페이지 (삽입됨)
- Target PDF의 5~10 페이지
```

## 주의사항

- 페이지 번호는 1부터 시작합니다
- 출력 파일은 기존 파일을 덮어씁니다
- 파일 경로에 한글이 포함되어 있으면 경로를 `r""` 형태로 지정하는 것이 안전합니다

## 라이선스

이 프로젝트는 자유롭게 사용 가능합니다.
