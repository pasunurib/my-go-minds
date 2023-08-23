from tkinter import *
#Functionality Part
def total():
    soapprice=int(bathsoapEntry.get())*20
    facecream=int(faceCreamEntry.get())*50
    facewash= int(facewashEntry.get()) * 100
    haircream = int(hairsprayEntry.get()) * 150
    hairgell= int(hairgelentry.get()) * 50
    bodylotion = int(bodylotionEntry.get()) * 60

    Totalcosmeticprice =soapprice+facecream+facewash+haircream+hairgell+bodylotion
    cosmeticpriceEntry.insert(0,f'{Totalcosmeticprice} Rs')















'''GUI '''
root=Tk()
root.title('Tea Shop Bill')
root.geometry('1200x600')
root.iconbitmap('icon.ico')
headinglabel=Label(root,text='BILL PAYMENT',font=('Arial',30,'bold')
                   ,bg='gray20',fg='gold',bd=12,relief=GROOVE)
headinglabel.pack(fill=X)

#Body Heading
customer_details_frame=LabelFrame(root,text='Customer Details',font=('Arial',15,'bold',)
                                  ,fg='gold',relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)

#Name Label
name_label=Label(customer_details_frame,text='Name',font=('Arial',15,'bold'),bg='gray20',
                 fg='white')

name_label.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',12),bd=7,width=16)
nameEntry.grid(row=0,column=1,padx=8)

#Phone Label code
phone_label=Label(customer_details_frame,text='Phone Number',font=('Arial',15,'bold'),bg='gray20',
                 fg='white')

phone_label.grid(row=0,column=2,padx=20)
phoneEntry=Entry(customer_details_frame,font=('arial',12),bd=7,width=16)
phoneEntry.grid(row=0,column=3,padx=8)

#Bill Number Label

bill_num_label=Label(customer_details_frame,text='Bill Number',font=('Arial',15,'bold'),bg='gray20',
                 fg='white')

bill_num_label.grid(row=0,column=4,padx=20)

billnumEntry=Entry(customer_details_frame,font=('arial',12),bd=7,width=16)
billnumEntry.grid(row=0,column=5,padx=8)

#Search Button

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=12)
searchButton.grid(row=0,column=6,padx=20,pady=8)

#Products Frame

productsFrame=Frame(root)
productsFrame.pack(fill=X)

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold')
                                  ,fg='gold',relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)

#Bath Soap
bathsoaplabel=Label(cosmeticsFrame,text='Bath Soap',font=('Arial',12,'bold',)
                                  ,fg='white',bg='gray20')
bathsoaplabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)
#Face Cream
facecreamlabel=Label(cosmeticsFrame,text='Face Cream',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
facecreamlabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

faceCreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
faceCreamEntry.grid(row=1,column=1,pady=9,padx=10)
faceCreamEntry.insert(0,0)
#Face Wash

facewashlabel=Label(cosmeticsFrame,text='Face Wash',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
facewashlabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)
#Hairspray

hairsparylabel=Label(cosmeticsFrame,text='Hair Spray',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
hairsparylabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)
#Hair Gel

hairGellabel=Label(cosmeticsFrame,text='Hair Gell',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
hairGellabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelentry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelentry.grid(row=4,column=1,pady=9,padx=10)
hairgelentry.insert(0,0)
#Body Lotion

bodylotionlabel=Label(cosmeticsFrame,text='Body Lotion',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
bodylotionlabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

#(Grocery Column)
groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold')
                                  ,fg='gold',relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

#Rice
ricelabel=Label(groceryFrame,text='Rice',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
ricelabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)
#Oil

oillabel=Label(groceryFrame,text='Oil',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
oillabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)
#Daal
daallabel=Label(groceryFrame,text='Daal',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
daallabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

daallEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daallEntry.grid(row=2,column=1,pady=9,padx=10)
daallEntry.insert(0,0)
#Wheat

wheatlabel=Label(groceryFrame,text='Wheat',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
wheatlabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)
#Sugar

sugarlabel=Label(groceryFrame,text='Sugar',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
sugarlabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)

sugarEntry.insert(0,0)
#Tea Powder

tealabel=Label(groceryFrame,text='Tea Power',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
tealabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10)

teaEntry.insert(0,0)
#Cool Drinks

cooldrinkFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold')
                                  ,fg='gold',relief=GROOVE,bg='gray20')
cooldrinkFrame.grid(row=0,column=2)

#Maaza

maazalabel=Label(cooldrinkFrame,text='Maaza',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
maazalabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

maazaEntry=Entry(cooldrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)

maazaEntry.insert(0,0)
#Thumsup

tumsuplabel=Label(cooldrinkFrame,text='Thums Up',font=('arial',12,'bold')
                                  ,fg='white',bg='gray20')
tumsuplabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

tumsupEntry=Entry(cooldrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
tumsupEntry.grid(row=1,column=1,pady=9,padx=10)

tumsupEntry.insert(0,0)
#Pepsi

pepsilabel=Label(cooldrinkFrame,text='Pepsi',font=('arial',12,'bold')
                                  ,fg='white',bg='gray20')
pepsilabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(cooldrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=2,column=1,pady=9,padx=10)

pepsiEntry.insert(0,0)
#sprite

spritelabel=Label(cooldrinkFrame,text='Sprite',font=('arial',12,'bold')
                                  ,fg='white',bg='gray20')
spritelabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

spriteEntry=Entry(cooldrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=3,column=1,pady=9,padx=10)

spriteEntry.insert(0,0)
#Dew

dewlabel=Label(cooldrinkFrame,text='Dew',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
dewlabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

dewEntry=Entry(cooldrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=4,column=1,pady=9,padx=10)

dewEntry.insert(0,0)
#Frooti

frootilabel=Label(cooldrinkFrame,text='Frooti',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
frootilabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

frootiEntry=Entry(cooldrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=5,column=1,pady=9,padx=10)

frootiEntry.insert(0,0)
#Bill Frame

billFrame=Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=10)

billarealabel=Label(billFrame,text='Bill Area',font=('times new roman',13,'bold'),bd=7,relief=GROOVE)
billarealabel.pack(fill=X)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billFrame,height=18,width=60,yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

#Bill Menu

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',13,'bold')
                                  ,fg='gold',relief=GROOVE,bg='gray20')
billmenuFrame.pack(fill=X)


#Cosmestic cosmeticprice
cosmeticpricelabel=Label(billmenuFrame,text='Cosmetic Price',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
cosmeticpricelabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=9,padx=10)

#Grocery Price

grocerypricelabel=Label(billmenuFrame,text='Grocery Price',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
grocerypricelabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=9,padx=10)

#Cool drigrocery

colddrinkpricelabel=Label(billmenuFrame,text='ColdDrink Price',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
colddrinkpricelabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

colddrinkpriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
colddrinkpriceEntry.grid(row=2,column=1,pady=9,padx=10)



#Cosmestic cosmeticprice
cosmetictaxlabel=Label(billmenuFrame,text='Cosmetic Tax',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
cosmetictaxlabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=9,padx=10)

#Grocery Price

grocerytaxlabel=Label(billmenuFrame,text='Grocery Tax',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
grocerytaxlabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=9,padx=10)

#Cool drigrocery

colddrinktaxlabel=Label(billmenuFrame,text='ColdDrink Tax',font=('arial',12,'bold',)
                                  ,fg='white',bg='gray20')
colddrinktaxlabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')

colddrinktaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
colddrinktaxEntry.grid(row=2,column=3,pady=9,padx=10)

#Button Frame

Buttonframe=Frame(billmenuFrame,bd=8,relief=GROOVE)
Buttonframe.grid(row=0,column=4,rowspan=3)

#total Button
totalbutton=Button(Buttonframe,text='Total',font=('arial',14,'bold'),bg='gray20',fg='white',bd=5,width=8
                   ,pady=10,command=total)
totalbutton.grid(row=0,column=0,pady=20)

#Bill bbill

billbutton=Button(Buttonframe,text='Bill',font=('arial',14,'bold'),bg='gray20',fg='white',bd=5,width=8
                   ,pady=10)
billbutton.grid(row=0,column=1,pady=20)

#Email

emailbutton=Button(Buttonframe,text='Email',font=('arial',14,'bold'),bg='gray20',fg='white',bd=5,width=8
                   ,pady=10)
emailbutton.grid(row=0,column=2,pady=20)

#Print
printbutton=Button(Buttonframe,text='Print',font=('arial',14,'bold'),bg='gray20',fg='white',bd=5,width=8
                   ,pady=10)
printbutton.grid(row=0,column=3,pady=20)

#clear

clearbutton=Button(Buttonframe,text='clear',font=('arial',14,'bold'),bg='gray20',fg='white',bd=5,width=8
                   ,pady=10)
clearbutton.grid(row=0,column=4,pady=20)



























root.mainloop()