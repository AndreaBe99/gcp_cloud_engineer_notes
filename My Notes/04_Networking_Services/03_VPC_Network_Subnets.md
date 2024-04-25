# VPC Network Subnets

A **Subnet** is a *subnetwork* of a VPC network.

- Each VPC network consists of one or more **subnets** (useful IP ranges partition), also known in Google Cloud as **subnetworks**.
- Each subnet is associated with a region, and all instances in the subnet are in the same region.
- The name or region of a subnet **cannot be changed** after you have created it.
  - We need to delete the subnet and create a new one with the desired name or region.
- Primary and secondary ranges for **subnets cannot overlap** with any allocated range.
  - Any primary or secondary range of another subnet in the same network or any IP range of subnets in peered networks.
  - ***They must be unique valid cidr blocks.***

## Increasing subnet IP space

Google CLoud VPC has a feature to increase the IP space of a subnet without any workloads shutdown or downtime, but there are some caveats:

- The new subnets **must not overlap** with the other subnets in the same VPC network in any region.
- The new subnets **must stay inside** the RFC 1918 address-space.
- The new network range must be **larger than the orginal**, i.e. the prefix length must be smaller.
- Once a subnet has been expanded, you **cannot undo it**.

Auto-mode VPC networks start with a `/20` subnet, and you can expand it to a `/16`.

## Reserved IP addresses

There are some IP addresses that are reserved for Google Cloud services and cannot be used in the VPC network:

- the first IP address in each subnet is reserved for the **Network address**.
- the second IP address in each subnet is reserved for the **Default Gateway**, it allows you to access the internet.
- the second-to-last IP address in the primary IP range for the subnet is reserve for **Google Cloud future use**.
- the last address in the IP range for the subnet is for the **Broadcast address**.

**NOTE:** The IP addresses are no reserved in the secondary IP ranges, but only in the primary IP range.

