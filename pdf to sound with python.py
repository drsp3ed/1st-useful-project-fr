import pdfplumber
import docx2txt
from gtts import gTTS
from pathlib import Path

def wordtosound(path, language):
    if Path(path).is_file and Path(path).suffix == '.docx':
        text = docx2txt.process(path)
        audio_file = gTTS(text=text, lang=language, slow=False)
        file_name = Path(path).stem
        audio_file.save(f'{file_name}.mp3')


def texttosound(path, language):
    if Path(path).is_file and Path(path).suffix == '.txt':
        text_list = []
        f = open(path)
        text_list = f.read()
        f.close()
        text = ''.join(text_list)
        audio_file = gTTS(text=text, lang=language, slow=False)
        file_name = Path(path).stem
        audio_file.save(f'{file_name}.mp3')

def pdftosound(path, language):
    if Path(path).is_file() and Path(path).suffix == '.pdf':
        with pdfplumber.PDF(open(file=path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)    
        text.replace('\n', '')

        audio_file = gTTS(text=text, lang=language, slow=False)
        file_name = Path(path).stem
        audio_file.save(f'{file_name}.mp3')

if __name__ == '__main__':
    path_to_file = input ('Enter the path to your file:\n')
    lang = input('Which language would you like to listen to?\n')
    if Path(path_to_file).is_file and Path(path_to_file).suffix == '.pdf':
        pdftosound(path=path_to_file, language=lang)
    elif Path(path_to_file).is_file and Path(path_to_file).suffix == '.txt':
        texttosound(path=path_to_file, language=lang)
    if Path(path_to_file).is_file and Path(path_to_file).suffix == '.docx':
        wordtosound(path=path_to_file, language=lang)