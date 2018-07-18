curl -X GET -G \
  'https://api.foursquare.com/v2/venues/explore' \
    -d client_id="" \
    -d client_secret="" \
    -d v="20180323" \
    -d ll="40.7243,-74.0018" \
    -d query="coffee" \
    -d limit=1

curl -X GET -G \
  'https://api.foursquare.com/v2/checkins/recent' \
    -d oauth_token="" \
    -d v="20180718" \
    -d limit=1
    
curl 'https://foursquare.com/oauth2/authenticate
?client_id=YOUR_CLIENT_ID
&response_type=code
&redirect_uri=YOUR_REGISTERED_REDIRECT_URI'


    
curl 'https://foursquare.com/oauth2/authenticate
?client_id=YOUR_CLIENT_ID
&response_type=code
&redirect_uri=YOUR_REGISTERED_REDIRECT_URI'

