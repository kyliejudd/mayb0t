# Mayb0t

Just messing about with json returned from the petitions site. 

Mayb0t is pretty straight forward connect to your fav petition and get the json https://petition.parliament.uk/petitions/241584.json 

Then sort the two dictionaries and tweet them. 

This runs in aws lambda hence the serverless config.

### create your aws ssm secure parameters to hold twitter stuff

`aws ssm put-parameter --name /twitter/accessKey --type SecureString --value YOUR_ACCESS_KEY  --profile personal --region eu-west-1` 

rinse and repeat for all params needed. 

### serverless 

Install serverless 
https://serverless.com/ 

```
serverless create --template aws-python3 --path mayb0t
cd mayb0t/
sls plugin install -n serverless-python-requirements
virtualenv -p $(which python3.6) env
source env/bin/activate
pip install -r requirements.txt
```

edit your serverless as desired. 
and deploy 
`serverless deploy --profile personal`

### todo 
fooking petitions site keeps going down might need to handle that better.
