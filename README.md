# CAIP - Text-to-Speech Pipeline

This project uses AWS Polly to convert text files to MP3 audio files and automatically uploads them to S3 via GitHub Actions workflows.

## Setup

### AWS Credentials and S3 Bucket

1. **Create AWS IAM User:**
   - Go to AWS IAM Console → Users → Create User
   - Attach policies: `AmazonPollyFullAccess` and `AmazonS3FullAccess`
   - Create Access Key (Access Key ID and Secret Access Key)

2. **Create S3 Buckets:**
   - Create two S3 buckets: one for production, one for beta
   - Note the bucket names and desired paths (e.g., `my-bucket/prod/` or `my-bucket/beta/`)

3. **Configure GitHub Secrets:**
   - Go to your repository → Settings → Secrets and variables → Actions
   - Add the following secrets:
     - `AWS_ACCESS_KEY_ID` - Your AWS Access Key ID
     - `AWS_ACCESS_KEY` - Your AWS Secret Access Key
     - `AWS_REGION` - Your AWS region (e.g., `us-east-1`)
     - `S3_BUCKET_PROD` - Production S3 bucket name
     - `S3_BUCKET_PROD_PATH` - Production S3 path (e.g., `audio/prod/`)
     - `S3_BUCKET_BETA` - Beta S3 bucket name
     - `S3_BUCKET_PATH_BETA` - Beta S3 path (e.g., `audio/beta/`)

## Usage

### Modifying the Text

1. Edit `speech.txt` with your desired text content
2. The script reads this file and converts it to speech using AWS Polly
3. The output is saved as `example.mp3` and uploaded to S3

### Triggering Workflows

**Production Workflow (on_merge.yml):**
- Automatically triggers when you push to the `main` branch
- Uploads MP3 to the production S3 bucket

**Beta Workflow (on_pull_request.yml):**
- Automatically triggers when you create or update a pull request
- Uploads MP3 to the beta S3 bucket

**Manual Trigger:**
- You can also manually trigger workflows from the Actions tab in GitHub

## Verifying Uploaded MP3 Files

1. **Via AWS Console:**
   - Go to AWS S3 Console
   - Navigate to your configured bucket and path
   - Look for `example.mp3` file
   - Check the timestamp to verify it's the latest upload

2. **Via AWS CLI:**
   ```bash
   aws s3 ls s3://YOUR_BUCKET_NAME/YOUR_PATH/
   ```

3. **Via GitHub Actions:**
   - Go to Actions tab in your repository
   - Check the workflow run logs
   - Look for the "Convert txt to mp3" step output
   - Verify the S3 upload command completed successfully

## Local Testing (Optional)

To test locally before pushing:

```bash
pip install boto3
# Set AWS credentials via environment variables or AWS CLI
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1

python synthesize.py
```

The script will generate `example.mp3` locally.
