# Cloud IAM Best Practices

## Principle of Least Privilege

***Apply only th minimal access level required for what's needed to perform the job.***

- This can be done using **Predefined Roles** over **Primitive Roles**.
- Grant roles at the **smallest scope possible**.
- Child resources cannot restrict access granted on it's parent.
- **Restrict** who can create and manage service accounts.
- **Be cautious** with `Owner` role, as it has full control over the project.

## Resource Hierarchy

- **Mirror** your Google Cloud resources hierarchy structure to your organization's structure.
- Use projects to group resources that share **the same trust boundaries**.
- Set policies at the **organization level and at the project level**, rather than at the resource level.
- Use the security principles of **least privilege** to grant IAM roles.
- Grant roles for users or groups at the **folder level** instead of setting it at the project level, if **spanning across multiple projects**.

## Service Accounts

- When using Service Accounts, **treat each app as a separate trust boundary**.
- **Do not delete Service Accounts** that are in use by running services.
- **Rotate user managed Service Account keys** regularly.
- **Name Service Account keys** to reflect use and permissions.
- **Restrict** Service Account access
- **Don't** check in Service Account keys into source code repositories.

## Auditing

- Use **Cloud Audit Logs** to regularly **audit IAM policy changes**.
- **Audit** who can edit IAM policies on projects.
- **Export** audit logs to Cloud Storage for long-term retention.
- Regularly **audit service account key** access.
- **Restrict log access** with logging roles.

## Policy Management

- To grant access to **all projects** in your organization, use an **organization-level policy**.
- Grant roles to a **Google group instead of individuals users** where possible.
- When granting **multiple roles to a particular task**, create a **Google group** instead.