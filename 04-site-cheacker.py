import urllib.request as urllib

def main(url):
    response = urllib.urlopen(url)
    print("Connected to site ",url )
    print("the responsecode was ", response.getcode())

input_url= input("Input the url of the site:")

main(input_url)