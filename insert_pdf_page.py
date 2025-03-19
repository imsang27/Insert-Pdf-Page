from PyPDF2 import PdfReader, PdfWriter
import os

def insert_page(source_pdf, target_pdf, n, m, output_pdf):
    # PDF 읽기
    reader_source = PdfReader(source_pdf)
    reader_target = PdfReader(target_pdf)
    writer = PdfWriter()

    # target PDF의 첫 m-1 페이지를 writer에 추가
    for i in range(m-1):
        writer.add_page(reader_target.pages[i])

    # source PDF의 n번째 페이지를 추가 (0-based indexing)
    writer.add_page(reader_source.pages[n-1])

    # target PDF의 나머지 페이지 추가
    for i in range(m-1, len(reader_target.pages)):
        writer.add_page(reader_target.pages[i])

    # 결과 저장
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

def main():
    # 경로를 r""로 처리하여 변수를 사용
    source_pdf = r"추출할 페이지가 있는 PDF.pdf"
    target_pdf = r"삽입할 PDF.pdf"
    n = int(28) # 추출할 페이지
    m = int(28) # 삽입할 위치
    output_pdf = r"./merged_pdf.pdf"  # 경로만 말고 PDF 이름까지 넣어야 함.

    # 함수 실행
    insert_page(source_pdf, target_pdf, n, m, output_pdf)
    print(f"페이지가 성공적으로 삽입된 파일은 {output_pdf} 입니다.")

# 실행
if __name__ == "__main__":
    main()
