# Cloud SDK and CLI

Cloud SDK is a set of **command line tools** that allow you to manage resources through the the terminal.

It includes commands like:

- `gcloud`
- `gsutil`
- `bq`
- `kubectl`

To manage resources la Compute Engine, Cloud Storage, BigQuery, Kubernetes Engine, etc.

This tools can be run interactively or with automation scripts, and with them you can do everything you can do in the console (and more).

With the command:

- `gcloud init` you can initialize, authorize and set up your account to use the SDK.
- `gcloud auth login` you can authenticate with your Google account and set the current account as active.
- `gcloud config` you can configure account, and projects.
  - `gcloud config list` you can list the current configuration and properties.
- `gcloud components` you can install, update and remove SDK components.
- `gcloud --help` you can get help on the command (exit with `ctrl+C`).


All the `gcloud` commands follow the same pattern:

```bash
gcloud [component] [entity] [operation] [positional arguments] [flags]
```

For example:

```bash
gcloud compute instances create my-instance --zone=us-central1-a
```

### Demo

A video demo of the installation proces of Cloud SDK and CLI can be found [here](https://youtu.be/jpno8FSqpc8?si=SMXIuCxNRNHsNPtt&t=11918).

The video follows the Quickstart guide for the Cloud SDK, which can be found [here](https://cloud.google.com/sdk/docs/install-sdk?hl=it).

## Managing Cloud SDK

### `gcloud init`

First initialize the SDK with:

```bash
gcloud init
```

that performs the initial setup tasks, i.e. it setup a Cloud SDK configuration and stes a base set of properties and this usually covers the active account, the current project, and if API is enabled, the default Compute Engine region and zone.

**NOTE**: If you are in a remote terminal session with no access to a browser, you can use the `gcloud init --console-only` flag to perform the initialization in the terminal.

1. When we run `gcloud init`, it will give us a couple of different options to choose.

2. First, it will ask us what configuration we want to use. We can create a new configuration, or we can use an existing one.

    ![gcloud init](images/08_Cloud_SDK_and_CLI_01.png)

3. Then, it will ask us to log in with our Google account. We will be redirected to a page where we can log in and give the SDK the necessary permissions.

4. After that, we will be asked to choose a project. We can create a new project, or we can use an existing one.

5. Finally, we will be asked to choose a default Compute Engine zone. We can choose one of the available zones, or we can skip this step.

### `gcloud auth`

If we don't want to set up the whole configuration, we can just authenticate with our Google account by running:

```bash
gcloud auth login
```

**NOTE**: When we run the CLoud SDK we can have only one active account at a time. If we want to switch accounts, we can run `gcloud auth login` again.

To check the current account, we can run:

```bash
gcloud auth list
```

Instead, if we want to remove an account, i.e. credentials and access tokens, we can run:

```bash
gcloud auth revoke [ACCOUNT]
```

### `gcloud info`

To get information about the current configuration, we can run:

```bash
gcloud info
```

![gcloud info](images/08_Cloud_SDK_and_CLI_02.png)


### `gcloud config`

A configuration is a named set of gcloud cli properties, and it works as a profile.

To get all the information about the current configuration, we can run:

```bash
gcloud config list
```

Instead, to switch between configurations, we can run:

```bash
gcloud config configurations activate [CONFIGURATION_NAME]
```

To create a new configuration, we can run:

```bash
gcloud config configurations create [CONFIGURATION_NAME]
```

To see the properties of a configuration, we can run:

```bash
gcloud config configurations describe [CONFIGURATION_NAME]
```

We can also change the project, the account, the region, and the zone of the current configuration.

For example, to change the project, we can run:

```bash
gcloud config set project [PROJECT_ID]
```

Instead, if it is for the compute instance, we can run:

```bash
gcloud config set compute/zone [ZONE]
```

**NOTE**: Only the properties that **are not in the core property section**, are the ones that can be set.

### `gcloud components`

To install, update, and remove SDK components, we can use the `gcloud components` command.

To **list** all the available components, we can run:

```bash
gcloud components list
```

To **install** a component, we can run:

```bash
gcloud components install [COMPONENT]
```

To **remove** a component, we can run:

```bash
gcloud components remove [COMPONENT]
```

To **update all** the installed components, we can run:

```bash
gcloud components update
```

### `gcloud` interactive shell

To use the `gcloud` interactive shell, we need to install the beta component:

```bash
gcloud components install beta
```

Then, we can run:

```bash
gcloud beta interactive
```

Now for every command we run, we will have auto-completion and suggestions. 
