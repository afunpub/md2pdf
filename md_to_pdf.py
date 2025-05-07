import os
import markdown
from weasyprint import HTML

def convert_md_to_pdf(folder_path, output_pdf_path):
    """
    將指定資料夾內所有 .md 檔案合併轉換為一個 PDF 檔案。

    Args:
        folder_path (str): 包含 .md 檔案的資料夾路徑。
        output_pdf_path (str): 輸出 PDF 檔案的路徑。
    """
    md_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])
    all_html = ""

    if not md_files:
        print(f"資料夾 '{folder_path}' 中沒有找到任何 .md 檔案。")
        return

    for md_file in md_files:
        md_file_path = os.path.join(folder_path, md_file)
        try:
            with open(md_file_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
                html_content = markdown.markdown(markdown_content)
                # 在每個檔案的 HTML 內容之間添加分隔符（可選）
                all_html += f"<div style='page-break-after: always;'></div>\n{html_content}\n"
        except Exception as e:
            print(f"處理檔案 '{md_file}' 時發生錯誤：{e}")
            return

    try:
        HTML(string=all_html).write_pdf(output_pdf_path)
        print(f"成功將資料夾 '{folder_path}' 中的所有 .md 檔案合併轉換為 '{output_pdf_path}'。")
    except Exception as e:
        print(f"生成 PDF 檔案 '{output_pdf_path}' 時發生錯誤：{e}")

if __name__ == "__main__":
    # folder_path = input("請輸入包含 .md 檔案的資料夾路徑：")
    # output_pdf_path = input("請輸入輸出 PDF 檔案的路徑和名稱（例如：output.pdf）：")
    folder_path = "."  # 替換為你的資料夾路徑
    output_pdf_path = "output.pdf"  # 替換為你的輸出 PDF 檔案路徑和名稱

    convert_md_to_pdf(folder_path, output_pdf_path)
    print(f"位於 '{folder_path}' 的所有 .md 檔案已合併至 '{output_pdf_path}'。")