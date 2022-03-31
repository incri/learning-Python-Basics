Data_type = {

"W" : "Weight",
"KG": "kilo_gram",
"G": "gram",
"L" : "Length",
"KM": "Kilo_meter",
"M" : "meter",

}


def kg_to_g (data):
    convert  = int (data) * 1000
    return convert


def g_to_kg (data):
    convert = int (data) / 1000
    return convert


def km_to_m (data):
    convert = int (data) * 1000
    return convert


def m_to_km (data):
        convert = int (data) / 1000
        return convert



        
print (
"\t","W =>",Data_type["W"],"\n",
"\t","L =>",Data_type["L"],"\n",
)

data_type = input ("Enter your data type : ")

if (data_type) == "W":
    print (
    "\t","KG =>",Data_type["KG"],"\n",
    "\t","G =>",Data_type["G"],"\n",
    )

    sub_data_type = input ("Enter your data type :")
    
    if sub_data_type == "KG":
        info = input ("enter your data :")

        print ("In gram =" + str(kg_to_g(info)))
        
    else :
        info = input ("enter your data :")
        
        print ("In kilogram =" + str(g_to_kg(info)))
        
else :
    print (
    "\t","KM =>",Data_type["KM"],"\n",
    "\t","M =>",Data_type["M"],"\n",
    )
         
    sub_data_type = input ("Enter your data type :")
         
    if sub_data_type == "KM":
        info = input ("enter your data :")
         
        print ("In meter =" + str(km_to_m(info)))
        
    else :
        info = input ("enter your data :")
        print ("In kilometer =" + str(m_to_km(info)))     


    

    


   
