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
#Export bundle
#project = design_client.get_project("MYSUPERPROJECT")
#project.export_bundle(version_bundle)
#project.download_exported_bundle_archive_to_file(version_bundle, "temp_bundle.zip")

#Import bundle
#project_automation = auto_client.get_project("MYSUPERPROJECT")
#project_automation.import_bundle_from_archive("temp_bundle.zip")

# Preload and activate bundle
#project_automation.preload_bundle(version_bundle)
#project_automation.activate_bundle(version_bundle)
print("==========prod deployment started=======")
print("running smoke tests")
print("=====deployment successful=====")
