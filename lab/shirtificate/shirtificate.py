from fpdf import FPDF
class PDF(FPDF):
    def __init__(self, type):
        self.pdf = FPDF(orientation='portrait', unit='mm', format='A4')
        self.pdf.set_margin(15)
        self.pdf.add_page()
        self.pdf.set_font("helvetica", "B", 47)
        self.pdf.set_text_color(r=0, g=0, b=0)
        # put tittle
        self.pdf.text(x=45, y=50, txt='CS50 Shirtificate')
        self.pdf.set_y(80)
        # image load
        self.pdf.image("shirtificate.png", w=self.pdf.epw )
        self.pdf.set_font("helvetica", "B", 25)
        self.pdf.set_text_color(r=255, g=255, b=255)
        # text load
        self.pdf.text(x=55, y=150, txt=f'{type} took CS50')
        self.pdf.output("shirtificate.pdf")



def main():

    type = input("Name: ").strip()
    pdf = PDF(type)





if __name__ == '__main__':
    main()