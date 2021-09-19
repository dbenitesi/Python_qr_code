#importar pandas como pd
import pandas as pd
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer, RoundedModuleDrawer
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask, RadialGradiantColorMask
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=25,
    border=1,
    )
i= 1
registros= 8
#ssid= df['SSID'][i]
while registros > i:
    hide="True"
    atype="WPA"
    #clave=df['PASS'][i]
    path_file = "data.xlsx"
    col_types = {"SSID":str,"PASS":str }
    n_hoja = "data"
        #Leer el excel
    df= pd.read_excel(path_file, sheet_name=n_hoja, dtype=col_types)
        #df.columns.values
        
        # Wifi Structure to print on QR
    ssid= df['SSID'][i]
    clave=df['PASS'][i]
    i = i + 1
    todo= "WIFI:T:%s;S:%s;P:%s;H:%s" % (atype,ssid,clave,hide)
        #print(todo)
    #ruta del excel 
    #def Impresion():
        # Wifi Structure to print on QR
        # WiFi Verification
    print(todo)
        # Adding $todo to data ima
    qr.add_data(todo)
        # Setting properity to size image
    qr.make(fit=True)
        # Getting the king of QR
    img = qr.make_image(image_factory=StyledPilImage)
        # Saving the code in a file
    img.save(ssid+".png")
    
    







#imprime= df.loc[[i],"SSID"]
#print(imprime)
# ssid1=df["SSID"]
# print(ssid1)

