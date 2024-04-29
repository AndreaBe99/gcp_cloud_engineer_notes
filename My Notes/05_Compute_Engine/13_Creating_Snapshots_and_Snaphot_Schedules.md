# Creating Snapshots and Snaphot Schedules

A video demo of this lab is available [here](https://youtu.be/jpno8FSqpc8?si=dgcvvrNLIeGEREAc&t=46210).

## Creating an VM Instance

First, make sure to have the `default` VPC network created. 

Run the following command to create a VM instance:

```bash
gcloud compute instances create bowtie-instance \
    --zone=us-east1-b \
    --machine-type=e2-micro \
    --subnet=default \
    --image=debian-10-buster-v20210916 \
    --image-project=debian-cloud \
    --boot-disk-size=10GB \
    --boot-disk-type=pd-standard
```

Now, SSH into the VM instance:

```bash
gcloud compute ssh bowtie-instance --zone=us-east1-b
```

Once inside the VM instance, verify the name of the instance:

```bash
hostname

# Output
# bowtie-instance
```

Now create a text file:

```bash
sudo nano fileofbowtie.txt
```

Add some text to the file and save it.

List the files in the directory:

```bash
ls -al
```

## Creating a Snapshot

Now go back to the Console and create a snapshot of the disk.

1. Go to the **Compute Engine** page.
2. Click on **Disks** section.
3. Click on the three dots on the right side of the disk.
4. Click on **Create snapshot**.

An alternative way to create a snapshot is the following.

1. Go to the **Compute Engine** page.
2. Click on **Snapshots** section.
3. Click on **Create snapshot** and fill in the details.
   - **Name**: `bowtie-snapshot`
   - **Description**: `Snapshot of the bowtie-instance disk`
   - **Source disk**: `bowtie-instance`
   - **Location**: Check `Regional`
   - **Select location**: `us-east1`
     - **NOTE:** We can select a region different from the disk's region.
   - **Labels**: `env: testing`
4. Click on **Create**.

## Creating a new VM instance from a Snapshot

Now, let's create a new VM instance from the snapshot.

1. Go to the **Compute Engine** page.
2. Go to the **VM instances** section.
3. Click on **Create instance** and fill in the details.
   - **Name**: `bowtie-instance-2`
   - **Labels**: `env: testing`
   - **Region**: `us-east1`
   - **Zone**: `us-east1-b`
   - **Machine type**: `e2-micro`
   - **Boot disk**: Select **Change** button.
     - **Snapshot** tab
       - **Snapshot**: `bowtie-snapshot`
       - **Boot disk type**: `Standard persistent disk`
       - **Size (GB)**: `10`
   - Leave the rest as default.
4. Click on **Create**.

Now, SSH into the new VM instance:

```bash
gcloud compute ssh bowtie-instance-2 --zone=us-east1-b
```

Run the following command to verify the name of the instance:

```bash
hostname

# Output
# bowtie-instance-2
```

List the files in the directory:

```bash
ls -al
```

We can see that the `fileofbowtie.txt` file is present in the new VM instance.

## Creating a Snapshot Schedule

Now, let's create a snapshot schedule.

1. Go to the **Compute Engine** page.
2. Click on **Snapshot** section.
3. Click on **Snapshot schedules** tab.
4. Click on **Create snapshot schedule**.
    - **Name**: `bowtie-diskschedule`
    - **Description**: `Snapshot schedule for bowtie-instance disk`
    - **Region**: `us-east1`
    - **Storage location**: `Regional`
    - **Select location**: `us-east1`
    - **Schedule options**:
      - **Frequency**: `Daily`
      - **Start time (UTC)**: `06:00 - 07:00`
      - **Auto-delete snapshots after**: `14 days`
    - **Deletion rule**: `Keep snapshots`
    - **Labels**: `env: testing`
5. Click on **Create**.

Now we need to attach the snapshot schedule to the disk.

1. Go to the **Compute Engine** page.
2. Click on **Disks** section.
3. Click on the `bowtie-instance` disk.
4. Click on **Edit**.
    - **Snapshot schedule**: `bowtie-diskschedule`
5. Click on **Save**.

Now we can create a new snapshot schedule for the `bowtie-instance-2` disk. This time, we will create the schedule using the `gcloud` command.

```bash
gcloud compute resource-policies create snapshot-schedule bowtie-diskschedule-2 \
    --description="Snapshot schedule for bowtie-instance-2 disk" \
    --region=us-east1 \
    --max-retention-days=14 \
    --on-source-disk-delete=apply-retention-policy \
    --daily-schedule \
    --start-time=06:00 \
    --storage-location=us-east1

# Output
# ERROR: (gcloud.compute.resource-policies.create.snapshot-schedule) Could not fetch resource:
# - Insufficient Permission: Request had insufficient authentication scopes.
```

We need to add the right permissions to the service account.

But we can also switch user.

```bash
gcloud auth login
```

Re-run the command to create the snapshot schedule.

Now we can attach the snapshot schedule to the disk.

```bash
gcloud compute disks add-resource-policies bowtie-instance-2 \
    --resource-policies=bowtie-diskschedule-2 \
    --zone=us-east1-b
```