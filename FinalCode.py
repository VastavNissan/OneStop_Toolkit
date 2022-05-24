from tkinter import *
from tkinter import messagebox
from tkinter import Tk,StringVar, ttk
from tkinter.font import BOLD
from PIL import ImageTk, Image
import tkinter.font as font
from googletrans import Translator
from forex_python.converter import CurrencyRates
import pyttsx3
from tkinter import filedialog
from pytube import YouTube
import requests

root = Tk()
root.title("OneStop ToolKit")
root.resizable(0,0)
root.geometry("500x500")

background_image = ImageTk.PhotoImage(Image.open("D:\\demo2.png"))
background_label = Label(root, image = background_image)
background_label.place(relwidth = 1, relheight =1)


def start():
    start = Toplevel()
    start.title("OneStop ToolKit")
    start.resizable(0,0)
    start.geometry("500x500")

    bg = ImageTk.PhotoImage(file="D:\\screen4.png")
    canvas = Canvas(start, width=500, height=500)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2
        image = Image.open("D:\\screen4.png")
        resized = image.resize((500,500), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')
    start.bind("<Configure>", resize_image)

    
    calculate = PhotoImage(file = "D:\\calc.png")
    photoimage1 = calculate.subsample(12,12)
    calculator_button= Button(start, image = photoimage1,command=calc,borderwidth=0, bg ="#323232", activebackground = "#323232")
    calculator_button.place(relx=0.41,rely=0.15)
    calculator_button.photoimage1 = photoimage1


    lang = PhotoImage(file = "D:\\translate.png")
    photoimg1 = lang.subsample(10,10)
    language_button= Button(start, image = photoimg1,command=Language,borderwidth=0, bg ="#171717", activebackground = "#171717")
    language_button.place(relx=0.2,rely=0.77)
    language_button.photoimg1 = photoimg1

    youtube = PhotoImage(file = "D:\\youtube.png")
    photoimg2 = youtube.subsample(10,7)
    youtube_button= Button(start, image = photoimg2,borderwidth=0,command=youtube_download, bg ="#2D2D2D", activebackground = "#2D2D2D")
    youtube_button.place(relx=0.38,rely=0.77)
    youtube_button.photoimg2 = photoimg2

    speech = PhotoImage(file = "D:\\speech.png")
    photoimg3 = speech.subsample(10,10)
    speech_button= Button(start, image = photoimg3,command = text_to_speech, borderwidth=0, bg ="#2D2D2D", activebackground = "#2D2D2D")
    speech_button.place(relx=0.52,rely=0.77)
    speech_button.photoimg3 = photoimg3

    convertor = PhotoImage(file = "D:\\convert.png")
    photoimg4 = convertor.subsample(6,6)
    convertor_button= Button(start, image = photoimg4,command = unit_Converter, borderwidth=0, bg ="#171717", activebackground = "#171717")
    convertor_button.place(relx=0.69,rely=0.77)
    convertor_button.photoimg4 = photoimg4


photo2 = PhotoImage(file = "D:\\power.jpg" )
photoimage2 = photo2.subsample(3,3)
start_button=Button(root, image = photoimage2,command=start,borderwidth=0,bg ="#262728", activebackground = "#262728")
start_button.place(relx=0.1,rely=0.82)
start_button.photoimage = photoimage2

def calc():
    def iCalc(source, side):
        storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
        storeObj.pack(side=side, expand =YES, fill =BOTH)
        return storeObj
 
    def button(source, side, text, command=None):
        storeObj = Button(source, text=text, command=command)
        storeObj.pack(side=side, expand = YES, fill=BOTH)
        return storeObj
 
    class app(Frame):
        def __init__(self):
            Frame.__init__(self)
            self.option_add('*Font', 'arial 20 bold')
            self.pack(expand = YES, fill =BOTH)
            self.master.title('Calculator')
 
            display = StringVar()
            Entry(self, relief=RIDGE, textvariable=display, justify='right'
              , bd=30, bg="powder blue").pack(side=TOP,expand=YES, fill=BOTH)
 
            for clearButton in (["C"]):
                erase = iCalc(self, TOP)
                for ichar in clearButton:
                    button(erase, LEFT, ichar, lambda
                        storeObj=display, q=ichar: storeObj.set(''))
 
            for numButton in ("789/", "456*", "123-", "0.+"):
                FunctionNum = iCalc(self, TOP)
                for iEquals in numButton:
                    button(FunctionNum, LEFT, iEquals, lambda
                        storeObj=display, q=iEquals: storeObj
                        .set(storeObj.get() + q))
 
            EqualButton = iCalc(self, TOP)
            
            for iEquals in "=":
                if iEquals == '=':
                    btniEquals = button(EqualButton, LEFT, iEquals)
                    btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                                storeObj=display: s.calc(storeObj), '+')
 
                else:
                    btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                    (storeObj.get() + s))

        def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")
    
    app()

def Language():
    Language = Toplevel()
    Language.geometry('500x620')

    background_image = ImageTk.PhotoImage(Image.open("D:\\bglang.jpeg"))
    background_label = Label(Language, image = background_image)
    background_label.place(relwidth = 1, relheight =1)
    background_image.ref = background_image

    Language.title(" ONESTOP-TOOLKIT")
    Label(Language, text = "LANGUAGE TRANSLATOR", font = ('Lora',23,BOLD), bg='#55b8ed', foreground='#fff15e').place(x=48,y=30)

    Input_text = Text(Language,font = 'arial 10', height = 5, wrap = WORD, padx=5, pady=5, width = 50,bg="#accbe3")
    Input_text.place(x=65,y = 160)
    Output_text = Text(Language,font = 'arial 10', height = 5, wrap = WORD, padx=5, pady= 5, width =50, bg="#accbe3")
    Output_text.place(x = 65 ,y = 440)

    LANGUAGES_LIST ={"Arabic","Chinese","English","French","Gujarati", "Hindi","Italian","Japanese","Kannada","Korean","Malayalam","Marathi","Odia","Punjabi","Russian","Spanish","Telugu","Urdu"}
    language = list(LANGUAGES_LIST)
    src_lang = ttk.Combobox(Language, values= language, width =22)
    src_lang.place(x=170,y=120)
    src_lang.set('choose input language')
    dest_lang = ttk.Combobox(Language, values= language, width =22)
    dest_lang.place(x=170,y=400)
    dest_lang.set('choose output language')

    def Translate():
        translator = Translator()
        translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)

    trans_btn = Button(Language, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = '#c72c41',foreground="white", activebackground = 'sky blue')
    trans_btn.place(x = 200, y= 310 )



def text_to_speech():
    
    window = Toplevel()
    window.geometry('375x400')
    window.resizable(0,0)
    background_image = ImageTk.PhotoImage(file="D:\\speech_to_text.jpg")
    canvas = Canvas(window, width=375, height=400)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0, 0, image=background_image, anchor='nw')

    def resize_image():
            global image, resized, image2
            image = Image.open("D:\\speech_to_text.jpg")
            resized = image.resize((375,400), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(resized)
            canvas.create_image(0, 0, image=image2, anchor='nw')
    canvas.bind("<Configure>", resize_image())


    window.title("Text to Speech")

    engine=pyttsx3.init()

    def female():
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        Message = entry_field.get()
        engine.say(Message)
        engine.runAndWait()
        
    def male():
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        Message = entry_field.get()
        engine.say(Message)
        engine.runAndWait()

    Label(window, text = "Enter Text", font = "consolas 15 bold", bg = "#002b36", fg = "#17aaf9").place(x=125,y=20)

    Msg = StringVar()
    entry_field = Entry(window,textvariable = Msg, width ='50')
    entry_field.place(height = 50, x=30 , y=60)
   

    def Exit():
        window.destroy()

    Button(window,text="Male",font = "consolas 15 bold", width = 6,command = male,bg = "OrangeRed1",borderwidth=5).place(x = 40, y=180)
    Button(window,text="Female",font = "consolas 15 bold",command = female, bg = "OrangeRed1",borderwidth=5).place(x = 250, y=180)
    Button(window, text = "EXIT", font = "consolas 15 bold", width = 6, command = Exit, bg = "#7E354D",borderwidth=5).place(x = 145, y=280)

def unit_Converter():
    ###################################################################
     
    unit = Toplevel()
    unit.title('OneStop ToolKit')
    unit.geometry("400x450")
    background_unit = ImageTk.PhotoImage(Image.open("D:\\mobile2.png"))
    unit_label = Label(unit, image = background_unit)
    unit_label.place(relwidth = 1, relheight =1)
    background_unit.ref = background_unit

    widget = Button(unit, text="QUIT", bg="white", fg="red",font = ("Arial", 12, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=unit.destroy).place(x=240,y=375)

    #############################################################################################################################################

    def CurrencyConverter():

        ids = {"Indian Rupees" : 'INR',"US Dollar" : 'USD', "Euros" : 'EUR', "Australian Dollar" : "AUD", "Canadian Dollar" : "CAD", "Qatar Doha" : 'QAR', "Arab Emirates Dirham" : 'AED', "Pound Sterling" : 'GBP', "Japanese Yen" : 'JPY',}

        def convert(amt, frm, to):
            amt = float(amt)
            c = CurrencyRates()
            if frm == to:
                result = amt
            else:
                result = c.convert(frm, to, int(amt))
            return result

        def callback():
                try:
                    amt = float(in_field.get())
                                
                except ValueError:
                    out_amt.set('Invalid input')
                    return None
                if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
                    out_amt.set('Input or output unit not chosen')
                    return None
                else:
                    frm = ids[in_unit.get()]
                    to = ids[out_unit.get()]
                    out_amt.set(convert(amt, frm, to))

        root = Toplevel()
        root.title("Currency Converter")

        # initiate frame
        mainframe = Frame(root)
        mainframe.pack(fill=BOTH, expand=1)
        titleLabel = Label (mainframe, text = "Currency Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)
        in_amt = StringVar()
        in_amt.set('0')
        out_amt = StringVar()

        in_unit = StringVar()
        out_unit = StringVar()
        in_unit.set('Select Unit')
        out_unit.set('Select Unit')

        # Add input field
        in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
        in_field.grid(row=1, column=2, sticky=(W, E))

        # Add drop-down for input unit
        in_select = OptionMenu(mainframe, in_unit, "Indian Rupees","US Dollar", "Euros", "Australian Dollar", "Canadian Dollar", "Qatar Doha", "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen").grid(column=3, row=1, sticky=W)
        # Add output field and drop-down
        ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
        in_select = OptionMenu(mainframe, out_unit, "Indian Rupees","US Dollar", "Euros", "Australian Dollar", "Canadian Dollar", "Qatar Doha", "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen").grid(column=3, row=3, sticky=W)
        calc_button = ttk.Button(mainframe, text="Calculate",command=callback).grid(column=2, row=2, sticky=E)

    ##############################################################################################################

    def WeightConverter():
            # factors to multiply to a value to convert from the following units to meters(m)
        factors = {'kg' : 1000, 'hg' : 100, 'dg' : 10, 'g' : 1,'deg' : 0.1, 'cg' : 0.01, 'mg' : 0.001}
        ids = {"Kilogram" : 'kg', "Hectagram" : 'hg', "Decagram" : 'dg', "Decigram" : 'deg', "Kilogram" : 'kg', "gram" : 'g', "centigram" : 'cg', "milligram" : 'mg'}
        # function to convert from a given unit to another
        def convert(amt, frm, to):
            if frm != 'g':
                amt = amt * factors[frm]
                return amt / factors[to]
            else:
                return amt / factors[to]

        def callback():
            try:
                amt = float(in_field.get())
            except ValueError:
                out_amt.set('Invalid input')
                return None
            if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
                out_amt.set('Input or output unit not chosen')
                return None
            else:
                frm = ids[in_unit.get()]
                to = ids[out_unit.get()]
                out_amt.set(convert(amt, frm, to))

        # initiate window
        root = Toplevel()
        root.title("Weight Converter")

        # initiate frame
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.pack(fill=BOTH, expand=1)
        titleLabel = Label (mainframe, text = "Weight Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)

        in_amt = StringVar()
        in_amt.set('0')
        out_amt = StringVar()

        in_unit = StringVar()
        out_unit = StringVar()
        in_unit.set('Select Unit')
        out_unit.set('Select Unit')

        # Add input field
        in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
        in_field.grid(row=1, column=2, sticky=(W, E))

        # Add drop-down for input unit
        in_select = OptionMenu(mainframe, in_unit, "Kilogram","Hectagram","Decagram", "gram", "Decigram","Centigram", "Milligram") .grid(column=3, row=1, sticky=W)

        # Add output field and drop-down
        ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
        in_select = OptionMenu(mainframe, out_unit, "Kilogram","Hectagram","Decagram", "gram", "Decigram","Centigram", "Milligram").grid(column=3, row=3, sticky=W)
        calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    #############################################################################################################################################################

    def LengthConverter():
            # factors to multiply to a value to convert from the following units to meters(m)
        factors = {'nmi' : 1852, 'mi' : 1609.34, 'yd' : 0.9144, 'ft' : 0.3048, 'inch' : 0.0254, 'km' : 1000, 'm' : 1, 'cm' : 0.01, 'mm' : 0.001}
        ids = {"Nautical Miles" : 'nmi', "Miles" : 'mi', "Yards" : 'yd', "Feet" : 'ft', "Inches" : 'inch', "Kilometers" : 'km', "meters" : 'm', "centimeters" : 'cm', "millileters" : 'mm'}

        # function to convert from a given unit to another
        def convert(amt, frm, to):
            if frm != 'm':
                amt = amt * factors[frm]
                return amt / factors[to]
            else:
                return amt / factors[to]

        def callback():
            try:
                amt = float(in_field.get())
            except ValueError:
                out_amt.set('Invalid input')
                return None
            if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
                out_amt.set('Input or output unit not chosen')
                return None
            else:
                frm = ids[in_unit.get()]
                to = ids[out_unit.get()]
                out_amt.set(convert(amt, frm, to))

        # initiate window
        root = Toplevel()
        root.title("Length Converter")

        # initiate frame
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.pack(fill=BOTH, expand=1)
        titleLabel = Label (mainframe, text = "Length Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)

        in_amt = StringVar()
        in_amt.set('0')
        out_amt = StringVar()

        in_unit = StringVar()
        out_unit = StringVar()
        in_unit.set('Select Unit')
        out_unit.set('Select Unit')

        # Add input field
        in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
        in_field.grid(row=1, column=2, sticky=(W, E))

        # Add drop-down for input unit
        in_select = OptionMenu(mainframe, in_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers", "meters", "centimeters", "millileters").grid(column=3, row=1, sticky=W)

        # Add output field and drop-down
        ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
        in_select = OptionMenu(mainframe, out_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers", "meters", "centimeters", "millileters").grid(column=3, row=3, sticky=W)
        calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    ###################################################################################################################################################################

    def TemperatureConverter():
        def convert():
            celTemp = celTempVar.get()
            fahTemp = fahTempVar.get()

            if celTempVar.get() != 0.0:
                celToFah = (celTemp *  9/5 + 32)
                fahTempVar.set(celToFah)

            elif fahTempVar.get() != 0.0:
                fahToCel = ((fahTemp - 32) * (5/9))
                celTempVar.set(fahToCel)

        def reset():
            top = Toplevel(padx=50, pady=50)
            top.grid()
            message = Label(top, text = "Reset Complete")
            button = Button(top, text="OK", command=top.destroy)

            message.grid(row = 0, padx = 5, pady = 5)
            button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

            fahTempVar.set(int(0))
            celTempVar.set(int(0)) 
            
        top = Toplevel()
        top.title("Temperature Converter")
        ###MAIN###
        celTempVar = IntVar()
        celTempVar.set(int(0))
        fahTempVar = IntVar()
        fahTempVar.set(int(0))

        titleLabel = Label (top, text = "Temperature Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)
    
        celLabel = Label (top, text = "Celcius: ", font = ("Arial", 16), fg = "red")
        celLabel.grid(row = 2, column = 1, pady = 10, sticky = NW)

        fahLabel = Label (top, text = "Fahrenheit: ", font = ("Arial", 16), fg = "blue")
        fahLabel.grid(row = 3, column = 1, pady = 10, sticky = NW)

        celEntry = Entry (top, width = 10, bd = 5, textvariable = celTempVar)
        celEntry.grid(row = 2, column = 1, pady = 10, sticky = NW, padx = 125 )

        fahEntry = Entry (top, width = 10, bd = 5, textvariable = fahTempVar)
        fahEntry.grid(row = 3, column = 1, pady = 10, sticky = NW, padx = 125 )

        convertButton =Button (top, text = "Convert", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = convert)
        convertButton.grid(row = 4, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 55)

        resetButton = Button (top, text = "Reset", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = reset)
        resetButton.grid(row = 4, column = 2,ipady = 8, ipadx = 12, pady = 5, sticky = NW)

    ####################################################################################################
    #TEMPERATURE CONVERTER
    widget = Button(unit, text="Temperature converter", bg="white" , fg="red",font = ("Arial", 12, "bold"), bd=5,  activebackground = "green", activeforeground="blue", command=TemperatureConverter).place(x=103,y=150)
    widget = Button(unit, text="Length Converter", bg="white" , fg="red",font = ("Arial", 12, "bold"), bd=5,  activebackground = "green", activeforeground="blue", command=LengthConverter).place(x=103,y=210)
    widget = Button(unit, text="Currency converter", bg="white" , fg="red",font = ("Arial", 12, "bold"), bd=5, activebackground = "green", activeforeground="blue", command=CurrencyConverter).place(x=103,y=90)
    widget = Button(unit, text="Weight Converter", bg="white" , fg="red",font = ("Arial", 12, "bold"), bd=5, activebackground = "green", activeforeground="blue", command=WeightConverter).place(x=103,y=270)


def youtube_download():
    
    Folder_Name = ""

    #file location
    def openLocation():
        global Folder_Name
        Folder_Name = filedialog.askdirectory()
        if(len(Folder_Name) <= 0):
            
            messagebox.showerror("Error","Please Choose Folder!!")
            
        else:
            location.config(text=Folder_Name,fg="green")
            

    def DownloadVideo():
        try:
            def check_video_url(url):
                checker_url = "https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v="
                video_url = checker_url + url
                request = requests.get(video_url)
                valid = request.status_code == 200
                
                if (url == "" or valid == "False"):              
                    messagebox.showerror("Error","Please paste a valid URL")

            choice = ytdchoices.get()
            url = ytdEntry.get()
            check_video_url(url)
        except Exception:
            messagebox.showerror("Error","Please paste a valid URL")


        try:

            if(len(url)>1):
                yt = YouTube(url)

                if(choice == choices[0]):
                    select = yt.streams.filter(progressive=True).first()

                elif(choice == choices[1]):
                    select = yt.streams.filter(progressive=True,file_extension='mp4').last()

                elif(choice == choices[2]):
                    select = yt.streams.filter(only_audio=True).first()

                
            #download function
            select.download(Folder_Name)
            
        except Exception:
            messagebox.showerror("Error","Please paste a valid URL")
            

    youtube = Toplevel()
    youtube.title("YouTube Downloader")
    youtube.geometry("850x450") #set window
    youtube.resizable(0,0)
    background_youtube = ImageTk.PhotoImage(Image.open("D:\\youtube_bg.png"))
    background_label = Label(youtube, image = background_youtube)
    background_label.place(relwidth = 1, relheight =1)
    background_youtube.ref = background_youtube


    #Ytd Link Label
    ytdLabel = Label(youtube,text="Enter the Video's URL",font=("jost",13))
    ytdLabel.place(x= 20, y= 50)

    #Entry Box
    ytdEntryVar = StringVar()
    ytdEntry = Entry(youtube,width=43,textvariable=ytdEntryVar)
    ytdEntry.place(x = 210, y = 50, height = 25)


    #btn of save file
    saveEntry = Button(youtube,width=13,bg="red",font = 15,bd=6,fg="white",activebackground="green",text="Choose Path",command=openLocation)
    saveEntry.place(x = 165, y = 120)

    #Error Msg location
    location = Label(youtube,text = "Path", fg="red",font=("jost",12,BOLD), width= 25)
    location.place(x = 110, y =200, height = 25)

    #Download Quality
    ytdQuality = Label(youtube,text="Select Video Quality",font=("jost",15))
    ytdQuality.place(x = 20, y = 270)

    #combobox
    choices = ["144p","720p","Only Audio"]
    ytdchoices = ttk.Combobox(youtube,values=choices)
    ytdchoices.set("Quality")
    ytdchoices.place(x = 250, y = 270, height = 25)

    #donwload btn
    downloadbtn = Button(youtube,text="Download",width=10,font = 15,bd =6, bg="red",fg="white",activebackground="green",command=DownloadVideo)
    downloadbtn.place(x = 180, y = 350)

mainloop()
