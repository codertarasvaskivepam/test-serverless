
### Serverless Commands
#### Install all required modules

```bash
npm install -g serverless
npm install
```
#### Deploy serverless resources
```bash
serverless deploy --env dev
```
#### To remove serverless resources
```bash
serverless remove
```

#### To start workflow just curl it
```curl
curl -X POST  https://oy1gmsbq5b.execute-api.us-east-1.amazonaws.com/dev/shop
```

### Cloudformation commands
#### Install awscli
```bash
source venv/bin/activate
pip install awscli
```
#### To delete cloudformation stack
```bash
aws cloudformation delete-stack --stack-name test-serverless
```
#### set-up githubtoken
```bash
export githubtoken=your_token
```