import aws_cdk as cdk
from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk import aws_codecommit as codecommit
import aws_cdk.aws_ec2 as ec2
from aws_cdk.pipelines import ManualApprovalStep
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct
from github_codepipeline.stage import Stage

class GithubCodepipeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.backend_repository =  codecommit.Repository.from_repository_name(
            self,
            "github-to-aws",
            repository_name="github-codepipe" # aws codecommit repository name
        )
        pipeline = CodePipeline(
            self,
            "github-to-codepipe",
            pipeline_name=self.backend_repository.repository_name,
            cross_account_keys=True,
            self_mutation=True,
            synth=ShellStep("Synth",
                            input=CodePipelineSource.code_commit(
                            repository=self.backend_repository, 
                            branch="master"
                            ),
                            commands=[
                                "npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"
                            ]
                            )        
        )  
        ###### AWS acc - dev-env  ######--master
        dev_stage = pipeline.add_stage(Stage(
            self,
            "dev-env", #change
            env=cdk.Environment(account="991958799346", region="eu-central-1")
            )
        )
        dev_stage.add_pre(ManualApprovalStep('approval'))