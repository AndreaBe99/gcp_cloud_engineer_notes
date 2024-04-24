# Policies and Conditions

Recall:

![Policies Architecture](images/01_Cloud_IAM_03.png)

- **Policies** are a collection of statements that define who has what type of access to your resources.
  - A policy is attached to a resource and is used to enforce access control whenever that resource is accessed.
- **Bindings** binds one or more members with a single role and any context-specific conditions.

So a binding is a tuple of (members, role, condition), and adding metadata and audit config we obtain a policy.

## Policy Statements

An example of a **Policy Statement**:

```json
{
    "bindings": [
        {
            "role": "roles/storage.admin",
            "members": [
                "user:tonybowtieace@gmail.com"
            ]
        },
        {
            "role": "roles/storage.objectViewer",
            "members": [
                "user:larkfederkenge@gmail.com"
            ],
            "condition": {
                "title": "Expires_January_1_2021",
                "description": "Do not grant access after January 1, 2021",
                "expression": "request.time < timestamp('2021-01-01T00:00:00Z')"
            }
        }
    ],
    "etag": "BwW9z3Q8f3Y=",
    "version": 3
}
```

We can write the same policy in YAML format:

```yaml
bindings:
- members:
  - user: tonybowtieace@gmail.com
    role: roles/storage.admin
- members:
    - user: larkfederkenge@gmail.com
    role: roles/storage.objectViewer
    condition:
        title: Expires_January_1_2021
        description: Do not grant access after January 1, 2021
        expression: request.time < timestamp('2021-01-01T00:00:00Z')
etag: BwW9z3Q8f3Y=
version: 3
```

To query the policy, we can use the following command:

```bash
# Get the IAM policy for a project
gcloud projects get-iam-policy [PROJECT_ID]

# Get the IAM policy for a folder
gcloud resource-manager folders get-iam-policy [FOLDER_ID]

# Get the IAM policy for an organization
gcloud organizations get-iam-policy [ORG_ID]
```

### Policy Versions

There are three versions of the IAM policy schema:

- `1`: of the IAM syntax schema for policy supports binding one role to one or more members. 
  - **It does not support conditional role bindings**. So, we version 1 you will not see the `condition` field.
- `2`: is used for **Google's internal use** and so queries will not return version 2 policies.
- `3`: it introduces the `condition` field to support conditional role bindings.

### Policy Limitations

The following are some limitations of IAM policies:

- Each resource can only have one policy and this includes organization, folder, and project.
- Each IAM policy has a maximum of 1500 members or 250 Google groups.
- Policy changes will take uo to 7 minutes to fully propagate across GCP.
- There is a limit of 100 conditional role binding per policy.

## Conditions

**Conditions** are attributes that are either based on resources or on details about the request (timestamp, originating/destination IP address, etc).

*Conditional Role Binding* is another name for a policy that includes a condition, they can be added to a new or existing policy.


### Examples

Time-based example:

```yaml
bindings:
- members:
  - user: tonybowtieace@gmail.com
    role: roles/storage.admin
- members:
    - user: larkfederlagen@gmail.com
    role: roles/storage.objectViewer
    condition:
        title: Business_hours_access
        description: business hours access Monday-Friday
        expression: request.time.getHours("America/Toronto") >= 9 &&
                    request.time.getHours("America/Toronto") <= 17 &&
                    // Day of the week ranges from 0 to 6, where 0 is Sunday and 6 is Saturday
                    request.time.getDayOfWeek("America/Toronto") >= 1 &&
                    request.time.getDayOfWeek("America/Toronto") <= 5
etag: BwW9z3Q8f3Y=
version: 3
```

Resource-based example:

```yaml
bindings:
- members:
  - user: larkfederlagen@gmail.com
    role: roles/owner
- members:
    - group: developer@bowtieinc.com
    role: roles/compute.instanceAdmin
    condition:
        title: Dev_only_access
        description: Only access to development VMs
        expression: (resource.type == "compute.googleapis.com/Disk" &&
                    resource.name.startsWith("project-cat-bowties/region/us-central1/disk/development")) ||
                    (resource.type == "compute.googleapis.com/Instance" &&
                    resource.name.startsWith("project-cat-bowties/region/us-central1/instance/development")) ||
                    (resource.type != "compute.googleapis.com/Instance" &&
                    resource.type != "compute.googleapis.com/Disk")
version: 3
```

### Condition Limitations

Some limitations of conditions include:

- Conditions are limited to specific services and resources.
- Primitive role are unsupported.
- Members cannot be allUsers or allAuthenticatedUsers.
- Limit of 100 conditional role bindings per policy.
- 20 role binding for same role and member.

## AuditConfig Logs

**AuditConfig** logs are used to log all the changes made to the IAM policy. This is useful for tracking changes and for compliance purposes.

It specifies the auto-configuration for a service, thar defines which permission types are logged and wht identities (if any) are exempted from logging.

Example:

```yaml
auditConfigs:
- auditLogConfigs:
  - logType: DATA_READ
  - logType: ADMIN_READ
  - logType: DATA_WRITE
  service: allServices
- auditLogConfigs:
  - exemptedMembers:
    - tonybowtieace@gmail.com
    - logType: ADMIN_READ
  service: storage.googleapis.com
```

