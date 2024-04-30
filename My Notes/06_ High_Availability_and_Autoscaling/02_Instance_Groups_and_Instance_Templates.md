# Instance Groups and Instance Templates

Instance groups are a great way to setup a group of identical servers.

Used in conjunction with instance groups, instance templates handle the instance properties to deploy instance groups into your environment.

## Instance Groups

**Instance groups** are a collection of virtual machine (VM) instances that you can manage as a single entity.

Compute Engine offers two types of instance groups:

- **Managed** instance groups or MIGs
  - Let you operate applications on multiple identical VMs.
  - You can make your workload scalable and highly available by taking advantage of automated MIG features, like:
    - autoscaling
    - autohealing
    - regional (multi-zone) deployment
    - automatic updating

- **Unmanaged** instance groups
  - Let you low balance across a fleet of VMs that you manage yourself.

### Managed Instance Groups

Managed instance groups are a collection of virtual machine (VM) instances that you can manage as a single entity.

![Managed Instance Groups](images/02_Instance_Groups_and_Instance_Templates_01.png)

In terms of use cases, MIGs are ideal for:

- **Stateless serving** workloads
  - Such as web-site front ends, web-servers, and web-site applications.
  - As they does not preserve its state and saves no data to persistent storage.
  - All user and session data stays with the client and makes scaling up and down easier.

- **Stateless batch** workloads
  - These are high performance or high throughput computing workloads.
  - Such as image processing from a queue.

- **Stateful workloads**
  - Use stateful managed instance groups or stateful MIGs.
  - They include application with stateful data or configuration, such as databases, legacy monolith type applications, and long running batch computations with checkpoints.
  - You can improve uptime and resiliency of these type of application with autohealing, controlled updates, and regional (multi-zone) deployment, while preserving each instance's unique state, including instance names, persistent disks, and metadata.

The types of workloads that you can run on managed instance groups are:

- **Auto-healing**
  - MIGs maintains high availability of your application by proactively keeping your instances in a *running* state.
  - A MIG will automatically *recreate* an instance if it is terminated due to a failure (not in a *running* state).
  - It takes care of application-based auto-healing
  - Improve application availability by relying on a health check that detects freezing, crashing, or overloading, and then *recreates* the instance.

- **Regional (multi-zone) deployment**
  - There is the option to deploy a MIG in a single zone or across multiple zones in a region.
  - Regional MIGs provide higher availability, because the instances are spread across multiple zones in a region.
  - Google recommends using regional MIGs over zonal MIGs as you can manage twice as many MIGs as zonal MIGs (2000 vs 1000).
  - You can spread your application among multiple zones, instead of a single zone, or managing multiple zonal MIGs across different zones.
  - This protect against zonal failures and improve application availability.


- **Load balancing**
  - It can use instance groups to serve traffic, so you can add instance groups to a target pool or to a backend.
  - Instance group is a type of backend, and the instances in the instance groups respomf to traffic from the load balancer.
  - The backend service in turn knows which instances it can use and how much traffic they can handle and how much traffic they are currently handling.
  - The backend service monitors the health checking and does not send new connections to unhealthy instances.

- **Auto-scaling**
  - Dynamically add or remove instances from the MIG based on the load.
  - You can configure policies to automatically scale the number of instances in a managed instance group based on the load.

- **Auto-updating**
  - You can easily and safely deploy new versions of your application by updating the instance template that the MIG uses.
  - You can also control the speed and the scope of the update, in order to minimize disruptions to your application.
  - You can perform rolling updates, which gradually replace instances in the MIG with instances created from the new template.
  - And also perform canary updates, which create a small number of instances from the new template and gradually increase the number of instances until all instances are running the new version.

You can reduce the cost of your workloads by using preemptible VMs in a managed instance group, and when they are deleted, auto-healing will recreate them, when the preemptible capacity is available.

You can also deploy containers to instances in a managed instance group, by using a container-optimized OS image or a container-optimized instance template.

When you create a managed instance group, you must define a VPC network that will reside in. When you don't specify a network, Google attempts to use the default network.

### Unmanaged Instance Groups

Unmanaged instance groups can contain heterogeneous instances, and these are instances that are of mixed sizes of CPU, RAM, as well as instance types.

You can remove instances from an unmanaged instance group wheneever you want.

But there is a major downside, indeed, Unmanaged instance groups **do not provide autoscaling, autohealing, or rolling updates, anf multi-zone deployment.**

They are not a good choice for deploying highly available and scalable workloads.

You can use unmanaged instance groups if you need **to apply load balancing** to a groups of these mixed types of instances or if you need to manage the instances yourself.

## Instance Templates

To launch an instance group into any environment, you need to define an **instance template**, i.e. a resource that you can use to create virtual machine instances and manage instance groups.

- Instance templates define:
  - Machine type
  - Boot disk image or container image
  - Labels
  - Other instance properties

- You can use an instance template to create a MIG or a VM instance.
  - It is a global resource, that is not bound to a zone or region, but you can restrict a template to a specific zone, by calling out specific zonal resources.

**If you want to create a group of identical instances you must use an instance template to create a MIG.**

- Instance templates are designed to create instances with identical configurations, so **you cannot update or change an existing instance template** after you create it.
  - If you need to make changes to the configuration, you must create a new instance template.

- You can create a template based on an existing instance, or existing instance template. to use an existing VM as template, you can save the configuration with:

    ```bash
    gcloud instance-templates create
    ```

    or using the Google Cloud Console, goin to the instance template page and click on the **Create instance template** button.

- To make changes, you can create another one with similar properties using the console.