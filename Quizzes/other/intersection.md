



### Repository


#### 122

You are configuring service accounts for an application that spans multiple projects. Virtual Machines (VMs) running in the web-applications project need access to BigQuery datasets in crm-databases-proj. You want to follow Google-recommended practices to give access to the service account in the web-applications project. What should you do?

- [ ] Give project owner for web-applications appropriate roles to crm-databases-proj.
- [ ] Give project owner role to crm-databases-proj and the web-applications project.
- [ ] Give project owner role to crm-databases-proj and bigquery.dataViewer role to web-applications.
- [x] Give bigquery.dataViewer role to crm-databases-proj and appropriate roles to web-applications.

#### 123

An employee was terminated, but their access to Google Cloud Platform (GCP) was not removed until 2 weeks later. You need to find out this employee accessed any sensitive customer information after their termination. What should you do?

- [ ] View System Event Logs in Stackdriver. Search for the user's email as the principal.
- [ ] View System Event Logs in Stackdriver. Search for the service account associated with the user.
- [x] View Data Access audit logs in Stackdriver. Search for the user's email as the principal.
- [ ] View the Admin Activity log in Stackdriver. Search for the service account associated with the user.

#### 124

You need to create a custom IAM role for use with a GCP service. All permissions in the role must be suitable for production use. You also want to clearly share with your organization the status of the custom role. This will be the first version of the custom role. What should you do?

- [x] Use permissions in your role that use the 'supported' support level for role permissions. Set the role stage to ALPHA while testing the role permissions.
- [ ] Use permissions in your role that use the 'supported' support level for role permissions. Set the role stage to BETA while testing the role permissions.
- [ ] Use permissions in your role that use the 'testing' support level for role permissions. Set the role stage to ALPHA while testing the role permissions.
- [ ] Use permissions in your role that use the 'testing' support level for role permissions. Set the role stage to BETA while testing the role permissions.

#### 123

Your company has a large quantity of unstructured data in different file formats. You want to perform ETL transformations on the data. You need to make the data accessible on Google Cloud so it can be processed by a Dataflow job. What should you do?

- [ ] Upload the data to BigQuery using the bq command line tool.
- [x] Upload the data to Cloud Storage using the gsutil command line tool.
- [ ] Upload the data into Cloud SQL using the import function in the console.
- [ ] Upload the data into Cloud Spanner using the import function in the console.

#### 124

You need to manage multiple Google Cloud projects in the fewest steps possible. You want to configure the Google Cloud SDK command line interface (CLI) so that you can easily manage multiple projects. What should you do?

- [x] 1. Create a configuration for each project you need to manage. 2. Activate the appropriate configuration when you work with each of your assigned Google Cloud projects.
- [ ] 1. Create a configuration for each project you need to manage. 2. Use gcloud init to update the configuration values when you need to work with a non-default project.
- [ ] 1. Use the default configuration for one project you need to manage. 2. Activate the appropriate configuration when you work with each of your assigned Google Cloud projects.
- [ ] 1. Use the default configuration for one project you need to manage. 2. Use gcloud init to update the configuration values when you need to work with a non-default project.

#### 123

Your Managed Instance Group raised an alert stating that new instance creation has failed to create new instances. You need to maintain the number of running instances specified by the template to be able to process expected application traffic. What should you do?

- [x] Create an instance template that contains valid syntax which will be used by the instance group. Delete any persistent disks with the same name as instance names.
- [ ] Create an instance template that contains valid syntax that will be used by the instance group. Verify that the instance name and persistent disk name values are not the same in the template.
- [ ] Verify that the instance template being used by the instance group contains valid syntax. Delete any persistent disks with the same name as instance names. Set the disks.autoDelete property to true in the instance template.
- [ ] Delete the current instance template and replace it with a new instance template. Verify that the instance name and persistent disk name values are not the same in the template. Set the disks.autoDelete property to true in the instance template.

#### 124

Your company is moving from an on-premises environment to Google Cloud. You have multiple development teams that use Cassandra environments as backend databases. They all need a development environment that is isolated from other Cassandra instances. You want to move to Google Cloud quickly and with minimal support effort. What should you do?

- [ ] 1. Build an instruction guide to install Cassandra on Google Cloud. 2. Make the instruction guide accessible to your developers.
- [x] 1. Advise your developers to go to Cloud Marketplace. 2. Ask the developers to launch a Cassandra image for their development work.
- [ ] 1. Build a Cassandra Compute Engine instance and take a snapshot of it. 2. Use the snapshot to create instances for your developers.
- [ ] 1. Build a Cassandra Compute Engine instance and take a snapshot of it. 2. Upload the snapshot to Cloud Storage and make it accessible to your developers. 3. Build instructions to create a Compute Engine instance from the snapshot so that developers can do it themselves.

#### 125

You have a Compute Engine instance hosting a production application. You want to receive an email if the instance consumes more than 90% of its CPU resources for more than 15 minutes. You want to use Google services. What should you do?

- [ ] 1. Create a consumer Gmail account. 2. Write a script that monitors the CPU usage. 3. When the CPU usage exceeds the threshold, have that script send an email using the Gmail account and smtp.gmail.com on port 25 as SMTP server.
- [x] 1. Create a Stackdriver Workspace, and associate your Google Cloud Platform (GCP) project with it. 2. Create an Alerting Policy in Stackdriver that uses the threshold as a trigger condition. 3. Configure your email address in the notification channel.
- [ ] 1. Create a Stackdriver Workspace, and associate your GCP project with it. 2. Write a script that monitors the CPU usage and sends it as a custom metric to Stackdriver. 3. Create an uptime check for the instance in Stackdriver.
- [ ] 1. In Stackdriver Logging, create a logs-based metric to extract the CPU usage by using this regular expression: CPU Usage: ([0-9] {1,3})% 2. In Stackdriver Monitoring, create an Alerting Policy based on this metric. 3. Configure your email address in the notification channel.

#### 126

You have an application that uses Cloud Spanner as a backend database. The application has a very predictable traffic pattern. You want to automatically scale up or down the number of Spanner nodes depending on traffic. What should you do?

- [ ] Create a cron job that runs on a scheduled basis to review Cloud Monitoring metrics, and then resize the Spanner instance accordingly.
- [ ] Create a Cloud Monitoring alerting policy to send an alert to oncall SRE emails when Cloud Spanner CPU exceeds the threshold. SREs would scale resources up or down accordingly.
- [ ] Create a Cloud Monitoring alerting policy to send an alert to Google Cloud Support email when Cloud Spanner CPU exceeds your threshold. Google support would scale resources up or down accordingly.
- [x] Create a Cloud Monitoring alerting policy to send an alert to webhook when Cloud Spanner CPU is over or under your threshold. Create a Cloud Function that listens to HTTP and resizes Spanner resources accordingly.

#### 127

Your company publishes large files on an Apache web server that runs on a Compute Engine instance. The Apache web server is not the only application running in the project. You want to receive an email when the egress network costs for the server exceed 100 dollars for the current month as measured by Google Cloud. What should you do?

- [ ] Set up a budget alert on the project with an amount of 100 dollars, a threshold of 100%, and notification type of email.
- [ ] Set up a budget alert on the billing account with an amount of 100 dollars, a threshold of 100%, and notification type of email.
- [x] Export the billing data to BigQuery. Create a Cloud Function that uses BigQuery to sum the egress network costs of the exported billing data for the Apache web server for the current month and sends an email if it is over 100 dollars. Schedule the Cloud Function using Cloud Scheduler to run hourly.
- [ ] Use the Cloud Logging Agent to export the Apache web server logs to Cloud Logging. Create a Cloud Function that uses BigQuery to parse the HTTP response log data in Cloud Logging for the current month and sends an email if the size of all HTTP responses, multiplied by current Google Cloud egress prices, totals over 100 dollars. Schedule the Cloud Function using Cloud Scheduler to run hourly.

#### 128

You have designed a solution on Google Cloud that uses multiple Google Cloud products. Your company has asked you to estimate the costs of the solution. You need to provide estimates for the monthly total cost. What should you do?

- [x] For each Google Cloud product in the solution, review the pricing details on the products pricing page. Use the pricing calculator to total the monthly costs for each Google Cloud product.
- [ ] For each Google Cloud product in the solution, review the pricing details on the products pricing page. Create a Google Sheet that summarizes the expected monthly costs for each product.
- [ ] Provision the solution on Google Cloud. Leave the solution provisioned for 1 week. Navigate to the Billing Report page in the Cloud Console. Multiply the 1 week cost to determine the monthly costs.
- [ ] Provision the solution on Google Cloud. Leave the solution provisioned for 1 week. Use Cloud Monitoring to determine the provisioned and used resource amounts. Multiply the 1 week cost to determine the monthly costs.

#### 129

You have an application that receives SSL-encrypted TCP traffic on port 443. Clients for this application are located all over the world. You want to minimize latency for the clients. Which load balancing option should you use?

- [ ] HTTPS Load Balancer.
- [ ] Network Load Balancer.
- [x] SSL Proxy Load Balancer.
- [ ] Internal TCP/UDP Load Balancer. Add a firewall rule allowing ingress traffic from 0.0.0.0/0 on the target instances.

#### 130

You have an application on a general-purpose Compute Engine instance that is experiencing excessive disk read throttling on its Zonal SSD Persistent Disk. The application primarily reads large files from disk. The disk size is currently 350 GB. You want to provide the maximum amount of throughput while minimizing costs. What should you do?

- [ ] Increase the size of the disk to 1 TB.
- [ ] Increase the allocated CPU to the instance.
- [x] Migrate to use a Local SSD on the instance.
- [ ] Migrate to use a Regional SSD on the instance.

#### 131

Your Dataproc cluster runs in a single Virtual Private Cloud (VPC) network in a single subnet with range 172.16.20.128/25. There are no private IP addresses available in the VPC network. You want to add new VMs to communicate with your cluster using the minimum number of steps. What should you do?

- [x] Modify the existing subnet range to 172.16.20.0/24.
- [ ] Create a new Secondary IP Range in the VPC and configure the VMs to use that range.
- [ ] Create a new VPC network for the VMs. Enable VPC Peering between the VMs' VPC network and the Dataproc cluster VPC network.
- [ ] Create a new VPC network for the VMs with a subnet of 172.32.0.0/16. Enable VPC network Peering between the Dataproc VPC network and the VMs VPC network. Configure a custom Route exchange.

#### 132

You manage an App Engine Service that aggregates and visualizes data from BigQuery. The application is deployed with the default App Engine Service account. The data that needs to be visualized resides in a different project managed by another team. You do not have access to this project, but you want your application to be able to read data from the BigQuery dataset. What should you do?

- [ ] Ask the other team to grant your default App Engine Service account the role of BigQuery Job User.
- [x] Ask the other team to grant your default App Engine Service account the role of BigQuery Data Viewer.
- [ ] In Cloud IAM of your project, ensure that the default App Engine service account has the role of BigQuery Data Viewer.
- [ ] In Cloud IAM of your project, grant a newly created service account from the other team the role of BigQuery Job User in your project.

#### 133

You need to create a copy of a custom Compute Engine Virtual Machine (VM) to facilitate an expected increase in application traffic due to a business acquisition. What should you do?

- [ ] Create a Compute Engine snapshot of your base VM. Create your images from that snapshot.
- [ ] Create a Compute Engine snapshot of your base VM. Create your instances from that snapshot.
- [ ] Create a custom Compute Engine image from a snapshot. Create your images from that image.
- [x] Create a custom Compute Engine image from a snapshot. Create your instances from that image.

#### 134

You have deployed an application on a single Compute Engine instance. The application writes logs to disk. Users start reporting errors with the application. You want to diagnose the problem. What should you do?

- [ ] Navigate to Cloud Logging and view the application logs.
- [ ] Connect to the instance's serial console and read the application logs.
- [ ] Configure a Health Check on the instance and set a Low Healthy Threshold value.
- [x] Install and configure the Cloud Logging Agent and view the logs from Cloud Logging.

#### 135

An application generates daily reports in a Compute Engine Virtual Machine (VM). The VM is in the project corp-iot-insights. Your team operates only in the project corp-aggregate-reports and needs a copy of the daily exports in the bucket corp-aggregate-reports-storage. You want to configure access so that the daily reports from the VM are available in the bucket corp-aggregate-reports-storage and use as few steps as possible while following Google-recommended practices. What should you do?

- [ ] Move both projects under the same folder.
- [x] Grant the VM Service Account the role Storage Object Creator on corp-aggregate-reports-storage.
- [ ] Create a Shared VPC network between both projects. Grant the VM Service Account the role Storage Object Creator on corp-iot-insights.
- [ ] Make corp-aggregate-reports-storage public and create a folder with a pseudo-randomized suffix name. Share the folder with the IoT team.

#### 136

You built an application on your development laptop that uses Google Cloud services. Your application uses Application Default Credentials for authentication and works fine on your development laptop. You want to migrate this application to a Compute Engine Virtual Machine (VM) and set up authentication using Google-recommended practices and minimal changes. What should you do?

- [x] Assign appropriate access for Google services to the service account used by the Compute Engine VM.
- [ ] Create a service account with appropriate access for Google services, and configure the application to use this account.
- [ ] Store credentials for service accounts with appropriate access for Google services in a config file, and deploy this config file with your application.
- [ ] Store credentials for your user account with appropriate access for Google services in a config file, and deploy this config file with your application.

#### 137

You need to create a Compute Engine instance in a new project that doesn't exist yet. What should you do?

- [x] Using the Cloud SDK, create a new project, enable the Compute Engine API in that project, and then create the instance specifying your new project.
- [ ] Enable the Compute Engine API in the Cloud Console, use the Cloud SDK to create the instance, and then use the --project flag to specify a new project.
- [ ] Using the Cloud SDK, create the new instance, and use the --project flag to specify the new project. Answer yes when prompted by Cloud SDK to enable the Compute Engine API.
- [ ] Enable the Compute Engine API in the Cloud Console. Go to the Compute Engine section of the Console to create a new instance, and look for the Create In A New Project option in the creation form.

#### 138

Your company runs one batch process in an on-premises server that takes around 30 hours to complete. The task runs monthly, can be performed offline, and must be restarted if interrupted. You want to migrate this workload to the cloud while minimizing cost. What should you do?

- [ ] Migrate the workload to a Compute Engine Preemptible VM.
- [ ] Migrate the workload to a Google Kubernetes Engine cluster with Preemptible nodes.
- [x] Migrate the workload to a Compute Engine VM. Start and stop the instance as needed.
- [ ] Create an Instance Template with Preemptible VMs On. Create a Managed Instance Group from the template and adjust Target CPU Utilization. Migrate the workload.

#### 139

You are developing a new application and are looking for a Jenkins installation to build and deploy your source code. You want to automate the installation as quickly and easily as possible. What should you do?

- [x] Deploy Jenkins through the Google Cloud Marketplace.
- [ ] Create a new Compute Engine instance. Run the Jenkins executable.
- [ ] Create a new Kubernetes Engine cluster. Create a deployment for the Jenkins image.
- [ ] Create an instance template with the Jenkins executable. Create a Managed Instance Group with this template.

#### 140

You have downloaded and installed the gcloud command line interface (CLI) and have authenticated with your Google Account. Most of your Compute Engine instances in your project run in the europe-west1-d zone. You want to avoid having to specify this zone with each CLI command when managing these instances. What should you do?

- [x] Set the europe-west1-d zone as the default zone using the gcloud config subcommand.
- [ ] In the Settings page for Compute Engine under Default location, set the zone to europe-west1-d.
- [ ] In the CLI installation directory, create a file called default.conf containing zone=europe-west1-d.
- [ ] Create a Metadata entry on the Compute Engine page with key compute/zone and value europe-west1-d.

#### 141

The core business of your company is to rent out construction equipment at large scale. All the equipment that is being rented out has been equipped with multiple sensors that send event information every few seconds. These signals can vary from engine status, distance traveled, fuel level, and more. Customers are billed based on the consumption monitored by these sensors. You expect high throughput - up to thousands of events per hour per device - and need to retrieve consistent data based on the time of the event. Storing and retrieving individual signals should be atomic. What should you do?

- [ ] Create a file in Cloud Storage per device and append new data to that file.
- [ ] Create a file in Cloud Filestore per device and append new data to that file.
- [ ] Ingest the data into Datastore. Store data in an entity group based on the device.
- [x] Ingest the data into Cloud Bigtable. Create a row key based on the event timestamp.

#### 142

You are asked to set up application performance monitoring on Google Cloud projects A, B, and C as a single pane of glass. You want to monitor CPU, memory, and disk. What should you do?

- [ ] Enable API and then share charts from project A, B, and C.
- [ ] Enable API and then give the metrics.reader role to projects A, B, and C.
- [ ] Enable API and then use default dashboards to view all projects in sequence.
- [x] Enable API, create a workspace under project A, and then add projects B and C.

#### 143

You created several resources in multiple Google Cloud projects. All projects are linked to different billing accounts. To better estimate future charges, you want to have a single visual representation of all costs incurred. You want to include new cost data as soon as possible. What should you do?

- [x] Configure Billing Data Export to BigQuery and visualize the data in Data Studio.
- [ ] Visit the Cost Table page to get a CSV export and visualize it using Data Studio.
- [ ] Fill all resources in the Pricing Calculator to get an estimate of the monthly cost.
- [ ] Use the Reports view in the Cloud Billing Console to view the desired cost information.

#### 144

Your company has workloads running on Compute Engine and on-premises. The Google Cloud Virtual Private Cloud (VPC) is connected to your WAN over a Virtual Private Network (VPN). You need to deploy a new Compute Engine instance and ensure that no public Internet traffic can be routed to it. What should you do?

- [x] Create the instance without a public IP address.
- [ ] Create the instance with Private Google Access enabled.
- [ ] Create a deny-all egress firewall rule on the VPC network.
- [ ] Create a route on the VPC to route all traffic to the instance over the VPN tunnel.

#### 145

Your team maintains the infrastructure for your organization. The current infrastructure requires changes. You need to share your proposed changes with the rest of the team. You want to follow Google's recommended best practices. What should you do?

- [ ] Use Deployment Manager templates to describe the proposed changes and store them in a Cloud Storage bucket.
- [x] Use Deployment Manager templates to describe the proposed changes and store them in Cloud Source Repositories.
- [ ] Apply the changes in a development environment, run gcloud compute instances list, and then save the output in a shared Storage bucket.
- [ ] Apply the changes in a development environment, run gcloud compute instances list, and then save the output in Cloud Source Repositories.

#### 146

You have a Compute Engine instance hosting an application used between 9 AM and 6 PM on weekdays. You want to back up this instance daily for disaster recovery purposes. You want to keep the backups for 30 days. You want the Google-recommended solution with the least management overhead and the least number of services. What should you do?

- [ ] 1. Update your instances' metadata to add the following value: snapshot-schedule: 0 1 * * * 2. Update your instances' metadata to add the following value: snapshot-retention: 30.
- [x] 1. In the Cloud Console, go to the Compute Engine Disks page and select your instance's disk. 2. In the Snapshot Schedule section, select Create Schedule and configure the following parameters: Schedule frequency: Daily. Start time: 1:00 AM - 2:00 AM. Autodelete snapshots after: 30 days.
- [ ] 1. Create a Cloud Function that creates a snapshot of your instance's disk. 2. Create a Cloud Function that deletes snapshots that are older than 30 days. 3. Use Cloud Scheduler to trigger both Cloud Functions daily at 1:00 AM.
- [ ] 1. Create a bash script in the instance that copies the content of the disk to Cloud Storage. 2. Create a bash script in the instance that deletes data older than 30 days in the backup Cloud Storage bucket. 3. Configure the instance's crontab to execute these scripts daily at 1:00 AM.

#### 147

Your existing application running in Google Kubernetes Engine (GKE) consists of multiple pods running on four GKE n1-standard-2 nodes. You need to deploy additional pods requiring n2-highmem-16 nodes without any downtime. What should you do?

- [ ] Use gcloud container clusters upgrade. Deploy the new services.
- [x] Create a new Node Pool and specify machine type n2-highmem-16. Deploy the new pods.
- [ ] Create a new cluster with n2-highmem-16 nodes. Redeploy the pods and delete the old cluster.
- [ ] Create a new cluster with both n1-standard-2 and n2-highmem-16 nodes. Redeploy the pods and delete the old cluster.

#### 148

You have an application that uses Cloud Spanner as a database backend to keep current state information about users. Cloud Bigtable logs all events triggered by users. You export Cloud Spanner data to Cloud Storage during daily backups. One of your analysts asks you to join data from Cloud Spanner and Cloud Bigtable for specific users. You want to complete this ad hoc request as efficiently as possible. What should you do?

- [ ] Create a dataflow job that copies data from Cloud Bigtable and Cloud Storage for specific users.
- [ ] Create a dataflow job that copies data from Cloud Bigtable and Cloud Spanner for specific users.
- [ ] Create a Cloud Dataproc cluster that runs a Spark job to extract data from Cloud Bigtable and Cloud Storage for specific users.
- [x] Create two separate BigQuery external tables on Cloud Storage and Cloud Bigtable. Use the BigQuery console to join these tables through user fields, and apply appropriate filters.

#### 149

You are hosting an application from Compute Engine Virtual Machines (VMs) in us-central1-a. You want to adjust your design to support the failure of a single Compute Engine zone, eliminate downtime, and minimize cost. What should you do?

- [x] Create Compute Engine resources in us-central1-b. Balance the load across both us-central1-a and us-central1-b.
- [ ] Create a Managed Instance Group and specify us-central1-a as the zone. Configure the Health Check with a short Health Interval.
- [ ] Create an HTTP(S) Load Balancer. Create one or more global forwarding rules to direct traffic to your VMs.
- [ ] Perform regular backups of your application. Create a Cloud Monitoring Alert and be notified if your application becomes unavailable. Restore from backups when notified.

#### 150

A colleague handed over a Google Cloud Platform project for you to maintain. As part of a security checkup, you want to review who has been granted the Project Owner role. What should you do?

- [ ] In the console, validate which SSH keys have been stored as project-wide keys.
- [ ] Navigate to Identity-Aware Proxy and check the permissions for these resources.
- [ ] Enable Audit Logs on the IAM &amp; admin page for all resources, and validate the results.
- [x] Use the command gcloud projects get-iam-policy to view the current role assignments.

#### 151

You are running multiple VPC-native Google Kubernetes Engine clusters in the same subnet. The IPs available for the nodes are exhausted, and you want to ensure that the clusters can grow in nodes when needed. What should you do?

- [ ] Create a new subnet in the same region as the subnet being used.
- [ ] Add an alias IP range to the subnet used by the GKE clusters.
- [ ] Create a new VPC, and set up VPC peering with the existing VP.
- [x] Expand the CIDR range of the relevant subnet for the cluster.

#### 152

You have a batch workload that runs every night and uses a large number of Virtual Machines (VMs). It is fault-tolerant and can tolerate some of the VMs being terminated. The current cost of VMs is too high. What should you do?

- [x] Run a test using simulated maintenance events. If the test is successful, use preemptible N1 Standard VMs when running future jobs.
- [ ] Run a test using simulated maintenance events. If the test is successful, use N1 Standard VMs when running future jobs.
- [ ] Run a test using a Managed Instance Group. If the test is successful, use N1 Standard VMs in the Managed Instance Group when running future jobs.
- [ ] Run a test using N1 standard VMs instead of N2. If the test is successful, use N1 Standard VMs when running future jobs.

#### 153

You are working with a user to set up an application in a new VPC behind a firewall. The user is concerned about data egress. You want to configure the fewest open egress ports. What should you do?

- [x] Set up a low-priority (65534) rule that blocks all egress and a high-priority rule (1000) that allows only the appropriate ports.
- [ ] Set up a high-priority (1000) rule that pairs both ingress and egress ports.
- [ ] Set up a high-priority (1000) rule that blocks all egress and a low-priority (65534) rule that allows only the appropriate ports.
- [ ] Set up a high-priority (1000) rule to allow the appropriate ports.


#### 154

Your company runs its Linux workloads on Compute Engine instances. Your company will be working with a new operations partner that does not use Google Accounts. You need to grant access to the instances to your operations partner so they can maintain the installed tooling. What should you do?

- [x] Enable Cloud IAP for the Compute Engine instances, and add the operations partner as a Cloud IAP Tunnel User.
- [ ] Tag all the instances with the same network tag. Create a firewall rule in the VPC to grant TCP access on port 22 for traffic from the operations partner to instances with the network tag.
- [ ] Set up Cloud VPN between your Google Cloud VPC and the internal network of the operations partner.
- [ ] Ask the operations partner to generate SSH key pairs, and add the public keys to the VM instances.

#### 155

You have created a code snippet that should be triggered whenever a new file is uploaded to a Cloud Storage bucket. You want to deploy this code snippet. What should you do?

- [ ] Use App Engine and configure Cloud Scheduler to trigger the application using Pub/Sub.
- [x] Use Cloud Functions and configure the bucket as a trigger resource.
- [ ] Use Google Kubernetes Engine and configure a CronJob to trigger the application using Pub/Sub.
- [ ] Use Dataflow as a batch job, and configure the bucket as a data source.

#### 156

You have been asked to set up Object Lifecycle Management for objects stored in storage buckets. The objects are written once and accessed frequently for 30 days. After 30 days, the objects are not read again unless there is a special need. The objects should be kept for three years, and you need to minimize cost. What should you do?

- [ ] Set up a policy that uses Nearline storage for 30 days and then moves to Archive storage for three years.
- [x] Set up a policy that uses Standard storage for 30 days and then moves to Archive storage for three years.
- [ ] Set up a policy that uses Nearline storage for 30 days, then moves the Coldline for one year, and then moves to Archive storage for two years.
- [ ] Set up a policy that uses Standard storage for 30 days, then moves to Coldline for one year, and then moves to Archive storage for two years.

#### 157

You are storing sensitive information in a Cloud Storage bucket. For legal reasons, you need to be able to record all requests that read any of the stored data. You want to make sure you comply with these requirements. What should you do?

- [ ] Enable the Identity Aware Proxy API on the project.
- [ ] Scan the bucket using the Data Loss Prevention API.
- [ ] Allow only a single Service Account access to read the data.
- [x] Enable Data Access audit logs for the Cloud Storage API.

#### 158

You are the team lead of a group of 10 developers. You provided each developer with an individual Google Cloud Project that they can use as their personal sandbox to experiment with different Google Cloud solutions. You want to be notified if any of the developers are spending above $500 per month on their sandbox environment. What should you do?

- [ ] Create a single budget for all projects and configure budget alerts on this budget.
- [ ] Create a separate billing account per sandbox project and enable BigQuery billing exports. Create a Data Studio dashboard to plot the spending per billing account.
- [x] Create a budget per project and configure budget alerts on all of these budgets.
- [ ] Create a single billing account for all sandbox projects and enable BigQuery billing exports. Create a Data Studio dashboard to plot the spending per project.

#### 157

You are deploying a production application on Compute Engine. You want to prevent anyone from accidentally destroying the instance by clicking the wrong button. What should you do?

- [ ] Disable the flag Delete boot disk when instance is deleted.
- [x] Enable delete protection on the instance.
- [ ] Disable Automatic restart on the instance.
- [ ] Enable Preemptibility on the instance.

#### 158

Your company uses a large number of Google Cloud services centralized in a single project. All teams have specific projects for testing and development. The DevOps team needs access to all of the production services in order to perform their job. You want to prevent Google Cloud product changes from broadening their permissions in the future. You want to follow Google-recommended practices. What should you do?

- [ ] Grant all members of the DevOps team the role of Project Editor on the organization level.
- [ ] Grant all members of the DevOps team the role of Project Editor on the production project.
- [x] Create a custom role that combines the required permissions. Grant the DevOps team the custom role on the production project.
- [ ] Create a custom role that combines the required permissions. Grant the DevOps team the custom role on the organization level.

#### 159

You are building an application that processes data files uploaded from thousands of suppliers. Your primary goals for the application are data security and the expiration of aged data. You need to design the application to: Restrict access so that suppliers can access only their own data. Give suppliers write access to data only for 30 minutes. Delete data that is over 45 days old. You have a very short development cycle, and you need to make sure that the application requires minimal maintenance. Which two strategies should you use? (Choose two.)

- [x] Build a lifecycle policy to delete Cloud Storage objects after 45 days.
- [x] Use signed URLs to allow suppliers limited time access to store their objects.
- [ ] Set up an SFTP server for your application, and create a separate user for each supplier.
- [ ] Build a Cloud function that triggers a timer of 45 days to delete objects that have expired.
- [ ] Develop a script that loops through all Cloud Storage buckets and deletes any buckets that are older than 45 days.

#### 160

Your company wants to standardize the creation and management of multiple Google Cloud resources using Infrastructure as Code. You want to minimize the amount of repetitive code needed to manage the environment. What should you do?

- [x] Develop templates for the environment using Cloud Deployment Manager.
- [ ] Use curl in a terminal to send a REST request to the relevant Google API for each individual resource.
- [ ] Use the Cloud Console interface to provision and manage all related resources.
- [ ] Create a bash script that contains all requirement steps as gcloud commands.

#### 161

You are performing a monthly security check of your Google Cloud environment and want to know who has access to view data stored in your Google Cloud Project. What should you?

- [ ] Enable Audit Logs for all APIs that are related to data storage.
- [x] Review the IAM permissions for any role that allows for data access.
- [ ] Review the Identity-Aware Proxy settings for each resource.
- [ ] Create a Data Loss Prevention job.

#### 162

Your company has embraced a hybrid cloud strategy where some of the applications are deployed on Google Cloud. A Virtual Private Network (VPN) tunnel connects your Virtual Private Cloud (VPC) in Google Cloud with your company's on-premises network. Multiple applications in Google Cloud need to connect to an on-premises database server, and you want to avoid having to change the IP configuration in all of your applications when the IP of the database changes. What should you do?

- [ ] Configure Cloud NAT for all subnets of your VPC to be used when egressing from the VM instances.
- [x] Create a private zone on Cloud DNS, and configure the applications with the DNS name.
- [ ] Configure the IP of the database as custom metadata for each instance, and query the metadata server.
- [ ] Query the Compute Engine internal DNS from the applications to retrieve the IP of the database.

#### 163

You have developed a containerized web application that will serve internal colleagues during business hours. You want to ensure that no costs are incurred outside of the hours the application is used. You have just created a new Google Cloud project and want to deploy the application. What should you do?

- [ ] Deploy the container on Cloud Run for Anthos, and set the minimum number of instances to zero.
- [x] Deploy the container on Cloud Run (fully managed), and set the minimum number of instances to zero.
- [ ] Deploy the container on App Engine flexible environment with autoscaling, and set the value min_instances to zero in the app.yaml.
- [ ] Deploy the container on App Engine flexible environment with manual scaling, and set the value instances to zero in the app.yaml.

#### 164

You have experimented with Google Cloud using your own credit card and expensed the costs to your company. Your company wants to streamline the billing process and charge the costs of your projects to their monthly invoice. What should you do?

- [ ] Grant the financial team the IAM role of Billing Account User on the billing account linked to your credit card.
- [ ] Set up BigQuery billing export and grant your financial department IAM access to query the data.
- [ ] Create a ticket with Google Billing Support to ask them to send the invoice to your company.
- [x] Change the billing account of your projects to the billing account of your company.

#### 165

You are running a data warehouse on BigQuery. A partner company is offering a recommendation engine based on the data in your data warehouse. The partner company is also running their application on Google Cloud. They manage the resources in their own project, but they need access to the BigQuery dataset in your project. You want to provide the partner company with access to the dataset. What should you do?

- [ ] Create a Service Account in your own project, and grant this Service Account access to BigQuery in your project.
- [ ] Create a Service Account in your own project, and ask the partner to grant this Service Account access to BigQuery in their project.
- [ ] Ask the partner to create a Service Account in their project, and have them give the Service Account access to BigQuery in their project.
- [x] Ask the partner to create a Service Account in their project, and grant their Service Account access to the BigQuery dataset in your project.

#### 166

Your web application has been running successfully on Cloud Run for Anthos. You want to evaluate an updated version of the application with a specific percentage of your production users (canary deployment). What should you do?

- [ ] Create a new service with the new version of the application. Split traffic between this version and the version that is currently running.
- [x] Create a new revision with the new version of the application. Split traffic between this version and the version that is currently running.
- [ ] Create a new service with the new version of the application. Add HTTP Load Balancer in front of both services.
- [ ] Create a new revision with the new version of the application. Add HTTP Load Balancer in front of both revisions.

#### 167

Your company developed a mobile game that is deployed on Google Cloud. Gamers are connecting to the game with their personal phones over the Internet. The game sends UDP packets to update the servers about the gamers' actions while they are playing in multiplayer mode. Your game backend can scale over multiple Virtual Machines (VMs), and you want to expose the VMs over a single IP address. What should you do?

- [ ] Configure an SSL Proxy load balancer in front of the application servers.
- [ ] Configure an Internal UDP load balancer in front of the application servers.
- [ ] Configure an External HTTP(s) load balancer in front of the application servers.
- [x] Configure an External Network load balancer in front of the application servers.

#### 168

You are working for a hospital that stores its medical images in an on-premises data room. The hospital wants to use Cloud Storage for archival storage of these images. The hospital wants an automated process to upload any new medical images to Cloud Storage. You need to design and implement a solution. What should you do?

- [ ] Create a Pub/Sub topic, and enable a Cloud Storage trigger for the Pub/Sub topic. Create an application that sends all medical images to the Pub/Sub topic.
- [ ] Deploy a Dataflow job from the batch template, Datastore to Cloud Storage. Schedule the batch job on the desired interval.
- [x] Create a script that uses the gsutil command line interface to synchronize the on-premises storage with Cloud Storage. Schedule the script as a cron job.
- [ ] In the Cloud Console, go to Cloud Storage. Upload the relevant images to the appropriate bucket.

#### 169

Your auditor wants to view your organization's use of data in Google Cloud. The auditor is most interested in auditing who accessed data in Cloud Storage buckets. You need to help the auditor access the data they need. What should you do?

- [x] Turn on Data Access Logs for the buckets they want to audit, and then build a query in the log viewer that filters on Cloud Storage.
- [ ] Assign the appropriate permissions, and then create a Data Studio report on Admin Activity Audit Logs.
- [ ] Assign the appropriate permissions, and the use Cloud Monitoring to review metrics.
- [ ] Use the export logs API to provide the Admin Activity Audit Logs in the format they want.

#### 170

You received a JSON file that contained a private key of a Service Account in order to get access to several resources in a Google Cloud project. You downloaded and installed the Cloud SDK and want to use this private key for authentication and authorization when performing gcloud commands. What should you do?

- [ ] Use the command gcloud auth login and point it to the private key.
- [x] Use the command gcloud auth activate-service-account and point it to the private key.
- [ ] Place the private key file in the installation directory of the Cloud SDK and rename it to credentials.json.
- [ ] Place the private key file in your home directory and rename it to GOOGLE_APPLICATION_CREDENTIALS.

#### 171

You are working with a Cloud SQL MySQL database at your company. You need to retain a month-end copy of the database for three years for audit purposes. What should you do?

- [x] Set up an export job for the first of the month. Write the export file to an Archive class Cloud Storage bucket.
- [ ] Save the automatic first-of-the-month backup for three years. Store the backup file in an Archive class Cloud Storage bucket.
- [ ] Set up an on-demand backup for the first of the month. Write the backup to an Archive class Cloud Storage bucket.
- [ ] Convert the automatic first-of-the-month backup to an export file. Write the export file to a Coldline class Cloud Storage bucket.

#### 172

You are monitoring an application and receive user feedback that a specific error is spiking. You notice that the error is caused by a Service Account having insufficient permissions. You are able to solve the problem but want to be notified if the problem recurs. What should you do?

- [ ] In the Log Viewer, filter the logs on severity ˜Error' and the name of the Service Account.
- [ ] Create a sink to BigQuery to export all the logs. Create a Data Studio dashboard on the exported logs.
- [x] Create a custom log-based metric for the specific error to be used in an Alerting Policy.
- [ ] Grant Project Owner access to the Service Account.

#### 173

You are developing a financial trading application that will be used globally. Data is stored and queried using a relational structure, and clients from all over the world should get the exact identical state of the data. The application will be deployed in multiple regions to provide the lowest latency to end users. You need to select a storage option for the application data while minimizing latency. What should you do?

- [ ] Use Cloud Bigtable for data storage.
- [ ] Use Cloud SQL for data storage.
- [x] Use Cloud Spanner for data storage.
- [ ] Use Firestore for data storage.

#### 174

You are about to deploy a new Enterprise Resource Planning (ERP) system on Google Cloud. The application holds the full database in-memory for fast data access, and you need to configure the most appropriate resources on Google Cloud for this application. What should you do?

- [ ] Provision preemptible Compute Engine instances.
- [ ] Provision Compute Engine instances with GPUs attached.
- [ ] Provision Compute Engine instances with local SSDs attached.
- [x] Provision Compute Engine instances with M1 machine type.

#### 175 

You have developed an application that consists of multiple microservices, with each microservice packaged in its own Docker container image. You want to deploy the entire application on Google Kubernetes Engine so that each microservice can be scaled individually. What should you do?

- [ ] Create and deploy a Custom Resource Definition per microservice.
- [ ] Create and deploy a Docker Compose File.
- [ ] Create and deploy a Job per microservice.
- [x] Create and deploy a Deployment per microservice.

#### 176

You will have several applications running on different Compute Engine instances in the same project. You want to specify at a more granular level the service account each instance uses when calling Google Cloud APIs. What should you do?

- [x] When creating the instances, specify a Service Account for each instance.
- [ ] When creating the instances, assign the name of each Service Account as instance metadata.
- [ ] After starting the instances, use gcloud compute instances update to specify a Service Account for each instance.
- [ ] After starting the instances, use gcloud compute instances update to assign the name of the relevant Service Account as instance metadata.

#### 177

You are creating an application that will run on Google Kubernetes Engine. You have identified MongoDB as the most suitable database system for your application and want to deploy a managed MongoDB environment that provides a support SLA. What should you do?

- [ ] Create a Cloud Bigtable cluster, and use the HBase API.
- [x] Deploy MongoDB Atlas from the Google Cloud Marketplace.
- [ ] Download a MongoDB installation package, and run it on Compute Engine instances.
- [ ] Download a MongoDB installation package, and run it on a Managed Instance Group.


#### 178

You are managing a project for the Business Intelligence (BI) department in your company. A data pipeline ingests data into BigQuery via streaming. You want the users in the BI department to be able to run the custom SQL queries against the latest data in BigQuery. What should you do?

- [ ] Create a Data Studio dashboard that uses the related BigQuery tables as a source and give the BI team view access to the Data Studio dashboard.
- [ ] Create a Service Account for the BI team and distribute a new private key to each member of the BI team.
- [ ] Use Cloud Scheduler to schedule a batch Dataflow job to copy the data from BigQuery to the BI team's internal data warehouse.
- [x] Assign the IAM role of BigQuery User to a Google Group that contains the members of the BI team.

#### 179

Your company is moving its entire workload to Compute Engine. Some servers should be accessible through the Internet, and other servers should only be accessible over the internal network. All servers need to be able to talk to each other over specific ports and protocols. The current on-premises network relies on a demilitarized zone (DMZ) for the public servers and a Local Area Network (LAN) for the private servers. You need to design the networking infrastructure on Google Cloud to match these requirements. What should you do?

- [x] 1. Create a single VPC with a subnet for the DMZ and a subnet for the LAN. 2. Set up firewall rules to open up relevant traffic between the DMZ and the LAN subnets, and another firewall rule to allow public ingress traffic for the DMZ.
- [ ] 1. Create a single VPC with a subnet for the DMZ and a subnet for the LAN. 2. Set up firewall rules to open up relevant traffic between the DMZ and the LAN subnets, and another firewall rule to allow public egress traffic for the DMZ.
- [ ] 1. Create a VPC with a subnet for the DMZ and another VPC with a subnet for the LAN. 2. Set up firewall rules to open up relevant traffic between the DMZ and the LAN subnets, and another firewall rule to allow public ingress traffic for the DMZ.
- [ ] 1. Create a VPC with a subnet for the DMZ and another VPC with a subnet for the LAN. 2. Set up firewall rules to open up relevant traffic between the DMZ and the LAN subnets, and another firewall rule to allow public egress traffic for the DMZ.
