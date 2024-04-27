# Compute Engine Overview

**Compute Engine** is a service that lets create and run virtual machines known as **instances**, that are hosted on Google's infrastructure.

So it is an **Infrastructure as a Service (IaaS)**, because Google cares about the virtualization platform, the physical server, the network, the storage, and the security.

The instances are available in different **sizes** and **types**, and each instance is charged by the second after the first minute, because it is a consumption-based model.

The instances are launched in a VPC network, and they will sit on host in **zones**, which are isolated locations within a region. We have the possibility of using:

- a **multi-tenant** host, where the server that is hosting your instance is shared with other, but each instance is isolated
- a **sole-tenant** host, where the server is dedicated to you

## Machine Configuration

When creating an instance, we have different options to configure the machine:

![Machine Configuration](images/02_Compute_Engine_Overview_01.png)

- **Cores and Memory**
  - *Predefined* or *Custom* machine types
    - we can choose from many *Predefined* machine types, for general purpose, memory optimized, compute optimized, etc, or we can create a *Custom* machine type
    - we can choose between Intel and AMD processors
    - each *vCPU* is a hyper-thread of a physical core
    - the network throughput is up to *2 Gbps per vCPU*, so if we have a machine with 4 vCPUs, we will have a network throughput of 8 Gbps

- **Operating System**
  - *Public* images
    - Compute Engine provides a set of *public* images, like Linux, or Windows
    - the boot disk is a persistent disk, that is attached to the instance with the same size of the that you choose
  - *Custom* images
    - a boot disk that you own and control access
    - are available only to your cloud project unless you specifically decide to share them with other projects or organization
    - you can create a custom image from a boot disk snapshot, or from an image file that you upload
    - custom images that you import add no cost to your instances, but you are charged for the storage that they use
  - *Market-place* images
    - quickly deploy functional software packages that run on Google Cloud
    - it is an only-one instance template that include the OS and the software

- **Storage**: we can choose the type of storage, and the amount of storage
  - Performance vs Cost
    - *Standard* persistent disk
      - HDD
      - low cost
      - good for sequential read/write
    - *Balanced* SSD & *SSD*
      - SSD
      - high performance
      - good for random read/write
    - *Local SSD*
      - SSD
      - high performance
      - good for temporary data
      - it is physically attached to the host machine
      - the data is lost when the instance is terminated

- **Networking**
  - Auto, Default, or Custom network
    - *Auto network*
      - Compute Engine automatically creates a network for you
      - it is a global network
    - *Default network*
      - Compute Engine automatically creates a network for you
      - it is a regional network
    - *Custom network*
      - you create the network
      - it is a global network
  - Many available *regions* and *zones*
  - *Firewall rules*
    - we can create firewall rules to allow or deny traffic to the instance
    - the default rule allows all traffic from the same network, and denies all traffic from other networks
  - *Network Load Balancer*
    - distribute the traffic across multiple instances
    - it is a global service
    - it is a managed service, so we don't have to worry about the infrastructure