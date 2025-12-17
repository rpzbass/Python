import aspose.pdf as ap

input_pdf = "anuncio arena batel4.pdf"
output_ppt ="pdf_to_pptx4.pptx"

# Abrir documento PDF
document = ap.Document(input_pdf)

# Criar instância PptxSaveOptions
save_option = ap.PptxSaveOptions()

# Salvar PDF como PPT
document.save(output_ppt, save_option)