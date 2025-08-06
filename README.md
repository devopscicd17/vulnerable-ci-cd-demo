# AWS CI/CD Vulnerability Demo

This repository demonstrates a vulnerable Flask web app integrated with:

- **Snyk**: SAST & SCA scanning with SARIF generation
- **TruffleHog**: Secrets detection in source and Git history
- **OWASP ZAP**: Runtime DAST baseline scan

## Features

- CI/CD via AWS CodePipeline (CodeCommit → CodeBuild → CodeDeploy)
- `buildspec.yml` runs all scans and outputs JSON/SARIF/report artifacts
- Scan output files: `snyk.sarif`, `trufflehog.json`, `zap-report.html`

## Setup

1. Create a CodeCommit repo and push this project
2. Configure CodeBuild with:
   - Environment variables: `SNYK_TOKEN`
   - IAM permissions for CodeCommit, SecretsManager, S3/ECR (optional)
3. (Optional) Add CodeDeploy with `appspec.yml` and deployment hooks

## Viewing Scan Results

- Snyk output is shown as SARIF; integrate with GitHub Code Scanning or view raw SARIF
- TruffleHog outputs full JSON scan results
- ZAP produces `zap-report.html` for dynamic vulnerability findings
