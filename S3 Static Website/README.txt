# Periodic Table Static Website Deployment on AWS S3

This project demonstrates how to deploy a simple static website displaying the periodic table using Amazon S3's static website hosting feature.

## Prerequisites
Before proceeding with the steps, ensure you have the following:
- An AWS account
- AWS S3 bucket creation permissions
- Basic knowledge of HTML and CSS

## Deployment Steps

### 1. Create an S3 Bucket
1. Log in to your [AWS Management Console](https://aws.amazon.com/console/).
2. Navigate to the **S3** service.
3. Click **Create bucket**.
4. Provide a unique bucket name (e.g., `periodictable1807`).
5. Select the appropriate AWS region.
6. Uncheck **Block all public access** (since the website must be publicly accessible).
7. Click **Create bucket**.

### 2. Develop the Static Website Locally
1. Create an `index.html` file containing the HTML structure of the periodic table.
2. Create a `style.css` file to style the periodic table.
3. Ensure all necessary assets (images, scripts, etc.) are included in the project directory.

### 3. Upload Files to the S3 Bucket
1. Navigate to the **S3** bucket you created.
2. Click the **Upload** button.
3. Select all website files (`index.html`, `style.css`, and other necessary assets).
4. Click **Upload**.

### 4. Configure Static Website Hosting
1. Open the **Properties** tab of your S3 bucket.
2. Scroll down to **Static website hosting** and click **Edit**.
3. Enable **Static website hosting**.
4. Set the **Index document** to `index.html`.
5. Click **Save changes**.

### 5. Set Permissions for Public Access
1. Open the **Permissions** tab.
2. Click **Bucket Policy** and add the following policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::periodictable1807/*"
    }
  ]
}
```

3. Click **Save changes**.

### 6. Access the Deployed Website
1. In the **Properties** tab, scroll to **Static website hosting**.
2. Copy the **Bucket website endpoint**.
3. Open the link in a browser to view your deployed periodic table website.

## Conclusion
You have successfully deployed a static periodic table website on AWS S3 using static website hosting. This setup allows users to access the website globally via the provided bucket endpoint.


