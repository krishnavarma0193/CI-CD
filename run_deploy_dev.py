import dataikuapi

#Define the connections

#Design
host = "https://dss-1a544458-915ab95d-dku.us-east-1.app.dataiku.io/"
apiKey = "Foo123Foo123F123Foo123"

#Automation
host_auto = "http://localhost:23456"
apiKey_auto = "Bar234Bar234Bar234Bar234"

#design_client= dataikuapi.DSSClient(host, apiKey)
#auto_client = dataikuapi.DSSClient(host_auto, apiKey_auto)

version_bundle = "bundle_v1"
print("=======dev deployment and running tests==========")
print("=======tests successful, going for prod deployment=============")
