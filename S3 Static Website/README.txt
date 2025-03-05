Periodic Table Static Website Deployment on AWS S3

This project demonstrates how to deploy a simple static website displaying the periodic table using Amazon S3's static website hosting feature.

Prerequisites

Before proceeding with the steps, ensure you have the following:

An AWS account

AWS S3 bucket creation permissions

Basic knowledge of HTML and CSS

Deployment Steps

1. Create an S3 Bucket

Log in to your AWS Management Console.

Navigate to the S3 service.

Click Create bucket.

Provide a unique bucket name (e.g., periodictable1807).

Select the appropriate AWS region.

Uncheck Block all public access (since the website must be publicly accessible).

Click Create bucket.

2. Develop the Static Website Locally

Create an index.html file containing the HTML structure of the periodic table.

Create a style.css file to style the periodic table.

Ensure all necessary assets (images, scripts, etc.) are included in the project directory.

3. Upload Files to the S3 Bucket

Navigate to the S3 bucket you created.

Click the Upload button.

Select all website files (index.html, style.css, and other necessary assets).

Click Upload.

4. Configure Static Website Hosting

Open the Properties tab of your S3 bucket.

Scroll down to Static website hosting and click Edit.

Enable Static website hosting.

Set the Index document to index.html.

Click Save changes.

5. Set Permissions for Public Access

Open the Permissions tab.

Click Bucket Policy and add the following policy:

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

Click Save changes.

6. Access the Deployed Website

In the Properties tab, scroll to Static website hosting.

Copy the Bucket website endpoint.

Open the link in a browser to view your deployed periodic table website.

Conclusion

You have successfully deployed a static periodic table website on AWS S3 using static website hosting. This setup allows users to access the website globally via the provided bucket endpoint.
