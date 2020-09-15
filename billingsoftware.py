from tkinter import *
import math, random, os
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry(
            "1350x700+0+0" )  # 1350 * 700 are length and breadth and 0 + 0 means on x and y axis it should be start from 0.
        self.root.title( "BILLING SOFTWARE" )
        bg_color = "sandybrown"  # background color which is blue in this case
        title = Label( self.root, text="BILLING SOFTWARE", bd=12, relief=GROOVE, bg="sienna", fg="white",
                       font=("palatino", 30, "bold"), pady=2 ).pack( fill=X )
        # self.root because we are workin in it, text means on which text we need to apply label, bd means border, relief means border style
        # bg means background color, fg means font color and should ne in time new roma and have 30 sixe and should be bold.
        # pady = 2 means 2 gap from y axis to label of text, pack(fill=x) means fill is to x axis

        # ===========================VARIABLES==================================================================
        # ==================================COSMETIC VARIABLES========================================\
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.lotion = IntVar()

        # ===========================================GROCERY VARIABLES============================================
        self.rice = IntVar()
        self.oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        # ==========================================COLD DRINK VARIABLES==========================================
        self.maza = IntVar()
        self.cock = IntVar()
        self.fruity = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # =============================CUSTOMER VARIABLES===============================================
        self.customer_name = StringVar()
        self.phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint( 1000, 9999 )
        self.bill_no.set( str( x ) )
        self.search_bill = StringVar()

        # ========================================== DETAILS (PRICE & TAX) VARIABLES========================================
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ======================= CUSTOMER DETAIL FRAME ==============================================

        f1 = LabelFrame( self.root, bd=10, relief=GROOVE, text="Customer Details", font=("palatino", 22, "bold"), fg="sienna", bg=bg_color )  # if we use only label instead of labelframe then customer details will show in the middle
        f1.place( x=0, y=80, relwidth=1 )  # here only a single line will show having width 1 ,now we want it will adjust heigth automaticaly acc. to comtent

        cust_name = Label( f1, text="Name", font=("palatino", 20, "bold"), fg="white", bg=bg_color ).grid( row=0, column=0, padx=20, pady=5 )
        # now we need entery field
        name_entery = Entry(f1, width=18, font=("bookman", 12), textvariable=self.customer_name, bd=7, relief=SUNKEN ).grid( row=0, column=1, pady=5 ) # we use f1 because everything willl be present there related to customer details

        cust_phone = Label( f1, text="Phone", font=("palatino", 20, "bold"), fg="white", bg=bg_color ).grid(
            row=0, column=2, padx=20, pady=5 )

        phone_entery = Entry( f1, width=18, textvariable=self.phone, font=("bookman", 12), bd=7, relief=SUNKEN ).grid(
            row=0, column=3, pady=5 )  # we use f1 because everything willl be present there related to customer details

        cust_bill = Label( f1, text="Bill Number", font=("palatino", 20, "bold"), fg="white", bg=bg_color ).grid(
            row=0, column=4, padx=20, pady=5 )
        bill_entery = Entry( f1, width=18, textvariable=self.bill_no, font=("bookman", 12), bd=7, relief=SUNKEN ).grid(
            row=0, column=5, pady=5 )  # we use f1 because everything willl be present there related to customer details

        bill_button = Button( f1, text="Search", command = self.find_bill, width=10, bd=7, font=("comic sans ms", 12,"bold")).grid( row=0, column=6, pady=6,
                                                                                              padx=6 )

        # ============================================= COSMETIC FRAME ========================================================

        f2 = LabelFrame( self.root, bd=10, relief=GROOVE, text="Cosmetic", font=("palatino", 22, "bold"),
                         fg="sienna",
                         bg=bg_color )  # if we use only label instead of labelframe then customer details will show in the middle
        f2.place( x=5, y=180, width=325, height=380 )

        bath = Label( f2, text="Soaps", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid( row=0,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=10,
                                                                                                              sticky="w" )  # sticky means add all labels to the west if it is not used thn all will bhi in center
        bath_entry = Entry( f2, width=10, textvariable=self.soap, font=("bookman", 12), bd=5, relief=SUNKEN ).grid( row=0,
                                                                                                                  column=1,
                                                                                                                  padx=10,
                                                                                                                  pady=10 )

        face_cream = Label( f2, text="Face cream", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid(
            row=1, column=0, padx=10, pady=10, sticky="w" )
        face_cream_entry = Entry( f2, width=10, textvariable=self.face_cream, font=("bookman", 12), bd=5,
                                  relief=SUNKEN ).grid( row=1, column=1, padx=10, pady=10 )

        face_wash = Label( f2, text="Face Wash", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid(
            row=2, column=0, padx=10, pady=10, sticky="w" )
        face_wash_entry = Entry( f2, width=10, textvariable=self.face_wash, font=("bookman", 12), bd=5,
                                 relief=SUNKEN ).grid( row=2, column=1, padx=10, pady=10 )

        hair_spray = Label( f2, text="Hair Spray", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid(
            row=3, column=0, padx=10, pady=10, sticky="w" )
        hair_spray_entry = Entry( f2, width=10, textvariable=self.spray, font=("bookman", 12), bd=5, relief=SUNKEN ).grid(
            row=3, column=1, padx=10, pady=10 )

        hair_gel = Label( f2, text="Hair Gel", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid(
            row=4, column=0, padx=10, pady=10, sticky="w" )
        hair_gel_entry = Entry( f2, width=10, textvariable=self.gell, font=("bookman", 12), bd=5, relief=SUNKEN ).grid(
            row=4, column=1, padx=10, pady=10 )

        body_lotion = Label( f2, text="Body Lotion", font=("palatino", 16, "bold"), fg="white",
                             bg=bg_color ).grid( row=5, column=0, padx=10, pady=10, sticky="w" )
        body_lotion_entry = Entry( f2, width=10, textvariable=self.lotion, font=("bookman", 12), bd=5,
                                   relief=SUNKEN ).grid( row=5, column=1, padx=10, pady=10 )

        # ============================================= GROCERYFRAME ========================================================

        f3 = LabelFrame( self.root, bd=10, relief=GROOVE, text="Grocery", font=("palatino", 22, "bold"),
                         fg="sienna", bg=bg_color )
        f3.place( x=340, y=180, width=325, height=380 )

        rice = Label( f3, text="Rice", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid( row=0,
                                                                                                             column=3,
                                                                                                             padx=10,
                                                                                                             pady=10,
                                                                                                             sticky="w" )  # sticky means add all labels to the west if it is not used thn all will bhi in center
        rice_entry = Entry( f3, width=10, textvariable=self.rice, font=("bookman", 12), bd=5, relief=SUNKEN ).grid( row=0,
                                                                                                                  column=4,
                                                                                                                  padx=10,
                                                                                                                  pady=10 )

        oil = Label( f3, text="Oil", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid( row=1,
                                                                                                           column=3,
                                                                                                           padx=10,
                                                                                                           pady=10,
                                                                                                           sticky="w" )
        oil_entry = Entry( f3, width=10, font=("bookman", 12), textvariable=self.oil, bd=5, relief=SUNKEN ).grid( row=1,
                                                                                                                column=4,
                                                                                                                padx=10,
                                                                                                                pady=10 )

        daal = Label( f3, text="Daal", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid( row=2,
                                                                                                             column=3,
                                                                                                             padx=10,
                                                                                                             pady=10,
                                                                                                             sticky="w" )
        daal_entry = Entry( f3, width=10, textvariable=self.daal, font=("bookman", 12), bd=5, relief=SUNKEN ).grid( row=2,
                                                                                                                  column=4,
                                                                                                                  padx=10,
                                                                                                                  pady=10 )

        wheat = Label( f3, text="Wheat", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid( row=3,
                                                                                                               column=3,
                                                                                                               padx=10,
                                                                                                               pady=10,
                                                                                                               sticky="w" )
        wheat_entry = Entry( f3, width=10, textvariable=self.wheat, font=("bookman", 12), bd=5, relief=SUNKEN ).grid(
            row=3, column=4, padx=10, pady=10 )

        sugar = Label( f3, text="Sugar", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid( row=4,
                                                                                                               column=3,
                                                                                                               padx=10,
                                                                                                               pady=10,
                                                                                                               sticky="w" )
        sugar_entry = Entry( f3, width=10, textvariable=self.sugar, font=("bookman", 12), bd=5, relief=SUNKEN ).grid(
            row=4, column=4, padx=10, pady=10 )

        tea = Label( f3, text="Tea", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid( row=5,
                                                                                                           column=3,
                                                                                                           padx=10,
                                                                                                           pady=10,
                                                                                                           sticky="w" )
        tea_entry = Entry( f3, width=10, textvariable=self.tea, font=("bookman", 12), bd=5, relief=SUNKEN ).grid( row=5,
                                                                                                                column=4,
                                                                                                                padx=10,
                                                                                                                pady=10 )

        # ============================================= COLD FRAME ========================================================

        f4 = LabelFrame( self.root, bd=10, relief=GROOVE, text="Cold drinks", font=("palatino", 22, "bold"),
                         fg="sienna", bg=bg_color )
        f4.place( x=680, y=180, width=325, height=380 )

        maza = Label( f4, text="Maza", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid( row=0,
                                                                                                             column=5,
                                                                                                             padx=10,
                                                                                                             pady=10,
                                                                                                             sticky="w" )  # sticky means add all labels to the west if it is not used thn all will bhi in center
        maza_entry = Entry( f4, width=10, textvariable=self.maza, font=("bookman", 12), bd=5, relief=SUNKEN ).grid( row=0,
                                                                                                                  column=6,
                                                                                                                  padx=10,
                                                                                                                  pady=10 )

        cock = Label( f4, text="Cock", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid( row=1,
                                                                                                             column=5,
                                                                                                             padx=10,
                                                                                                             pady=10,
                                                                                                             sticky="w" )
        cock_entry = Entry( f4, width=10, textvariable=self.cock, font=("bookman", 12), bd=5, relief=SUNKEN ).grid( row=1,
                                                                                                                  column=6,
                                                                                                                  padx=10,
                                                                                                                  pady=10 )

        fruity = Label( f4, text="Frooty", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid( row=2,
                                                                                                                 column=5,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w" )
        fruity_entry = Entry( f4, width=10, textvariable=self.fruity, font=("bookman", 12), bd=5, relief=SUNKEN ).grid(
            row=2, column=6, padx=10, pady=10 )

        thumbsup = Label( f4, text="Thumbs Up", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid(
            row=3, column=5, padx=10, pady=10, sticky="w" )
        thumbsup_entry = Entry( f4, width=10, textvariable=self.thumbsup, font=("bookman", 12), bd=5,
                                relief=SUNKEN ).grid( row=3, column=6, padx=10, pady=10 )

        limca = Label( f4, text="Limca", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid( row=4,
                                                                                                               column=5,
                                                                                                               padx=10,
                                                                                                               pady=10,
                                                                                                               sticky="w" )
        limca_entry = Entry( f4, width=10, textvariable=self.limca, font=("bookman", 12), bd=5, relief=SUNKEN ).grid(
            row=4, column=6, padx=10, pady=10 )

        sprit = Label( f4, text="Sprite", font=("palatino", 16, "bold"), fg="white", bg=bg_color ).grid( row=5,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w" )
        sprit_entry = Entry( f4, width=10, textvariable=self.sprite, font=("bookman", 12), bd=5, relief=SUNKEN ).grid(
            row=5, column=6, padx=10, pady=10 )

        # =======================================BILL AREA================================================================
        f5 = Frame( self.root, bd=10, relief=GROOVE )
        f5.place( x=1010, y=180, width=340, height=380 )
        bill_title = Label( f5, text="Reciept", font=("comic sans ms",15, "bold"), bd=7, relief=GROOVE ).pack( fill=X )
        scroll_y = Scrollbar( f5, orient=VERTICAL )
        self.txtarea = Text( f5, yscrollcommand=scroll_y.set )  # self is used becauze we need it throughout the page
        scroll_y.pack( side=RIGHT, fill=Y )
        scroll_y.config( command=self.txtarea.yview )
        self.txtarea.pack( fill=BOTH, expand=1 )

        # =====================================DETAILS FRAME=======================================================
        f6 = LabelFrame( self.root, bd=10, relief=GROOVE, text="Details", font=("palatino", 22, "bold"),
                         fg="sienna", bg=bg_color )
        f6.place( x=0, y=560, relwidth=1,
                  height=140 )  # relwidth means width will be set acc to the  parent or acc to screeen

        d1 = Label( f6, text="Total Cosmetic Price", bg=bg_color, fg="white",
                    font=("palatino", 14, "bold") ).grid( row=0, column=0, padx=20, pady=1, sticky="w" )
        d1_entry = Entry( f6, width=18, textvariable=self.cosmetic_price, font="bookman 10", bd=7,
                          relief=SUNKEN ).grid( row=0, column=1, padx=10, pady=1 )

        d2 = Label( f6, text="Total Grocery Price", bg=bg_color, fg="white",
                    font=("palatino", 14, "bold") ).grid( row=1, column=0, padx=20, pady=1, sticky="w" )
        d2_entry = Entry( f6, width=18, textvariable=self.grocery_price, font="bookman 10 ", bd=7,
                          relief=SUNKEN ).grid( row=1, column=1, padx=10, pady=1 )

        d3 = Label( f6, text="Total Cold Dink Price", bg=bg_color, fg="white",
                    font=("bookman", 14, "bold") ).grid( row=2, column=0, padx=20, pady=1, sticky="w" )
        d3_entry = Entry( f6, width=18, textvariable=self.cold_drink_price, font="bookman 10 ", bd=7,
                          relief=SUNKEN ).grid( row=2, column=1, padx=10, pady=1 )

        # ====================================TAX DETAILS===============================================================

        t1 = Label( f6, text="Cosmetic Tax", bg=bg_color, fg="white", font=("palatino", 14, "bold") ).grid(
            row=0, column=2, padx=20, pady=1, sticky="w" )
        t1_entry = Entry( f6, width=18, textvariable=self.cosmetic_tax, font="bookman 10 ", bd=7, relief=SUNKEN ).grid(
            row=0, column=3, padx=10, pady=1 )

        t2 = Label( f6, text="Grocery Tax", bg=bg_color, fg="white", font=("palatino", 14, "bold") ).grid( row=1, column=2, padx=20, pady=1, sticky="w" )
        t2_entry = Entry( f6, width=18, textvariable=self.grocery_tax, font="bookman 10 ", bd=7, relief=SUNKEN ).grid(
            row=1, column=3, padx=10, pady=1 )

        t3 = Label( f6, text="Cold Dink Tax", bg=bg_color, fg="white", font=("palatino", 14) ).grid(
            row=2, column=2, padx=20, pady=1, sticky="w" )
        t3_entry = Entry( f6, width=18, textvariable=self.cold_drink_tax, font=("bookman", 10 ), bd=7,
                          relief=SUNKEN ).grid( row=2, column=3, padx=10, pady=1 )

        # ===================BUTTON FRAMe FOR TOTAL, GENERATE ETC============================================
        newframe = Frame( f6, bd=7, relief=GROOVE )
        newframe.place( x=750, width=585, height=105 )

        total_btn = Button( newframe, command=self.total, text="Total", bg="sienna", fg="white", pady=15, width=10,
                            bd=3, relief=RIDGE, font="arial 14 bold" ).grid( row=0, column=0, padx=5, pady=5 )

        gbill_btn = Button( newframe, command=self.bill_area, text="Generate Bill", bg="sienna", fg="white", pady=15,
                            width=10, bd=3, relief=RIDGE, font="arial 14 bold" ).grid( row=0, column=1, padx=5,
                                                                                        pady=5 )

        clear_btn = Button( newframe, command = self.clear_data, text="Clear", bg="sienna", fg="white", pady=15, width=10, bd=3, relief=RIDGE,
                            font="arial 14 bold" ).grid( row=0, column=2, padx=5, pady=5 )

        exit_btn = Button( newframe, command = self.exit_app, text="Exit", bg="sienna", fg="white", pady=15, width=10, bd=3, relief=RIDGE,
                           font="arial 14 bold" ).grid( row=0, column=3, padx=5, pady=5 )

        self.welcome_bill()

    def total(self):  # total of particular of three mains and it means value of one spray is 40 . get means ye value milegi ya hogi
        self.c_s_p = (self.soap.get() * 40)
        self.c_fc_p = (self.face_cream.get() * 40)
        self.c_fw_p = (self.face_wash.get() * 50)
        self.c_sp_p = (self.spray.get() * 6)
        self.c_g_p = (self.gell.get() * 100)
        self.c_l_p = (self.lotion.get() * 45)
        self.total_cosmetic_price = float(
            (self.c_s_p) +
            (self.c_fc_p) +
            (self.c_fw_p) +
            (self.c_sp_p) +
            (self.c_g_p) +
            (self.c_l_p)
        )
        self.cosmetic_price.set( "Rs  " + str( self.total_cosmetic_price ) )  # now we set the value
        self.c_tax = round( (self.total_cosmetic_price * 0.1), 2 )
        self.cosmetic_tax.set( "Rs  " + str( self.c_tax ) )  # meam 10 % tax on cosmetiv

        self.g_r_p = (self.rice.get() * 15)
        self.g_o_p = (self.oil.get() * 80)
        self.g_d_p = (self.daal.get() * 60)
        self.g_w_p = (self.wheat.get() * 40)
        self.g_s_p = (self.sugar.get() * 30)
        self.g_t_p = (self.tea.get() * 70)

        self.total_grocery_price = float(
            (self.g_r_p) +
            (self.g_o_p) +
            (self.g_d_p) +
            (self.g_w_p) +
            (self.g_s_p) +
            (self.g_t_p)
        )
        self.grocery_price.set( "Rs  " + str( self.total_grocery_price ) )
        self.g_tax = round( (self.total_grocery_price * 0.05), 2 )
        self.grocery_tax.set( "Rs  " + str( self.g_tax ) )

        self.cd_m_p = (self.maza.get() * 15)
        self.cd_c_p = (self.cock.get() * 20)
        self.cd_f_p = (self.fruity.get() * 30)
        self.cd_th_p = (self.thumbsup.get() * 40)
        self.cd_l_p = (self.limca.get() * 50)
        self.cd_s_p = (self.sprite.get() * 75)

        self.total_cold_drink_price = float(
            (self.cd_m_p) +
            (self.cd_c_p) +
            (self.cd_f_p) +
            (self.cd_th_p) +
            (self.cd_l_p) +
            (self.cd_s_p)
        )
        self.cold_drink_price.set( "Rs  " + str( self.total_cold_drink_price ) )
        self.cd_tax = round( (self.total_cold_drink_price * 0.05), 2 )
        self.cold_drink_tax.set( "Rs  " + str( self.cd_tax ) )

        self.total_bill = float(
            self.total_cosmetic_price +
            self.total_grocery_price +
            self.total_cold_drink_price +
            self.c_tax +
            self.g_tax +
            self.cd_tax
        )

    def welcome_bill(self):
        self.txtarea.delete( 1.0, END )
        self.txtarea.insert( END, "\t WELCOME RIA'S MARKET \n" )
        self.txtarea.insert( END, f"\n Bill Number : {self.bill_no.get()}" )
        self.txtarea.insert( END, f"\n Customer Name : {self.customer_name.get()} " )
        self.txtarea.insert( END, f"\n Phone Number : {self.phone.get()}" )
        self.txtarea.insert( END, f"\n ===================================" )
        self.txtarea.insert( END, f"\n PRODUCT\t\tQTY\t\tPRICE" )
        self.txtarea.insert( END, f"\n ===================================" )

    def bill_area(self):
        if self.customer_name.get() == "" or self.phone.get() == "":
            messagebox.showerror( "ERROR", "CUSTOMER DETAILS REQUIRED" )
        elif self.cosmetic_price.get() == "Rs  0.0" and self.grocery_price.get() == "Rs  0.0" and self.cold_drink_price.get() == "Rs  0.0":
            messagebox.showerror( "ERROR", "NO PRODUCT IS PURCHASED" )
        else:
            self.welcome_bill()
            # =========================COSMETIC IF CONDITION FOR GENRTATING BILL=================================
            if self.soap.get() != 0:
                self.txtarea.insert( END, f"\n Bath Soap \t\t{self.soap.get()}\t\t{self.c_s_p}" )
            if self.face_cream.get() != 0:
                self.txtarea.insert( END, f"\n Face Cream \t\t{self.face_cream.get()}\t\t{self.c_fc_p}" )
            if self.face_wash.get() != 0:
                self.txtarea.insert( END, f"\n Face Wash \t\t{self.face_wash.get()}\t\t{self.c_fw_p}" )
            if self.spray.get() != 0:
                self.txtarea.insert( END, f"\n Hair Spray \t\t{self.spray.get()}\t\t{self.c_sp_p}" )
            if self.gell.get() != 0:
                self.txtarea.insert( END, f"\n Hair Gell \t\t{self.gell.get()}\t\t{self.c_g_p}" )
            if self.lotion.get() != 0:
                self.txtarea.insert( END, f"\n Body Lotion \t\t{self.lotion.get()}\t\t{self.c_l_p}" )

            # =========================GROCERY IF CONDITION FOR GENRTATING BILL=================================
            if self.rice.get() != 0:
                self.txtarea.insert( END, f"\n Rice \t\t{self.rice.get()}\t\t{self.g_r_p}" )
            if self.oil.get() != 0:
                self.txtarea.insert( END, f"\n Oil \t\t{self.oil.get()}\t\t{self.g_o_p}" )
            if self.daal.get() != 0:
                self.txtarea.insert( END, f"\n Daal \t\t{self.daal.get()}\t\t{self.g_d_p}" )
            if self.wheat.get() != 0:
                self.txtarea.insert( END, f"\n Wheat \t\t{self.wheat.get()}\t\t{self.g_w_p}" )
            if self.sugar.get() != 0:
                self.txtarea.insert( END, f"\n Sugar \t\t{self.sugar.get()}\t\t{self.g_w_p}" )
            if self.tea.get() != 0:
                self.txtarea.insert( END, f"\n Tea \t\t{self.tea.get()}\t\t{self.g_t_p}" )

            # =========================COLD DRINK IF CONDITION FOR GENRTATING BILL=================================
            if self.maza.get() != 0:
                self.txtarea.insert( END, f"\n Maza \t\t{self.maza.get()}\t\t{self.cd_m_p}" )
            if self.cock.get() != 0:
                self.txtarea.insert( END, f"\n Cock \t\t{self.cock.get()}\t\t{self.cd_c_p}" )
            if self.fruity.get() != 0:
                self.txtarea.insert( END, f"\n Fruity \t\t{self.fruity.get()}\t\t{self.cd_f_p}" )
            if self.thumbsup.get() != 0:
                self.txtarea.insert( END, f"\n Thumbs Up \t\t{self.thumbsup.get()}\t\t{self.cd_th_p}" )
            if self.limca.get() != 0:
                self.txtarea.insert( END, f"\n Limca \t\t{self.limca.get()}\t\t{self.cd_l_p}" )
            if self.sprite.get() != 0:
                self.txtarea.insert( END, f"\n Sprite \t\t{self.sprite.get()}\t\t{self.cd_s_p}" )

            self.txtarea.insert( END, f"\n -----------------------------------" )

            if self.cosmetic_tax.get() != "Rs  0.0":
                self.txtarea.insert( END,
                                     f"\n COSMETIC TAX\t\t\t{self.cosmetic_tax.get()}" )  # throgh .get we fetch the value

            if self.grocery_tax.get() != "Rs  0.0":
                self.txtarea.insert( END, f"\n GROCERY TAX\t\t\t{self.grocery_tax.get()}" )

            if self.cold_drink_tax.get() != "Rs  0.0":
                self.txtarea.insert( END, f"\n COLD DRINK TAX\t\t\t{self.cold_drink_tax.get()}" )

            self.txtarea.insert( END, f"\n Total Bill \t\t\t Rs  {str( self.total_bill )}" )
            self.txtarea.insert( END, f"\n ------------------------------------" )
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno( "Save Bill", "Do you want to save Bill?" )
        if op > 0:
            self.bill_data = self.txtarea.get( 1.0, END )# 1.0 se end tk ye data get krle
            save_path = "C:/DELL/"
            b1_name = str( self.bill_no.get()) # here we opn python billing software file from os and put a file with name bill no. and it should be txt file and in read mode
            b1_complete = os.path.join(save_path, b1_name +".txt")
            file1 = open(b1_complete, "w")
            file1.write( self.bill_data )
            file1.close()
            messagebox.showinfo("Saved")
        else:
            return

    def find_bill(self):
        present = "no"

        for i in os.listdir("save_path"):
            if i.split('.')[0] ==self.search_bill.get():
                b1 = open("C:/DELL/" )
                self.txtarea.delete(1.0,END)
                for d in b1:
                    self.txtarea.insert(END, d)
                b1.close()
                present = "yes"
        if present =="no" :
            messagebox.showerror("ERROR", "INVALID BILL NUMBER")

    def clear_data(self):
        op = messagebox.askyesno( "EXIT", "DO YOU WANT TO CLEAR?" )
        if op > 0: # greater than 0 mean yea
            # ==================================COSMETIC VARIABLES========================================\
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.lotion.set(0)

            # ===========================================GROCERY VARIABLES============================================
            self.rice.set(0)
            self.oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # ==========================================COLD DRINK VARIABLES==========================================
            self.maza.set(0)
            self.cock.set(0)
            self.fruity.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # =============================CUSTOMER VARIABLES===============================================
            self.customer_name.set("")
            self.phone.set("")
            self.bill_no.set("")
            x = random.randint( 1000, 9999 )
            self.bill_no.set( str( x ))
            self.search_bill.set("")

            # ========================================== DETAILS (PRICE & TAX) VARIABLES========================================
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("EXIT", "DO YOU WANT TO EXIT?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App( root )
root.mainloop()
