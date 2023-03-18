# Push github code to AWS codecommit - (CI/CD) using CDK Pipelines

## In this article

- [Prerequisites](#prerequisites)
- [Github to Codecommit](#github-to-codecommit)
- [Push the code to GitHub](#push-the-code-to-github)

### Prerequisites

- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
- [OICD](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) in AWS

Follow this [guide](https://docs.aws.amazon.com/cdk/v2/guide/cdk_pipeline.html) will help setting up AWS CI/CD in CDK. The below step are executed based on this doc

### Github to Codecommit:

1. Execute [this]() CloudFormation script in Account A.
2. Create a new repository in AWS codecommit (e.g: `github-codepipeline`).
3. Clone [this]() github repo.
4. Copy the github code and paste in AWS repository created in step 2.
5. Execute the following commands in terminal.

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git add .
git commit -m "first commit"
git push
```

**Note**: Check your branch name `master` or `main`

### Push the code to GitHub

```git
git init
git remote set-url origin git@github.com:xxxx/first_app.git
git branch -M main
git push -u origin main
```

- In github verify and clone the github repo.
- From now, you'll be using github to push the code.

### Make integration between github and aws codecommit

- In github repo, create a directory .github/workflows.
- add a file: `.grade.yaml`
- In `.grade.yaml` file, change the following parameters:

```
env:
  INPUT_REPOSITORY_NAME : "<aws-codecommit-repo>"
  AWS_REGION : <aws-region>
  AWS_CODECOMMIT_URL: <aws codecommit repo url>
```

### example 1

- text

# Welcome to your CDK Python project

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

- `cdk ls`          list all stacks in the app
- `cdk synth`       emits the synthesized CloudFormation template
- `cdk deploy`      deploy this stack to your default AWS account/region
- `cdk diff`        compare deployed stack with current state
- `cdk docs`        open CDK documentation

Enjoy!

# Welcome to your CDK Python project

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

- `cdk ls`          list all stacks in the app
- `cdk synth`       emits the synthesized CloudFormation template
- `cdk deploy`      deploy this stack to your default AWS account/region
- `cdk diff`        compare deployed stack with current state
- `cdk docs`        open CDK documentation

Enjoy!
