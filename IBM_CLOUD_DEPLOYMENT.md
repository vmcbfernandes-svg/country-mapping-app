# IBM Cloud Code Engine Deployment Guide

This guide explains how to deploy your Country Mapping App to IBM Cloud Code Engine.

## Prerequisites

1. **IBM Cloud Account** (IBMers have access)
2. **IBM Cloud CLI** installed
3. **Docker** installed (for local testing)
4. **Code Engine plugin** for IBM Cloud CLI

## Step 1: Install IBM Cloud CLI Tools

```bash
# Install IBM Cloud CLI (if not already installed)
# Windows: Download from https://cloud.ibm.com/docs/cli

# Install Code Engine plugin
ibmcloud plugin install code-engine

# Login to IBM Cloud
ibmcloud login --sso
```

## Step 2: Set Up Code Engine Project

```bash
# Target your resource group
ibmcloud target -g Default

# Create a Code Engine project (or use existing)
ibmcloud ce project create --name country-mapping-app

# Select the project
ibmcloud ce project select --name country-mapping-app
```

## Step 3: Build and Deploy

### Option A: Deploy from Local Source (Recommended)

```bash
# Navigate to your app directory
cd c:/Users/VitorManuelBarbosaFe/Desktop/country-mapping-app

# Build and deploy in one command
ibmcloud ce application create \
  --name country-mapping-app \
  --build-source . \
  --strategy dockerfile \
  --port 8501 \
  --min-scale 0 \
  --max-scale 1 \
  --cpu 0.25 \
  --memory 0.5G \
  --env-from-configmap my-config
```

### Option B: Deploy from Container Registry

```bash
# 1. Build Docker image locally
docker build -t country-mapping-app:latest .

# 2. Tag for IBM Container Registry
docker tag country-mapping-app:latest us.icr.io/<your-namespace>/country-mapping-app:latest

# 3. Login to IBM Container Registry
ibmcloud cr login

# 4. Push image
docker push us.icr.io/<your-namespace>/country-mapping-app:latest

# 5. Deploy to Code Engine
ibmcloud ce application create \
  --name country-mapping-app \
  --image us.icr.io/<your-namespace>/country-mapping-app:latest \
  --port 8501 \
  --min-scale 0 \
  --max-scale 1 \
  --cpu 0.25 \
  --memory 0.5G
```

## Step 4: Access Your Application

```bash
# Get application URL
ibmcloud ce application get --name country-mapping-app

# The output will show your app URL, e.g.:
# https://country-mapping-app.xxxxxx.us-south.codeengine.appdomain.cloud
```

## Configuration Options

### Scaling
- `--min-scale 0`: Scale to zero when not in use (saves resources)
- `--max-scale 1`: Maximum 1 instance (sufficient for internal tool)
- Increase max-scale for higher traffic

### Resources
- `--cpu 0.25`: 0.25 vCPU (free tier friendly)
- `--memory 0.5G`: 512MB RAM (sufficient for Streamlit)
- Adjust based on usage

### Environment Variables
```bash
# Add environment variables if needed
ibmcloud ce application update \
  --name country-mapping-app \
  --env KEY=VALUE
```

## Free Tier Limits

IBM Cloud Code Engine free tier includes:
- **100,000 vCPU-seconds** per month
- **200,000 GB-seconds** per month
- Sufficient for internal tools with moderate usage

**Example calculation:**
- 0.25 vCPU × 0.5GB × 3600 seconds = 450 vCPU-seconds per hour
- ~222 hours of runtime per month within free tier

## Updating Your Application

```bash
# Update from source
ibmcloud ce application update \
  --name country-mapping-app \
  --build-source .

# Or update from new image
ibmcloud ce application update \
  --name country-mapping-app \
  --image us.icr.io/<your-namespace>/country-mapping-app:v2
```

## Monitoring

```bash
# View application status
ibmcloud ce application get --name country-mapping-app

# View logs
ibmcloud ce application logs --name country-mapping-app

# Follow logs in real-time
ibmcloud ce application logs --name country-mapping-app --follow
```

## Security Considerations

### 1. Data Sensitivity
- Your Excel file contains country mapping data
- Ensure compliance with IBM data policies
- Consider using IBM Cloud Object Storage for sensitive data

### 2. Access Control
- Code Engine apps are public by default
- Add authentication if needed:
  ```bash
  ibmcloud ce application update \
    --name country-mapping-app \
    --visibility private
  ```
- Use IBM App ID for SSO authentication

### 3. Network Security
- Apps run in isolated containers
- Use IBM Cloud VPC for additional network isolation

## Troubleshooting

### Build Fails
```bash
# Check build logs
ibmcloud ce buildrun logs --name <buildrun-name>

# Common issues:
# - Missing files in Dockerfile
# - Incorrect file paths
# - Dependencies not in requirements.txt
```

### Application Won't Start
```bash
# Check application logs
ibmcloud ce application logs --name country-mapping-app

# Common issues:
# - Port mismatch (ensure --port 8501)
# - Missing Excel file
# - Memory/CPU limits too low
```

### Slow Performance
- Increase CPU/memory allocation
- Check if scaling to zero causes cold starts
- Set min-scale to 1 for always-on availability

## Cost Optimization

1. **Scale to Zero**: Use `--min-scale 0` for infrequent use
2. **Right-size Resources**: Start small, monitor, adjust
3. **Monitor Usage**: Check IBM Cloud dashboard regularly
4. **Set Alerts**: Configure billing alerts

## Alternative: Deploy via Web Console

1. Go to https://cloud.ibm.com/codeengine
2. Create or select a project
3. Click "Create" → "Application"
4. Choose "Source code" or "Container image"
5. Configure settings (port 8501, resources)
6. Click "Create"

## Support

- **IBM Cloud Docs**: https://cloud.ibm.com/docs/codeengine
- **IBM Cloud Support**: Open ticket via IBM Cloud console
- **Internal IBM Slack**: #ibm-cloud-code-engine

## Next Steps

1. Deploy your app using Option A (simplest)
2. Test the application URL
3. Share with team members
4. Monitor usage and costs
5. Consider adding authentication for production use