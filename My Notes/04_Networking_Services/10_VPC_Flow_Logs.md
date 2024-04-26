# VPC Flow Logs

**NOTE:** Essential for the exam.

**Flow Logs** is an essential tool for network monitoring and analyzing network traffic coming in and going out of VPCs from VM instances. It captures information about the IP traffic going to and from network interfaces in a VPC.

VPC Flow Logs records a sample of a network flow, sent from and received by VM instances, including instances used as Google Kubernetes Engine (GKE) nodes.

These logs can be used for **network monitoring**, **forensics**, **real-time security analysis**, and **expense optimization**.

When you enable VPC Flow Logs, you enable for all VMs in the subnet, so basically you **enable it on a subnet by subnet basis**.

Flow Logs are aggregated by connection from Compute Engine VMs and exported in real time, and these logs can be exported to Cloud Logging for 30 days. If logs are needed for longer than 30 days, you can export them to Cloud Storage.

Google Cloud sample packets that leave an enter a VM to generate FLow Logs, but not every packet is captured into its own log record, about 1 out of very 10 packets is captured, but this sampling rate might be lowe depending on the VM's load, and **you can't change the sampling rate.**

So for this reason it compensates for missed packets by interpolating from the captured packets.

![VPC Flow Logs](images/10_VPC_Flow_Logs_01.png)

## Use Cases

There are several use cases for VPC Flow Logs:

- **Network monitoring**
  - Real-time visibility into network throughput and performance
- **Analyze network usage** and optimize network **traffic expenses**
- **Network forensics** when incidents occur
  - Investigate suspicious network activity
- **Real-time security analysis**
  - Stream to Pub/Sub and integrate with SIEM (Splunk, Rapid7, LogRhythm, etc.)

## Record Format

VPC Flow Logs are recorded in a specific format. Logs records contains:

- base fields which are the **core fields** of every log record
  - they are always included
- metadata fields that add additional information
  - metadata fields can be omitted to save storage costs

Some log fields are in a multi-field format with more than one piece of data in a given field. Fro example the `connection` field, that you see from the `Base` fields, is of the `ipDetails` format which contains the source and destination IP addresses and ports, plus the protocol, in a single field.

![VPC Flow Logs](images/10_VPC_Flow_Logs_02.png)

## Sample Logs

The following images are examples of VPC Flow Logs:

![VPC Flow Logs](images/10_VPC_Flow_Logs_03.png)

![VPC Flow Logs](images/10_VPC_Flow_Logs_04.png)