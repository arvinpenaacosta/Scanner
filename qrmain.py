from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from fastapi.responses import RedirectResponse
from fastapi import Response

from contextlib import closing
import datetime

import uvicorn


app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"))


app.mount("/static", StaticFiles(directory="static"), name="static")
#app.mount("/templates", StaticFiles(directory="templates"))

templates = Jinja2Templates(directory="templates")



#===================================================================
@app.get("/")
async def home(
        request: Request
        ):

    print("STARTING WEB APP - PAYPAL SCANNER")
    #return templates.TemplateResponse("signon.html", 
    return templates.TemplateResponse("masterpage.html", 
        {"request": request}
        )




#===================================================================
@app.get("/tmob")
async def home(
        request: Request
        ):

    print("STARTING WEB APP - TMOB SCANNER")
    #return templates.TemplateResponse("signon.html", 
    return templates.TemplateResponse("scan_tmob.html", 
        {"request": request}
        )


#===================================================================
@app.get("/paypal")
async def home(
        request: Request
        ):

    print("STARTING WEB APP - PAYPAL SCANNER")
    #return templates.TemplateResponse("signon.html", 
    return templates.TemplateResponse("scan_paypal.html", 
        {"request": request}
        )

#===================================================================
@app.get("/paypalpage3")
async def home(
        request: Request
        ):

    print("STARTING WEB APP - PAYPAL SCANNER3")
    #return templates.TemplateResponse("signon.html", 
    return templates.TemplateResponse("touchmanual.html", 
        {"request": request}
        )

#===================================================================
@app.get("/paypalpage4")
async def home(
        request: Request
        ):

    print("STARTING WEB APP - PAYPAL SCANNER4")
    #return templates.TemplateResponse("signon.html", 
    return templates.TemplateResponse("pp_scan_manual.html", 
        {"request": request}
        )

#===================================================================
@app.get("/paypalpage5")
async def home(
        request: Request
        ):

    print("STARTING WEB APP - PAYPAL SCANNER5")
    #return templates.TemplateResponse("signon.html", 
    return templates.TemplateResponse("pp_scan.html", 
        {"request": request}
        )

#===================================================================
@app.get("/test1")
async def home(
        request: Request
        ):

    print("STARTING WEB APP - PAYPAL SCANNER5")
    #return templates.TemplateResponse("signon.html", 
    #return templates.TemplateResponse("touchmouse2.html", 
    return templates.TemplateResponse("touchmouse.html", 
    #return templates.TemplateResponse("qrlocal.html", 
    #       return templates.TemplateResponse("saveget2.html", 

        {"request": request}
        )

#===================================================================
@app.post("/upload")
async def process_scan(
    request: Request, 
    scaninput1: str = Form(...),
    scaninput2: str = Form(...),
    scaninput3: str = Form(...),
    scaninput4: str = Form(...),
    scaninput5: str = Form(...),
    scaninput6: str = Form(...),
):

    print(scaninput1)
    print(scaninput2)
    print(scaninput3)
    print(scaninput4)
    print(scaninput5)
    print(scaninput6)
    
    #if scaninput1 is None and scaninput2 is None and scaninput3 is None and scaninput4 is None:
    #    okmsg = "FAILED: Scan Data is not complete..."
    #else:
    #    okmsg = "Successful Upload..."

    return templates.TemplateResponse("pp_scan.html",
        {   
            "request": request, 
            "scaninput1": scaninput1,
            "scaninput2": scaninput2,
            "scaninput3": scaninput3,
            "scaninput4": scaninput4,
            #"ok_message": okmsg
        }
    )


#===================================================================
@app.post("/upload")
async def process_scan(
    request: Request, 
    qrCodeValue1: str = Form(...),
    qrCodeValue2: str = Form(...)
):

    #print(qrCodeValue1)
    #print(qrCodeValue2)

    # Split the text into lines
    values = parse_text(qrCodeValue2)

    # Access the extracted values
    print(values["Computer Name"])
    print(values["Serial Number"])
    print(values["Mac Address"])
    

    if values["Computer Name"] is None:
        okmsg = "FAILED: QR Info not supported..."
    else:
        okmsg = "Successful Upload..."


    
    return templates.TemplateResponse("scan.html",
        {   
            "request": request, 
            "qrCodeValue1": qrCodeValue1,
            "qrCodeValue2": qrCodeValue2,
            "ok_message": okmsg
        }
    )




def parse_text(text):
    # Split the text into lines
    lines = text.split('\n')

    # Initialize variables to store values
    computer_name = None
    serial_number = None
    mac_address = None

    # Loop through each line and extract the values
    for line in lines:
        if line.startswith("Computer Name:"):
            computer_name = line.split(":")[1].strip()
        elif line.startswith("Serial Number:"):
            serial_number = line.split(":")[1].strip()
        elif line.startswith("Mac Address:"):
            mac_address = line.split(":")[1].strip()

    # Return the extracted values as a dictionary
    return {
        "Computer Name": computer_name,
        "Serial Number": serial_number,
        "Mac Address": mac_address
    }






if __name__ == "__main__":
    

    #uvicorn.run(app, host="0.0.0.0", port=8886)
    uvicorn.run(app, host="0.0.0.0")




# python -m venv <new env>


# python -m http.server 8887
# python -m http.server --bind 192.168.1.5 8887

# https://kb.firedaemon.com/support/solutions/articles/4000121705-openssl-3-1-3-0-and-1-1-1-binary-distributions-for-microsoft-windows

# pip install pyOpenSSL
# openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365
# openssl rsa -in server.key -out server_unencrypted.key


# uvicorn --host 192.168.1.5 --port 8887 --ssl-keyfile server_unencrypted.key --ssl-certfile server.crt --reload qrmain:app
# uvicorn --host 192.168.1.5 --port 8887 --ssl-keyfile server.key --ssl-certfile server.crt --reload qrmain:app

# uvicorn --host 192.168.1.33 --port 8887 --ssl-keyfile server_unencrypted.key --ssl-certfile server.crt --reload qrmain:app

# uvicorn --host 192.168.1.16 --port 8886 --ssl-keyfile server_unencrypted.key --ssl-certfile server.crt --reload qrmain:app