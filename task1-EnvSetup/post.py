from subprocess import call
# test docker 
call("docker run --rm hello-world", shell=True) # it will auto run and delete container
# clone MLOps Repo
call("git clone https://github.com/DataTalksClub/mlops-zoomcamp.git", shell=True)
# creating notebooks data dir
call("mkdir -p ~/notebooks/data/", shell=True)
# getting data
# ref: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
call("wget https://nyc-tlc.s3.amazonaws.com/trip+data/green_tripdata_2022-01.parquet -O ~/notebooks/data/jan.parquet", shell=True)
# to get Feb 2022 data while above one is of Jan, 22.
call("wget https://nyc-tlc.s3.amazonaws.com/trip+data/green_tripdata_2022-02.parquet -O ~/notebooks/data/feb.parquet", shell=True)
