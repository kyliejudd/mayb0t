
export CONSUMER_KEY=$(aws ssm get-parameter --name /twitter/consumerKey --with-decryption  --profile personal | jq -r '.Parameter.Value' )

export CONSUMER_SECRET=$(aws ssm get-parameter --name /twitter/consumerSecret --with-decryption  --profile personal | jq -r '.Parameter.Value')

export ACCESS_KEY=$(aws ssm get-parameter --name /twitter/accessKey --with-decryption  --profile personal | jq -r '.Parameter.Value')

export ACCESS_SECRET=$(aws ssm get-parameter --name /twitter/accessSecret --with-decryption  --profile personal | jq -r '.Parameter.Value')

python -c 'import main; main.tweet_top_consituency("foo","bar")'


python -c 'import main; main.tweet_top_10_countries("foo","bar")'
