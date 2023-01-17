from os import listdir
from os.path import join

from langdetect import detect

from uwazi_api.UwaziAdapter import UwaziAdapter

import PyPDF2


pdfs_folder_path = "PATH"
template = "ID"
should_contain = ""


def upload(maximum_pdf_number):
    total = 0
    for file in listdir(pdfs_folder_path):
        if ".pdf" not in file:
            continue

        if total >= maximum_pdf_number:
            return

        print(file)
        if upload_file(join(pdfs_folder_path, file)):
            total += 1


def get_language(pdf_file_path):
    with open(pdf_file_path, mode="rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        if len(pdf_reader.pages) < 2:
            return 'not enough pages'

        page = pdf_reader.pages[0]

        if should_contain and should_contain not in page.extract_text():
            return 'not valid'

        page = pdf_reader.pages[1]
        return detect(page.extract_text())


def upload_file(pdf_file_path):
    language = get_language(pdf_file_path)

    if language not in ['en']:
        print(language)
        return False

    uwazi_adapter = UwaziAdapter(user='', password='', url='http://localhost:3000')
    title = pdf_file_path.split('/')[-1]
    entity = {"title": title, "template": template}
    shared_id = uwazi_adapter.entities.upload(entity, "en")
    uwazi_adapter.files.upload_file(pdf_file_path, shared_id, language, title)
    return True


if __name__ == "__main__":
    upload(maximum_pdf_number=50)
