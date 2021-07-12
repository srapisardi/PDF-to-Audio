import PyPDF2, pyttsx3


file = input("Enter PDF file name: ")


try:
    pdf_reader = PyPDF2.PdfFileReader(open(file, 'rb'))
    speaker = pyttsx3.init()

    for page_num in range(pdf_reader.numPages):
        text = pdf_reader.getPage(page_num).extractText()
        speaker.say(text)
        speaker.runAndWait()

        speaker.stop()

    speaker.save_to_file(text, 'audio.mp3')
    speaker.runAndWait()
    
except:
    print(file, "Not Found.")
